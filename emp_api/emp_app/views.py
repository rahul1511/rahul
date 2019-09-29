from django.shortcuts import render ,get_list_or_404, get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from emp_app.models import Emp
from emp_app.serializers import Emp_serializer
from rest_framework.response import Response

# create a class based view for performing the curd opeations
class Emplist(APIView):
    # define a method for retriving the data from the database
    def get(self,request):
        #take the list based on models class
        lst=get_list_or_404(Emp)
        #take serialize object list based on serializers class
        Slst=Emp_serializer(lst,many=True)
        return Response(Slst.data)
