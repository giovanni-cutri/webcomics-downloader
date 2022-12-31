def get_first_url():
    return "https://questionablecontent.net/view.php?comic=1"


def get_title(soup):
    title = "Questionable Content"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#strip")

        for i in elements:
            images.append("https://questionablecontent.net" + i.attrs["src"][1:])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://questionablecontent.net/" + soup.select("#comicnav a")[2].attrs["href"]
    except IndexError:
        next_page_url = []

    if "#" in next_page_url:
        next_page_url = []

    return next_page_url
