import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping.settings'
import django
django.setup()
from selenium import webdriver
import time
from ingredient.models import Ingredient

print('ewg 크롤링 시작')
driver = webdriver.PhantomJS()
flag = 0

items=Ingredient.objects.filter(ewg_high_grade=-1, ewg_low_grade=-1)
for item in items:
    while True:
        try:
            driver.get("http://www.ewg.org/skindeep/")
            element_query = driver.find_element_by_name('query')
            element_query.clear()
            print(item.en_name)
            element_query.send_keys(item.en_name)
            element_query.submit()
            element_grade_img = driver.find_element_by_css_selector('#table-browse tbody tr:nth-child(2) td:nth-child(3) img')
            string = element_grade_img.get_attribute('src')
            low = string[58]
            high = string[60]
            print(item.en_name)
            item.ewg_high_grade = int(high)
            item.ewg_low_grade = int(low)
            item.save()
            break
        except:
            print(item.id)
            flag=flag+1
            if(flag==3):
                flag=0
                item.ewg_low_grade=0
                item.ewg_high_grade=11
                item.save()
                break
            else:
                print('에러발생')
                time.sleep(0.1)
