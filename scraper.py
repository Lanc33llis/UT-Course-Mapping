from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import argparse, json

from utils.courseParser import courseParser
from utils.scraperFunctions import exportMajors

with open("cache.txt", "r") as cache:
  cache = cache.read().splitlines()
  if len(cache) >= 2:
    EID = cache[0]
    PW = cache[1]

parser = argparse.ArgumentParser(description='Scrape UT Courses')
parser.add_argument("-e", "--eid", nargs="?", type=str, const="", help='UT EID')
parser.add_argument("-p", "--password", nargs="?", type=str, const="", help='UT Password')
args = parser.parse_args()

if args.eid and args.password:
  EID, PW = args.eid, args.password
  with open("cache.txt", "w") as cache:
    cache.write(EID + "\n" + PW + "\n")

driver = webdriver.Chrome()

courseRegistrarLink = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20219/'
driver.get(courseRegistrarLink)

timeout = 30

# log in using EID and password
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "login-button")))
driver.find_element(By.ID, "username").send_keys(EID)
driver.find_element(By.ID, "password").send_keys(PW)
driver.find_element(By.ID, "login-button").click()

#wait for course registrar to load after duo authorization
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "inner_header")))

# get the major list element
majorSelectionElement = driver.find_element(By.ID, "fos_fl")
majors = majorSelectionElement.find_elements(By.XPATH, "./child::*")[1:]
btn = driver.find_element(By.CSS_SELECTOR, "#search_area > div:nth-child(4) > div.form_area > form > div:nth-child(5) > div.submit_button > input[type=image]")

tree = {}

def recursiveFollow(driver, timeout, tree):
  try:
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#inner_body")))
    try:
      error = driver.find_element(By.CSS_SELECTOR, "#inner_body > div > p").text
      if error:
        return
    except:
      pass

    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#inner_body > table")))
    table = driver.find_element(By.CLASS_NAME, "rwd-table")
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]

    for row in rows:
      td1 = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
      if "course_header" in td1.get_attribute("class").split():
        courseName = td1.find_element(By.CSS_SELECTOR, "h2").text
        tree[courseName] = []
        print(courseName)
      else:
        try:
          link = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a") 
          link.send_keys(Keys.CONTROL, Keys.ENTER)
          driver.switch_to.window(driver.window_handles[2])

          course = courseParser(driver, timeout)
          tree[list(tree.keys())[-1]] += [course]

          driver.close()
        except Exception as e:
          print(e)
          continue
        driver.switch_to.window(driver.window_handles[1])

    nextBtn = driver.find_element(By.CSS_SELECTOR, "#next_nav_link")
    nextBtn.click()
    recursiveFollow(driver, timeout, tree)
  except Exception as e:
    pass

# exportMajors(list(map(lambda e: e.text, majors)), "majors.txt")
for major in majors:  
  majorName = major.text
  print(majorName)
  tree[majorName] = {}
  major.click()
  btn.send_keys(Keys.CONTROL, Keys.ENTER)
  driver.switch_to.window(driver.window_handles[1])
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "search_area")))

  try:
    recursiveFollow(driver, timeout, tree[majorName])
  except Exception as e:
    pass

  driver.close()
  print()
  driver.switch_to.window(driver.window_handles[0])

driver.quit()
print()

print("Dumping to JSON File")
json.dump(tree, open("test.json", "w"))

print("Done")