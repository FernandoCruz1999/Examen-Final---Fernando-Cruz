import re
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from .config import BASE_URL, OFFERS_URL, HEADERS, SELECTORS, PRICE_SELECTORS, MAIN_TARGET, SAVE_PATH, PAGES_RANGE

class MercadoLibreScraper:

    def __init__(self):
        self.offers = []

    def get_page(self, url):
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None

    def extract_text(self, element):
        return element.text.strip() if element else None

    def extract_offer_info(self, offer):
        offer_data = {}

        for key, (tag, css_class) in SELECTORS.items():
            element = offer.find(tag, class_=css_class)
            offer_data[key] = self.extract_text(element)

        offer_data["old_price"] = self.get_price(offer, "old_price")
        offer_data["current_price"] = self.get_price(offer, "current_price")

        if offer_data["old_price"] is not None and offer_data["current_price"] is not None:
            offer_data["discount_money"] = round(offer_data["old_price"] - offer_data["current_price"], 2)
        else:
            offer_data["discount_money"] = None

        link_element = offer.find("a", href=True)
        offer_data["url"] = link_element["href"] if link_element else None

        return self.clean_data(offer_data)

    def extract_offers(self, soup):
        tag, css_class = MAIN_TARGET
        offers_elements = soup.find_all(tag, class_=css_class)

        for offer in offers_elements:
            offer_data = self.extract_offer_info(offer)
            self.offers.append(offer_data)

    def process_offers(self):
        self.offers = []
        html = self.get_page(OFFERS_URL)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            self.extract_offers(soup)

    def process_offers_pages(self, start_page=PAGES_RANGE[0], end_page=PAGES_RANGE[1]):
        self.offers = []

        for page in range(start_page, end_page + 1):
            page_url = f"{BASE_URL}/ofertas?page={page}"
            print(page_url)

            html = self.get_page(page_url)
            if html:
                soup = BeautifulSoup(html, "html.parser")
                self.extract_offers(soup)
            else:
                print(f"No se pudo obtener la página {page}")

    def get_offers(self):
        return self.offers

    def get_price(self, offer, price_type):
        tag, class_name = PRICE_SELECTORS.get(price_type, (None, None))

        if not tag or not class_name:
            return None

        price_element = offer.find(tag, class_=class_name)

        if not price_element:
            return None


        fraction = price_element.find("span", class_=PRICE_SELECTORS["fraction"])
        cents = price_element.find("span", class_=PRICE_SELECTORS["cents"])

        price_fraction = self.clean_price(fraction.get_text(strip=True)) if fraction else "0"
        price_cents = self.clean_price(cents.get_text(strip=True)) if cents else "00"

        try:
            return float(f"{price_fraction}.{price_cents}")
        except ValueError:
            return None

    def clean_price(self, value):
        if value:
            value = re.sub(r"[^\d]", "", value)
        return value if value else "0"

    def clean_data(self, offer):

        if offer.get("discount"):
            offer["discount"] = int(re.sub(r"[^\d]", "", offer["discount"]))

        if offer.get("rating"):
            offer["rating"] = float(offer["rating"])

        if offer.get("reviews_count"):
            offer["reviews_count"] = int(re.sub(r"[^\d]", "", offer["reviews_count"]))

        if offer.get("coupon"):
            match = re.search(r"(\d+)", offer["coupon"])
            offer["coupon"] = int(match.group(1)) if match else None

        offer["free_shipping"] = 1 if offer.get("free_shipping") == "Envío gratis" else 0

        if offer.get("seller"):
            offer["seller"] = offer["seller"].replace("Por ", "")

        return offer

    def save(self, path = SAVE_PATH, prefix = "ofertas_"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.json"

        filepath = os.path.join(path, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(self.offers, file, indent=4, ensure_ascii=False)
            print(f"Datos guardados en {filename}")
        except Exception as e:
            print(f"Error al guardar JSON: {e}")

# scraper = MercadoLibreScraper()
# scraper.process_offers()
# scraper.save()
