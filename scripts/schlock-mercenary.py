def get_first_url():
    return "https://www.schlockmercenary.com/2000-06-12"


def get_title(soup):
    try:
        title = soup.select(".strip-date")[0].getText().strip()
    except IndexError:
        title = "no-title"
        
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("meta[property='og:image']")
        for i in elements:
            images.append(i.attrs["content"].split("?")[0])
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = "https://www.schlockmercenary.com" + soup.select(".next-strip")[0].attrs["href"]
    except IndexError:
        next_page_url = []

    return next_page_url
