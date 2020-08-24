from selenium.webdriver import Remote
from components import ProductWidgetList


class HomePage:
    def __init__(self, driver: Remote):
        self._driver = driver
        self.product_list = ProductWidgetList(self._driver)
