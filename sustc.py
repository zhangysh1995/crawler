import scrapy


class sustc(scrapy.Spider):
    name = 'news'
    start_urls = ['http://www.sustc.edu.cn/news_events_/p/1']

    prefix = 'http://www.sustc.edu.cn/news_events_/p/'
    page = 1

    def parse(self, response):
        for block in response.css('div.block'):
            inner = block.css('div.innerTxt')
            yield {
                'title': inner.css('div.tit a::text').extract_first(),
                'abstract': inner.css('div.dig::text').extract_first()
            }
        self.page += 1
        next_page = self.prefix + str(self.page)
        # next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)