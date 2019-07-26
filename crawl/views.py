from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import re


class CrawlerView(TemplateView):
    template_name = 'crawl.html'
    domain = 'apple.com'

    def crawl(self, request_url):
        domain = self.kwargs['domain']
        emails = []
        print('===========Working on!, Wait!============')
        try:
            response = requests.get(request_url)
            new_emails = re.findall(r"[a-z0-9\.\-+_]+@" + domain, response.text)
            if new_emails:
                emails.append(new_emails)
        except:
            pass
        return emails

    def get_links(self, url):
        link_result = []
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        html_page = response.read()
        soup = BeautifulSoup(html_page, "lxml")
        for link in soup.findAll('a'):
            d = link.get('href')
            link_result.append(d)
        return link_result

    def get(self, request, *args, **kwargs):

        domain = self.kwargs['domain']

        url_d = 'https://duckduckgo.com/?q=email+"%40"+++' + domain + '+++""&ia=web&count=50&first=51'
        link_3 = self.get_links(url_d)

        url_y = 'https://in.search.yahoo.com/search?p=%5B%40"%20+%20' + domain + '%20+%20"%5D&pz=100'
        link_4 = self.get_links(url_y)

        url_ya = 'https://yandex.com/search/?text="%40"%20%20%20' + domain + '%20%20%20""&lr=20983'
        link_5 = self.get_links(url_ya)

        url_ask = "https://www.ask.com/web?q=email+" + domain + "&o=0&qo=homepageSearchBox"
        link_6 = self.get_links(url_ask)

        # links = link_3 + link_4 + link_5 + link_6
        links = link_6
        nodup_link = list(set(links))
        filtered_links = [i for i in nodup_link if re.search("http", i)]
        final_links = list(set(filtered_links))
        mails = [self.crawl(f) for f in final_links]

        final_emails = []
        for flat_lists in mails:
            for flat_list in flat_lists:
                item_list = list(set(flat_list))
                for item in item_list:
                    if item not in final_emails:
                        final_emails.append(item)
        print(final_emails)
        data = {}
        data.update({
            'domain': self.domain,
            'mails': final_emails
        })
        print(data)
        # return render(request, self.template_name, data)
        return HttpResponse(json.dumps(data), content_type='application/json')






