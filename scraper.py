import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# UT EID Parsing so we don't have to store our EID and password in this repo

parser = argparse.ArgumentParser(description='Scrape UT Courses')
parser.add_argument("eid", metavar="e", type=str, help='UT EID')
parser.add_argument("password", metavar="p", type=str, help='UT Password')
args = parser.parse_args()

username, password = args.eid, args.password

driver = webdriver.Chrome()

courseRegistrarLink = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20219/'
driver.get(courseRegistrarLink)

timeout = 30

# log in using EID and password
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "login-button")))
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

#wait for course registrar to load after duo authorization
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "inner_header")))

# get the major list element
majorSelectionElement = driver.find_element(By.ID, "fos_fl")
majors = majorSelectionElement.find_elements(By.XPATH, "./child::*")[1:]
btn = driver.find_element(By.CSS_SELECTOR, "#search_area > div:nth-child(4) > div.form_area > form > div:nth-child(5) > div.submit_button > input[type=image]")

def recursiveFollow(driver, timeout):
  try:
    nextBtn = driver.find_element(By.CSS_SELECTOR, "#next_nav_link")
    nextBtn.click()

    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "search_area")))
    table = driver.find_element(By.CLASS_NAME, "rwd-table")
    rows = table.find_elements(By.CSS_SELECTOR, "td.course_header")

    for row in rows:
      print(row.text)
    recursiveFollow(driver, timeout)
  except:
    pass

for major in majors:  
  print(major.text)
  major.click()
  btn.send_keys(Keys.CONTROL, Keys.ENTER)
  driver.switch_to.window(driver.window_handles[1])
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "search_area")))

  try:
    table = driver.find_element(By.CLASS_NAME, "rwd-table")
    rows = table.find_elements(By.CSS_SELECTOR, "td.course_header")

    for row in rows:
      print(row.text)

    recursiveFollow(driver, timeout)
  except Exception:
    pass

  driver.close()
  print()
  driver.switch_to.window(driver.window_handles[0])


driver.quit()
