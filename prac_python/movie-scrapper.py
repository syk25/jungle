import requests
from bs4 import BeautifulSoup
import re

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

responses = requests.get(url)

soup = BeautifulSoup(responses.text, "html.parser")

movies = soup.find_all("div", class_="box-contents")

# print(movies)

movies_db = []

pattern = r'\d{4}\.\d{2}\.\d{2}'

for movie in movies:
    title = movie.find("strong", class_="title").text
    score = movie.find("strong", class_="percent").find("span").text
    
    release = movie.find("span", class_="txt-info").find("strong").text
    
    match = re.search(pattern, release)
    release = match.group()
    
    link = f"http://www.cgv.co.kr{movie.find("a")["href"]}"
    
    movie = {
        "title":title,
        "score":score,
        "release":release,
        "link":link
    }
    
    movies_db.append(movie)

print(movies_db)
# 오늘 날짜

# 영화리스트
# 영화제목
# 영화 링크
# 영화 예매율
# 개봉일