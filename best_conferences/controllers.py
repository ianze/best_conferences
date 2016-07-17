"""Handle endpoints for submiting and looking up talks"""
import json

from flask import request

from best_conferences import app
from best_conferences.exceptions import TalkNotFound
from best_conferences.services import TalkService


@app.route('/talk', methods=['POST'])
def submit_talk():
    talk = request.get_json()

    if not ('title' in talk and
        'speaker' in talk and
        'abstract' in talk):
        return 'Missing parameter', 400

    id = TalkService().store_talk(talk)

    response = {'talkId': id}

    return json.dumps(response)


@app.route('/talk/<int:talk_id>')
def get_talk(talk_id):

    try:
        talk = TalkService().get_talk(talk_id)
        return json.dumps(talk)
    except TalkNotfound:
        error = {'error': 'talk not found'}
        return json.dumps(error), 404
