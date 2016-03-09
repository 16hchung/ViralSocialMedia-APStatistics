#Original: https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "INSERT KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YoutubeService = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def constructRequest(options):
  # Call the search.list method to retrieve results matching the specified query term.
  # search().list() reference: https://goo.gl/2PQauI
  search_response = YoutubeService.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()
  
  return search_response

def sampleSearchFromDocumentation(options):
  search_response = constructRequest(options)
  
  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print "Videos:\n", "\n".join(videos), "\n"
  print "Channels:\n", "\n".join(channels), "\n"
  print "Playlists:\n", "\n".join(playlists), "\n"
  
def newVideoTimeSeries(options):
  vidCounts = []
  search_response = constructRequest(options)
  
  





argparser.add_argument("--q", help="Search term", default="icebucket")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()

try:
  sampleSearchFromDocumentation(args)
except HttpError, e:
  print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)