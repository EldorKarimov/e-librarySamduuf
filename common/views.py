from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def api_response(data = None, status = True, status_code = status.HTTP_200_OK, message = None):
    """Standart API Response"""
    return Response(
        data={
            "success":status,
            "message":message,
            "data":data
        },
        status=status_code
    )