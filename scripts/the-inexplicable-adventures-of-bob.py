def get_first_url():
    return "https://bobadventures.thecomicseries.com/comics/1"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("meta[property='og:image']")

        for i in elements:
            images.append(i.attrs["content"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://bobadventures.thecomicseries.com/" + soup.select(".comic-button-single a")[-2].attrs["href"] + "/"
    except IndexError:
        next_page_url = []
    
    current_url = "https://bobadventures.thecomicseries.com/" + soup.select("option[selected='selected']")[0].attrs["value"]
    
    if next_page_url == current_url:
        next_page_url = []

    return next_page_url
