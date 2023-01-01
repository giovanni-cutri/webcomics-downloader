def get_first_url():
    return "https://cad-comic.com/comic/nice-melon/"


def get_title(soup):
    try:
        title = soup.select("h3")[0].getText()
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[style='max-width:100%; min-width:270px; height:auto;']")
        for i in elements:
            images.append(i.attrs["src"])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a[rel='next']")[0].attrs["href"]
    except IndexError:
        next_page_url = []
        
    return next_page_url
