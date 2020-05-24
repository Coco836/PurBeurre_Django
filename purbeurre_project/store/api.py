# -*- coding : utf8 -*-

import requests


class OpenFoodFactsApi:
    """ Retrieve different data from online API."""

    def fetch_stores_data_api(self):
        """
            Method allowing the program to search stores' data online
            with the Open Food Facts API.
        """
        # Recover data from Open Food Facts URL API with request get.
        response = requests.get(
                                "https://fr.openfoodfacts.org/categorie/"
                                "stores.json"
        )
        # Save the json data in a variable.
        json_data_file = response.json()
        # Get only the data needed: data besides the one in the "tags"
        # list are irrelevant here.
        return json_data_file.get('tags')
        

        
    def fetch_categories_data_api(self):
        """
            Method allowing the program to search categories' data online
            with the Open Food Facts API.
        """
        # Recover data from Open Food Facts URL API with request get.
        response = requests.get('https://fr.openfoodfacts.org/categories.json')
        # Save the json data in a variable.
        json_data_file = response.json()
        # Get only the data needed: data besides the one in the "tags"
        # list are irrelevant here.
        return json_data_file.get('tags')


    def fetch_products_data_api(self, category):
        """
            Method allowing the program to search products' data online
            with the Open Food Facts API.
        """
        # With the name of each category saved inside the database, do a
        # concatenation with the name of the category and the rest of the URL
        url_categories = (
                        f'''https://fr.openfoodfacts.org/categorie/{category}.json'''
        )
        # Recover data from Open Food Facts URL API with request get.
        response = requests.get(url_categories)
        # Save the json data in a variable.
        json_data_file = response.json()
        # Get only the data needed: data besides the one in the "products"
        # list are irrelevant here.
        return json_data_file.get('products')

