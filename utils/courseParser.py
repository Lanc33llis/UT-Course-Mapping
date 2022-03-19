from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# parses the detail table
def detailTableParser(driver: webdriver.Chrome, timeout):
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#details_table")))
  table = driver.find_element(By.CSS_SELECTOR, "#details_table")
  heads = table.find_elements(By.CSS_SELECTOR, "th")
  datas = table.find_elements(By.CSS_SELECTOR, "td")

  n = len(heads)

  details = {}
  for i in range(n):
    label = heads[i].text
    data = datas[i]

    elems = data.find_elements(By.CSS_SELECTOR, "ul > li")
    if len(elems) == 0:
      details[label] = data.text.strip().replace("\n", " ")
    else:
      details[label] = [e.text for e in elems]

  return details

# parses the current page the driver as a course page and returns an object course
# this will get complex very fast given that course descriptions are often handwritten
# and not consistent with their formatting
def courseParser(driver: webdriver.Chrome, timeout):
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#details")))

  return detailTableParser(driver, timeout)