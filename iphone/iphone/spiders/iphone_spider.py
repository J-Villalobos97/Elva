import scrapy

from iphone.items import IphoneItem

class IphoneSpider(scrapy.Spider):
    name = "iphone"

    allowed_domains = ['www.target.com']

    start_urls = [
        'https://www.target.com/p/apple-iphone-13-pro-max/-/A-84616123?preselect=84240109#link=sametab'
    ]

    def parse(self, response):
        iphone = IphoneItem()

        iphone['price'] = response.xpath('//div[@class="h-margin-b-x2"]/div/span/text()').extract()
        iphone['description'] = response.xpath('//div[@data-test="item-details-description"]/text()').extract()
        iphone['specifications'] = response.xpath('//div[@data-test="item-details-specifications"]/div/div/text() | //div[@data-test="item-details-specifications"]/div/div/b/text()').extract()
        iphone['highlights'] = response.xpath('//div[@class="styles__StyledRow-sc-1nuqtm0-0 viTSN"]/div/li/span/text()').extract()
        iphone['questions'] = response.xpath('//div[@class="h-margin-a-default"]/div/div/h3/span/text() | //li[@data-test="answer"]/p/span/text()').extract()
        iphone['images_urls'] = response.xpath('//div[@class="styles__CarouselProductThumbnailWrapper-sc-cwwbs3-1 kFVxiU"]/button/div/div/div/picture/img/@src').extract()
        iphone['title'] = response.xpath('//h1[@data-test="product-title"]/span/text()').extract()

        yield iphone