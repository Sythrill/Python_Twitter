from django.contrib import admin

# Register your models here.
from tweet import models
from tweet.models import Message, Comment, PersonalMessage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("content", "creation_date", "is_read", "created_by")
    exclude = ["content", "creation_date", "is_read", "created_by"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "creation_date", "get_message", "created_by")
    exclude = ["content", "creation_date", "message", "created_by"]

    def get_message(self, obj):
        return obj.message.content

    get_message.short_description = "message"


@admin.register(PersonalMessage)
class PersonalMessageAdmin(admin.ModelAdmin):
    list_display = ("content", "creation_date", "from_user", "to_user")
    exclude = ["content", "creation_date", "from_user", "to_user"]

    def from_user(self, obj):
        return obj.user.username

    from_user.short_description = 'from user'
