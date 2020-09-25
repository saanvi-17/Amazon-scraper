import scrapy
from ..items import AmazonscrapeItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?k=books&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1601041042&rnid=2684818031&ref=sr_nr_p_n_publication_date_1'
    ]

    def parse(self, response):
        items = AmazonscrapeItem()

        product_name = response.css(".a-color-base.a-text-normal").css('::text').extract()
        product_author = response.css(".a-color-secondary .a-size-base.a-link-normal").css('::text').extract()
        product_price = response.css(".a-price-whole::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

