#!/usr/bin/python
"""
Obsessed with self! Want to know unique pageview on my blogs.

1. Get the urls of my blogs. Need to make a single network call for this.

2. Call GA api for a single blog and get result

3. Call it for multiple blogs using threads
"""

import requests
from BeautifulSoup import BeautifulSoup

blog_url = "http://agiliq.com/blog/author/akshar/"

def fetch_blog_content(url):
    resp = requests.get(url)
    return resp.content

def get_post_urls(content):
    soup = BeautifulSoup(content)
    #articles = soup.findAll("article")
    kwargs = {'class': 'right_panel'}
    articles = soup.findAll(**kwargs)
    links = []
    for article in articles:
        anchor = article.find("a")
        links.append(anchor.get('href'))
    return links

content = fetch_blog_content(blog_url)
urls = get_post_urls(content)
for url in urls:
    print url