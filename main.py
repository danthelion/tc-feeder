import logging
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import random
from tenacity import retry, stop_after_attempt

load_dotenv()

logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__)


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

    LOGGER.info("Starting Chrome driver")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@retry(stop=stop_after_attempt(3))
def login(driver):
    driver.get("https://teveclub.hu")

    username = os.getenv("TC_USER", os.getenv("INPUT_TC_USER"))
    if not username:
        raise ValueError(
            "Username not found in environment. Please set either TC_USER or INPUT_TC_USER."
        )
    LOGGER.info(f"Logging in as {username}")

    password = os.getenv("TC_PASSWORD", os.getenv("INPUT_TC_PASSWORD"))
    if not password:
        raise ValueError(
            "Password not found in environment. Please set either TC_PASSWORD or INPUT_TC_PASSWORD."
        )

    username_element = driver.find_element(by="name", value="tevenev")

    username_element.send_keys(username)

    password_element = driver.find_element(by="name", value="pass")
    password_element.send_keys(password)

    login_form = driver.find_element(by="name", value="loginform")
    LOGGER.info(f"Submitting login form: {login_form}")
    login_form.submit()
    LOGGER.info("Submitted login form successfully")


@retry(stop=stop_after_attempt(3))
def feed(driver):
    LOGGER.info(f"Loading feed page")
    driver.get("https://teveclub.hu/myteve.pet")
    try:
        _feed = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[3]/td[1]/center/div/form/input',
        )
        _feed.click()
        LOGGER.info(f"Clicked feed button")
    except NoSuchElementException:
        LOGGER.info(
            f"Feed button not found, skipping. Camel probably already fed today."
        )
        pass


@retry(stop=stop_after_attempt(3))
def train(driver):
    LOGGER.info(f"Loading training page")
    driver.get("https://teveclub.hu/tanit.pet")
    try:
        _train = driver.find_element(
            by="xpath",
            value='//*[@id="content ize"]/tbody/tr/td/table/tbody/tr[1]/td/font/b/div/form[1]/div/input',
        )
        _train.click()
        LOGGER.info(f"Clicked train button")
    except NoSuchElementException:
        LOGGER.info(
            f"train button not found, skipping. Camel probably already studied today."
        )
        pass

@retry(stop=stop_after_attempt(3))
def onenumbergame(driver):
    LOGGER.info(f"Loading egyszamjatek page")
    driver.get("https://teveclub.hu/egyszam.pet")
    onenumbergame_input = driver.find_element(
        by=By.NAME, value='honnan'
    )
    randnum = random.randint(1, 10000)
    onenumbergame_input.send_keys(str(randnum))
    LOGGER.info(f"Submitted guess {randnum}")
    onenumbergame_submit = driver.find_element(
        by=By.NAME, value='tipp'
    )
    onenumbergame_submit.submit()
    LOGGER.info(f"Submitted guess")

def main():
    chrome_driver = get_driver()
    login(driver=chrome_driver)
    feed(driver=chrome_driver)
    train(driver=chrome_driver)
    onenumbergame(driver=chrome_driver)


if __name__ == "__main__":
    main()
