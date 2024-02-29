import scrapy


class SlickchartsSpiderSpider(scrapy.Spider):
    name = "slickcharts_spider"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://slickcharts.com"]

    def parse(self, response):
        def parse(self, response):
        rows = response.xpath('//table[@id="table-performance"]/tbody/tr')
        for row in rows:
            number = row.xpath('.//td[1]/text()').get()
            company = row.xpath('.//td[2]/a/text()').get()
            symbol = row.xpath('.//td[3]/a/text()').get()
            ytd_return = row.xpath('.//td[6]/text()').get()

            yield {
                'number': number,
                'company': company,
                'symbol': symbol,
                'ytd_return': ytd_return
            }
            

