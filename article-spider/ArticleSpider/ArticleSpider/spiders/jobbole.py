# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        获取下一页的 url 并交给 scrapy 进行下载
        1. 获取文章列表页中的文章 url 并交给解析函数进行具体字段的解析
        2. 获取下一页的 url 并交给 scrapy 进行下载，下载完成后交给 parse 函数
        """
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # Request(url=post_url,callback=self.parse_detail)
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            
            yield Request(url=parse.urljoin(response.url,post_url), meta={"front_image-url":image_url}, callback=self.parse_detail)

        # 下一页进行下载
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url,post_url), callback=self.parse_detail)

    """
    提取文章的具体字段
    """
    def parse_detail(self, response):
        title = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()').extract()[0]
        
        """
        使用 css 选择器
        """
        # 文章封面图
        front_image_url = response.meta.get(front_image_url,"")
        create_data = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("/",".")
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*？(\d+).*",fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*？(\d+).*",comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        content = response.css("div.entry").extract()[0]
        tags = response.css(".entry-meta-hide-on-mobile a::text").extract()[0]
        [element for element in tags if not element.endswith("评论")]
        tags = ','.join(tags)



    