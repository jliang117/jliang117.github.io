from bs4 import BeautifulSoup
import urllib
import requests
import cStringIO
import json
from PIL import Image


def get_static_google_map(filename_wo_extension, center=None, zoom=None, imgsize="500x500", maptype="roadmap", markers=None ):
    """retrieve a map (image) from the static google maps server

     See: http://code.google.com/apis/maps/documentation/staticmaps/

        Creates a request string with a URL like this:
        http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap
&markers=color:blue|label:S|40.702147,-74.015794&sensor=false"""

    apiKey='AIzaSyBm3sluCWXvu-s5kZ4ZMIAkcXaY27PduHU'
    # assemble the URL
    # request =  "http://maps.googleapis.com/maps/api/js?key="+apiKey+"&"

    request = "http://maps.google.com/maps/api/staticmap?"
    # request = "http://maps.google.com/maps?"
    # base URL, append query params, separated by &
    # if center and zoom  are not given, the map will show all marker locations
    if center != None:
        request += "center=%s&" % center
        #request += "center=%s&" % "40.714728, -73.998672"   # latitude and longitude (up to 6-digits)
        #request += "center=%s&" % "50011" # could also be a zipcode,
        #request += "center=%s&" % "Brooklyn+Bridge,New+York,NY"  # or a search term
    if center != None:
        request += "zoom=%i&" % zoom  # zoom 0 (all of the world scale ) to 22 (single buildings scale)


    request += "size=%ix%i&" % (imgsize)  # tuple of ints, up to 640 by 640
    request += "maptype=%s&" % maptype  # roadmap, satellite, hybrid, terrain


    # add markers (location and style)
    if markers != None:
        for marker in markers:
                request += "%s&" % marker


    #request += "mobile=false&"  # optional: mobile=true will assume the image is shown on a small screen (mobile device)
    request += "sensor=false&"   # must be given, deals with getting loction from mobile device
    print request

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
  """docstring for MarkerData"""
  def __init__(self, title, latitude, longitude,description):
    self.title = title
    self.latitude = latitude
    self.longitude = longitude
    self.description = description

  def __json__(self):
    return{'title':self.title,'latitude':self.latitude, 'longitude':self.longitude,'description':self.description}

def convertParagraphToMarker(paragraph):
  print(paragraph)


def saveScrapeToJson(filename):
  url = 'http://www.thechoosybeggar.com'
  r = requests.get(url,timeout=10)
  soup = BeautifulSoup(r.text,"html5lib")
# print(soup.find("div", {'class':"entry"}))

#create markerList
  markerDataList = []
  marker_list = []
  for sectionData in soup.find_all("div",class_="entry"):
  # print(type(sectionData))
    #print(sectionData)
    #print('Number of paragraphs: %d' % (i))
    paragraphs = sectionData.find_all('p')
    usefulData = paragraphs[1]
    #print(usefulData)
    markerText = usefulData.getText()
    if"map" not in markerText:
      continue
    firstWord = markerText.split(" ")[0]
    # print(firstWord)
    # markerText = markerText.replace(" ","+")
    print(markerText)
    mapLink = usefulData.find('a').get('href')
  # print(mapLink)
    mapUrlSplit = mapLink.split("/")
    for s in mapUrlSplit:
    # print(s)
      if s.startswith("@"):
        latLong = s.split(",")
        latitude = latLong[0][1:]
        longitude = latLong[1]
        # print("Latitude:"+latitude)
        # print("Longitude:"+longitude)
        marker_list.append("markers=size:large|label:"+firstWord+"|color:0xFFFF00|"+latitude+","+longitude+"|")
        markerDataList.append(MarkerData(firstWord,latitude,longitude,markerText))
# for marker in marker_list:
#   print(marker)
  with open(filename,'wb') as outfile:
    json.dump(markerDataList,outfile,cls=MyEncoder)

  get_static_google_map("google_map_example3", center="manhattan",zoom=18, imgsize=(500,500), markers=marker_list)

saveScrapeToJson('scrapeJson.json')
