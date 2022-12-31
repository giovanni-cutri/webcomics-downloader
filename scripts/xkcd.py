def get_first_url():
    return "https://xkcd.com/1/"


def get_title(soup):
    try:
        title = soup.select("#ctitle")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#comic img")
        for i in elements:
            images.append("https:" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://xkcd.com" + soup.select("a[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if "#" in next_page_url:
        next_page_url = []

    return next_page_url
