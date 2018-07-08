import requests
from termcolor import colored

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
    content = colored(quote["contents"]["quotes"][0]["quote"],'green')
    author = colored(quote["contents"]["quotes"][0]["author"],'blue')

    print(quote_format.format(
        quote_body=content,
        quote_author=author,

    ))
