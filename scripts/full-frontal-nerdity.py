def get_first_url():
    return "https://ffn.nodwick.com/?p=6"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"]
    except IndexError:
        title = "Full Frontal Nerdity"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".comicpane img")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
