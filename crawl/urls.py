
from django.conf.urls import url
from .views import CrawlerView

urlpatterns = [
    url(r'crawl/', CrawlerView.as_view(), name='crawl'),
]
