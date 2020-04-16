#works in classic mode only
#this is a primitive code(semi-automated)
#keep in touch for the updated one
#make sure to download these modules 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#replace the below path with yours
b=webdriver.Chrome('/home/cyk/Documents/chromedriver (2)')
b.get('https://www.facebook.com')
#now login into the page usually and open the post
a = raw_input("after opening the post click enter")
com= b.find_element_by_class_name('_1mf ')
for i in range(100):
    com.send_keys("Ammababoi " + str(i) +" this post deserves attention") 
    com.send_keys(Keys.RETURN)
    sleep(2)
    com=b.find_element_by_class_name('_1mf ')
