from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from antlr4 import *

from utLexer import utLexer
from utParser import utParser
from utListener import utListener

import re, json, pprint
from functools import reduce

from utils.majors import majorNameToCode

# parses the detail table
def detailTableParser(driver: webdriver.Chrome, timeout) -> dict:
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
      # new line is a new row in the table unfortunately. New line means a course meets twice on the same day
      details[label] = data.text.strip().replace("\n", " ")
    else:
      details[label] = [e.text for e in elems]

  return details

#parses the prereqs from the description
def prereqParser(s: str):
  nouns = re.finditer(r"([A-Z][a-z]+(\s[A-Z][a-z]+)*)", s)
  majors = list(filter(lambda x: x.group(0) in majorNameToCode, nouns))

  s = s.replace(";", " and")
  s = s.replace("and and", "and")
  s = s.replace("or or", "or")

  t = re.findall(f"({reduce(lambda a, b: f'{a}|{b.group(0)}', majors[1:], majors[0].group(0))})|" + r"(\d{3}\w{0,1})|" + r"(\band|\bor)", s)
  t = list(map(lambda e: [s for s in e if s][0], t))
  
  if t[0] == "and" or t[0] == "or":
    t = t[1:]
  if t[-1] == "and" or t[-1] == "or":
    t = t[:-1]

  t = reduce(lambda a, b: f"{a} {b}", t)

  t = re.sub(r";|and and|and or", "and", t)
  t = re.sub(r"or or", "or", t)

  #edge case for "CODE, MAJOR"
  cmec = re.finditer(r"(\d{3}\w{0,1}) ([A-Z][a-z]+)", t)
  for ec in cmec:
    t = t.replace(ec.group(0), f"{ec.group(1)} and {ec.group(2)}")

  inputStream = InputStream(t)
  lexer = utLexer(inputStream)
  stream = CommonTokenStream(lexer)
  parser = utParser(stream)
  tree = parser.parse()
  listener = utListener()
  walker = ParseTreeWalker()
  walker.walk(listener, tree)
  result = listener.tree

  return result

def descriptionParser(driver: webdriver.Chrome, timeout):
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#details")))

  pElems = driver.find_elements(By.CSS_SELECTOR, "#details > p")
  prereqs = "None"

  prereqText = list(filter(lambda e: "Prerequisite" in e.text, pElems))
  if len(prereqText) > 0:
    print(prereqText[0].text)
    try:
      prereqs = prereqParser(prereqText[0].text)
    except Exception as e:
      prereqs = "Couldn't Parse"

  return {"Prereqs": prereqs, **detailTableParser(driver, timeout)}

# parses the current page the driver as a course page and returns an object course
# this will get complex very fast given that course descriptions are often handwritten
# and not consistent with their formatting
def courseParser(driver: webdriver.Chrome, timeout):
  WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#details")))

  return descriptionParser(driver, timeout)