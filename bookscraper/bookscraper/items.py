from scrapy import Item, Field
    
class BookItem(Item):
    title = Field()
    category = Field()
    price = Field()
    upc = Field()
    image_url = Field()
    url = Field()
    pass
