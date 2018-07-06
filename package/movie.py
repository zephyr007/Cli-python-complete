import requests
from pprint import pprint

info="""
------------------------------------------------------------------------------------------
{tit}
Genre:{gen}
Cast:{cast}
{ratings}/10
------------------------------------------------------------------------------------------
"""

def do_movie(title):
    url = 'http://www.omdbapi.com/?t={}&apikey=2bf615e8'.format(title)
    res=requests.get(url)
    data=res.json()
    pprint(data)

#tio =input('Enter title of the Movie : ')
#do_movie(tio)