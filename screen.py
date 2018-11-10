from selenium import webdriver
from sys import stdout
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, os, time
#from Login_Page import Login_Page
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from io import BytesIO
from PIL import Image

#Reference: https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver

if __name__ == "__main__":

    driver = webdriver.Firefox()
    verbose = 0

    #open page
    driver.get('https://www.meadjohnson.com.cn/cma#cma-body')
    #driver.get('https://www.baidu.com/')
    driver.maximize_window()

    #get total height of page
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

    scrollheight = driver.execute_script(js)
    #print('scrollheight:'+str(scrollheight))
        
    js = 'return Math.min( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
    scroll_each_height = driver.execute_script(js)

    if verbose > 0:
        print(scrollheight)

    slices = []
    offset = 0
    offset_arr=[]
    image_num = 0
    image_height = 0
    ratio = 1

    #separate full screen in parts and make printscreens
    while offset < scrollheight:
        time.sleep(2)
        if verbose > 0: 
            print(offset)

        #scroll to size of page 
        if (scrollheight-offset)<scroll_each_height:
            #if part of screen is the last one, we need to scroll just on rest of page
            driver.execute_script("window.scrollTo(0, %s);" % scrollheight)
            offset_arr.append(scrollheight-offset)
        else:
            driver.execute_script("window.scrollTo(0, %s);" % offset)
            offset_arr.append(offset)

        #create image (in Python 3.6 use BytesIO)
        img = Image.open(BytesIO(driver.get_screenshot_as_png()))

        offset += scroll_each_height
        if ratio == 1 :
            image_height = img.size[1]
            ratio = scroll_each_height/img.size[1]
        image_num += 1
        #append new printscreen to array
        slices.append(img)


        if verbose > 0:
            driver.get_screenshot_as_file('screen_%s.jpg' % (offset))
            print(scrollheight)

    image_all_height = scrollheight/ratio

    #create image with 
    screenshot = Image.new('RGB', (slices[0].size[0], int(image_all_height)))
    offset2 = 0

    #now glue all images together
    for img in slices:
        if image_num ==1 :
            screenshot.paste(img, (0, image_height*offset2))
        elif offset2 < (image_num - 1) :
            screenshot.paste(img, (0, image_height*offset2))
        else:
            screenshot.paste(img, (0, (image_height * (offset2 - 1) + int(offset_arr[offset2]/ratio))))
        offset2 += 1

    screenshot.save(str(time.time())+'.png')