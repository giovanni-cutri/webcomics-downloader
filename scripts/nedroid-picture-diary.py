def get_first_url():
    return "http://nedroid.com/2005/09/2210-whee/"


def get_title(soup):
    try:
        title = soup.select("#comic img")[0].attrs["alt"]
    except IndexError:
        title = "Nedroid Picture Diary"
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
        
    return next_page_url
