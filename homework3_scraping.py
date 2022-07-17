import bs4
import requests
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'CRM', 'python']  # Change "web" on "CRM" (no match's)


def get_info_preview():
    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    header = Headers(headers=True)
    response = requests.get(url, headers=header.generate())
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for elem in articles:
        preview = elem.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        prev = [info.find('p').text for info in preview]
        for key in KEYWORDS:
            if key in str(prev):
                date = elem.find(class_='tm-article-snippet__datetime-published'
                                 ).find('time').attrs['title'].split(', ')[0]
                title = elem.find('h2').find('span').text
                link = elem.find(class_='tm-article-snippet__title-link').attrs['href']
                print(f'<{date}> - <{title}> - <{base_url+link}>')
                print()


if __name__ == '__main__':
    get_info_preview()


def get_info_article():
    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    header = Headers(headers=True)
    response = requests.get(url, headers=header.generate())
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for elem in articles:
        link = elem.find(class_='tm-article-snippet__title-link').attrs['href']
        response = requests.get(base_url+link, headers=header.generate())
        text_article = response.text
        soup2 = bs4.BeautifulSoup(text_article, features='html.parser')
        body = soup2.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        prev = [info.find_all('p') for info in body]
        for key in KEYWORDS:
            if key in str(prev):
                print('______________________________________________________')
                date = elem.find(class_='tm-article-snippet__datetime-published'
                                 ).find('time').attrs['title'].split(', ')[0]
                title = elem.find('h2').find('span').text
                link = elem.find(class_='tm-article-snippet__title-link').attrs['href']
                print(f'<{date}> - <{title}> - <{base_url+link}>')


if __name__ == '__main__':
    get_info_article()
