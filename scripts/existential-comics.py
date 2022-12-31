def get_first_url():
    return "https://existentialcomics.com/comic/1"


def get_title(soup):
    try:
        title = soup.select("h3")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".comicImg")
        for i in elements:
            images.append("https:" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        tag = soup.select(".nav-table td")[3]
        if "a href" in str(tag):
            link = str(tag).split('a href="')[-1].split('">')[0]
            next_page_url = "https://existentialcomics.com/" + link
        else:
            next_page_url = []
    except IndexError:
        next_page_url = []

    return next_page_url
