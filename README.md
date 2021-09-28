# Spiced Academy - Final Project
## How AI can make money online

![How AI can make money online](https://github.com/MichaMichalski/spiced-final-project/raw/main/pics/How_to_Make_Money_online.png "How AI can make money online")

This project was highly inspired by Youtube videos with titles as "How to make money online".
Within these videos serveral aspects on how to earn some money on the side are shown. Almost every single one of these shows "blogging" as a viable way to earn money.

This means putting up a simple website in which you can write blog articles about whatever topic you are interested in, your "niche".

In this project I am going to find out wether it's possible to train a Deep Learning model in order to write blog articles related to traveling.

### 1. Get the Data

In the Notebook `scrape_it_all.ipynb` I used following packages...:

  * `bs4` also known as `BeautifulSoup`
  * `requests` in order to execute http requests
  * `newspaper3k` to extract the Article only
  * `psycopg2` to insert the data in a locally hosted `PostgreSQL` database

I decided to scrape Blog articles from [Foxnomad](https://foxnomad.com) as this Blog has been going around for many years and the articles read as I would expect a professional blogger to write.

After exporting the data to `.csv` the model has to be trained.

### 2. Train the model
