from selenium.webdriver import Remote
from components import ProductWidgetListComponent, CartModuleBlockComponent


class HomePage:
    """Described 'Home' page."""
    def __init__(self, driver: Remote):
        self._driver = driver
        self.product_list = ProductWidgetListComponent(self._driver)
        self.cart_module_block = CartModuleBlockComponent(self._driver)

