from selenium.webdriver import Remote
from components import ProductWidgetListComponent, CartModuleBlockComponent


class HomePage:
    def __init__(self, driver: Remote):
        self._driver = driver
        self.product_list = ProductWidgetListComponent(self._driver)
        self.cart_module_block = CartModuleBlockComponent(self._driver)

