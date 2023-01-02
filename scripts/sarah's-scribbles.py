def get_first_url():
    return "https://sarahcandersen.com/page/869"


def get_title(soup):
    title = "Sarah's Scribbles"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("article img")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://sarahcandersen.com/" + soup.select("#pagination a")[-1].attrs["href"]
    except IndexError:
        next_page_url = []

    if len(soup.select("#pagination a")) != 4 and "/page/2" in next_page_url:
        next_page_url = []

    return next_page_url
