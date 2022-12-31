def get_first_url():
    return "https://pixietrixcomix.com/menage-a-3/for-new-readers"


def get_title(soup):
    name = soup.select(".cc-newsheader")[0].getText()
    if name != "":
        name = name + " - "
    date = soup.select(".cc-publishtime")[0].getText().split("Posted")[-1].split("at")[0].strip()   
    title = name + date
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("#cc-comic")

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
