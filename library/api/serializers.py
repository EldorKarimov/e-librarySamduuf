from rest_framework import serializers
from django.utils.translation import activate

from library.models import BookCategory, BookLang, Publication, EBook

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id', 'name', 'slug', 'created', 'updated')

class BookLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLang
        fields = ('id', 'name', 'created', 'updated')
        

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'name', 'created', 'updated')
        

class EBookSerializer(serializers.ModelSerializer):
    category = BookCategorySerializer()
    lang = BookLangSerializer()
    publication = PublicationSerializer()
    writing = serializers.SerializerMethodField()

    class Meta:
        model = EBook
        fields = ('id', 'name', 'views', 'downloads', 'writing', 'num_of_pages', 'year_of_pub', 'description', 'image', 'qr', 'lang', 'publication', 'category')

    def get_writing(self, obj):
        print(obj.description)
        return obj.get_writing_display()
    
    def to_representation(self, instance):
        request = self.context.get('request')
        lang = request.GET.get('lang', 'uz')

        activate(lang)  
        
        return super().to_representation(instance)