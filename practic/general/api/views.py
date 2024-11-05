from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin,
                                    RetrieveModelMixin)
from general.api.serializers import (VredPrivichkiSerializer, UserCreateSerializer, UserRetrievSerializer,
                                     CelCreateSerializer, CelListSerializer, CommentSerializer, CelUpdateSerializer,
                                     IslamListSerializers, IslamRetrieveSerializers, IslamCreateSerializers)
from general.models import Islam, VredPrivichki, Cel, Comment, User
from rest_framework.permissions import IsAuthenticated,  AllowAny
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
    def get_serializer_class(self):
        if self.action == 'create':
            return IslamCreateSerializers
        if self.action == 'retrieve':
            return IslamRetrieveSerializers
        return IslamListSerializers
    permission_classes = [IsOwner]

    def retrieve(self, request, *args, **kwargs):
        # print(request.data, '-----------data')
        # print(self.request, '---------request.data')
        # print(args, '-----------------args')
        # print(kwargs["pk"], '-----------------kwargs')
        # print( self.request.user, request.user, kwargs["pk"])
        user = Islam.objects.filter(id=kwargs["pk"]).last()
        instance = Islam.objects.filter(user=self.request.user, id=kwargs["pk"])
        # print(user, instance)
        if not instance or (instance and user not in instance):
            raise PermissionDenied('Вы неможете посмотреть чужие дела')


        serializer = self.get_serializer(instance[0])
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        res = Islam.objects.all().filter(user=user).order_by('-id')
        return res

class VredPrivichkiViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsOwner]
    serializer_class = VredPrivichkiSerializer
    def get_queryset(self):
        user = self.request.user
        res = VredPrivichki.objects.all().filter(user_id=user).order_by('-id')
        return res

    def retrieve(self, request, *args, **kwargs):
        user = VredPrivichki.objects.filter(id=kwargs["pk"]).last()
        instance = VredPrivichki.objects.filter(user=self.request.user, id=kwargs["pk"])

        if not instance or (instance and user not in instance):
            raise PermissionDenied('Вы неможете посмотреть чужие дела')
        serializer = self.get_serializer(instance[0])
        return Response(serializer.data)



class CelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    def get_serializer_class(self):
        if self.action == 'create':
            return CelCreateSerializer
        if self.action == 'update':
            return CelUpdateSerializer
        return CelListSerializer

    def get_queryset(self):
        user = self.request.user
       
        res = Cel.objects.all().filter(author_id=user).order_by('-id')
        # res = Cel.objects.all().prefetch_related('author__comments').filter(author_id=user).order_by('-id')
        return res





class CommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsOwner,]

    def get_queryset(self):
        user = self.request.user
        res = Comment.objects.all().filter(author=user).order_by('-id')
        # res = Comment.objects.all().prefetch_related('cel').order_by('-id')
        return res