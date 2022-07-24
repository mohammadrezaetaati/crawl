from django.contrib import admin
from django.urls import path

from .views import Crawl, AddUrl


urlpatterns = [
    path("", Crawl.as_view(), name="creatlink"),
    path("add-url", AddUrl.as_view(), name="add-url"),
]
