from pathlib import Path

import scrapy


class ClassSpider(scrapy.Spider):
    name = "get_classes"

    async def start(self):
        urls = [
            "https://www.deanza.edu/schedule/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "debug.txt"
        classname = "classes: "
        for classn in response.css("#dept-select option::text").getall():
            classname += "\n" + classn
        Path(filename).write_text(classname)