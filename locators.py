from selenium.webdriver.common.by import By


class LocatorsProductPage:
    ADD_TO_CART_BUTTON = (By.ID, 'add_to_cart')
    QUANTITY_FIELD = (By.ID, 'quantity_wanted')
    ADD_TO_WISHLIST_BUTTON = (By.ID, 'wishlist_button')

    QUANTITY_UP_BUTTON = (By.CLASS_NAME, 'product_quantity_up')
    QUANTITY_DOWN_BUTTON = (By.CLASS_NAME, 'product_quantity_down')


class LocatorsCartModuleBlock:
    SUCCESS_CART_TEXT = (By.XPATH, '//h2[contains(.,"Product successfully added to your shopping cart")]')


class LocatorsProductWidgetList:
    PRODUCT_WIDGET = (By.CLASS_NAME, 'product-container')


class LocatorsProductWidget:
    PRODUCT_NAME = (By.XPATH, './/a[@class="product-name"]')
    ADD_TO_CART_BUTTON = (By.XPATH, './/a[@title="Add to cart"]')
    MORE_BUTTON = (By.XPATH, './/a[@title="View"]')
    QUICK_VIEW_BUTTON = (By.CLASS_NAME, '.quick-view')