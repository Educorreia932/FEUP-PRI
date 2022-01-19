# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

QUERY_URL = "http://localhost:8983/solr/music/query?q=love&q.op=OR&defType=edismax&indent=true&qf=name%20lyrics%20artists.name%20artists.genres%20albums.name"
QUERY = 4
WEIGHT = 0

results = requests.get(QUERY_URL).json()['response']['docs']


with open('search_names_and_jsons/names_w' + str(WEIGHT) + '_q' + str(QUERY) + '.txt','w') as tf:
    for r in results:
        tf.write(r["name"])
        tf.write("\n")
