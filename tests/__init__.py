import json


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client().post(
        url, data=json.dumps(json_dict), content_type='application/json')


def post_json_header(client, url, json_dict, token):
    """Send dictionary json_dict as a json to the specified url """
    return client().post(
        url,
        data=json.dumps(json_dict),
        content_type='application/json',
        headers={'Authorization': 'Bearer ' + token})


def get_token(resp):
    """Return token from response"""
    access = json_of_response(resp)
    access_token = access['token']
    return access_token
