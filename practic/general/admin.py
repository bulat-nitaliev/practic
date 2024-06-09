from django.contrib import admin
from general.models import User, Islam, VredPrivichki, Cel, Comment
from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Islam)
class IslamModelAdmin(admin.ModelAdmin):
    pass

@admin.register(VredPrivichki)
class VredPrivichkiModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Cel)
class CelModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass
