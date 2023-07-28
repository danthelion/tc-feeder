import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()


def get_driver():
    chrome_service = ChromeService(ChromeDriverManager().install())

    chrome_options = webdriver.ChromeOptions()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


def login(driver):
    driver.get("https://teveclub.hu")

    username = driver.find_element(by="name", value="tevenev")
    username.send_keys(os.getenv("TC_USER"))

    password = driver.find_element(by="name", value="pass")
    password.send_keys(os.getenv("TC_PASSWORD"))

    form = driver.find_element(by="name", value="loginform")
    form.submit()


def feed(driver):
    driver.get("https://teveclub.hu/myteve.pet")
    try:
        _feed = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[3]/td[1]/center/div/form/input',
        )
        _feed.click()
    except NoSuchElementException:
        pass


def learn(driver):
    driver.get("https://teveclub.hu/tanit.pet")
    try:
        _learn = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[1]/td/font/b/div/form[1]/div/input',
        )
        _learn.click()
    except NoSuchElementException:
        pass


def main():
    driver = get_driver()
    login(driver)
    # feed(driver)
    # learn(driver)


if __name__ == "__main__":
    main()
