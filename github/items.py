# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class GithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    userName = Field()
    name = Field()
    watches = Field()
    stars = Field()
    forks = Field()
    commits = Field()
    branches = Field()
    releases = Field()
    contributor = Field()
    language = Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()


