# Import
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.urls import reverse
from django.apps import apps
Category = apps.get_model('store', 'Category')
Product = apps.get_model('store', 'Product')


# Create your tests here.


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        self.data_product = {
            'name': 'nutella',
            'description': 'product_description',
            'url': 'https://url',
            'nutrition_grade': 'd',
            'image': 'https://image',
        }
        self.data_substitute = {
            'name': 'chocolat',
            'description': 'product_description',
            'url': 'https://url',
            'nutrition_grade': 'a',
            'image': 'https://image',
        }
        self.data_category = {
            'name': 'pâte à tartiner'
        }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_1_signup_and_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('sign_up')))
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("last_name").send_keys('testname')
        self.selenium.find_element_by_name("first_name").send_keys('test')
        self.selenium.find_element_by_name("email").send_keys(
                                                        'emailtest@email.fr'
                                                        )
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '''//input[@value="S'inscrire"]'''
                                            ).click()
        self.selenium.find_element_by_class_name("connection-link").click()
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '//input[@value="Se connecter"]'
                                            ).click()
        self.selenium.get('%s%s' % (
                                    self.live_server_url,
                                    reverse('saved_food')
                                    ))

    def test_2_search(self):
        Product.objects.create(**self.data_product)
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        self.selenium.find_element_by_id("product").send_keys('nutella')
        self.selenium.find_element_by_id('btn-accueil').click()

    def test_3_add_favorite(self):
        # Sign-up and log-in user
        self.selenium.get('%s%s' % (self.live_server_url, reverse('sign_up')))
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("last_name").send_keys('testname')
        self.selenium.find_element_by_name("first_name").send_keys('test')
        self.selenium.find_element_by_name("email").send_keys(
                                                        'emailtest@email.fr'
                                                        )
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '''//input[@value="S'inscrire"]'''
                                        ).click()
        self.selenium.find_element_by_class_name("connection-link").click()
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '//input[@value="Se connecter"]'
                                            ).click()

        # Create products, category and add link to them
        product = Product.objects.create(**self.data_product)
        category = Category.objects.create(**self.data_category)
        substitute = Product.objects.create(**self.data_substitute)
        product.categories.add(category)
        substitute.categories.add(category)

        # Add substitute as favorite
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        self.selenium.find_element_by_id("product").send_keys('nutella')
        self.selenium.find_element_by_id('btn-accueil').click()
        self.selenium.find_element_by_id("prod-name").click()
        self.selenium.find_elements_by_id("category-search")[0].click()
        self.selenium.find_element_by_name("button-save").click()
        self.selenium.get('%s%s' % (
                                    self.live_server_url,
                                    reverse('saved_food')
                                    ))

    def test_4_change_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('sign_up')))
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("last_name").send_keys('testname')
        self.selenium.find_element_by_name("first_name").send_keys('test')
        self.selenium.find_element_by_name("email").send_keys(
                                                        'emailtest@email.fr'
                                                        )
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '''//input[@value="S'inscrire"]'''
                                            ).click()
        self.selenium.find_element_by_class_name("connection-link").click()
        self.selenium.find_element_by_name("username").send_keys('Test')
        self.selenium.find_element_by_name("password").send_keys('Password1')
        self.selenium.find_element_by_xpath(
                                            '//input[@value="Se connecter"]'
                                            ).click()
        self.selenium.find_element_by_class_name("change-pwd").click()
        self.selenium.find_element_by_name(
                                            "old_password"
                                            ).send_keys('Password1')
        self.selenium.find_element_by_name(
                                            "new_password1"
                                            ).send_keys('Password234')
        self.selenium.find_element_by_name(
                                            "new_password2"
                                            ).send_keys('Password234')
        self.selenium.find_element_by_xpath(
                                            '''//input[@value="Changer '''
                                            '''mon mot de passe"]'''
                                            ).click()
