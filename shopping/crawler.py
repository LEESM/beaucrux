import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping.settings'
import django
django.setup()
from selenium import webdriver
import time
import datetime
import random
import xlwt

def makeurl(page):
	first_url = 'http://m.ssg.com/search.ssg?target=mobile&query=mcm&viewType=lst&page='
	url = first_url + str(page)
	return(url)

def makedetail(item_id):
	first_url = 'http://www.ssg.com/item/itemView.ssg?itemId='
	url = first_url+str(item_id)
	return(url)

def crawler():
	driver=webdriver.Firefox()
	for page in range(1,22):
		driver.get(makeurl(page))
		item_list =driver.find_elements_by_name('attnTgtIdnfNo1')
		for item in item_list:
			item_id = item.get_attribute("value")
			driver.get(makedetail(item_id))
			item_name = driver.find_element_by_class_name("item_title")
			item_price = driver.find_element_by_class_name("ssg_price price")
			item_content = driver.find_elemnt_by_id("descContents")
			print(item_name)
			print(item_price)
			print(item_content)
	driver.quit()

def main():
	crawler()

main()