#coding:utf8
#!/usr/bin/python3
#
# Coded by faelmoraiz on 22, jan, 2018
#

import time, os, random, re                                                                                      
from bs4 import BeautifulSoup as bs           
from selenium import webdriver       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By                                

os.system('clear')                                       

bro = webdriver.Chrome()                                 
bro.set_window_size(1090,1050)
bro.set_window_position(830, 30)
bro.get('http://www.instagram.com/')

bro = webdriver.Chrome()

perf=bro.find_elements_by_xpath("//a[@class='_2g7d5 notranslate _95hvo']")

links=[]

for perfil in perf:
  link=perfil.get_attribute("href")
  if link not in links:
    links.append(link)

for page in links:
  num=len(links);i+=1
  bro.get(page)
  time.sleep(random.randrange(5,40))
  try:
    bro.find_elements(By.XPATH, '//button[text()="Seguir"]')[0].click()
    print('[+]',str(i),'de',str(num),'- Seguindo!')
  except:
    print('[!]',str(i),'de',str(num),'- Já segue.')
