import milestone1
import milestone2
import os
import csv
import urllib.request
import json
import matplotlib.pyplot as plt

url = "https://data.buffalony.gov/resource/6xz2-syui.json"
keys = ['title', 'category', 'type', 'medium', 'frame', 'photo_url_link', 'artist', 'site', 'street_address', 'city', 'zip_code', 'state', 'latitude', 'longitude']

def cacheAndLoadData(file):
    if not os.path.isfile(file):
      response = urllib.request.urlopen(url)
      content = response.read().decode()
      data = json.loads(content)
      dataset=milestone2.convertToLists(keys, data)
      dataset.insert(0, keys)
      milestone2.writeRecords(file,dataset)
    aLists = milestone2.loadRecords(file)
    return milestone2.convertToDictionaries(keys, aLists)

def cleanData(data):
    for a_dict in data:
        for key, value in a_dict.items():
            if key == "category":
                if value == "PAINTINGS":
                    a_dict[key] = "PAINTING"
                elif value == "DECORATIVE OBJECTS":
                    a_dict[key] = "DECORATIVE OBJECT"
                elif value in ["GRAPHIC", "GRAPHICS", "GRAPHICS ARTS"]:
                    a_dict[key] = "GRAPHIC ARTS"
    return None


def plotPieForKey(key, data):
    frequencies = milestone1.computeFrequency(key, data)
    labels = frequencies.keys()
    plt.pie(frequencies.values(), labels=labels)
    plt.show()

def plotBarForKey(key, data):
    frequencies = milestone1.computeFrequency(key, data)
    plt.barh(list(frequencies.keys()), frequencies.values())
    plt.show()

def plotFilteredBarForKey(key, fkey, fval, data):
    filter_data = milestone1.filterByKey(fkey, fval, data)
    frequencies = milestone1.computeFrequency(key, filter_data)
    plt.barh(list(frequencies.keys()), frequencies.values())
    plt.show()
