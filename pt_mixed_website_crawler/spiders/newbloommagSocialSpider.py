import scrapy
class NewbloommagSocialSpider(scrapy.Spider):
    name = 'newbloommagSocialSpider'
    start_urls = ['https://newbloommag.net/category/main/social-movements/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.cb-post-title a::text')[0].get(),
                'content': post.css('.cb-excerpt ::text')[0].get(),
                'image': post.css('.cb-mask img::attr(src)').extract(),
                'url': post.css('.cb-mask a::attr(href)').extract(),
            }