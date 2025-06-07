from rest_framework import serializers
from datetime import datetime
from .models import Department, Employee, Attendance, Performance
from users.models import CustomUser
from crum import get_current_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name', 'created_by']
        read_only_fields = ['id', 'created_by']

    def validate(self, attrs):
        attrs['created_by'] = get_current_user()
        return super().validate(attrs)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'user', 'department', 'address', 'date_of_joining']
        read_only_fields = ['id', 'user']

    def validate(self, attrs):
        attrs['user'] = get_current_user()
        return super().validate(attrs)


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']
        read_only_fields = ['id', 'employee', 'date']

    def validate(self, attrs):
        employee = Employee.objects.filter(user=get_current_user()).first()
        if not employee:
            raise serializers.ValidationError("User is not a valid employee to record attendance. Please register yourself as an employee")
        attrs['employee'] = employee
        attrs['date'] = datetime.date(datetime.now())
        return super().validate(attrs)


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'employee', 'rating', 'review_date']
        read_only_fields = ['id', 'review_date']

    def validate(self, attrs):
        employee = Employee.objects.filter(user=get_current_user()).first()
        if not employee:
            raise serializers.ValidationError("User is not a valid employee to record attendance. Please register yourself as an employee")
        if employee == attrs['employee']:
            raise serializers.ValidationError("You cannot give rating to yourself")
        attrs['review_date'] = datetime.date(datetime.now())
        return super().validate(attrs)


