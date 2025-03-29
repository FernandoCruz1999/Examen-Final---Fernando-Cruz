
BASE_URL = "https://www.mercadolibre.com.pe"
OFFERS_URL = f"{BASE_URL}/ofertas#nav-header"
PAGES_RANGE = (1,5)

SAVE_PATH = "./data"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

MAIN_TARGET = ("div", "andes-card")

SELECTORS = {
    "title": ("a", "poly-component__title"),
    "type": ("span", "poly-component__highlight"),
    "brand": ("span", "poly-component__brand"),
    "seller": ("span", "poly-component__seller"),
    "rating": ("span", "poly-reviews__rating"),
    "reviews_count": ("span", "poly-reviews__total"),
    "discount": ("span", "andes-money-amount__discount"),
    "installments": ("span", "poly-price__installments"),
    "coupon": ("span", "poly-coupons__pill"),
    "free_shipping": ("div", "poly-component__shipping"),
}

PRICE_SELECTORS = {
    "old_price": ("s", "andes-money-amount--previous"),
    "current_price": ("div", "poly-price__current"),
    "fraction": "andes-money-amount__fraction",
    "cents": "andes-money-amount__cents",
}
