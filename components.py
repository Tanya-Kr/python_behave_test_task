from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsCartModuleBlock, LocatorsProductWidgetList, LocatorsProductWidget


class CartModuleBlock:
    def __init__(self, driver: Remote):
        self._driver = driver

    def get_success_cart_text(self):
        try:
            WebDriverWait(self._driver, 5) \
                .until(EC.visibility_of_element_located(*LocatorsCartModuleBlock.SUCCESS_CART_TEXT))
            return True
        except TimeoutException:
            return False


class ProductWidgetList:
    def __init__(self, driver: Remote):
        self._driver = driver
        self._product_list = self.generate_products_list()

    def generate_products_list(self) -> list:
        product_widgets = self._driver.find_elements(*LocatorsProductWidgetList.PRODUCT_WIDGET)
        product_list = []
        for product in product_widgets:
            product_list.append(ProductWidget(product, self._driver))
        return product_list

    def click_add_cart_button(self, product_name):
        product = self._get_product_instance(product_name)
        product.click_add_cart_button()

    def click_more_button(self, product_name):
        product = self._get_product_instance(product_name)
        product.click_more_button()

    def _get_product_instance(self, product_name):
        for product in self._product_list:
            if product.get_name() == product_name:
                hover = ActionChains(self._driver).move_to_element(product.product_widget)
                hover.perform()
                return product


class ProductWidget:
    def __init__(self, product_widget: WebElement, driver: Remote):
        self._driver = driver
        self.product_widget = product_widget

    def get_name(self):
        return self.product_widget.find_element(*LocatorsProductWidget.PRODUCT_NAME).get_attribute('title')

    def click_add_cart_button(self):
        self.product_widget.find_element(*LocatorsProductWidget.ADD_TO_CART_BUTTON).click()

    def click_more_button(self):
        self.product_widget.find_element(*LocatorsProductWidget.MORE_BUTTON).click()
