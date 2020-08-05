import requests
from bs4 import BeautifulSoup
import csv
soup_object = []
for i in range(1,101,10):
    base_url ="https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=47"
    start_url ="&start="
    star_num =str(i)
    rest_url ='&refresh_start=0'

    URL = base_url + start_url + star_num + rest_url

    response = requests.get(URL)
    soup_object.append(BeautifulSoup(response.text,'html.parser'))
# print(soup)
for soup in soup_object:

    news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li')
# print(news_section)


    for news in news_section:
        a_tag = news.select_one('dl>dt>a')
        news_title = a_tag['title']
        news_link = a_tag['href']

        news_data ={
            'title' :news_title,
            'hyperlink':news_link
        }
        with open('./naver_news.csv','a',encoding='utf-8') as csvfile:
            fieldnames = ['title','hyperlink']
            csvwriter =csv.DictWriter(csvfile,fieldnames=fieldnames)
            csvwriter.writerow(news_data)