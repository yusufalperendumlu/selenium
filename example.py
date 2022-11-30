from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\chromedriver.exe")
url = "https://www.sneaksup.com/?matchtype=e&utm_term=sneaks%20up&gclid=Cj0KCQiAm5ycBhCXARIsAPldzoVCBGPJ-Snf_s51zJOb8_QW41EnlbgByR__WNR5qgoNaV8To4_CogcaAtKHEALw_wcB"
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.get(url+"pages/Erkek")
time.sleep(6)
driver.back()
time.sleep(2)
driver.forward()



time.sleep(2)
driver.close()