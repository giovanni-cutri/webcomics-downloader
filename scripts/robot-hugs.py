def get_first_url():
    return "https://www.robot-hugs.com/comic/decision/"


def get_title(soup):
    try:
        title = soup.select("meta[property='og:title']")[0].attrs["content"]
    except IndexError:
        title = "Robot Hugs"
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
        next_page_url = soup.select(".single-comic-navigation a")[-2].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if len(soup.select(".single-comic-navigation a")) != 5 and "hourly-comic-day-2021" in next_page_url:
        next_page_url = []

    return next_page_url
