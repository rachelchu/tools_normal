from selenium import webdriver

import os, time

if __name__ == "__main__":

    '''
    Use Edge brower
    Step1:Download "MicrosoftWebDriver"; 
    Step2:Put "MicrosoftWebDriver" to Python Path; 
    '''
    #driver = webdriver.Edge()


    '''
    Use Firefox brower
    Step1:Download "geckodriver"; 
    Step2:Put "geckodriver" to Python Path; 
    '''
    #driver = webdriver.Firefox()


    '''
    Use chrome brower
    Step1:Download "chromedriver"; 
    Step2:Put "chromedriver" to Chrome Path; 
    '''
    ''''''
    chrome = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chrome
    driver = webdriver.Chrome(chrome)
    

    driver.get('https://www.meadjohnson.com.cn/')
    driver.save_screenshot(str(time.time())+'.png')
    driver.quit()