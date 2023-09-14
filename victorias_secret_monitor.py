from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import random
import string
from bs4 import BeautifulSoup
from collections import defaultdict
import schedule
import time
import send_hook
from send_hook import Restock

stock_changes = defaultdict(str)

def init():
    cfg = open("config.txt", "r")
    hook = cfg.readline()
    send_hook.hook_testing(hook)

    

def scrape():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--log-level=3') #VS throws an annoying error with the chat if you run headless selenium, let's ignore that 
    driver = webdriver.Chrome(options=options)

    # Clear out all previous web history and cookies
    driver.delete_all_cookies()
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get('chrome://settings/clearBrowserData') # for chrome
    time.sleep(2)
    actions = webdriver.ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
    actions.perform()
    actions = webdriver.ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
    actions.perform()

    characters = string.ascii_letters
    url = "https://www.victoriassecret.com/us/pink/accessories-catalog/5000008137?"
    randStr = ''.join(random.choice(characters) for _ in range(10))
    url += randStr

    driver.get(url)

    try:
        #I have to use selenium because there's some XHR request loading in sizes for each SKU.
        #I'm not sure what it is now, but finding the XHR and being able to request sizes from there would be much prefereable.
        #For now, this is an incomplete solution.
        wait = WebDriverWait(driver, 5)
        elem_exists = EC.presence_of_element_located((By.XPATH, "//img[@class='prism-image' and @alt='Beige']"))
        wait.until(elem_exists)
        
        button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div[3]/div[2]/div/div[4]/div[2]/div[2]/div[1]")
        button.click()

        scrapeInfo = driver.page_source
        driver.quit()

        soupy = BeautifulSoup(scrapeInfo, 'html.parser')
        parent_div = soupy.find('div', class_='sc-vcal1v-0 jtANLe prism-layout-flex prism-layout sc-5xth68-1 ljIygu')
        sizedivs = parent_div.find_all('div', role=True)

        data_values = [div['data-value'] for div in sizedivs if div.has_attr('data-value')]
        data_instock = [div['aria-disabled'] for div in sizedivs if div.has_attr('aria-checked')]

        imgurl = "https://www.victoriassecret.com/p/760x1013/tif/zz/23/08/22/04/1115846933H6_OF_F.jpg"


        sizes_restocked = []
        for i, data_value in enumerate(data_values):
            cur_state = data_instock[i]
            val_key = data_value
            prev_state = stock_changes.get(val_key, None)

            print(cur_state)
            print(data_values[i])

            if prev_state == "false" and cur_state == "true":
                sizes_restocked.append(data_values[i])
                #newrestock = Restock(url, imgurl, "Victoria's Secret", "1122553-MDSD", data_value, imgurl)
                #send_hook.ping(newrestock)
                pass
            elif prev_state == "true" and cur_state == "false":
                # send_webhook #for debug
                pass
            else:
                stock_changes[val_key] = cur_state  # update stock
        if len(sizes_restocked) > 0:
            new_restock = Restock(url, imgurl, "Victoria's Secret [Click for direct URL]", "1122553-MDSD", sizes_restocked, imgurl)
            send_hook.ping(new_restock)
    except (NoSuchElementException, TimeoutException) as e:
        pass
        print("Product not found.")
        #the product is not there, nothing we can do


# Schedule the scraping job to run every minute
schedule.every(1).minutes.do(scrape)

#Todo: rotate SKU being monitored to save proxies


# Keep running indefinitely
init()
scrape()
while True:
    schedule.run_pending()
    time.sleep(1)