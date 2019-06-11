from bs4 import BeautifulSoup
import requests
import json
import os


class MyEncoder(json.JSONEncoder):
  """
  JSONEncoder subclass that leverages an object's `__json__()` method,
  if available, to obtain its default JSON representation.

  """

  def default(self, obj):
    if hasattr(obj, '__json__'):
      return obj.__json__()
    return json.JSONEncoder.default(self, obj)


class MarkerData():

  def __init__(self, title, latitude, longitude, description):
    self.title = title
    self.latitude = latitude
    self.longitude = longitude
    self.description = description

  def __json__(self):
    return{'title': self.title, 'latitude': self.latitude, 'longitude': self.longitude, 'description': self.description}




def saveScrapeToJson(filename):
  HEADERS = {'User-agent':'sample sale scraper - contact on twitter @j_liang_'}
  URL = 'http://www.thechoosybeggar.com'
  r = requests.get(URL, headers=HEADERS, timeout=10)

  soup = BeautifulSoup(r.text, "html5lib")

# create markerList
  markerDataList = []
  marker_list = []
  for sectionData in soup.find_all("div", class_="entry"):
    print(type(sectionData))
    print(sectionData)
    paragraphs = sectionData.find_all('p')

    if len(paragraphs) <= 1:  # skip if just one paragraph
      continue

    usefulData = paragraphs[1]
    print("Found Paragraph %s:" % usefulData)
    markerText = usefulData.getText()
    #print("MarkerText: %s" % markerText)
    if "am" not in markerText:
      continue
    firstWord = markerText.split(" ")[0]
    # print(firstWord)
    # markerText = markerText.replace(" ","+")
    mapLink = usefulData.find('a').get('href')
  # print(mapLink)
    mapUrlSplit = mapLink.split("/")
    for s in mapUrlSplit:
      print(s)
      if s.startswith("@"):
        latLong = s.split(",")
        latitude = latLong[0][1:]
        longitude = latLong[1]
        # print("Latitude:"+latitude)
        # print("Longitude:"+longitude)
        marker_list.append("markers=size:large|label:" + firstWord +
                           "|color:0xFFFF00|" + latitude + "," + longitude + "|")
        markerDataList.append(MarkerData(
            firstWord, latitude, longitude, markerText))

  with open(filename, 'w') as outfile:
    json.dump(markerDataList, outfile, cls=MyEncoder)



saveScrapeToJson('pins.json')
