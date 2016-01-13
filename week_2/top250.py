# -*- coding:utf-8 -*-
import requests
import lxml.html
from bs4 import BeautifulSoup
from openpyxl import Workbook

class Douban:
    def __init__(self):
        self.url = 'http://movie.douban.com/top250'
        self.session = requests.session()

    def collect_data(self,index):
        r = self.session.request('get',self.url,params ={'start':index})
        self.html = r.text

    def xpath_filter(self):
        doc = lxml.html.fromstring(self.html)
        movie_name = doc.xpath('//ol//a/span[1]/text()')
        movie_people = [i.strip().split('\xa0\xa0\xa0')[0][4:] for i in doc.xpath('//li//p[1]/text()[1]')]
        movice_type = [i.strip().split('\xa0/\xa0') for i in doc.xpath('//li//p[1]/text()[2]')]
        movie_star = doc.xpath("//div[@class='star']/span[2]/text()")
        self.movie_data=[list(list(zip(movie_name,movie_people,movie_star))[i])+movice_type[i] for i in range(len(movice_type))]
        return self.movie_data

    def bs_filter(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        movie_name = [i.find('span','title').string.strip() for i in soup.find_all('div','hd')]
        movie_date = [list(i.find('p').stripped_strings) for i in soup.find_all('div','bd')][1:]
        movie_people = [i[0].split('\xa0\xa0\xa0')[0][4:] for i in movie_date]
        movice_type = [i[1].split('\xa0/\xa0') for i in movie_date]
        movie_star = [i.find('span','rating_num').string.strip() for i in soup.find_all('div','star')]
        self.movie_data=[list(list(zip(movie_name,movie_people,movie_star))[i])+movice_type[i] for i in range(len(movice_type))]

    def excel_maker(self,way):
        wb = Workbook()
        dest_filename = 'top250.xlsx'
        ws1 = wb.active
        ws1.title = "top250"
        ws1.append(['片名','导演','评分','时间','国家','类型'])
        for i in range(0,250,25):
            self.collect_data(i)
            self.xpath_filter() if way == 'xpath' else self.bs_filter()
            for row in self.movie_data:
                ws1.append(row)
        wb.save(filename = dest_filename)

if __name__ == '__main__':
    a = Douban()
    a.excel_maker('xpath')
    a.excel_maker('bs')



