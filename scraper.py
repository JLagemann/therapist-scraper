import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         "https://quotes.toscrape.com/tag/humor/",
#     ]

#     def parse(self, response):
#         for quote in response.css("div.quote"):
#             yield {
#                 "author": quote.xpath("span/small/text()").get(),
#                 "text": quote.css("span.text::text").get(),
#             }

#         next_page = response.css('li.next a::attr("href")').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)
# def table_parser(therapist_table):
#     return therapist_table.split("<p>")

def remove_css_elements(str):
    str = str.replace("<p>", "")
    str = str.replace("</p>", "")
    str = str.replace("<span>", "")
    str = str.replace("</span>", "")
    str = str.replace("<br>", "")
    str = str.replace("\r", "")
    str = str.replace("\n", "")
    str = str.replace("  ", "")
    return str

class EMDRSpider(scrapy.Spider):
    name = "emdr"
    start_urls = ["https://emdr-es.org/Terapeutas",
                  ]

    def parse(self, response):
        for therapist_table in response.css("div.resultado-busquedas-modulo"):
            # print(table_parser(therapist_table))
            yield {
                "Psicologo": therapist_table.css("h4 > span::text").extract(),
                "Detalles": [remove_css_elements(s) for s in therapist_table.css("p").extract()]
                # "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.PagedList-skipToNext a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
