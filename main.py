# launch the browser
# open url
# find element by id/class
# perform action (click/type)
# verify result
# close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_web_interaction():
    driver = webdriver.Chrome()
    driver.fullscreen_window()

    try:
        driver.get("https://www.powerlearnprojectafrica.org/")

        learn_more = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[9]/div/div/div/div/div/div[1]/div[3]/button")
            )
        )
        learn_more.click()
        time.sleep(2)

        got_it = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[9]/div/div/div/div/div[3]/button[2]")
            )
        )
        got_it.click()
        time.sleep(2)

        academy = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "PLP Academy"))
        )
        academy.click()
        time.sleep(2)

        # Switch to the new tab that opened
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)

        print("Current url:", driver.current_url)
        assert "academy" in driver.current_url, "Navigation to Academy failed"

        login = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='login']"))
        )
        login.click()

        webdriver_wait = WebDriverWait(driver, 10)
        webdriver_wait.until(EC.url_contains("login"))

        # Fill in the email
        email = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys("stvnoyaro@gmail.com")

        # Fill in the password
        password = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys("27k.Fvj7TXDLs_U")

        # click sign in button
        sign_in = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/div[1]/div[2]/div[2]/form/button")
            )
        )
        sign_in.click()

        later_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='scoped-theme-wrapper']/div[2]/div/div/div[2]/div[2]/button[1]",
                )
            )
        )
        later_button.click()

        scan = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/button[2]')
            )
        )

        scan.click()
        time.sleep(2)

        certificate = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div[1]/main/div/div[1]/aside/div[2]/div/a[8]/div',
                )
            )
        )

        certificate.click()
        time.sleep(3)

        view_certificate = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="scoped-theme-wrapper"]/div/div/div/div[2]/div[2]/button',
                )
            )
        )
        view_certificate.click()
        time.sleep(10)

        download_cert = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="scoped-theme-wrapper"]/div/div/button')
            )
        )
        download_cert.click()

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


test_web_interaction()
