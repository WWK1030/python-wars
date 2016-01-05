# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

URL = 'http://movie.douban.com/top250'


def get_a_page(start):
    param = {'start': start}
    return requests.get(URL, param).content


def get_every_info(data):
    soup = BeautifulSoup(data)
    lis = soup.find('ol').find_all('li')
    for li in lis:
        name = li.find('span', attrs={'class': 'title'}).text
        info = li.find('div', attrs={'class': 'bd'}).text

        infos = [x.strip() for x in info.strip().split('\n') if len(x) > 0]
        infos = [x for x in infos if len(x) > 0]
        year = infos[1].split('/')[0]
        director = infos[0].split('导演:')[1].split('主演')[0]
        region = infos[1].split('/')[1]
        category = infos[1].split('/')[2]
        star = li.find('span', attrs={'class': 'rating_num'}).text
        print("name: %s, director %s, region %s, year %s, star %s, category %s" % (
            name, director, region, year, star, category))


if __name__ == '__main__':
    for i in range(0, 250, 25):
        get_every_info(get_a_page(i))
