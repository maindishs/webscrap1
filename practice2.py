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
headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=M3LUAGP45ABV6; NRTK=ag^#all_gr^#1_ma^#-2_si^#0_en^#0_sp^#0; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NM_VIEWMODE_AUTO=basic; nx_ssl=2; page_uid=UynPedprvhGsslEozqRssssss04-127520; NM_THUMB_PROMOTION_BLOCK=Y; BMR=s=1596506677761^&r=https^%^3A^%^2F^%^2Fm.blog.naver.com^%^2Fllhbum^%^2F221785604032^&r2=https^%^3A^%^2F^%^2Fwww.google.com^%^2F; csrf_token=972fbe65-2ba0-47f2-b0f2-412716d3d933',
}

for movie in final_movie_data:
    movie_code = movie['code']
    REVIEW_URL =f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}#tab'
    params = (
        ('code', movie_code),
        ('type', 'after^'),
        ('isActualPointWriteExecute', 'false^'),
        ('isMileageSubscriptionAlready', 'false^'),
        ('isMileageSubscriptionReject', 'false'),
    )
    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

        # print(review_response.text)
    soup = BeautifulSoup(response.text,'html.paser')

    print(soup.select('body > div > div > div.score_result > ul > li')  