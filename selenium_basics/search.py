from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def task1():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.quit()


def task2():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@class='gh-td gh-sch-btn']"))
        )
        get_url = driver.current_url
        print("The current url is:" + str(get_url))
    finally:
        driver.quit()


def task3():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@class='gh-td gh-sch-btn']"))
        )
        get_url = driver.current_url
        print("The current url is:" + str(get_url))
        search_field = driver.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
        search_field.send_keys("women watch")
        search_button.click()
    finally:
        driver.quit()


def task4():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@class='gh-td gh-sch-btn']"))
        )
        get_url = driver.current_url
        print("The current url is:" + str(get_url))
        search_field = driver.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
        search_field.send_keys("women watch")
        search_button.click()
        search_result_header = driver.find_element(By.XPATH, "//h1[@class='srp-controls__count-heading']")
        expected_header = "women watch"
        assert expected_header in search_result_header.text, 'Expected ' + expected_header + ' should be a part of ' + search_result_header.text
    finally:
        driver.quit()


task1()
task2()
task3()
task4()