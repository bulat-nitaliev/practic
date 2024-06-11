from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin,
                                    RetrieveModelMixin)
from general.api.serializers import (IslamSerializers, VredPrivichkiSerializer, UserCreateSerializer, UserRetrievSerializer,
                                     CelCreateSerializer, CelListSerializer, CommentSerializer, CelUpdateSerializer)
from general.models import Islam, VredPrivichki, Cel, Comment, User
from rest_framework.permissions import IsAuthenticated, AllowAny
from general.permissions import IsOwner
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from datetime import datetime, date

class UserVievSet(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    # permission_classes = [AllowAny,]
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserRetrievSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    @action(methods=['get'], detail=False, url_path='me')
    def me(self, request):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



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
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)

    

class CommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        res = Comment.objects.all().filter(author_id=user).order_by('-id')
        return res