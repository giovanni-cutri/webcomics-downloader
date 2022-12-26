import requests
import bs4
from time import sleep


def get_first_url():
    return "https://xkcd.com/1/"


def get_images_url(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        sleep(0.5)

    global soup
    soup = bs4.BeautifulSoup(res.text, "lxml")

    images = []
    images.append("https:" + soup.select("#comic img")[0].attrs["src"])

    return images


def get_title():
    title = soup.select("#ctitle")[0].getText()
    return title

def get_next_page_url(url):
    try:
        next_page_url = "https://xkcd.com" + soup.select("ul.comicNav a[rel='next']")[0].attrs["href"]
    except:
        pass
    if "#" in next_page_url:
        next_page_url = []

    return next_page_url


def main():
    pass



if __name__ == "__main__":
    main()