import os
import requests
from bs4 import BeautifulSoup


def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 404:
            return False
        return True
    except requests.RequestException:
        return False


def main():
    
    broken_links = []

  with open("supported-webcomics.md", "r", encoding='utf-8') as f:
    content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    links = [a.get("href") for a in soup.find_all("a", href=True)]

  for link in links:
      if link.startswith("http"):
          if not check_link(link):
              broken_links.append(link)

  if broken_links:
      with open("BROKEN_LINKS_FOUND", "w") as f:
          for link in broken_links:
                f.write(f"{link}\n")
        exit(1)


if __name__ == '__main__':
    main()
