from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                    RetrieveModelMixin)
from general.api.serializers import (IslamSerializers, VredPrivichkiSerializer, UserCreateSerializer,
                                     CelCreateSerializer, CelListSerializer, CommentSerializer, CelUpdateSerializer)
from general.models import Islam, VredPrivichki, Cel, Comment, User
from rest_framework.permissions import c, AllowAny
from general.permissions import IsOwner
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

class UserVievSet(GenericViewSet, CreateModelMixin):
    permission_classes = [AllowAny,]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class IslamViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = IslamSerializers
    permission_classes = [IsOwner]
    def get_queryset(self):
        user = self.request.user
        res = Islam.objects.all().filter(user_id=user).order_by('-id')
        return res

class VredPrivichkiViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsOwner]
    serializer_class = VredPrivichkiSerializer
    # queryset = VredPrivichki.objects.all().order_by('-id')
    def get_queryset(self):
        user = self.request.user
        res = VredPrivichki.objects.all().filter(user_id=user).order_by('-id')
        return res


class CelViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CelCreateSerializer
        if self.action == 'update':
            return CelUpdateSerializer
        return CelListSerializer

    def get_queryset(self):
        user = self.request.user
        res = Cel.objects.all().filter(author_id=user).order_by('-id')
        return res

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class CommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        res = Comment.objects.all().filter(author_id=user).order_by('-id')
        return res