# Downlaod movies from console for Super lazy Lads
# (no egybest popup ads sh*t no more)
# Ceiv 21/05/2022
# enjoy :)
import os
import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Trying to Install required module: BeautifulSoup\n")
    os.system('python -m pip install BeautifulSoup4')

import webbrowser

moviesInfo = []
moviesLinks = []
movies = []

# hadnling missing search results
while True:
    # avoid empty input
    while True:
        movieName = input("Movie name >")
        if movieName != "":
            break
    # forming search link
    x = movieName.split()
    name = "+".join(x)
    result = requests.get("https://mycima.cloud/search/" + name)
    src = result.content
    soup = BeautifulSoup(src, "html.parser")

    # getting search results
    moviesInfo = soup.find_all("div", {"class": "Thumb--GridItem"})
    if len(moviesInfo) > 0:
        break
    print("No such a movie :( try again !")

# handling single or multiple serach results
if len(moviesInfo) > 1:
    for y in range(len(moviesInfo)):
        print(str(y) + " : " + moviesInfo[y].text)

    # handling wrong or non mumerical input
    while (1):
        choice = int(input("choose movie: "))
        if choice in range(len(moviesInfo)):
            break
    chosenMovie = moviesInfo[int(choice)]

    # movie download page  multiple results
    link = chosenMovie.find("a").attrs['href']
else:
    # movie download page single result
    link = moviesInfo[0].find("a").attrs['href']

# opening movie link one
result = requests.get(link)
src = result.content
soup = BeautifulSoup(src, "html.parser")
movies = soup.find_all("a", {"class": "hoverable activable"})

# getting movies links for each movie
for movie in movies:
    if "upbaam" in movie['href']:
        moviesLinks.append(movie['href'])

# listing movie links according to quality
for i in range(len(moviesLinks)):
    print(str(i) + " : " + str(moviesLinks[i]))
quality = input("choose quality > ")

# opening the download popup
webbrowser.open(moviesLinks[int(quality)])
