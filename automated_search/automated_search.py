from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1.Open eBay watch page ( Watch for sale | eBay  )
# 2.Select option Brand / Rolex in Filter pane
# 3.Verify the first two result items contain “rolex” in their title
# 4.Store title and price of the first two results in a variable
# 5.Open item in a new tab and verify the title and the price by comparing them with the stored data
# 6.Uncheck “Rolex“ option
# 7.Check “Casio“ option
# 8.Verify the last two result items contain “Casio“ in their title
# 9.Save and print all the mismatches if any

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0")
driver.refresh()
rolex_checkbox = driver.find_element(By.XPATH,"//div[text() = 'Brand']/ancestor::li[@class = 'x-refine__main__list ']//input[contains(@class, 'checkbox') and @aria-label = 'Rolex']")
rolex_checkbox.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'srp-river-results']//span[@role = 'heading']")))
rolex_titles = driver.find_elements(By.XPATH, "//div[@id = 'srp-river-results']//span[@role = 'heading']")
rolex_prices = driver.find_elements(By.XPATH, "//div[@id = 'srp-river-results']//span[@class = 's-item__price']")
first_two_titles = []
first_two_prices = []

mismatches = []

for item in rolex_titles[:2]:
    first_two_titles.append(item.text)
    if 'rolex' not in item.text.lower():
        mismatches.append(item.text.lower() + 'is not contains Rolex')
    # assert 'rolex' in item.text.lower()

for item in rolex_prices[:2]:
    first_two_prices.append(item.text)

for i, item in enumerate(rolex_titles[:2]):
    item.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class = 'x-item-title__mainTitle']/span")))
    text = driver.find_element(By.XPATH,"//h1[@class = 'x-item-title__mainTitle']/span").text
    price = driver.find_element(By.XPATH,"//div[@class = 'x-price-primary']/span").text
    if first_two_titles[i].lower() != text.lower():
        mismatches.append(first_two_titles[i].lower() + " is not equal to " + text.lower())
    # assert first_two_titles[i].lower() == text.lower()
    if first_two_prices[i].lower()not in price.lower():
        mismatches.append(first_two_prices[i].lower() + " is not a part of  " + price.lower())
    # assert first_two_prices[i].lower() in price.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

rolex_checkbox = driver.find_element(By.XPATH,"//div[text() = 'Brand']/ancestor::li[@class = 'x-refine__main__list ']//input[contains(@class, 'checkbox') and @aria-label = 'Rolex']")
rolex_checkbox.click()
casio_checkbox = driver.find_element(By.XPATH,
                                     "//div[text() = 'Brand']/ancestor::li[@class = 'x-refine__main__list ']//input[contains(@class, 'checkbox') and @aria-label = 'Casio']")
casio_checkbox.click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class = 's-item__title']/span[contains(text(), 'Casio')]")))
items2 = driver.find_elements(By.XPATH, "//div[@class = 's-item__title']/span[contains(text(), 'Casio')]")
last_two_items = []

for i in items2[-2:]:
    last_two_items.append(i.text)
    if 'casio' not in i.text.lower():
        mismatches.append(i.text.lower() + 'is not contains Casio')
    # assert 'casio' in i.text.lower()
print(mismatches)

driver.quit()
