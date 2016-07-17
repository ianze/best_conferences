import collections
import datetime

from best_conferences.exceptions import TalkNotFound


global talks
talks = collections.OrderedDict()


class TalkService(object):
    """Handle talk logic and storage"""
    def __init__(self):
        global listings
        self.talks = talks

    def store_talk(self, talk):
        """Inserting one talk"""

        talk_id= len(self.talks) + 1

        talk["id"] = talk_id
        self.talks[talk_id] = talk

        return talk_id

    def get_talk(self, talk_id):
        """Return talk or raise exception if not found"""
        talk = self.talks.get(talk_id)

        if talk:
            return talk
        else:
            raise TalkNotFound("")
