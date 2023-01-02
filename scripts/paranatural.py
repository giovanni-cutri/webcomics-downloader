def get_first_url():
    return "https://www.paranatural.net/comic/chapter-1"


def get_title(soup):
    try:
        title = soup.select(".cc-newsheader")[0].getText()
    except IndexError:
        title = "Paranatural"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#cc-comic")
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
