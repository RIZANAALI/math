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
