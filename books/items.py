# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import dataclasses

import scrapy


@dataclasses.dataclass
class BookItem:
    title: str
    price: float
    amount_in_stock: int
    rating: int
    category: str
    description: str
    upc: str
