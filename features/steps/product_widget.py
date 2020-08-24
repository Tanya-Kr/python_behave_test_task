from behave import *
from pages.home_page import HomePage
from pages.product_page import ProductPage

HOME_PAGE_URL = 'http://automationpractice.com'
PRODUCT_NAME = 'Faded Short Sleeve T-shirts'


@given(u'a user visits home page "{url}"')
def step(context, url):
    context.browser.get(HOME_PAGE_URL)
    context.home_page = HomePage(context.browser)


@when('click on Add to cart button on widget with product name "{name}"')
def step(context, name):
    context.home_page.product_list.click_add_cart_button(PRODUCT_NAME)


@then('pop up with success message is displayed on same page')
def step(context):
    assert context.home_page.cart_module_block.get_success_cart_text()


@when('click on \'More\' button')
def step(context):
    context.home_page.product_list.click_more_button(PRODUCT_NAME)


@then('product page is open')
def step(context):
    context.product = ProductPage(context.browser)
    assert PRODUCT_NAME in context.product.title
