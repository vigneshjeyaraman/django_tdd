# this will help us mock the function as we are calling the actual
# one but instead we are just calling one created for testing purpose.
# using this we can simulate things
from unittest.mock import patch
# for calling command in source code
from django.core.management import call_command
# Django throws this error when DB is not available.
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # patch will mock django connectionhadler to always return True
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            # wait_for_db here is the name of the file inside commands folder
            # which is inside management folder. It is the command which get
            # called when we call antthing with
            # manage.py
            call_command('wait_for_db')
            # if return value is True call count will be one it means
            # DB is started already
            self.assertEqual(gi.call_count, 1)

    # what patch decortar does is same it will mock the required function
    # and we can mock the return value. Here we have mocked time.sleep
    # so that instead of sleeping for a second we just return true and come out
    # this is done just to avoid unnecessary wait in test.
    # Patch decorator will pass an extra argument which even we don't use
    # have to pass in our function else it will throw an error.
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # side effects is an amazing attribute given by mock
            # using this we can side effects to required function
            # like here we are raising operation error for 5 times and then
            # we are returing true.
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
