import django_filters
from django_filters import rest_framework as filters
from employee.models import Employee, Department, Attendance, Performance


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'name': ['exact', 'iexact', 'icontains', 'istartswith']
        }


class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'department': ['exact'],
            'date_of_joining': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'user': ['exact']
        }


class AttendanceFilter(filters.FilterSet):
    class Meta:
        model = Attendance
        fields = {
            'employee': ['exact'],
            'status': ['exact'],
            'date': ['exact', 'gt', 'gte', 'lt', 'lte']
        }
