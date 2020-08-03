import logging
from api import OpenFoodFactsApi
from django.db import IntegrityError
import django
django.setup()
from django.apps import apps
Category = apps.get_model('store', 'Category')
Product = apps.get_model('store', 'Product')
logger = logging.getLogger('Pur Beurre')


class Update:
    @staticmethod
    def update_product():
        """ Method that update products data """

        api = OpenFoodFactsApi()
        categories = Category.objects.all()

        # Retrieve name of all the categories in database
        for category in categories:
            for json_product in api.fetch_products_data_api(category.name):
                try:
                    product = Product.from_api(json_product)
                except KeyError as error:
                    logger.warning(error)
                else:
                    # Get only API data of products already saved in database
                    if Product.objects.filter(url=product.url).exists():
                        product_db = Product.objects.get(url=product.url)
                        # Check if the name of the product has changed
                        if product.name is not product_db.name:
                            # Try updating the name of the product
                            try:
                                Product.objects.filter(url=product.url).update(
                                    name=product.name
                                )
                            except IntegrityError as error:
                                logger.warning(error)
                        # Check if the description of the product has changed
                        if product.description is not product_db.description:
                            # Try updating the description of the product
                            try:
                                Product.objects.filter(url=product.url).update(
                                    description=product.description
                                )
                            except IntegrityError as error:
                                logger.warning(error)
                        # Check if the nutriscore of the product has changed
                        if product.nutrition_grade is not product_db.nutrition_grade:
                            # Try updating the nutriscore of the product
                            try:
                                Product.objects.filter(url=product.url).update(
                                    nutrition_grade=product.nutrition_grade
                                )
                            except IntegrityError as error:
                                logger.warning(error)
                        # Check if the image of the product has changed
                        if product.image is not product_db.image:
                            # Try updating the image of the product
                            try:
                                Product.objects.filter(url=product.url).update(
                                    image=product.image
                                )
                            except IntegrityError as error:
                                logger.warning(error)


data_update = Update()
data_update.update_product()
