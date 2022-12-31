def get_first_url():
    return "http://brawlinthefamily.keenspot.com/comic/theshowdown/"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().split("–", 1)[-1].replace("–", "-").strip()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#comic img")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("link[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
