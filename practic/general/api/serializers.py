from rest_framework import serializers
from rest_framework.response import Response
from general.models import Islam, VredPrivichki, Comment, Cel, User
from datetime import datetime

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'email',
                  'first_name',
                  'last_name')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class IslamSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Islam
        fields = ('quran',
                'solat_duha',
                'solat_vitr',
                'mechet_fard',
                'tauba',
                'sadaka',
                'zikr_ut',
                'zikr_vech',
                'rodstven_otn',
                'user',
                'created_at')

class VredPrivichkiSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = VredPrivichki
        fields = ('son',
                'telefon',
                'haram',
                'eda',
                'user',
                'created_at')

# class VredPrivichkiCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = VredPrivichki
#         fields = ('son',
#                 'telefon',
#                 'haram',
#                 'eda',
#                 'user',
#                 'created_at')

class CelListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Cel
        fields = ('author',
                'name',
                'comment',
                'dt_beg',
                'dt_end')

    def get_comment(self, obj):
        print(self)
        comment = self.context['request'].user.comments.filter(cel=obj)
        print(*comment)
        return [i.body for i in comment] if comment else ''

class CelUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Cel
        fields = ('author',
                'name',
                'comment',
                'dt_beg',
                )

    def get_comment(self, obj):
        # print(self)
        comment = self.context['request'].user.comments.filter(cel=obj)
        # print(*comment)
        return [i.body for i in comment] if comment else ''



        return Response(serializer.data)

class CelCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cel
        fields = ('author',
                'name',
                'dt_beg')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = (
            'body',
            'author',
            'cel',
            'created_at',
        )