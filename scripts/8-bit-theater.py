def get_first_url():
    return "https://www.nuklearpower.com/2001/03/02/episode-001-were-going-where/"


def get_title(soup):
    try:
        title = soup.select("div.navbar-title")[0].getText()
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
        next_page_url = soup.select("a[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
