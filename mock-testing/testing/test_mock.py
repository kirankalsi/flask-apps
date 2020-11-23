from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_football(self):
    # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)

    def test_badminton(self):
    # We will mock a response of 2 and test that we get badminton returned.
        with patch('requests.get') as g:
            g.return_value.text = "2"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)

    def test_hockey(self):
    # We will mock a response of 3 and test that we get hockey returned.
        with patch('requests.get') as g:
            g.return_value.text = "3"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)

    def test_boxing(self):
    # We will mock a response of 4(any other num) and test that we get boxing returned.
        with patch('requests.get') as g:
            g.return_value.text = "4"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)
