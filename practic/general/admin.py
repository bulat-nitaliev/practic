from django.contrib import admin
from general.models import User, Islam, VredPrivichki, Cel, Comment
from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )
    fields = (
        "first_name",
        "last_name",
        "username",
        "password",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        "last_login",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    search_fields = (
        "id",
        "username",
    )
    list_filter = (
        "username",
        "is_staff",
        "is_superuser",
        "is_active",
    )

@admin.register(Islam)
class IslamModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quran',
        'solat_duha',
        'solat_vitr',
        'mechet_fard',
        'tauba',
        'sadaka',
        'zikr_ut',
        'zikr_vech',
        'rodstven_otn',
        'created_at',
        'user',
    )
    readonly_fields  = ('created_at','user',)
    list_filter = (
        "user",
    )

@admin.register(VredPrivichki)
class VredPrivichkiModelAdmin(admin.ModelAdmin):
    list_display = (
        'son',
        'telefon',
        'haram',
        'eda',
        'created_at',
        'user',
    )
    readonly_fields  = ('created_at','user',)
    list_filter = (
        "user",
    )

@admin.register(Cel)
class CelModelAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'name',
        'dt_beg',
        'dt_end',
        'get_comment_count'
    )
    readonly_fields  = ('dt_beg','author',)
    list_filter = (
        "author",
    )
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("comments")
    
    get_comment_count.short_description = 'comment_count'

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        'get_body',
        'author',
        'cel',
        'created_at',
    )
    readonly_fields  = ('created_at','author',)
    list_filter = (
        "author",
    )

    def get_body(self, obj):
        if len(obj.body) > 64:
            return obj.body[:61] + '...'
        return obj.body
    
    get_body.short_description = 'body'
