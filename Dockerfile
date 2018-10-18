FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# uncomment the following line to run the contracts check
# CMD [ "scrapy", "check" ]

CMD [ "python3", "./run_crawler.py" ]