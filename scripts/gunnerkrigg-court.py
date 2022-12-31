def get_first_url():
    return "https://www.gunnerkrigg.com/?p=1"


def get_title(soup):
    name = soup.select("h4")[0].getText()
    if name != "":
        name = name + " - "
    date = soup.select(".content")[0].getText().split(" |")[0].replace("Tom", "").strip()   
    title = name + date
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select(".comic_image")
        for i in elements:
            images.append("https://www.gunnerkrigg.com" + i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.gunnerkrigg.com/" + soup.select("a.right")[0].attrs["href"]
    except IndexError:
        next_page_url = []
    except KeyError:
        next_page_url = []

    return next_page_url
