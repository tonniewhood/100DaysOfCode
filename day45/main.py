
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in titles]
titles = titles[::-1]

print(titles)

with open("movies.txt", mode="w") as file:

    for title in titles:
        
        new_title = ""

        for char in title: 
            try:
                new_title += char.encode("ascii", "ignore").decode("ascii")
            except UnicodeEncodeError:
                new_title += ""

        file.write(f"{new_title}\n")

