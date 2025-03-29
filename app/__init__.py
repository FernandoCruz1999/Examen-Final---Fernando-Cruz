from flask import Flask, render_template
from app.scrapers import MercadoLibreScraper

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def home():
        return render_template("home.html")

    @app.route("/results", methods=['GET'])
    def results():
        scraper = MercadoLibreScraper()
        scraper.process_offers()
        offers = scraper.get_offers()
        scraper.save()
        return render_template("results.html", offers=offers)

    @app.route("/all-results", methods=['GET'])
    def all_results():
        scraper = MercadoLibreScraper()
        scraper.process_offers_pages()
        offers = scraper.get_offers()
        scraper.save(prefix='ofertas_pagina_')
        return render_template("results.html", offers=offers)



    return app