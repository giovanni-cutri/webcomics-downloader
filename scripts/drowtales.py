def get_first_url():
    return "https://www.drowtales.com/moonless-age/4192"


def get_title(soup):
    try:
        title = soup.select("#browser")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".maincontent img")

        for i in elements:
            images.append("https://www.drowtales.com/moonless-age/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.drowtales.com/moonless-age/" + soup.select("a.next")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
