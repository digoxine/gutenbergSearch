from django.core.management.base import BaseCommand, CommandError
from polls.config import BASE_URL
from polls.models import Author, Book
from polls.serializers import AuthorSerializer, BookSerializer
import requests
import time
from bs4 import BeautifulSoup
class Command(BaseCommand):
    help = 'Refresh the list of books'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        url = BASE_URL + str(400)
        html_text = requests.get(url).text
        self.parse(html_text)
        soup = BeautifulSoup(html_text, 'html.parser')
        
        #print(author.contents)

        
        #Book.objects.all().delete()
        

    def parse(self, htmlPage):
        '''
        return JSON containing all books
        '''
        res = dict()
        soup = BeautifulSoup(htmlPage, 'html.parser')
        for author in soup.find_all(itemprop="creator"):
            lastName, firstName, date = author.contents[0].split(', ')
            birthDate, deathDate = date.split('-')   
            author = Author(lastName, firstName, birthDate, deathDate)
            serializerAuthor = AuthorSerializer(author)
            #print(serializerAuthor.data)
        soup = BeautifulSoup(htmlPage, 'html.parser')    
        subjects = []
        for translator in soup.find_all(datatype="dcterms:LCSH"):
            print(translator.a.contents[0].replace('\n',''))

