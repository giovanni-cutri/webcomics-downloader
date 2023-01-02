def get_first_url():
    return "https://reallifecomics.com/comic.php/?comic=title-1"


def get_title(soup):
    try:
        title = soup.select("#date h4")[0].getText()
    except IndexError:
        title = "Real Life Comics"
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
        next_page_url = soup.select("a.comic-nav-next")[0].attrs["onclick"].replace("location.href=", "").replace("'", "").replace(";", "")
    except IndexError:
        next_page_url = []

    return next_page_url
