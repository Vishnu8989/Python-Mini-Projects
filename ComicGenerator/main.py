import requests
import random
from flask import Flask

url = ""


def get_comic(num=-1):
    x = num
    if x == -1:
        x = random.randint(100, 2000)
    global url
    url = f"https://xkcd.com/{x}/info.0.json"
    print(url)
    response = requests.get(url)
    d1 = response.json()
    return d1


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main_page():
    data = get_comic()
    main = str(data['transcript']).replace('\n', "<br>")
    web = f"""
    <center>
        <h1>{data['safe_title']}</h1>
        <img src="{data['img']}" alt="{data['alt']}">
    </center>
    <br>
    <center>
    Original Link : <a href="{url}">{url}</a>
    </center>
    """
    return web


app.run(port=6002)
