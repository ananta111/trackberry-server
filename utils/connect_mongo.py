import urllib

from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connnect_mongo():
    url = urllib.parse.quote_plus("mongodb+srv://bhujasTestUser:motekomomo@123@bhujastest.bxjmr.mongodb.net/track-berry?retryWrites=true&w=majority")
    client = MongoClient(
        url,
        server_api=ServerApi('1'))
    db = client.test