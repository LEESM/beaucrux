import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping.settings'
import django
django.setup()
from selenium import webdriver
import time
from ingredient.models import Ingredient

#46732 시작
#57103 끝
def old_crawler():
    print('크롤링 시작')
    driver=webdriver.PhantomJS()
    print('webdriver ok')
    driver.get("https://www.kcia.or.kr/cid/Document/020.Ingredient_shis/INGREDIENT_SHIS_10L.asp")
    print('url ok')
    for no in range(46732,57103):
        while True:
            try:
                check=Ingredient.objects.get(kcia_no=no)
                break
            except:
                pass
            try:
                driver.execute_script("fView('{no}')".format(no=no))
                ko_name = driver.find_element_by_css_selector('table:nth-child(3) tr:nth-child(1) td:nth-child(2)')
                if ko_name.text=='':
                    print('빈 번호')
                    break
                en_name = driver.find_element_by_css_selector('table:nth-child(3) tr:nth-child(2) td:nth-child(2)')
                purpose = driver.find_element_by_css_selector('table:nth-child(3) tr:nth-child(8) td:nth-child(2)')
                q=Ingredient(kcia_no=no,ko_name=ko_name.text, en_name=en_name.text, purpose=purpose.text)
                q.save()
                print('check4')
                print(str(no)+ko_name.text+en_name.text+purpose.text)
                driver.get("https://www.kcia.or.kr/cid/Document/020.Ingredient_shis/INGREDIENT_SHIS_10L.asp")
                break
            except:
                print('에러발생')
                time.sleep(2)


#503page, 16.5.9.
'''    
def new_crawler():
        print('크롤링 시작')
        driver = webdriver.Firefox()
        driver.get("https://www.kcia.or.kr/cid/Document/020.Ingredient_shis/INGREDIENT_SHIS_10L.asp")
        for i in range(503,0,-1):
                while True:
                        try:
                                driver.execute_script("fGoPage('{i}')".format(i=i))

                        except:
                                print('에러')
                                time.sleep(3)
'''
old_crawler()