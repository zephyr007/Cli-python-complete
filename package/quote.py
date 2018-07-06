import requests
import sys

url = ('http://quotes.rest/qod.json')

quote_format = """
 ----------------------------------
|         Quote of the day         |
 ----------------------------------
 {quote_body}\n
                    \t\t-by : {quote_author}

"""


def do_quote():
    response = requests.get(url)
    quote = response.json()
    content = quote["contents"]["quotes"][0]["quote"]
    author = quote["contents"]["quotes"][0]["author"]

    print(quote_format.format(
        quote_body=content,
        quote_author=author,

    ))
