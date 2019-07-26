
from django.conf.urls import url
from .views import CrawlerView

urlpatterns = [
    url(r'^', CrawlerView.as_view(), name='crawl'),
]
