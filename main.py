import argparse
import os
import importlib
import requests
import bs4
from time import sleep


def main():
    title = parse_arguments()
    path = os.path.join(os.getcwd(), "comics", title)
    download(path, title)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="the title of the webcomic you want to download in snake_case")
    args = parser.parse_args()
    return args.title


def download(path, title):

    # import the module for the webcomic chosen by the user
    webcomic = importlib.import_module("scripts." + title, package=None)

    make_folder(path)

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

    # downloaded comics' urls will be saved in this file
    with open(path + "/archive.txt", "a", encoding="utf-8") as output:

        while 1:

            soup = scrape_webpage(url)

            if url not in done_urls:
                done_urls.append(url)
                print("Downloading issue #" + str(counter) + "...")
                issue_title_raw = webcomic.get_title(soup)
                issue_title = clean(issue_title_raw)
                images_url = webcomic.get_images_url(soup)

                # some webcomics use multiple files for a single comic
                page_counter = ""
                if len(images_url) > 1:
                    page_counter = "-1"

                for i in images_url:
                    try:
                        img = requests.get(i, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"}).content
                        ext = i.split(".")[-1]
                        with open(path + "/" + str(counter) + " - " + issue_title + page_counter + "." + ext, 'wb') as f:
                            f.write(img)
                        if len(images_url) > 1: 
                            page_counter = "-" + str(abs(int(page_counter)) + 1)
                    except requests.exceptions.HTTPError:
                        pass

                output.write(url + "\n")
                
            url = webcomic.get_next_page_url(soup)

            # if there is not an url for the next page (i.e. the comic has ended)
            if not url:
                break

            counter = counter + 1

    print("Done.")


def make_folder(path):

    # make folder to store the webcomic
    try:
        os.makedirs(path)
    except OSError:
        pass

    
def scrape_webpage(url):

    # use default headers
    headers = requests.utils.default_headers()

    while True:

        # some webcomics (like the-gamercat) return a ChunkedEncodingError and the webpage cannot be read in its entirety
        # thus we read the webpage chunk by chunk and we store the source in this variable
        # the partial source we eventually get is sufficient to download the webcomic, as the error occurs around the last lines of the source
        source = ""
        try:
            with requests.get(url, stream=True, headers=headers) as res:
                res.raise_for_status()
                for chunk in res.iter_content(chunk_size=8192): 
                    source = source + str(chunk)
                break
        # when the ChunkedEncodingError occurs, break the loop
        except requests.exceptions.ChunkedEncodingError:
            break
        # if a HTTPError occurs (notably 429 Too Many Requests), sleep for 0.5 seconds and retry
        # also, if there is a 406 response, changing headers will fix it
        except requests.exceptions.HTTPError:
            sleep(0.5)
            headers = {"User-Agent": "XY"}
    
    # replace unicode-escape characters with the utf-8 version
    source = source.encode().decode('unicode-escape')
    soup = bs4.BeautifulSoup(source, "lxml")
    return soup


def clean(title_raw):

    # remove Windows forbidden characters for filenames
    title = title_raw.replace("<", "&lt;").replace(">", "&gt;").replace(":", "").replace('"', "'").replace("/", "-").replace("\\", "-").replace("|", "-").replace("?", "&quest;").replace("*", "&ast;")
    return title


if __name__ == "__main__":
    main()
