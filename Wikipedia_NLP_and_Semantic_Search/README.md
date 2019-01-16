# Semantic Search

## The Task

The task has three parts -- data collection, data exploration / algorithm development, then finally predictive modeling. 

### Part 1 -- Collection

We want you to query the wikipedia API and **collect all of the articles** under the following wikipedia categories:

* [Machine Learning](https://en.wikipedia.org/wiki/Category:Machine_learning)
* [Business Software](https://en.wikipedia.org/wiki/Category:Business_software)

The results of the query will be written to PostgreSQL tables, `page` and `category`. 

### Part 2 -- Search

Use Latent Semantic Analysis to search the pages. Given a search query, find the top 5 related articles to the search query.

### Part 3 -- Predictive Model

Build a predictive model from the data. When a new article from wikipedia comes along, predict what category the article should fall into. 

## Infrastructure

The `docker-compose.yml` file was used to build this project.



