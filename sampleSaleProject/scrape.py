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
  """
The site content looks like:

<p class="lead">Tuesday through Friday, 6/4-6/7, 
  <a href="https://www.260samplesale.com/" rel="noreferrer noopener" target="_blank">260 Sample Sale 
  </a>hosts 
  <a href="http://www.montblanc.com/en-us/home.html" rel="noreferrer noopener" target="_blank">Mont Blanc
  </a>. Watches, writing instruments, leather accessories and jewelry will all be up to 80% off.
</p>

*usefulData*
</div>
<p>Mont Blanc – 260 Fifth Ave btw 28th &amp; 29th – Tues-Thurs 9am-7pm, Fri 9am-12pm – 
<a href="https://www.google.com/maps/place/260+Sample+Sale/@40.7451863,-73.9895217,17z/data=!3m1!4b1!4m5!3m4!1s0x89c259a63b66ffeb:0x85f1cf2e6ed1fa24!8m2!3d40.7451823!4d-73.987333" 
rel="noreferrer noopener" target="_blank">Map
</a>
</p>:


  """
  HEADERS = {'User-agent':'sample sale scraper - contact on twitter @j_liang_'}
  URL = 'http://www.thechoosybeggar.com'
  r = requests.get(URL, headers=HEADERS, timeout=10)

  soup = BeautifulSoup(r.text, "html5lib")

# create markerList
  markerDataList = []
  marker_list = []
  for sectionData in soup.find_all("div", class_="entry"):
    paragraphs = sectionData.find_all('p')

    if len(paragraphs) <= 1:  # skip if just one paragraph
      continue

    usefulData = paragraphs[1]
    markerText = usefulData.getText()
    
    if "am" not in markerText: # skipping this entry if there's no date
      continue

    firstWord = markerText.split(" ")[0]

    mapLink = usefulData.find('a').get('href')
    mapUrlSplit = mapLink.split("/")
    for s in mapUrlSplit:
      if s.startswith("@"):
        latLong = s.split(",")
        latitude = latLong[0][1:]
        longitude = latLong[1]
        marker_list.append("markers=size:large|label:" + firstWord +
                           "|color:0xFFFF00|" + latitude + "," + longitude + "|")
        markerDataList.append(MarkerData(
            firstWord, latitude, longitude, markerText))

  with open(filename, 'w') as outfile:
    json.dump(markerDataList, outfile, cls=MyEncoder)



saveScrapeToJson('pins.json')
