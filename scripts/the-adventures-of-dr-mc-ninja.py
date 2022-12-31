def get_first_url():
    return "http://drmcninja.com/archives/comic/0p1/"


def get_title(soup):
    try:
        title = soup.select("option[selected='selected']")[0].getText() + " - " + soup.select("option[selected='true']")[0].getText() 
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#comic img")

        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("link[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    if next_page_url == "http://drmcninja.com/archives/news/dr-hastings-final-thoughts/":
        next_page_url = "http://drmcninja.com/archives/comic/33p147/"

    if next_page_url == "http://drmcninja.com/archives/news/welcome-new-reader/":
        next_page_url = []

    return next_page_url
