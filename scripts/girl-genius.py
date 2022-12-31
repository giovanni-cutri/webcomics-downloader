def get_first_url():
    return "https://www.girlgeniusonline.com/comic.php?date=20021104"


def get_title(soup):
    title = soup.select("#datestring")[0].getText()
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("IMG[ALT='Comic']")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a#topnext")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
