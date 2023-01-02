def get_first_url():
    return "https://www.1111comics.me/comic/unfinished/"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText()
    except IndexError:
        title = "1111 Comics"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".cms img")
        for i in elements:
            images.append("https://www.1111comics.me/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.1111comics.me/" + soup.select(".pl2 a")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    return next_page_url
