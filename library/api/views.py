from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.http import JsonResponse

from .serializers import EBookSerializer
from library.models import BookCategory, BookLang, Publication, EBook
from common.views import api_response

class EBookListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @extend_schema(
        summary="Get details of a single e-book",
        description="Returns complete information about a specific e-book",
        responses={
            200: EBookSerializer,
            400: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "Error description here"},
                    "code": {"type": "integer", "example": 400}
                }
            }, 
            404: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "EBook not found."},
                    "code": {"type": "integer", "example": 404}
                }
            }
        },
        parameters=[
            OpenApiParameter(
                name='category',
                description='Filter by category slug',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name='language',
                description='Filter by language ID',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name='writing',
                description='Filter by writing system (KR for Krill, LT for Latin)',
                required=False,
                type=str,
                enum=['KR', 'LT'],
                location=OpenApiParameter.QUERY
            ),
        ],
    )
    
    def get(self, request):
        category_slug = request.GET.get('category')
        books = EBook.objects.all()
        if category_slug:
            books = books.filter(category__slug = category_slug)
            
        serializer = EBookSerializer(books, many = True, context = {'request':request})
        return api_response(data=serializer.data)