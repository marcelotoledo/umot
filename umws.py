# umws.py --- umot web service server

# Copyright  (C)  2015  Marcelo Toledo <marcelo@marcelotoledo.com>

# Version: 1.0
# Keywords: 
# Author: Marcelo Toledo <marcelo@marcelotoledo.com>
# Maintainer: Marcelo Toledo <marcelo@marcelotoledo.com>
# URL: http://

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# Commentary: 

# Methods

# Websites

# GET  /api/v1.0/websites
# GET  /api/v1.0/websites/<int:website_id>
# POST /api/v1.0/websites/

# Link

# POST /api/v1.0/links/
# GET  /api/v1.0/links/search/?q=url

# Code:

from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import abort
from flask import url_for
import db
import model

app = Flask(__name__)

@app.route('/api/v1.0/websites', methods=['GET'])
def get_websites():
    results = db.session.query(model.Website).order_by(model.Website.id).all()

    json_results = []
    for r in results:
        d = {'id': r.id,
             'website': r.website }
        json_results.append(d)

    return jsonify(websites=json_results)

@app.route('/api/v1.0/websites/<int:website_id>', methods=['GET'])
def get_website(website_id):
    try:
        website = db.session.query(model.Website).filter_by(id = website_id).first()    
        d = {'id': website.id,
             'website': website.website }

        return jsonify(websites=d)
    except:
        return jsonify({"message": "Website could not be found."}), 404

@app.route('/api/v1.0/websites/', methods=['POST'])
def create_website():
    if not request.json or not 'website' in request.json:
        return jsonify({"message": "Missing required parameter."}), 400
       
    n = model.Website(website=request.json['website'])
    db.session.add(n)
    db.session.commit()

    return jsonify({"message": "Success!"}), 200

@app.route('/api/v1.0/links/search/', methods=['GET'])
def search_link():
    if not 'q' in request.args:
        return jsonify({"message": "Missing required parameter."}), 400

    link = db.session.query(model.Link).filter_by(link = request.args['q']).first()
    
    if link is None:
        return jsonify({"message": "Link could not be found."}), 404
        
    return jsonify({"message": "Success!"}), 200

@app.route('/api/v1.0/links/', methods=['POST'])
def create_link():
    if not request.json or (not 'website_id' and 'link') in request.json:
        return jsonify({"message": "Missing required parameter."}), 400
       
    n = model.Link(website_id=1, link=request.json['link'])
    db.session.add(n)
    db.session.commit()

    return jsonify({"message": "Success!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
