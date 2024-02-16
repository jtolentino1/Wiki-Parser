# Wiki-Parser

A simple Wikipedia API web-parser that takes in a search term as an argument and takes the wikipedia page for said search term and saves it as a .txt file.

### Prereqs

First must install all necessary libaries. Get started with:

```
pip install -r requirements.txt
```

### Usage

```
python3 main.py -s <searchTerm> -o <outputTextFile>

eg. python3 main.py -s entrepreneurship -o ent.txt
```

tip: if more than one word, like Business administration, use underscore like: business_administration