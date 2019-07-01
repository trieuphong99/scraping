import os
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
import codecs


def clean_html_tags(html):
    """

    :param html: html
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')  # create a new bs4 object from the html data loaded
    text =''
    for article_field in soup.find_all("div", "hero--title"):
        for article in article_field.find_all("div", "text--block-content section-block-content"):
            for script in article(["script", "style"]):  # remove all javascript and stylesheet code
                script.extract()
            # get text
            text = article.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())  # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            for i in range(0, 10):
                text = text.replace(str(i), "")
            text = text.replace("\'", "\n")
            text = text.replace(",", "\n")
            text = text.replace(".", "\n")
            text = text.replace("\"", "\n")
            for i in range(0, 5):
                text = text.replace("\n\n", "\n").replace("\n ", "\n").replace(" \n", "\n")
    return text


def scraping_to_file(url,dir_path=None):
    """

    :param url: website address
    :param dir_path: dir to make new file
    :return:
    """
    html = ""

    try:
        page = requests.get(url.rstrip())        #to extract page from website
        html = page.content             #to extract html code from page
    except Exception:
        url = url.replace("https://", "http://")
        try:
            page = requests.get(url.rstrip())  # to extract page from website
            html = page.content  # to extract html code from page
        except Exception as e:
            print(e)

    try:
        text = clean_html_tags(html)

        filename = url.rstrip()
        filename = filename.replace(".", "_")
        filename = filename.replace("https://", '')
        filename = filename.replace("http://", '')
        filename = filename.replace("www", '')
        filename = filename.replace("/", "_")

        filename = filename+".txt"

        filename = dir_path+filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        f.close()
    except Exception as e:
        print(e)


def scraping(url):
    """

    :param url: website address
    :return: text
    """

    try:
        page = requests.get(url.rstrip())        #to extract page from website
        html = page.content             #to extract html code from page
        text = clean_html_tags(html)

    except Exception as e:
        print(e)

    return text


#fin = open("//home//trieuphong//Desktop//test.csv", "r")
#for i in range(0, 25):
#    line = fin.readline()
#    scraping_to_file(line, "//home//trieuphong//Desktop//")

#links = open("//home//trieuphong//PycharmProjects//new//womanandkids_link.txt", "r")
with open("//home//trieuphong//PycharmProjects//new//womanandkids_link.txt") as links:
    for ith_link in links:
        text = scraping_to_file(ith_link, "//home//trieuphong//Desktop//")


