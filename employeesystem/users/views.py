from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
        ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin,
                        RetrieveModelMixin, GenericViewSet):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        if str(self.request.method).lower() == 'post':
            return []
        return [IsAuthenticated()]


router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
