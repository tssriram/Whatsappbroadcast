# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:07:21 2020

@author: Tharun
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

nm="_2S1VP copyable-text selectable-text"
stringa=list()

input("Enter after scanning")

with open('Second571.csv', 'r') as file:
    reader = csv.reader(file)
    for name in reader:
       
        name1=''.join(name)
        
        wait = WebDriverWait(driver, 5)

        try:

            #searcher = driver.find_element_by_xpath('//div[@class = "{}"][@data-tab="3"]'.format(nm))
            searcher = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="{}"][@data-tab="3"]'.format(nm))))
            searcher.clear()
            searcher.send_keys(name)
            time.sleep(0.75)
        except:
            stringa.append(name1+" Error 1 \n")
            continue
            #time.sleep(2.5)
            
        try:
            #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name1))
            user = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@title="{}"]'.format(name1))))
            user.click()
            time.sleep(0.25)
            
            #time.sleep(2)
        except:
            stringa.append(name1+" Error 2 \n")
            
            continue
            
        try:
            #msgbox1 = driver.find_element_by_class_name('_1Plpp')
            msgbox1=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_1Plpp')))
            msgbox1.send_keys(Keys.CONTROL, "v")
            time.sleep(0.75)
            
            #time.sleep(3)
        except:
            stringa.append(name1+" Error 3 \n")
            continue
        
    
        try:
            #msgbox2 = driver.find_element_by_xpath('//div[@class = "{}"][@data-tab="1"]'.format(nm))
            msgbox2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="{}"][@data-tab="1"]'.format(nm))))
            
            msgbox2.send_keys("*Register here:* https://forms.gle/C3E78Rc1XjPaLgaC7")
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys("*May 13th, 5 PM*")
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys("We would like to invite you to attend the webinar- *Post COVID: The landscape for Start-ups and Entrepreneurs*.")
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys("The Startup landscape is going to be dramatically altered following the COVID-19 pandemic. This webinar would highlight the opportunities that this would throw up. *Prof. Thillai Rajan would also talk about the strategies that start-up founders need to adopt to seize the momentum*.")
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys("Warm regards, ")
            msgbox2.send_keys(Keys.SHIFT, Keys.ENTER)
            msgbox2.send_keys("Team YNOS (www.ynos.in)")
            time.sleep(0.75)
            
        except:
            stringa.append(name1+" Error 4 \n")
            continue
            
        try:
            #driver.find_element_by_class_name('_3nfoJ').click()
            sender = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_3nfoJ')))
            sender.click()
            time.sleep(1)
            
        except:
            stringa.append(name1+" Error 5 \n")
            continue

file = open('errors.csv', 'w+', newline ='') 
file.truncate()

with file:     
    write = csv.writer(file) 
    for element in stringa:
        write.writerow([element,])     
    