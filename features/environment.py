from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options


@fixture
def browser_chrome(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    context.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)
    yield context.browser
    context.browser.quit()

    try:
        context.browser.get("https://www.google.com/")
    except exceptions.InvalidSessionIdException as e:
        print(e.msg)


def before_all(context):
    use_fixture(browser_chrome, context)
