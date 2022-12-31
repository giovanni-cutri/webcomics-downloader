def get_first_url():
    return "https://www.giantitp.com/comics/oots0001.html"


def get_title(soup):
    try:
        title = soup.select("b")[-1].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("td[align='center'] img")

        for i in elements:
            source = i.attrs["src"]
            if "comics/" in source:
                images.append(source)
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.giantitp.com" + soup.select("td[align='center'] a")[5].attrs["href"]
    except IndexError:
        next_page_url = []
    
    if "/comics" not in next_page_url:
        next_page_url = "https://www.giantitp.com" + "/comics/" + soup.select("td[align='center'] a")[5].attrs["href"]

    current_comic_number = soup.select("td[align='center'] img")[7].attrs["src"].split("oots/")[-1].split("_")[0]

    if current_comic_number in next_page_url:
        next_page_url = []

    return next_page_url
