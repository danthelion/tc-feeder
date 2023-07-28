import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller


load_dotenv()


def get_driver():
    print(
        f"Installing chromedriver version {chromedriver_autoinstaller.get_chrome_version()}"
    )
    chromedriver_autoinstaller.install()

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

    print("Starting Chrome driver")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def login(driver):
    driver.get("https://teveclub.hu")

    username = driver.find_element(by="name", value="tevenev")
    username.send_keys(os.getenv("TC_USER"))

    password = driver.find_element(by="name", value="pass")
    password.send_keys(os.getenv("TC_PASSWORD"))

    form = driver.find_element(by="name", value="loginform")
    print(f"Submitting form: {form}")
    form.submit()
    print("Submitted form")


def feed(driver):
    print(f"Loading feed page")
    driver.get("https://teveclub.hu/myteve.pet")
    try:
        _feed = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[3]/td[1]/center/div/form/input',
        )
        _feed.click()
        print(f"Clicked feed button")
    except NoSuchElementException:
        pass


def learn(driver):
    print(f"Loading learn page")
    driver.get("https://teveclub.hu/tanit.pet")
    try:
        _learn = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[1]/td/font/b/div/form[1]/div/input',
        )
        _learn.click()
        print(f"Clicked learn button")
    except NoSuchElementException:
        pass


def main():
    driver = get_driver()
    login(driver)
    feed(driver)
    learn(driver)


if __name__ == "__main__":
    main()
