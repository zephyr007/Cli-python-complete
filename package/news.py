import requests
from pprint import pprint

res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=e5a1249e520c4357829f91ff154b362e")


def printed(rep):
    for art in rep.get("articles", []):
        title = art.get("title", "N/A")
        au = art.get("author", "N/A")
        time = art.get("publishedAt", "N/A")
        desc = art.get("description", "N/A")
        ui = """
-----------------------------------------------------------------------------------------------------------
   {ti}
   
   By :{au}
   At:{tim}

   {de}

-----------------------------------------------------------------------------------------------------------""".format(ti=title, au=au, tim=time, de=desc)
        print(ui)
        #pprint(art)
        q = input("Press any key to next News Or q to Quit \n")

        print()
        if (q == "q"):
            break


def do_news():
    data = res.json()
    printed(data)
