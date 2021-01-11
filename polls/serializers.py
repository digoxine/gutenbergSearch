from rest_framework.serializers import ModelSerializer
from polls.models import Author, Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('lastName', 'firstName', 'birthDate', 'deathDate')
    
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('_all_')