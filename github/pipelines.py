# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline


class GithubPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def file_path(self, request, response=None, info=None):
        no_space_url = request.url.replace(' ', '')

        c = no_space_url.split('/')
        return c[3] + '/%s' % (c[4]) + '.zip'