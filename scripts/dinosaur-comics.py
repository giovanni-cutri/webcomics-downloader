def get_first_url():
    return "https://www.qwantz.com/index.php?comic=1"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().rsplit("-", 1)[0].strip()
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
        next_page_url = "https://www.qwantz.com/" + soup.select("a[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
