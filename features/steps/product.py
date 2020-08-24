from behave import *
from pages.product_page import ProductPage

PRODUCT_URL = 'http://automationpractice.com/index.php?id_product=2&controller=product'


@given(u'a user visits product page "{url}"')
def step(context, url):
    context.browser.get(PRODUCT_URL)
    context.product = ProductPage(context.browser)


@when('click on Add to cart button')
def step(context):
    context.product.product_info.click_add_cart_button()


@then('pop up with success message is displayed')
def step(context):
    assert context.product.cart_module_block.get_success_cart_text()


@when('click on button to up product quantity')
def step(context):
    context.product.product_info.click_quantity_up_button()


@when('change quantity on 3')
def step(context):
    context.product.product_info.change_quantity("3")


@when('click on button to down product quantity')
def step(context):
    context.product.product_info.click_quantity_down_button()


@then('product quantity should be equal 2')
def step(context):
    assert context.product.product_info.get_quantity() == "2"
