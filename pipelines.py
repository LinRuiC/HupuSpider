# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class HupuspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import scrapy
import os

class HupuspiderPipeline(object):
    def process_item(self, item, spider):
        # 新闻标题作为文件夹名字
        filename = item['newstitle']
        filename += ".txt"

        # 每条新闻放到对应的球队文件夹中
        savepath='虎扑新闻'+'/'+item['teamname']+'/'+ item['newstitle'] +'/'+filename
        fp = open(savepath, 'w',encoding='utf-8')
        fp.write(item['content'])
        fp.close()

        return item

class HupuImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageurl"]
        yield scrapy.Request(image_url[0])

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，
        # 就放到 image_path里，ImagesPipeline源码剖析可见
        image_path = [x["path"] for ok, x in results if ok]

        # 每张新闻配图放到对应的球队文件夹中
        os.rename(self.IMAGES_STORE + "/" + image_path[0],
                  self.IMAGES_STORE + "/" + item["teamname"] + "/" + item["newstitle"] + "/" + item[
                      "newstitle"] + ".jpg")

        return item

    #get_media_requests的作用就是为每一个图片链接生成一个Request对象，
    # 这个方法的输出将作为item_completed的输入中的results，
    # results是一个元组，每个元组包括(success, imageinfoorfailure)。
    # 如果success=true，imageinfoor_failure是一个字典，
    # 包括url/path/checksum三个key。



