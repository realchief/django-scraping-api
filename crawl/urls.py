
from django.conf.urls import url
from django.urls import path
from .views import CrawlerView

urlpatterns = [
    # path('crawl/(?P<domain>)/$', CrawlerView.as_view(), name='crawl'),
    url(r'^crawl/(?P<domain>[\w/.]+)/$', CrawlerView.as_view(), name='crawl'),
]
