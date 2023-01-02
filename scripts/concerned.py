def get_first_url():
    return "http://www.screencuisine.net/hlcomic/index.php?date=2005-05-01"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText()
    except IndexError:
        title = "Concerned"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[src*='comics']")
        for i in elements:
            images.append("http://screencuisine.net/hlcomic/" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "http://screencuisine.net/hlcomic/" + soup.select("table td a")[-2].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if len(soup.select("table td a")) == 6 and "date=2006-10-31" in next_page_url: 
        next_page_url = []

    return next_page_url
