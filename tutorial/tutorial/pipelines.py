# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
class TutorialPipeline(object):
    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['name']:
            if item['id']:
                return item
        else:
            raise DropItem("Moissing name in %s" % item)

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('item.jl','w')
    
    def close_spider(self, spider):
        self.file.close()
    
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

        