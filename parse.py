import config
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

eventname = {}

driver = webdriver.Chrome(executable_path=config.driver)
driver.get("https://gg.bet/ru/betting/?page=2")
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located(
    (By.CLASS_NAME, "__app-CompetitorLogo-logo")
))
time.sleep(2)

data = driver.page_source

soup = BeautifulSoup(data, 'html.parser')
events = soup.findAll("div",
                      attrs={"class": "sportEventRow__container___2gQB0"})

for event in events:
    title = event.find("div",
                       attrs={"class", "sportEventRow__header___1vVf1"})

    if(title is not None):
        eventname[title.find("span").text] = 0

for event in events:
    title = event.find("div",
                       attrs={"class", "sportEventRow__header___1vVf1"})

    if(title is not None):
        eventname[title.find("span").text] += 1

    body = event.find("div", attrs={"class", "sportEventRow__body___3Ywcg"})
    time = body.find("div", attrs={"class", "dateTime__time___zdAqe"}).text
    date = (body.find("div", attrs={"class", "dateTime__today___teyUe"})
                .find("span").text)
    midd = body.find("div",
                     attrs={"class", "__app-MiddlePartMatchRow-container"})
    lc = midd.find("div",
                   attrs={"class", "middlePartMatchRow__bunch-left___3KZAo"})
    rc = midd.find("div",
                   attrs={"class", "middlePartMatchRow__bunch-right___3CW7s"})
    coef = midd.findAll("div",
                        attrs={"odd__ellipsis___3b4Yk"})
