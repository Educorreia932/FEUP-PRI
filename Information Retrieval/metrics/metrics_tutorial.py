from unittest import result
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import requests
import urllib
import json

from sklearn.metrics import PrecisionRecallDisplay

colors = [
    "#1F3F2A", 
    "#1FDF6F", 
    "#1DB954", 
    "#098E2A",
]

sb.set_palette(sb.color_palette(colors))

#QRELS_FILE = "data/relevant.txt"


# Read qrels to extract relevant documents
#relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))

#relevant_list_attribute = "name"

# Read qrels to extract relevant documents
#relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
#results = requests.get(QUERY_URL).json()['response']['docs']

systems = [
    "name lyrics artists.name artists.genres albums.name",
    "name^5 lyrics^3 artists.name^1 artists.genres albums.name^3",
    "name^1 lyrics^3 artists.name artists.genres^5 albums.name",
    "name^3 lyrics^5 artists.name artists.genres albums.name"
]

#_, ax = plt.subplots(figsize=(10, 10))

#interpolated_precision = []
#interpolated_recall = []

for i, system in enumerate(systems):
    # Get query results from Solr instance
    qf = urllib.parse.quote(system)
    query_url = f"http://localhost:8983/solr/music/select?defType=edismax&df=name%2Clyrics%2Cartists.name%2Cartists.genre&indent=true&q.op=OR&q=love&qf={qf}&wt=json&rows=20"

    #results = requests.get(query_url).json()#['response']#['docs']

    with open(str(i) + ".json", "w") as outfile:
        json.dump(requests.get(query_url).json(), outfile)