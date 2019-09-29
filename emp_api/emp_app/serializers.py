from rest_framework import serializers
from emp_app.models import Emp
# create a serializer file that erilize the modeldata in the database
class Emp_serializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
