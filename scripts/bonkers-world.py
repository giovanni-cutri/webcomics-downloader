def get_first_url():
    return "https://bonkersworld.net/hotmail-doesnt-work-with-linux-firefox-2-0"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText()
    except IndexError:
        title = "Bonkers World"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("p img")
        for i in elements:
            images.append("https://bonkersworld.net/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://bonkersworld.net/" + soup.select("#nav")[0].attrs["data-nxt"]
    except IndexError:
        next_page_url = []
        
    if next_page_url == "https://bonkersworld.net/":
        next_page_url = []

    return next_page_url
