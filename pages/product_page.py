from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from components import CartModuleBlockComponent
from locators import LocatorsProductPage


class ProductPage:
    """Described 'Product' page."""
    def __init__(self, driver: Remote):
        self._driver = driver
        self.cart_module_block = CartModuleBlockComponent(self._driver)
        self.product_info = ProductInfoBox(self._driver)
        self.title = self._driver.title


class ProductInfoBox:
    """Described  right sidebar on 'Product' page."""
    def __init__(self, driver: Remote):
        self._driver = driver
        self._quantity_field = self._driver.find_element(*LocatorsProductPage.QUANTITY_FIELD)

    def change_quantity(self, quantity: str):
        self._quantity_field.clear()
        self._quantity_field.send_keys(quantity)

    def get_quantity(self) -> str:
        return self._quantity_field.get_attribute("value")

    def click_quantity_up_button(self) -> None:
        self._driver.find_element(*LocatorsProductPage.QUANTITY_UP_BUTTON).click()

    def click_quantity_down_button(self) -> None:
        self._driver.find_element(*LocatorsProductPage.QUANTITY_DOWN_BUTTON).click()

    def click_color_button(self, color_name: str) -> None:
        color_name = color_name.lower().capitalize()
        self._driver.find_element(By.XPATH, f'//ul[@id="color_to_pick_list"]//a[@name="{color_name}"]')

    def click_add_cart_button(self) -> None:
        self._driver.find_element(*LocatorsProductPage.ADD_TO_CART_BUTTON).click()

    def click_add_wishlist_button(self) -> None:
        self._driver.find_element(*LocatorsProductPage.ADD_TO_WISHLIST_BUTTON).click()
