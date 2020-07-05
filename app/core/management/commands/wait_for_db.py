import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    # handle is something which get called whennever we call management
    def handle(self, *args, **options):
        # to print out things on screen
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        # this will output print in green color
        self.stdout.write(self.style.SUCCESS('Database available!'))
