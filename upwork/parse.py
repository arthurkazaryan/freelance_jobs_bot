import requests
from bs4 import BeautifulSoup
from pathlib import Path

url = 'https://www.upwork.com/nx/jobs/search/?ontology_skill_uid=1031626730405085184&sort=recency'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}


def prepare_message():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    messages = []
    print(soup)
    with open(Path.cwd().joinpath('./found_jobs.txt'), 'r') as title_file:
        titles = title_file.read().split('\n')
    with open(Path.cwd().joinpath('./found_jobs.txt'), 'a') as title_file:
        for section in soup.find_all('section', class_='air-card air-card-hover job-tile-responsive'):
            link = 'https://www.upwork.com' + section.h4.a.attrs['href']
            title = section.h4.a.text.strip()
            description = section.find('span', class_='js-description-text').text.strip().replace(';', '.')
            location = section.find('span', class_='d-none ff-location').text.strip()
            try:
                price = section.find('div', class_='col-xs-6 col-sm-3 col-md-3 m-md-bottom').span.text.strip()
            except AttributeError:
                price = 'no_data'
            payment_type = section.find('div', class_='col-xs-6 col-sm-3 col-md-3 m-md-bottom').small.text.strip()
            categories = []
            for category in section.find_all('span', class_='js-skill d-inline-block'):
                categories.append(category.text.strip())
            categories = ', '.join(categories)
            if title not in titles:
                messages.append(f'{link}\n\U0001f4bcTitle: {title}\n\U0001f5c4Categories: {categories}\n\U0001f9feDescription: {description}\n\U0001f30dLocation: {location}\n\U0001f4b0Payment type: {payment_type}\n\U0001f4b5Price: {price}')
                title_file.write(f'{title}\n')

    return messages

print(prepare_message())
