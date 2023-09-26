"""
Django command to wait for db to be up
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """django command to wait for db"""

    def handle(self, *args, **options):
        pass