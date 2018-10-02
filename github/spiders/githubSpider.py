# -*- coding: utf-8 -*-
import re

import scrapy
import os

from ..items import GithubItem


class GithubspiderSpider(scrapy.Spider):
    name = 'githubSpider'
    allowed_domains = ['github.com']
    start_urls = ['https://www.github.com/']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resName = input("请输入需要爬取的Github用户ID：\n")
        self.start_urls = ['http://www.github.com/' + self.resName + '?tab=repositories']
        self.dirName = self.resName + '\'s Projects'

    def parse(self, response):
        if self.resName and  not os.path.exists('./'+ self.dirName):
            os.makedirs('./'+ self.dirName)
        #获取该用户所有仓库的地址
        repositoriesList = response.xpath('//div[@id="user-repositories-list"]/ul/li')
        if repositoriesList:
            for link in repositoriesList:
                url = link.xpath('.//h3/a/@href').extract_first()
                next_url = response.urljoin(url)
                languageType = ''
                try:
                    languageType = link.xpath('.//span[@class = "mr-3"]/text()').extract_first()
                    if languageType:
                        re.sub(r'\s+', '', languageType)
                        re.sub(r'\\n', '', languageType)
                        languageType = re.search(r'\w{2,}', languageType).group()
                except :
                    print("Error!\n")
                yield scrapy.Request(next_url,callback=lambda response, languageType=languageType: self.parse_repositor(response, languageType))

    def parse_repositor(self,response,languageType):
        fileUrl = response.url + "/archive/master.zip"
        #获取语言成分
        item = GithubItem()
        item['userName'] = self.resName
        if languageType:
            item['language'] = languageType
        else:
            item['language'] = 'None'

        #获取commits branches releases contributor
        numList = response.xpath('.//ul[@class = "numbers-summary"]/li')
        nums = []
        if numList:
            for num in numList:
                cnt = num.xpath('.//span/text()').extract_first()
                if cnt:
                    cnt = re.search(r'\d+',cnt).group()
                nums.append(cnt)
        item['commits'] = nums[0]
        item['branches'] = nums[1]
        item['releases'] = nums[2]
        item['contributor'] = nums[3]

        #获取star fork watch 项目名
        head = response.xpath('.//h1[@class = "public "]/strong/a/text()').extract_first()
        item['name'] = head
        item['file_urls'] = []
        item['file_urls'] = [fileUrl]
        print(item['file_urls'])

        headNums = response.xpath('.//ul[@class = "pagehead-actions"]/li/a[contains(@class,"social-count")]/text()').extract()
        headnums = []
        if headNums:
            for headNum in headNums:
                headNum = re.search(r'\d+',headNum).group()
                headnums.append(headNum)
        item['watches'] = headnums[0]
        item['stars'] = headnums[1]
        item['forks'] = headnums[2]

        yield item
