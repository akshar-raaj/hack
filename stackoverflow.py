#40368
import requests
from requests.exceptions import ConnectionError
from threading import Thread
import time
from threading import Lock
from BeautifulSoup import BeautifulSoup

base_url = "http://stackoverflow.com/users/839549/akshar?tab=answers&sort=activity&page="
#base_url = "http://stackoverflow.com/users/104349/daniel-roseman?tab=answers&sort=activity&page="
stackoverflow_url = "http://stackoverflow.com"
base_page_number = 1
first_page = base_url + "1"
num_views = 0
lock = Lock()
should_wait = False

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url 
        super(GetUrlThread, self).__init__()

    def run(self):
        global num_views
        global should_wait
        try:
            if should_wait:
                time.sleep(10)
            should_wait = False
            resp = requests.get(self.url)
        except ConnectionError:
            print "Connection Error happened"
            should_wait = True
        view_count = get_view_count(resp)
        lock.acquire()
        num_views = num_views + view_count
        lock.release()


def get_view_count(question_href_resp):
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

#single_answer_list_threads = []
#class SingleAnswerListThread(Thread):
    #def __init__(self, url, number):
        #self.url = url

    #def run(self):
        #resp = requests.get(url)
        #soup = BeautifulSoup(resp.content)
        #accepted_answer_divs = soup.findAll("div", {"class": "answer-votes answered-accepted default"})

while True:
    url = base_url + str(base_page_number)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content)
    accepted_answer_divs = soup.findAll("div", {"class": "answer-votes answered-accepted default"})
    threads = []
    for accepted_answer in accepted_answer_divs:
        absolute_question_href = get_question_absolute_href(accepted_answer)
        t = GetUrlThread(absolute_question_href)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    next_page = soup.find("span", {"class": "page-numbers next"})
    if not next_page:
        break
    base_page_number = base_page_number + 1
print num_views