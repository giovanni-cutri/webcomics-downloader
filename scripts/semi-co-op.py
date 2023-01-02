def get_first_url():
    return "https://www.semicoop.com/comic/no-system/"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().split(" • ")[0]
    except IndexError:
        title = "Semi Co-op"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".webcomic-image img")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a.next-webcomic-link")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    current_url = soup.select("link[rel='canonical']")[0].attrs["href"]

    if next_page_url == current_url:
        next_page_url = []

    return next_page_url
