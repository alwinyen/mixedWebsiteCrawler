import scrapy
class TaiwaninsightPoliticsSpider(scrapy.Spider):
    name = 'taiwaninsightPoliticsSpider'
    start_urls = ['https://taiwaninsight.org/category/politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.entry-title a::text')[0].get(),
                'content': post.css('.entry-content p::text')[0].get(),
                'image': post.css('img::attr(src)').extract(),
                'url': post.css('.entry-title a::attr(href)').extract(),
            }