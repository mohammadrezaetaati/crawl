from django.db import models


class Crawler(models.Model):

    url_page = models.CharField(max_length=1000, null=True, blank=True)
    url = models.JSONField(null=True, blank=True)
    img = models.JSONField(null=True, blank=True)
    count_url = models.IntegerField(null=True, blank=True)
    count_img = models.IntegerField(null=True, blank=True)
    time_crawl = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.url_page


class Images(models.Model):

    crawler = models.ForeignKey(Crawler, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.image
