from django.contrib import admin

from .models import Friend

class FriendAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'profile_image')

    def profile_image(self, obj):
        return '<img src="%s" width="50" heith="50">' % obj.photo
    profile_image.allow_tags = True

admin.site.register(Friend, FriendAdmin)