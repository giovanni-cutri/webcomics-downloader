def get_first_url():
    return "https://abstrusegoose.com/1"


def get_title(soup):
    try:
        title = soup.select("h1.storytitle")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[src*='strips']")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        links = soup.select("a")
        for i in links:
            if "Next" in i.getText():
                next_page_url = i.attrs["href"]
                break
            next_page_url = []
    except IndexError:
        next_page_url = []

    return next_page_url
