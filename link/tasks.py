from celery import shared_task

from .utils import read_url, get_link


@shared_task
def crawl(csv):

    get_link(read_url(csv))
