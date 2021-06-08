from flask import Flask, request
import json, re

class Asset:
    def __init__(self, asset_name: str, asset_type: str, asset_class: str):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.asset_class = asset_class

"""
INPUT: A dictionary
OUTPUT: Boolean
DESCRIPTION: validateBody makes sure the dictionary given has the correct keys and value input
A valid dictionary should comes in as {"asset_name": some_name, "asset_type": satellite/antenna, "asset_class": dove/dish/etc}
"""
def validateBody(body) -> bool:
    if len(body) != 3: 
      return False
    if body.keys() != set(["asset_name", "asset_type","asset_class"]):  
    	return False
    if len(body.get("asset_name")) < 4 or len(body.get("asset_name")) > 64:
      return False
    if body.get("asset_name")[0] in ["-", "_"]:
      return False
    if bool(re.match('^[a-zA-Z0-9-_]+$', body.get("asset_name"))) == False:
      return False
    if body.get("asset_name") in asset_dict:
    	return False
    if body.get("asset_type") not in ("satellite", "antenna"):
      return False
    if body.get("asset_class") not in asset_type_class[body.get("asset_type")]:
      return False
    return True

app = Flask(__name__)
asset_dict = {}
asset_type_class = {"satellite": ["dove", "rapideye", "skysat"], "antenna": ["dish", "yagi"]}

"""
INPUT: Either a POST or GET request 
OUTPUT: Correct JSON / status / corresponding error
DESCRIPTION: getAssets creates an Asset object after it's been validated
or grabs all the Asset objects and returns them

An entry in the in memory should look like -- {"asset_name": Asset(asset_name, asset_type, asset_class)}
NOTE: Using .form method on a given request returns back a dictionary data structure
"""
@app.route("/assets", methods = ['POST', 'GET'])
def getAssets(): 
    if request.method == 'POST':
      requestBody = request.form
      if not validateBody(requestBody):
        return "Bad Asset form-data given", 400
      if requestBody.get("asset_name") in asset_dict:
        return "Duplicate asset_name", 400
      asset_dict[requestBody.get("asset_name")] = requestBody
      return "Asset created successfully", 200
    elif request.method == 'GET':
      return json.dumps(asset_dict)

"""
INPUT: A GET request 
OUTPUT: Correct JSON / status / corresponding error
DESCRIPTION: getAsset returns the Asset information to a corresponding asset_name
NOTE: We are putting the information we want to output into a dictionary in case 
there's any extra stuff in the given object thatwe don't want to return for now.
"""
@app.route('/assets/<name>')
def getAsset(name):
    if name in asset_dict:
      whole_dict = asset_dict[name]
      return_dictionary = {'asset_name': whole_dict.get("asset_name"), 'asset_type': whole_dict.get("asset_type"), 'asset_class': whole_dict.get("asset_class")}
      return json.dumps(return_dictionary)
    else:
    	return "Asset does not exist", 404