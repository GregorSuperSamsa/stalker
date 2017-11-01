# -*- coding: utf-8 -*-

from flask import Flask
import json
from olx import olx


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def scrap():
    scrapper = olx.OlxScraper()
    query = 'bbs'
    scrapper.set_query(query)
    adds = scrapper.scrap

    jason = ''
    html = ''
    html += '<br>www.olx.bg</br>'
    html += '<br>Search for: ' + query
    html += '<br><br><br>'
    for add in adds:
        html += '<table>'
        html += '<tr>' + '<td>date:     </td>' + '<td>' + add.date      + '</td></tr>'
        html += '<tr>' + '<td>headline: </td>' + '<td>' + add.headline + '</td></tr>'
        html += '<tr>' + '<td>text:     </td>' + '<td>' + add.text      + '</td></tr>'
        html += '<tr>' + '<td>location: </td>' + '<td>' + add.location  + '</td></tr>'
        html += '<tr>' + '<td>price:    </td>' + '<td>' + add.price     + '</td></tr>'
        html += '</table>'
        #html += 'image url:' + add.image_url
        html += '<img src=' + add.thumbnail + '>'
        html += '<br><br><br>'
        jason += json.dumps(add, ensure_ascii=False, default=lambda o: o.__dict__, indent=4)
    html += 'json:<br><br>'
    html += jason
    return html
# ... service calls go here

if __name__ == '__main__':
    app.run(debug = True)