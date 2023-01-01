def get_first_url():
    return "https://dilbert.com/strip/1989-04-16"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("meta[property='og:image']")
        for i in elements:
            images.append(i.attrs["content"] + ".jpg")
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://dilbert.com/" + soup.select("a.js-load-comic-newer")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
