
from django.conf.urls import url
from django.urls import path
from .views import CrawlerView

urlpatterns = [
    path('crawl', CrawlerView.as_view(), name='crawl'),
]
