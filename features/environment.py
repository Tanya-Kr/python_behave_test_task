from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def browser_chrome(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)
    yield context.browser
    context.browser.quit()


def before_all(context):
<<<<<<< HEAD
    use_fixture(browser_chrome, context)
=======
    use_fixture(browser_chrome, context)
>>>>>>> parent of 00640a5... "Add environment module"
