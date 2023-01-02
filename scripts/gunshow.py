def get_first_url():
    return "https://www.gunshowcomic.com/1"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText().rsplit(" - ", 1)[-1].strip()
    except IndexError:
        title = "Gunshow"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img.strip")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.gunshowcomic.com/" + soup.select(".snavb a")[-2].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if len(soup.select(".snavb a")) != 10 and "899" in next_page_url:
        next_page_url = []

    return next_page_url
