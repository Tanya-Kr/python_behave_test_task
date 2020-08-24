from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsCartModuleBlock, LocatorsProductWidgetList, LocatorsProductWidget


class CartModuleBlockComponent:
    """Described modular window that shown when product is added to cart."""
    def __init__(self, driver: Remote):
        self._driver = driver

    def check_display_success_cart_text(self) -> bool:
        """Check presents success text in cart modular window."""
        try:
            WebDriverWait(self._driver, 5) \
                .until(EC.visibility_of_element_located(LocatorsCartModuleBlock.SUCCESS_CART_TEXT))
            return True
        except TimeoutException:
            return False


class ProductWidgetListComponent:
    """Described list of product that displayed on 'Home', 'Category' pages."""
    def __init__(self, driver: Remote):
        self._driver = driver
        self._product_list = self.generate_product_list()

    def generate_product_list(self) -> list:
        """Create product_list filled with ProductWidget class instances.

        :return: list
        """
        product_widgets = self._driver.find_elements(*LocatorsProductWidgetList.PRODUCT_WIDGET)
        product_list = []
        for product in product_widgets:
            product_list.append(ProductWidgetComponent(product, self._driver))
        return product_list

    def click_add_cart_button(self, product_name: str) -> None:
        """Click on 'Add to cart' button of the product found by product name.

        :param product_name: string
        :return: None
        """
        product = self._get_product_instance(product_name)
        product.click_add_cart_button()

    def click_more_button(self, product_name: str) -> None:
        """Click on 'More' button of the product found by product name.

        :param product_name: string
        :return: None
        """
        product = self._get_product_instance(product_name)
        product.click_more_button()

    def click_quick_view_button(self, product_name: str) -> None:
        """Click on 'Quick view' button of the product found by product name.

        :param product_name: string
        :return: None
        """
        product = self._get_product_instance(product_name)
        product.click_quick_view_button()

    def _get_product_instance(self, product_name: str):
        """Return product from list found by name."""
        for product in self._product_list:
            if product.get_name() == product_name:
                hover = ActionChains(self._driver).move_to_element(product.product_widget)
                hover.perform()
                return product


class ProductWidgetComponent:
    """Described single product that displayed in product list on 'Home', 'Category' pages."""
    def __init__(self, product_widget: WebElement, driver: Remote):
        self._driver = driver
        self.product_widget = product_widget

    def get_name(self) -> None:
        return self.product_widget.find_element(*LocatorsProductWidget.PRODUCT_NAME).get_attribute('title')

    def click_add_cart_button(self) -> None:
        self.product_widget.find_element(*LocatorsProductWidget.ADD_TO_CART_BUTTON).click()

    def click_more_button(self) -> None:
        self.product_widget.find_element(*LocatorsProductWidget.MORE_BUTTON).click()

    def click_quick_view_button(self) -> None:
        self.product_widget.find_element(*LocatorsProductWidget.QUICK_VIEW_BUTTON).click()
