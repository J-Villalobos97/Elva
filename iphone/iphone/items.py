# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IphoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    specifications = scrapy.Field()
    highlights = scrapy.Field()
    questions = scrapy.Field()
    images_urls = scrapy.Field()
    title = scrapy.Field()
