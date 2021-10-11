# Automatic Blog writing with Deep Learning
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

I decided to scrape Blog articles from [Foxnomad](https://foxnomad.com) as this Blog has been going around for many years and the articles read as I would expect a professional blogger to write. This ws also enough to retrieve more than 2500 articles.

After exporting the data to `scrapes_text.csv` the model has to be trained.

### 2. Train the model

After finding out in `transfer_learning.ipynb`, that my GPU simply doesn't have the necessary requirements to train the model, I moved to [Google Colab Notebooks](https://colab.research.google.com/) in order to get access to more memory and also a better GPU.

With this environment I was able to perform the fine-tuning. I downloaded the notebook afterwards `finetune_GPTneo.ipynb`.

I used the `happytransformer` library as this one makes it very easy to fine-tune NLP models shared with the [huggingface community](https://huggingface.co/).

In order to compare the results I wanted to creat an interface which makes it easy to compare the results to the model without fine-tuning, but also be able to "play around" with settings of such a model.

### 3. Create the interface

I decided to go with the `Streamlit` in order to create a nice web interface to interact with the model and this is how it looks like:

![My Streamlit interface](https://github.com/MichaMichalski/spiced-final-project/raw/main/pics/mymodel_3beams.JPG "My Streamlit interface")

### 4. Conclusion

In this project I learned, that training NLP models requires a lot of resources. You need really good equipment which you rarely find in a personal computer yet some gaming PCs may have enough cumputational power to do so.
This whole discipline is moving towards cloud computing solutions as AWS or Azure in order to keep up with such demands.

I also learned, that creating high quality texts takes more effort than a "quick" fine-tune of a NLP model.

In order to achieve quality, it makes sense to take a look at companies with solutions as [Jarvis.ai](https://www.jarvis.ai/). This company is highly specialized in creating marketing texts such as blog articles, but also advertisements and many more.

In order to create high quality texts it makes sense to take a look at the approches of such company and after figuring out how they work, make some changes in order to accomplish your goals.

Feel free to check out the presentation `My_final_project_at_spiced.pdf`.

I took this project as my final presentation for my graduation at [Spiced Academy](https://www.spiced-academy.com/). Thanks for the great learning experience and the outstanding support of the amazing teachers!