def get_first_url():
    return "https://www.xpboostcomic.com/comic/first-steps/"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"].split(" | ")[0]
    except IndexError:
        title = "Experience Boost"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("meta[property='og:image']")
        for i in elements:
            images.append(i.attrs["content"].split("?")[0])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select(".comic-nav-next")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
