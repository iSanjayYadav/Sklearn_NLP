# Semantic Search

project from Data Science Immersive at General Assembly. All work is under "project-four-work." There are six notebooks and each one is given a "part." Parts are mapped to their corresponding sections. 

## The Task

The task has three sections -- data collection, data exploration / algorithm development, then finally predictive modeling. 


### Section 1: Collection (Parts 1-4) 

Section 1 involved querying the wikipedia API and **collecting all of the articles** under the following wikipedia categories:

* [Machine Learning](https://en.wikipedia.org/wiki/Category:Machine_learning)
* [Business Software](https://en.wikipedia.org/wiki/Category:Business_software)

The results of the query were then written to PostgreSQL tables, `page` and `category`.

### Section 2 -- Search (Part 5)

Section 2 involved using Latent Semantic Analysis and Natural Language Processing to search the pages. Built a function that, given a search query, finds the top 5 related articles.


### Section 3 -- Predictive Model (Part 6)

Section 3 involved building a predictive model from the data. Specifically, when a new article from wikipedia comes along, the model predicts what category the article should fall into. 

Finally, used the model to build a script that generates a category prediction given a new wikipedia url. 

## Infrastructure

Used a `docker-compose.yml` file to build the project.



