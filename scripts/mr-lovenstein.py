def get_first_url():
    return "https://www.mrlovenstein.com/comic/1"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().split(" | ")[-1]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#comic_main_image")
        for i in elements:
            images.append("https://www.mrlovenstein.com/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.mrlovenstein.com/" + soup.select(".nav_button a")[3].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if next_page_url.endswith("#"):
        next_page_url = []

    return next_page_url
