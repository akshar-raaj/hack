#40350
import requests
from threading import Thread
from BeautifulSoup import BeautifulSoup

base_url = "http://stackoverflow.com/users/839549/akshar?tab=answers&sort=activity&page="
stackoverflow_url = "http://stackoverflow.com"
base_page_number = 1
first_page = base_url + "1"
num_views = 0

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url 
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = get_single_question_response(self.url)
        return resp


def get_view_count(question_soup):
    """
    Give a BS instance containing response of a SO question page
    Find the view count on this page
    """
    question_soup = BeautifulSoup(question_href_resp.content)
    paras = question_soup.findAll("p", {'class': 'label-key'})
    view_count_para = paras[3]
    view_string = view_count_para.find("b").text
    view_count = int(view_string.replace(' times', ''))
    return view_count

def get_question_absolute_href(accepted_answer):
    """
    Given an accepted answer div
    Find the link of the question associated with that div
    """
    onclick = accepted_answer.attrs[0]
    href = onclick[1]
    quoted_href = href.split("=")[1]
    actual_relative_href = quoted_href.replace("'", "")
    question_href = actual_relative_href.split("#")[0]
    absolute_question_href = stackoverflow_url + question_href
    return absolute_question_href

def get_single_question_response(url):
    print url
    return requests.get(url)

while True:
    url = base_url + str(base_page_number)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content)
    accepted_answer_divs = soup.findAll("div", {"class": "answer-votes answered-accepted default"})
    threads = []
    for accepted_answer in accepted_answer_divs:
        absolute_question_href = get_question_absolute_href(accepted_answer)
        question_href_resp = get_single_question_response(absolute_question_href)
        view_count = get_view_count(question_href_resp)
        num_views = num_views + view_count
    break
    next_page = soup.find("span", {"class": "page-numbers next"})
    if not next_page:
        break
    base_page_number = base_page_number + 1
print num_views