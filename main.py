import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


load_dotenv()


def get_driver():
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
    print(f"Submitting login form: {form}")
    form.submit()
    print("Submitted login form successfully")


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
        print(f"Feed button not found, skipping. Camel probably already fed today.")
        pass


def train(driver):
    print(f"Loading training page")
    driver.get("https://teveclub.hu/tanit.pet")
    try:
        _train = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[1]/td/font/b/div/form[1]/div/input',
        )
        _train.click()
        print(f"Clicked train button")
    except NoSuchElementException:
        print(
            f"train button not found, skipping. Camel probably already studied today."
        )
        pass


def main():
    chrome_driver = get_driver()
    login(driver=chrome_driver)
    feed(driver=chrome_driver)
    train(driver=chrome_driver)


if __name__ == "__main__":
    main()
