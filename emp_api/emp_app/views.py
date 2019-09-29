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
    # create push method to add the object in the databases
    def post(self,request):
        # request method will retrive the dta written in contact in browser
        Slst=Emp_serializer(data=request.data)
        if Slst.is_valid():
            Slst.save()
            return Response(Slst.data, status=status.HTTP_201_OK)
        else:
            return Response(Slst.error, status=status.HTTP_400_BAD_REQUEST)

# now create another class based view for the modifiction
class Emp_modify(APIView):
    # create a method the retive the object for the selection
    def get_object(self,id):
        #try to check the object is available in data base or not
        try:
            return Emp.objects.get(id=id)
        except:
            return Response({'error':'object not found'}, status=status.HTTP_404_NOT_FOUND)
    # create a method to display in the browser
    def get(self,request,id):
        lst=self.get_object(id)
        Slst=Emp_serializer(lst)
        return Response(Slst.data)
    def put(self,request,id):
        lst=self.get_object(id)
        #serialize that element
        Slst=Emp_serializer(lst,data=request.data)
        # chect whethet the data modified is valid or not
        if Slst.is_valid():
            Slst.save()
            return Response(Slst.data,status=status.HTTP_200_OK)
        else:
            return Response(Slst.error,status=status.HTTP_404_BAD_REQUEST)
    # create another method to delete the data
    def delete(self,request,id):
        lst=self.get_object(id)
        lst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
