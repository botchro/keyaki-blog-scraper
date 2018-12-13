import requests
from bs4 import BeautifulSoup

baseUrl = "http://www.keyakizaka46.com"

requestUrl = baseUrl + "/s/k46o/diary/member/list?ima=0000&page=0&cd=member"
resp = requests.get(requestUrl)

soup = BeautifulSoup(resp.text, "html.parser")
articles = soup.find_all("article")

for article in articles:
    # member name, blog link
    titleTag = article.select_one(".box-ttl")
    nameObj = titleTag.select_one(".name")
    name = nameObj.text.rstrip().lstrip()
    linkObj = titleTag.select_one("a")
    title = linkObj.text
    link = baseUrl + linkObj["href"]

    # first image
    thumbnailImg = article.select_one("img")
    if thumbnailImg is None:
        imgUrl = ""
    else:
        imgUrl = baseUrl + thumbnailImg["src"]

    print(name + " " + title + " " + link + " " + imgUrl)