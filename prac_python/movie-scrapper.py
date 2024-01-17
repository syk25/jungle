import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.jungle

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