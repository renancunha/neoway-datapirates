from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from imdb_crawler.spiders.top_rated_by_genre_spider import TopRatedByGenreSpider

# the genres available at "Top Rated Movies by Genre"
GENRES_LIST = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'drama',
               'family', 'fantasy', 'film_noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance',
               'sci_fi', 'sport', 'thriller', 'war', 'western']

# number of titles to fetch for each genre            
FETCH_SIZE  = 500 

process = CrawlerProcess(get_project_settings())

# setup a crawler for each genre available
for genre in GENRES_LIST:
    process.crawl(TopRatedByGenreSpider, genre = genre, fetch_size = FETCH_SIZE)

# start the process
process.start()