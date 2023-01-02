def get_first_url():
    return "https://satwcomic.com/sweden-denmark-and-norway"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"].split(" - ")[0]
    except IndexError:
        title = "Scandinavia and the World"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[itemprop='image']")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a[accesskey='n']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
