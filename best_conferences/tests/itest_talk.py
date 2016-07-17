"""An end-to-end test for talk endpoint"""

import json

import requests

from nose.tools import assert_equal


def test_talk():

    host = "http://127.0.0.1:9090"

    talk_data = {
            "title" : "Fake it before you break it",
            "speaker" : "Uncle Bob",
            "abstract" : "We will outline our best talk",
        }

    # submitting a talk
    post_url = host + '/talk'
    create_response = requests.post(post_url,
        headers={'Content-Type': 'application/json'},
        data=json.dumps(talk_data))

    assert_equal(create_response.status_code, 200)

    created_listing = json.loads(create_response.content)
    created_id = created_listing["talkId"]
    print "Created new talk with ID: ", created_id

    # getting talk data
    get_url = host + '/talk/{talk_id}'.format(talk_id=created_id)
    get_response = requests.get(get_url)

    new_talk = json.loads(get_response.content)
    print "Talk details: "
    print new_talk

    assert_equal(get_response.status_code, 200)
    assert_equal(new_talk["title"], talk_data["title"])
    assert_equal(new_talk["speaker"], talk_data["speaker"])
    assert_equal(new_talk["abstract"], talk_data["abstract"])
