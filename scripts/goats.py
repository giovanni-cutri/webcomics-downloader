def get_first_url():
    return "https://goats.com/comic/2003/11/01/one-true-god/"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = [soup.select("meta[property='og:image']")[-1]]
        for i in elements:
            images.append(i.attrs["content"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("link[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    return next_page_url
