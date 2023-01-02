def get_first_url():
    return "http://freefall.purrsia.com/ff100/fv00001.htm"


def get_title(soup):
    try:
        title = soup.select("title")[0].getText()
    except IndexError:
        title = "Freefall"
    return title


def get_images_url(soup):

    images = []

    try:
        elements = [soup.select("img")[0]]
        for i in elements:
            if len(i.attrs["src"].split("/")) == 1:
                number_code = "/ff" + str(int(int(soup.select("TITLE")[0].getText().split(" ")[1]) / 100) + 100) + "/"
            else:
                number_code = ""
            images.append("http://freefall.purrsia.com" + number_code + i.attrs["src"])

    except IndexError:
        pass

    return images


def get_next_page_url(soup):

    next_tag = soup.select("a")[-1]
    if next_tag.getText() == "Next":
        if len(next_tag.attrs["href"].split("/")) == 1:
            number_code = "/ff" + str(int(int(soup.select("TITLE")[0].getText().split(" ")[1]) / 100) + 100) + "/"
        else:
            number_code = ""
        try:
            next_page_url = "http://freefall.purrsia.com" + number_code + next_tag.attrs["href"]
        except IndexError:
            next_page_url = []
    else:
        next_page_url = []

    return next_page_url
