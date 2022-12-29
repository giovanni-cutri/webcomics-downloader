import argparse
import os
import importlib
import requests
import bs4
from time import sleep


def main():
    title = parse_arguments()
    path = os.path.join(os.getcwd(), "comics", title)
    make_folder(path)
    download(path, title)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="the title of the webcomic you want to download in snake_case")
    args = parser.parse_args()
    return args.title


def make_folder(path):

    # make folder to store the webcomic
    try:
        os.makedirs(path)
    except OSError:
        pass


def download(path, title):

    # import the module for the webcomic chosen by the user
    webcomic = importlib.import_module("scripts." + title, package=None)

    url = webcomic.get_first_url()

    # keep track of the issue number
    counter = 1

    done_urls = []

    # check if some issues of the comic have already been downloaded
    try:
        with open(path + "/archive.txt", "r", encoding="utf-8") as f:
            done_urls = f.read().splitlines()
    except OSError:
        pass

    # if there are already some issues, start from the last one and go from there
    if done_urls:
        url = done_urls[-1]
        counter = len(done_urls)

    with open(path + "/archive.txt", "a", encoding="utf-8") as f:

        while 1:

            soup = scrape_webpage(url)

            if url not in done_urls:
                done_urls.append(url)
                print("Downloading issue #" + str(counter) + "...")
                issue_title = webcomic.get_title(soup)
                images_url = webcomic.get_images_url(soup)

                page_counter = ""
                if len(images_url) > 1:
                    page_counter = "-1"

                for i in images_url:
                    try:
                        img = requests.get(i).content
                        ext = i.split(".")[-1]
                        with open(path + "/" + str(counter) + " - " + issue_title + page_counter + "." + ext, 'wb') as f:
                            f.write(img)
                        if len(images_url) > 1: 
                            page_counter = "-" + str(abs(int(page_counter)) + 1)
                    except requests.exceptions.HTTPError:
                        pass

                f.write(url + "\n")
                
            url = webcomic.get_next_page_url(soup)

            # if there is not an url for the next page (i.e. the comic has ended)
            if not url:
                break

            counter = counter + 1

    print("Done.")


def scrape_webpage(url):

    while True:

        try:
            res = requests.get(url)
            res.raise_for_status()
            break
        except requests.exceptions.HTTPError:
            sleep(0.5)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    return soup


if __name__ == "__main__":
    main()
