def get_first_url():
    return "https://loadingartist.com/comic/born/"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"]
    except IndexError:
        title = "Loading Artist"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("source")
        for i in elements:
            if i.attrs["srcset"].startswith("/comic"):
                images.append("https://loadingartist.com" + i.attrs["srcset"].split(" ")[0])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://loadingartist.com/" + soup.select("a[title='Next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    return next_page_url
