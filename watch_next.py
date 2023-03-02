# Compulsory Task 2: Semantic Similarities

# Importing spaCy library

import spacy
nlp = spacy.load('en_core_web_md')

# Planet Hulk description, from which we will base recommendations

hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

print(f"You recently watched: Planet Hulk\nDescription: " + hulk)

model_sentence = nlp(hulk)

# Opening and preparing 'movies.txt' file

movies = open("movies.txt", "r")
movies = movies.read()
movies = movies.split('\n')

similarity_scores = []

# Looping through movies to establish similarity scores vs Planet Hulk description

for sentence in movies:
    similarity = nlp(sentence[9::]).similarity(model_sentence)
    similarity_scores.append(similarity)

# Identifying most similar movie vs Planet Hulk through reverse sorting

similarity_scores.sort(reverse=True)

# Looping back through movies to print recommended movie and accompanying description

for sentence in movies:
    similarity = nlp(sentence[9::]).similarity(model_sentence)
    if similarity == similarity_scores[0]:
        print(f"\nBased on your viewing history, we recommend you watch: " + sentence[0:7] + "\nDescription: " + sentence[9::])

# Result: based off the Planet Hulk description, this program returns the result 'Movie C'