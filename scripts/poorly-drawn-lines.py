def get_first_url():
    return "https://poorlydrawnlines.com/comic/hardly-essayists/"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().split("– ")[-1]
    except IndexError:
        title = "Poorly Drawn Lines"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[decoding='async']")
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
