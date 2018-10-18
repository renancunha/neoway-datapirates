# Data Pirates challenge

This repository contains the solution developed to solve the Data Pirates challenge proposed by Neoway. The challenge consists to collect 500 titles (for each available genre) from The Internet Movie Database (IMDb), sorted by 'Rating' and output it as jsonl files (one for each genre).

## Requirements

1. Docker

## Description

The solution was developed in Python 3.7 using the Scrapy framework. Scrapy is an application framework for writing web spiders that crawl websites and extract data from them [[Scrapy FAQ](https://docs.scrapy.org/en/latest/faq.html)].

The spider ``TopRatedByGenreSpider`` is responsible to fetch the IMDb Top Rated Movies pages (navigate in the pagination system until getting 500 titles for each genre), collect the necessary data (the titles) and yield the crawled items in the processing pipeline. This spider receives two inputs: ````genre```` (the name of the genre to fetch) and ````fetch_size```` (number of items that must be fetched, in descending order, by 'Ratings').
In a next step, an item pipeline named ``JsonWriterPipeline`` receives the objects crawled from IMDb and save it in jsonl files.

I chose to run that application inside a Docker container in order to facilitate the development environment setup and to avoid version mismatch of Python or libraries used.

## Usage

### Build the docker image:
    docker build -t imdb_crawler .

### Run the image to crawl the data:
    docker run -v "$(pwd)/output:/usr/src/app/output" imdb_crawler

As we are running the crawler inside the Docker container, the output files are created inside it. We need to move this outside the container. To do that, I created a shared volume at the root folder of the application named ``output`` and mapped it to the container folder ``/usr/src/app/output`` (this is where the application stores the jsonl files inside the container). The ``$(pwd)/output`` at the docker run command specifies the folder where we want to get the output, at the host (our machine in that case).

## Tests

Unit tests using Scrapy is a subject of discussion. Some people say that test against fake HTML response it's not suitable to guarantee that the spiders are crawling correctly, once you need to check the real HTML state. 

The Scrapy offers an integrated way of testing your spiders by the means of contracts [[Scrapy Contracts](https://doc.scrapy.org/en/latest/topics/contracts.html)]. In this solution I used some contracts at the ``TopRatedByGenreSpider`` to check if the crawling is working good with real data. At the Dockerfile you can uncomment a CMD that runs the ``scrapy check`` command.