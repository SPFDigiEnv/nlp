# Dockerfile - nltk
FROM python:latest
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Obtain the data modules - see https://www.py4u.net/discuss/222913
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader maxent_ne_chunker
RUN python -m nltk.downloader words
RUN python -m nltk.downloader movie_reviews
RUN python -m nltk.downloader stopwords
