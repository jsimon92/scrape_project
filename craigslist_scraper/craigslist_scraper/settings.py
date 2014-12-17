# -*- coding: utf-8 -*-

# Scrapy settings for craigslist_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'craigslist_scraper'

SPIDER_MODULES = ['craigslist_scraper.spiders']
NEWSPIDER_MODULE = 'craigslist_scraper.spiders'

ITEM_PIPELINES = ['craigslist_scraper.pipelines.MongoDBPipeline',]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "craigslist"
MONGODB_COLLECTION = "barter"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_scraper (+http://www.yourdomain.com)'
