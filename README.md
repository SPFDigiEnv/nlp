# NLP - Natural Language Processing
App to run set of NLP tools in docker with the latest Python version and using docker bind mounts to access local source code.
See also the blog related to this repo at <https://digitalenvironment.org/natural-language-processing-vader-sentiment-analysis-with-nltk>

## Use of bind mounting
The code is implemented 'with docker bind mounting', achieved with flags set in the `docker run` command. Here the source code is held locally, but <i>referenced</i> within the container. To edit the code to make any changes, the container will reference the edited file immediately as the edits are made. The image does not need to be rebuilt first. The workflow is (1) update the docker file and rebuild the image, (2) then in the container CLI run the python script, (3) edit the local Python script and rerun in the container to see the result.

### The Dockerfile
The Dockerfile will be:

```
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
```

### Build container
To construct the docker file:<br />
`-t` = use nametag (here 'nlp')<br />
`.` = with all the files in current folder

```
docker build -t nlp .
```

### Run container
To run the docker container file, to bind mount the development code instead of copying it across:<br />
`-t` = Allocate a pseudo-tty (foreground)<br />
`-i` = Keep STDIN open (foreground)<br />
`-v` = (from):(to)     - $(pwd) means the 'current folder'<br />
`-w` = working folder
`--name` = tagged container name

```
docker run -it -v $(pwd):/code -w /code --name="natural_language_toolkit" nlp /bin/bash
```

## Running the code
Run the source code file in Docker Desktop from within the container at the CLI (command line interface). The source code can be edited locally and then just re-run in the container as below:

```
python3 nlp-nltk_classification_test.py
```
