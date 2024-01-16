from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Article:
    def __init__(self, elem) -> None:
        self.link = elem.get_attribute('href')
        span_elems = elem.find_elements(By.TAG_NAME, 'span')
        self.date = span_elems[0].text
        self.author = span_elems[1].text if len(span_elems) > 1 else ''
        self.text = ''
        self.title = ''

class FinamNewsParser:
    def __init__(self) -> None:
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument(f'user-agent={user_agent}')

        self.driver = webdriver.Chrome(options=options)
        
    def collect_news(self, ticker, start = None, end = None, maxCount = None):
        template_url = 'https://www.finam.ru/quote/moex/{}/publications/'
        url = template_url.format(ticker)
    
        if not start or not end:
            self.driver.get(url)
        else:
            url +=  "{}/{}/{}".format('date',  start, end)
            self.driver.get(url)
            stop = False
            #кликаем кнопочку "Загрузить еще", пока не получим все новости за период
            while not stop:
                try:
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[(starts-with(@class, "pointer")) and (contains(@class, "cl-blue"))]')))
                    self.driver.execute_script("finfin.local.plugin_block_item_publication_list_filter_date.loadMore(this);")
                except:
                    stop = True

        print("Getting news from:  {}".format(url))
        links_section = self.driver.find_element(By.ID, 'finfin-local-plugin-block-item-publication-list-filter-date-content')
        a_elems = links_section.find_elements(By.TAG_NAME, 'a')

        articles = list(map(lambda elem: Article(elem), a_elems))

        for id, article in enumerate(articles):
            if maxCount is not None and id == maxCount:
                return articles[:maxCount]
    
            self.driver.get(article.link)
            try:
                title_section = self.driver.find_element(By.TAG_NAME, 'h1')
                article.title = title_section.text

                text_section = self.driver.find_element(
                    By.XPATH, 
                    '//div[(starts-with(@class, "finfin-local-plugin-publication-item-item-")) and (contains(@class, "-text"))]'
                )
                
                p_elems = text_section.find_elements(By.TAG_NAME, 'p')
                p_elems_text = list(map(lambda elem: elem.text, p_elems))

                if len(p_elems_text):
                    article.text = ' '.join(p_elems_text)
            except:
                print('Couldnt parse article from href: {}'.format(article.link))
        
        return articles