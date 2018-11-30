
from bs4 import BeautifulSoup
import urllib.request

def print_title(prof_name):
    '''
    :param prof_name: Given a prof name, print his pulication titles
    :return: None
    '''
    search_args = {"query": prof_name, "searchtype": "author"}
    query_params = urllib.parse.urlencode(search_args)
    url = "https://arxiv.org/search/?"+query_params
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, features="html.parser")
    count = 1
    for tag in soup.find_all("p", attrs={'class':"title is-5 mathjax"}):
        print("{0}) {1}".format(count, tag.text.strip()))
        count += 1

    if count == 1:
        print("Sorry, there are no publications")
    print("\n")

def scrape_prof_publications():
    '''
    From MIT faculty URL, scrape Prof name and then print their pub titles.
    :return:
    '''
    url = "https://www.eecs.mit.edu/people/faculty-advisors"
    # limitation: deal with reading whole page into memory.
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, features="html.parser")
    prof_count = 1
    for name_tag in soup.find_all("span", attrs={'class':"field-content card-title"}):
        prof_name = name_tag.text
        print("==== {0}) Prof. {1} ====".format(prof_count, prof_name))
        print_title(prof_name)
        prof_count += 1

scrape_prof_publications()
