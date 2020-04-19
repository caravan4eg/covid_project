# items.py
import scrapy
from scrapy_djangoitem import DjangoItem
from api.models import (
    Photo,
    Post,
    Project,
    Fact,
    Location,
)
import django
django.setup()


class PostItem(DjangoItem):
    django_model = Post


class PhotoItem(DjangoItem):
    django_model = Photo


class ProjectItem(DjangoItem):
    django_model = Project


class FactItem(DjangoItem):
    django_model = Fact

# class TenderItem(scrapy.Item):
#     number = scrapy.Field()
#     customer = scrapy.Field()
#     description = scrapy.Field()
#     price = scrapy.Field()
#     country = scrapy.Field()
#     url_addr = scrapy.Field()
#     deadline = scrapy.Field()
