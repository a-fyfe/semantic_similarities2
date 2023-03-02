# semantic_similarities2

## Semantic Similarities Pt2

**Overview:

A simple Python project using NLP to make a movie recommendation based on an inputted description
of a previously watched movie.

## Contents

* 1. Installation
* 2. Features

## 1. Installation

This project makes use of a Dockerfile to allow interested parties to run the watch_next.py file correctly.

The Dockerfile will execute the watch_next.py file's various requirements, as seen in requirements.txt

These include the use of the spaCy library.

For information on how to use Docker to deploy this web app, please refer to the following guide: 

https://www.devteam.space/blog/how-to-deploy-a-web-app-with-docker-containers/


## 2. Features

Run the watch_next.py file to see how from a provided movie description (in this case, one matching
'Planet Hulk'), a recommendation can be made from a list of movies and associated descriptions 
(stored in movies.txt).
