import argparse
import importlib
import requests
import os


def main():
    args = parse_arguments()
    download(args.title)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="the title of the webcomic you want to download in snake_case")
    args = parser.parse_args()
    return args


def download(title):

    try:
        path = os.path.join(os.getcwd(), "comics", title)
        os.makedirs(path)
    except OSError:
        pass

    webcomic = importlib.import_module("scripts." + title, package=None)
    url = webcomic.get_first_url()

    counter = 1

    while 1:
        images_url = webcomic.get_images_url(url)

        for i in images_url:
            try:
                img = requests.get(i).content
                title = webcomic.get_title()
                ext = i.split(".")[-1]
                with open(path + "/" + str(counter) + " - " + title + "." + ext, 'wb') as f:
                    f.write(img)
            except:
                pass

        url = webcomic.get_next_page_url(url)

        if not url:
            break

        counter = counter + 1


if __name__ == "__main__":
    main()
