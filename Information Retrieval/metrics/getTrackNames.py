# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

QUERY_URL = "http://localhost:8983/solr/music/query?q=live&q.op=OR&defType=edismax&indent=true&qf=name%5E3%20lyrics%5E5%20artists.name%20artists.genres%20albums.name"

results = requests.get(QUERY_URL).json()['response']['docs']


with open('names.txt','w') as tf:
    for r in results:
        tf.write(r["name"])
        tf.write("\n")