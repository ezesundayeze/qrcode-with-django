from rest_framework import serializers
from .models import Employees, Department


class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = (
            'fName',
            'lName',
            'department',
        )


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'name',
        )
