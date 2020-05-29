from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('C:/Users/Simon/Documents/Webscraping/chromedriver.exe')
driver.get('http://www.agbooth.com/pp_web/')

def navigate():
    driver.get('http://www.agbooth.com/pp_web/')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="isc_7table"]/tbody/tr[5]/td/div').click()
    time.sleep(1)
    count = 1
    while count < 15:
        driver.find_element_by_xpath('//*[@id="isc_X"]/table/tbody/tr/td').click()
        count+=1

    driver.find_element_by_xpath('//*[@id="isc_J"]/table/tbody/tr/td').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="isc_1J"]/table/tbody/tr/td').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="isc_1Ztable"]/tbody/tr[4]/td/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="isc_4G"]').click()
    driver.find_element_by_xpath('//*[@id="isc_3Q"]/table/tbody/tr/td').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="isc_56table"]/tbody/tr[7]/td/div').click()
    time.sleep(1)

navigate()
for fracOne in range(125):
    fracTwo = 0
    time.sleep(1)
    while fracTwo < 125:
        time.sleep(1)
        count = 0
        while count < fracOne:
            driver.find_element_by_xpath('//*[@id="isc_68"]/table/tbody/tr/td').click()
            count+=1
        count = 0
        while count < fracTwo:
            driver.find_element_by_xpath('//*[@id="isc_6Q"]/table/tbody/tr/td').click()
            count+=1
        driver.find_element_by_xpath('//*[@id="isc_5W"]/table/tbody/tr/td').click()
        time.sleep(1)
        output = driver.find_element_by_xpath('//*[@id="isc_7G"]/table/tbody/tr/td').text
        enrichment = output.split("\n")[2]
        yieldVal = output.split("\n")[3]
        print("Enrichment: " + enrichment)
        print("Yeild: " + yieldVal)
        if int(float(enrichment)) > 30 and int(float(yieldVal)) > 85:
            break
            print("Final Fraction One: " + fracOne)
            print("Final Fraction Two: " + fracTwo)
        navigate()
        fracTwo+=1
