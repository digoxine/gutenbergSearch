from django.core.management.base import BaseCommand, CommandError
from mytig.models import ProduitDisponible
from mytig.serializers import ProduitDisponibleSerializer
from mytig.config import baseUrl
import requests
import time
class Command(BaseCommand):
    help = 'Refresh the list of books'

    '''def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl)'''