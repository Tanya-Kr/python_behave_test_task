from selenium.webdriver.common.by import By


class LocatorsProductPage:
    ADD_TO_CART_BUTTON = (By.ID, 'add_to_cart')
    QUANTITY_FIELD = (By.ID, 'quantity_wanted')
    ADD_TO_WISHLIST_BUTTON = (By.ID, 'wishlist_button')

    QUANTITY_UP_BUTTON = (By.CLASS_NAME, 'product_quantity_up')
    QUANTITY_DOWN_BUTTON = (By.CLASS_NAME, 'product_quantity_down')

