#requirements -> selenium-wire

from seleniumwire import webdriver

import warnings
import os

warnings.simplefilter("ignore")

proxy = '45.153.22.66'
port = '6006'
proxy_user = 'wpblzgct'
proxy_password = 'sr3nmcaq1cyb'


def get_chromedriver(use_proxy=False, user_agent=None, headless=False):
    proxyOptions = {
        'proxy': {
            'http': "http://%s:%s@%s:%s" % (proxy_user, proxy_password, proxy, port),
            'https': "https://%s:%s@%s:%s" % (proxy_user, proxy_password, proxy, port)
        }
    } if use_proxy else False

    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--nogpu")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,1280")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--enable-javascript")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(
        os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options, seleniumwire_options=proxyOptions)
    return driver


def main():
    driver = get_chromedriver(use_proxy=True, headless=False)
    driver.get('https://www.google.com')
    print(driver.page_source)

main()

