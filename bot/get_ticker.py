
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import json
from tqdm import tqdm


def get_ticker_by_company(company_name):
    url = "https://www.finam.ru/quotes/indices/world/"
    driver = webdriver.Chrome()
    driver.get(url)

    search = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search-trigger').click()
    search_input = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search').find_element(By.TAG_NAME, 'input')
    search_input.send_keys(company_name)
    
    search_list = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search-result')
    
    # driver.implicitly_wait(1) # seconds

    try:
        element = WebDriverWait(search_list, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'a'))
        )
    except:
        # driver.quit()
        return None
    
    tickers_a = search_list.find_elements(By.TAG_NAME, 'a')
    for el in tickers_a: # московская биржа может быть не первой в списке. пример тинькофф - TCS Group
        stock_ticker = el.get_attribute('data-chpurl').split('/') # пара (биржа/тикер)

        if stock_ticker[0] == 'moex':
            return stock_ticker[1]

    return None


