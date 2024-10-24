from rest_framework import serializers
from general.models import Islam, VredPrivichki, Comment, Cel, User
from datetime import datetime, date
from rest_framework.exceptions import PermissionDenied

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

class UserRetrievSerializer(serializers.ModelSerializer):
    cels = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'cels',
        )

    def get_cels(self, obj):
        cel = self.context['request'].user.cels.filter(author=obj)
        return [i.name for i in cel] if cel else ''


class IslamListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Islam
        fields = (
                "id",
                'quran',
                'solat_duha',
                'solat_vitr',
                'fadjr',
                'mechet_fard',
                'tauba',
                'sadaka',
                'zikr_ut',
                'zikr_vech',
                'rodstven_otn',
                'user',
                'created_at')

class IslamCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Islam
        fields = (
                'quran',
                'solat_duha',
                'solat_vitr',
                'fadjr',
                'mechet_fard',
                'tauba',
                'sadaka',
                'zikr_ut',
                'zikr_vech',
                'rodstven_otn',
                'user',
                'created_at')

class IslamRetrieveSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Islam
        fields = (
                "id",
                'quran',
                'solat_duha',
                'solat_vitr',
                'fadjr',
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


class CelListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.SerializerMethodField()
    # comment = serializers.CharField(source='')
    class Meta:
        model = Cel
        fields = (
                'id',
                'author',
                'name',
                'comment',
                'dt_beg',
                'dt_end')

    def get_comment(self, obj):
        # cel = Cel.objects.all().filter(author=self.context['request'].user)
        # print([i.id for i in cel])
        comment = self.context['request'].user.comments.filter(cel=obj)
        return [i.body for i in comment] if comment else ''
        # return obj.body


class CelUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.SerializerMethodField()
    dt_end = serializers.DateField(initial=date.today,read_only=True)

    class Meta:
        model = Cel
        fields = ('author',
                'name',
                'comment',
                'dt_beg',
                'dt_end'
                )

    def get_comment(self, obj):
        comment = self.context['request'].user.comments.filter(cel=obj)
        return [i.body for i in comment] if comment else ''



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

    def create(self, validated_data):
        # print(Cel.objects.filter(author=self.context['request'].user))
        # print(Comment.objects.all().filter(author=self.context['request'].user).order_by('-id'))
        cel = [i.name for i in Cel.objects.filter(author=self.context['request'].user)]
        # print(validated_data['cel'].name, cel)

        if validated_data['cel'].name in cel:
            comment = Comment.objects.create(
                body=validated_data['body'],
                cel=validated_data['cel'],
                author=self.context['request'].user
            )
            comment.save()
            return comment
        raise PermissionDenied('Вы не можете добавить коментарий к чужой цели')
