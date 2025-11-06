from django.contrib import admin
from .models import Comment_Box,Friend_List
# from django.contrib.auth.models import User


# Register your models here.

class Comment_Admin(admin.ModelAdmin):

    list_display = ('Comment_Text','Comment_User_id','Comment_Post_id')

    search_fields = ['Comment_Text']

admin.site.register(Comment_Box,Comment_Admin)


class Friend_Admin(admin.ModelAdmin):

    list_display = ('current_user','friend_user','status')



admin.site.register(Friend_List,Friend_Admin)