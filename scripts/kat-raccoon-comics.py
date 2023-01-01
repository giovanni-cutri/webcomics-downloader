def get_first_url():
    return "https://katraccoon.com/comics/behind-the-gifs/the-tragic-tale-of-jack-and-lilly"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().split(" | ")[0]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("div.content img")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://katraccoon.com" + soup.select(".pagination a")[2].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if "#" in next_page_url:
        next_page_url = []

    return next_page_url
