def get_first_url():
    return "https://www.penny-arcade.com/comic/1998/11/18/the-sin-of-long-load-times"


def get_title(soup):
    try:
        title = soup.select("h1")[-1].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".comic-panel img")

        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.penny-arcade.com" + soup.select("#comic-panels")[0].attrs["href"]
    except IndexError:
        next_page_url = []
    except KeyError:
        next_page_url = []
        
    return next_page_url
