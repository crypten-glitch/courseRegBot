import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    WebDriverException,
    ElementClickInterceptedException,
)
import secret

chrome_options = Options()
chrome_options.add_argument("--headless") # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu") # Disable GPU hardware acceleration
chrome_options.add_experimental_option("detach", True)


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service, options=chrome_options)

    def open_page(self, url: str):
        self.browser.get(url)
        time.sleep(5)

    def close_browser(self):
        self.browser.quit()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)

    def click_button(self, by: By, value: str):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        button.click()

    def login(self, username: str, password: str):
        self.add_input(
            by=By.XPATH, value="<LOGIN USERNAME XPATH HERE>", text=username
        )
        self.add_input(
            by=By.XPATH, value="<LOGIN PASSWORD XPATH HERE>", text=password
        )
        self.click_button(by=By.XPATH, value="<LOGIN BUTTON XPATH HERE>")
        self.click_button(
            by=By.XPATH, value="<NAVIGATING BUTTON XPATH HERE>"
        )

    def click_button_repeatedly(self):
        for _ in range(100000):
            try:
                button = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "<REGISTER BUTTON XPATH HERE>",
                        )
                    )
                )
                if button.is_enabled():
                    print("Successfully clicked")
                    button.click()
                    time.sleep(2)
                else:
                    self.browser.refresh()
                    time.sleep(5)
            except ElementClickInterceptedException as e:
                continue
            except WebDriverException as e:
                if "ERR_CONNECTION_REFUSED" in str(e):
                    self.close_browser()
                    return False
                self.close_browser()
                return False
        return True


if __name__ == "__main__":
    driver_path = "<DRIVER FULL PATH HERE>"
    login_url = "<LOGIN PAGE URL HERE>"

    while True:
        browser = Browser(driver_path)
        try:
            browser.open_page(login_url)
            browser.login(secret.username, secret.password)
            if not browser.click_button_repeatedly():
                continue
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            browser.close_browser()
        break
