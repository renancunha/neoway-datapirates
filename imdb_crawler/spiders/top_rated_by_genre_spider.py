# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TopRatedByGenreSpider(CrawlSpider):
    """Spider to crawl the Top Rated Movies at IMDb website"""

    name = 'top_rated_by_genre_spider'

    def __init__(self, genre=None, fetch_size = 500, *args, **kwargs):
        self.total_fetched = 0
        self.genre = genre
        self.fetch_size = fetch_size
        self.start_urls = [
            'https://www.imdb.com/search/title?genres=%s&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=7D2DBK2FMRF92RDX51EQ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1' % genre,
        ]
    
    def parse(self, response):
        """
        Default callback used to scrapy the movies list and get the titles
        
        Testing Contracts:
        @url https://www.imdb.com/search/title?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=7D2DBK2FMRF92RDX51EQ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1
        @returns items 1
        @scrapes title year rating
        """
        for item in response.css('.lister-item'):
            
            # get title
            item_title = item.css('.lister-item-header a::text').extract_first()
            
            # get the year and remove parenthesis
            item_year = item.css('.lister-item-header .lister-item-year::text').extract_first()
            item_year = item_year[item_year.find("(")+1:item_year.find(")")]
            
            # get the rating
            item_rating = item.css('.ratings-bar strong::text').extract_first()

            self.total_fetched = self.total_fetched + 1
            yield {'title': item_title, 'year': item_year, 'rating': item_rating}

        next_page_url = response.css('.next-page').xpath('@href').extract_first()
        if (next_page_url is not None and self.total_fetched < self.fetch_size):
            yield scrapy.Request(response.urljoin(next_page_url))
        
