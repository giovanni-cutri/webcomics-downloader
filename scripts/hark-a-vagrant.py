def get_first_url():
    return "http://www.harkavagrant.com/index.php?id=1"


def get_title(soup):
    try:
        title = soup.select("img[title]")[0].attrs["title"]
    except IndexError:
        title = "no-title"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = soup.select("img[title]")
        for i in elements:
            images.append(i.attrs["src"].strip())
    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    try:
        next_page_url = soup.select("a[style='text-decoration: none']")[1].attrs["href"]
    except IndexError:
        next_page_url = []
        
    if "403" in soup.select("a[style='text-decoration: none']")[0].attrs["href"] and "404" in soup.select("a[style='text-decoration: none']")[1].attrs["href"]:
        next_page_url = []

    return next_page_url
