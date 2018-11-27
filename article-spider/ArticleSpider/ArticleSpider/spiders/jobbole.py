# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        """
        调用 extract 方法
        变成一个数组值，无法进一步 xpath
        """
        create_data = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("/",".")
        title = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()').extract()[0]
        # 为什么会为空？ 包含某个 class 名称
        vote = response.xpath("//span[@class='vote-post-up']/text()")
        # 需要使用 contains 函数来调用 span 中包含的某种类名
        vote = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*？(\d+).*",fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_nums = response.xpath("//a[@href='#article-comment']/span").extract()
        match_re = re.match(".*？(\d+).*",comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        
        content = response.xpath("//div[@class='entry']").extract()[0]

        # 通过数组的方式 进行过滤
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        [element for element in tag_list if not element.endswith("评论")]
        tag = ','.join(tag_list)
        
        """
        使用 css 选择器
        """
        create_data = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("/",".")
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        content = response.css("div.entry").extract()[0]
        tags = response.css(".entry-meta-hide-on-mobile a::text").extract()[0]
        tags = ','.join(tags)





    