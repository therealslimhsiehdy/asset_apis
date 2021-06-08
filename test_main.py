import main
import pytest

'''
DESCRIPTION:
This magical function can trigger test requests to main.py and will also keep track of requests for us
REFERENCE: https://flask.palletsprojects.com/en/2.0.x/testing/
'''
@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client

'''
DESCRIPTION:
All tests for validateBody function.
Includes validating:
1. A "correct" dictionary 
2. An empty dictionary
3. A dictionary key that isn't allowed
4. A duplicate asset_name
5. A wrong asset_type that isn't allowed
6. Unmatching satellite type to class
7. Unmatching antenna type to class
8. A name cannot start with underscore
9. A name cannot start with dash
10. A name cannot have anything that is nonalphanumeric or any other special characters other than "_" and "-"
11. A name with less than 4 characters
12. A name with more than 64 characters
'''

success = {"asset_name": "hello_world10", "asset_type": "satellite", "asset_class": "dove"}
empty_dict = {""}
incorrect_key = {"asset_wrong_key": "hello_world", "asset_type": "satellite", "asset_class": "dove"}
wrong_asset_type = {"asset_name": "hello_world1", "asset_type": "not-satellite", "asset_class": "dove"}
satellite_to_wrong_class = {"asset_name": "hello_world2", "asset_type": "satellite", "asset_class": "dish"}
antenna_to_wrong_class = {"asset_name": "hello_world3", "asset_type": "antenna", "asset_class": "dove"}
underscore_name = {"asset_name": "_underscorename", "asset_type": "satellite", "asset_class": "dove"}
dash_name = {"asset_name": "-underscorename", "asset_type": "satellite", "asset_class": "dove"}
nonalpha_name = {"asset_name": "hello*world", "asset_type": "satellite", "asset_class": "dove"}
less_name = {"asset_name": "the", "asset_type": "satellite", "asset_class": "dove"}
more_name = {"asset_name": "assetassetassetassetassetassetassetassetassetassetassetassetasset", "asset_type": "satellite", "asset_class": "dove"}

@pytest.mark.parametrize("test_input, expected", [(success, True), (empty_dict, False),
    (incorrect_key, False), (wrong_asset_type, False), (satellite_to_wrong_class, False),
    (antenna_to_wrong_class, False), (underscore_name, False), (dash_name, False), (nonalpha_name, False),
    (less_name, False), (more_name, False)])
def test_validateBody(test_input, expected):
    assert main.validateBody(test_input) == expected

'''
DESCRIPTION:
All tests for getAssets function.

Includes validating for the GET / POST calls:
1. GET - Checking for an empty json
2. POST - A valid request that was added to the dictionary and be successful
3. POST - A invalid request that shouldn't add to the dictionary and fail
4. GET - Printing out all the requests we added to the dictionary
'''
def test_getAssets_GET_success_emptydict(client):
    rv = client.get('/assets')
    assert b'{}' in rv.data

post_success_200 = {"asset_name": "hello_world", "asset_type": "satellite", "asset_class": "dove"}
def test_getAssets_POST_success_200(client):
    rv = client.post('/assets', data=post_success_200)
    assert rv.status_code == 200
    assert b'Asset created successfully' in rv.data

post_bad_body_400 = {"asset_name": "hello_world", "asset_type": "antenna", "asset_class": "dove"}
def test_getAssets_POST_fail_400(client):
    rv = client.post('/assets', data=post_bad_body_400)
    assert rv.status_code == 400
    assert b'Bad Asset form-data given' in rv.data

get_success_with_dict = {"asset_name": "hello_world5", "asset_type": "satellite", "asset_class": "dove"}
def test_getAssets_GET_success_with_dict(client):
    client.post('/assets', data=get_success_with_dict)
    rv = client.get('/assets')
    assert b'{"hello_world": {"asset_name": "hello_world", "asset_type": "satellite", "asset_class": "dove"}, "hello_world5": {"asset_name": "hello_world5", "asset_type": "satellite", "asset_class": "dove"}}' in rv.data

'''
DESCRIPTION:
All tests for getAsset function.

Includes validating:
1. Printing out JSON for a specified name
2. Error when searching for name that doens't exist in the dictionary
'''
def test_getAsset_existing_name(client):
    #rv = client.post('/assets', data=get_exist_dict)
    rv = client.get('/assets/hello_world5')
    assert b'{"asset_name": "hello_world5", "asset_type": "satellite", "asset_class": "dove"}' in rv.data

def test_getAsset_not_existing_name(client):
    rv = client.get('/assets/hello_world90')
    assert rv.status_code == 404
    assert b'Asset does not exist' in rv.data