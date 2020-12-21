from datetime import datetime
from webapp.model import db, News
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename='work.log', level=logging.INFO)

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        logging.info('Запрос успешен')
        return result.text 
        
    except(requests.RequestException, ValueError):
        logging.info('Сетевая ошибка')
        return False

def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)

def save_news(title, url, published):
    news_news = News(title=title, url=url, published=published)
    db.session.add(news_news)
    db.session.commit()
