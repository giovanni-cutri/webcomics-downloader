def get_first_url():
    return "https://www.egscomics.com/comic/2002-01-21"


def get_title(soup):
    try:
        title = soup.select("img#cc-comic")[0].attrs["title"]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img#cc-comic")

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
