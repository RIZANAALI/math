import math

example_variable = math.sqrt(16)
power_variable =  math.pow(2, 5)
ceil_variable = math.ceil(6.3)
floor_variable = math.floor(5.5)
fabs_variable = math.fabs(-9)
factorial_variable = math.factorial(4)
sin_variable = math.sin(math.pi/2)
cos_variable = math.cos(math.pi/2)
tan_variable = math.tan(math.pi)
log2_variable = math.log2(3)
log10_variable = math.log10(3)
degree_variable = math.degrees(math.pi/2)
radian_variable = math.radians(90)
euler_variable = math.e
infinity_variable = math.inf
nan_variable = math.nan
gcd_variable = math.gcd(4,5)
lcm_variable = math.lcm(3,4)
print(lcm_variable)  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                     ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)


    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    return float(text.split(":")[1])


def main():
   driver = get_driver()
   time.sleep(2)
   driver.find_element(By.ID,value="id_username").send_keys("automated")
   time.sleep(2)
   driver.find_element(By.ID,value="id_password").send_keys("automatedautomated" + Keys.RETURN)
   time.sleep(2)
   driver.find_element(By.XPATH,value="/html/body/nav/div/a").click()
   time.sleep(2)
   dynamic_element = driver.find_element(By.ID,value="displaytimer")
   return clean_text(dynamic_element.text)

print(main())


from datetime import datetime

dt = datetime(2024, 9, 25, 9, 25, 00)
print(dt)

now = datetime.now()
print(now.year)

from datetime import date
d = date(2024, 9, 25)
print(d)

today = date.today()
print(today.year)



from datetime import time
t = time(1, 30, 45)
print(t)
print(t.hour)


from datetime import timedelta, date
delta = timedelta(days=7)
print("timedelta",delta)
today = date.today()
print("date before:", today)


future_date = today - delta


print("after date:", future_date)

from datetime import datetime
date1 = datetime(2023, 9, 22, 10, 30)
date2 = datetime(2024, 9, 22, 10, 30)
print(date2-date1)
from calendar import isleap

print(isleap)
import yagmail
import os
from dotenv import load

load()


sender = "alicheruvattiali@gmail.com"
receiver = "xmtbazxyh@emlpro.com"
subject = 'test mail using python'
contents = ''' this is the content for sending mail'''
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")

from bs4 import BeautifulSoup
import requests


def get_rate(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    request = requests.get(url).content
    soup = BeautifulSoup(request,"html.parser").find("span",class_="ccOutputRslt").get_text()
    print(soup)
    rate = float(soup[:-4])
    return rate
def main():
    in_currency = input("Enter from the Currency code:")
    out_currency = input("Enter tom Currency code:")
    return get_rate(in_currency, out_currency)
print(main())

import yfinance as yf

ticker = input("Enter the Ticker:")
from_data = input("enter the start date(YYY-MM-DD):")
to_data = input("enter the end date(YYYY-MM-DD):")



stock_data = yf.download(ticker,start=from_data,end=to_data)
stock_data.to_html("stock_data.html")
print("stock data written to stock_data.html")


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                     ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)


    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    return float(text.split(":")[1])


def main():
   driver = get_driver()
   time.sleep(2)
   dynamic_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[2]")
   return clean_text(dynamic_element.text)

print(main())
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                     ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)


    driver.get("https://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[1]")
    return element.text
print(main())


from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                     ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)


    driver.get("https://automated.pythonanywhere.com")
    return driver







