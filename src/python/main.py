import os
from google.transit import gtfs_realtime_pb2
import requests

REALTIME_FEED_URL = 'http://rtcws.rtcsnv.com/gtfrt/tripUpdates.pb'


def known_good():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(REALTIME_FEED_URL)
    feed.ParseFromString(response.content)
    for entity in feed.entity:
      if entity.HasField('trip_update'):
        print(entity.trip_update)


known_good()
