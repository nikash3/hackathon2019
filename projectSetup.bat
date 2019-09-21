pip install virtualenv
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
pip install pyresparser
python -m spacy download en_core_web_sm
python -m nltk.downloader words
python -m nltk.downloader stopwords
pythonrun.py