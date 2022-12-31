def get_first_url():
    return "https://thegamercat.com/comic/06102011/"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"].split(" - The GaMERCaT")[0]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("meta[property='og:image']")
        for i in elements:
            images.append(i.attrs["content"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a.next-comic")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
