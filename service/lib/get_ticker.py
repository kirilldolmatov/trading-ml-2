
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lib.tickers import get_tickers

def get_ticker_by_company_two(company_name):
    tickers_filter, companies = get_tickers()

    if company_name.upper() in tickers_filter:
        return company_name
    return None

def get_ticker_by_company(company_name):
    try:
        url = "https://www.finam.ru/quotes/indices/world/"

        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-agent={user_agent}')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        trigger = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search-trigger')
        print(trigger)
        search_input = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search').find_element(By.TAG_NAME, 'input')
        search_input.send_keys(company_name)

        search_list = driver.find_element(By.ID, 'infinity-ui-left-header-menu-search-result')
        
        # driver.implicitly_wait(1) # seconds

        element = WebDriverWait(search_list, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'a'))
        )
        
        tickers_a = search_list.find_elements(By.TAG_NAME, 'a')
        tickers_filter, companies = get_tickers()
        
        for el in tickers_a: # московская биржа может быть не первой в списке. пример тинькофф - TCS Group
            stock_ticker = el.get_attribute('data-chpurl').split('/') # пара (биржа/тикер)
            
            if stock_ticker[0] == 'moex' and stock_ticker[1].upper() in tickers_filter:
                return stock_ticker[1]
    except Exception as ex:
        print(ex)

    return None


