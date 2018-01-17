# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from officespider.items import OfficespiderItem


class CentanetSpider(scrapy.Spider):
    """docstring for QuoteSpider."""

    name = "centanet"

    start_urls = [
        'http://sz.centanet.com/xiezilou/chuzu/g1/',
    ]

    def parse(self, response):
        for quote in response.css('div.result-cont ul.result-lists li.list'):
            yield {
                '标题': quote.css('h2 a::text').extract_first(),
                '地址': quote.css('span.add_text::text').extract_first(),
                '面积': quote.css('span.size').css('b::text').extract_first(),
                '价格': quote.css('div.price b::text').extract_first(),
            }

        next_page = response.css('a.nextpage::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
