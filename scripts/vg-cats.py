def get_first_url():
    return "https://www.vgcats.com/comics/?strip_id=0"


def get_title(soup):
    title = "VG Cats!"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("td img[src^='images/']")
        for i in elements:
            images.append("https://www.vgcats.com/comics/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.vgcats.com/comics/" + soup.select("a[href='http://www.vgcats.com/archive/'] + a")[-1].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
