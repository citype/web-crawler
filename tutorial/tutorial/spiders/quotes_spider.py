import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
         'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    """
    以下注释代码，其只要通过参数名 start_urls 就会默认实现
    """
    # def start_requests(self):
    #     urls = [
    #          'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        将两个网页的内容保存到本地 html 文件中
        """
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log("Save file %s" % filename)
        for quote in response.css('div.quote'):
            yield {
                'text':quote.css('span.text::text').extract_first(),
                'author':quote.css('small.author::text').extract_first(),
                'tags':quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    
    """
    以上代码，只要调用命令
    scrapy shell 'http://quotes.toscrape.com/page/1/'
    就会产生默认结构。
    """

    """
    最简单的方式去保存 scrapy data:
    scrapy crawl quotes -o quotes.json
    就能看到当前文件目录下生成的 json 文件
    """