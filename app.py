from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://lee:sparta@Cluster0.nw7w0pd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


app = Flask(__name__)





@app.route('/')
def hello_world():  # put application's code here
    return render_template('main.html')


@app.route('/Main', methods=['GET'])
def search_member():  # put application's code here
    name = request.args.get("name")
    name_list = list(db.gitDB.find({'id': name}, {'_id': False}))
    print(name_list)

    # 크롤링 영역
    #user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a
    data = requests.get(f"https://github.com/{name}?tab=repositories", headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    info = soup.select("#user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a")
    repo_list = [item.text.strip() for item in info]
    print(repo_list)
    return jsonify({'id_list': name_list, 'repo_list': repo_list})


if __name__ == '__main__':
    app.run(debug=True)
