from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .serializers import EBookSerializer
from library.models import BookCategory, BookLang, Publication, EBook

class EBookListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        books = EBook.objects.all()
        serializer = EBookSerializer(books, many = True, context = {'request':request})
        data = {
            'success':True,
            'data':serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)