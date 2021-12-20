from itemadapter import ItemAdapter
from quotes.models import Quotes

import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)

class CrawlingPipeline(object):
    def process_item(self, item, spider):
        # item.save()
        # author = clean_author(item['author'])
        # text = clean_text(item['text'])

        # Quote.objects.create(
        #     author=author,
        #     text=text,            
        # )

        # return item

        try:
            Quotes.objects.create(text=item['text'], author=item['author'])
            print("\n")
            logger.warn("Loaded quote {}".format(item['text']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item)
        return item