###########0806 최주원 강사님 라이브

import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://movie.naver.com/movie/running/current.nhn')

soup = BeautifulSoup(response.text,'html.parser')

movie = soup.select('#wrap > #container > #content>.article >.obj_section >.lst_wrap>ul>li')
# print(movie)

final_movie = []

for mo in movie:
    a_tag = mo.select_one('dl>dt>a')
    movie_title = a_tag.contents[0]
    movie_code = a_tag['href'].split('code=')[1]

    movie_data = {
        'title' : movie_title,
        'code' :movie_code
    }

    final_movie.append(movie_data)


# print(final_movie)



    # with open('./naver_movie.csv','a',encoding='utf-8') as csvfile:
    #     fieldnames = ['title','code']
    #     csvwriter =csv.DictWriter(csvfile,fieldnames=fieldnames)
    #     csvwriter.writerow(movie_data)
# 헤더스는 인증이 없으면 웬만 하면 ~필여 앖을거다

# REVIEW_URL =f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}#tab'

for movie in final_movie:
    # print(movie['code'])
    movie_code = movie['code']
    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )
    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)
    # print(response.text)
    
    soup = BeautifulSoup(response.text,'html.parser')
    # print(soup.select('body > div > div > div.score_result > ul > li'))
    # break
    review_list = soup.select('body > div > div > div.score_result > ul > li')
    count =0
    for review in review_list:
        score =''
        reple=''
        score = review.select_one('div.star_score>em').text
        
        if review.select_one(f'div.score_reple > p > spand[id = filtered_ment_{count}] > span[id=_unfold_ment{count}]'):
            reple = review.select_one(f'div.score_reple > p >span[id=_filtered_ment_{count}] >span> a')['data_src']
        else:

            reple = review.select_one(f'div.score_reple > p > span[id=_filtered_ment_{count}]').text.strip()
        
        print(score,reple)
        count+=1







