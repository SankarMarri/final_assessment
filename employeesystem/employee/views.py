from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
        ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, \
        IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter

from employee.models import Department, Employee, Attendance, Performance
from employee.serializers import DepartmentSerializer, EmployeeSerializer, \
        AttendanceSerializer, PerformanceSerializer


class DepartmentViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                        UpdateModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DepartmentSerializer


class EmployeeViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                      UpdateModelMixin, GenericViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()


class AttendanceViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                        UpdateModelMixin, GenericViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Attendance.objects.all()


class PerformanceViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                         UpdateModelMixin, GenericViewSet):
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Performance.objects.all()


router = DefaultRouter()
router.register('department', DepartmentViewSet, basename='department')
router.register('employee', EmployeeViewSet, basename='employee')
router.register('attendance', AttendanceViewSet, basename='attendance')
router.register('performance', PerformanceViewSet, basename='performance')
