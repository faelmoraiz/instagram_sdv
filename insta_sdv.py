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
bro.get('https://www.instagram.com/')
bro.set_window_size(50,100)
#bro.set_window_position(830, 30)

input('Preparação...')

perf=bro.find_elements_by_xpath("//a[@class='_2g7d5 notranslate _95hvo']")

links=[];i=0

for perfil in perf:
  link=perfil.get_attribute("href")
  if link not in links:
    links.append(link)

for page in links:
  tempo=random.randrange(5,40)
  num=len(links)
  bro.get(page)
  time.sleep(2)
  try:
    bro.find_elements(By.XPATH, '//button[text()="Seguir"]')[0].click();i+=1
    print('[+]',str(i),'de',str(num),'- Seguindo!')
    for x in range(tempo):
      time.sleep(1)
      print('[_]',str(tempo-x),'restantes...', end='\r')
  except:
    print('[!]',str(i),'de',str(num),'- Já segue.')
