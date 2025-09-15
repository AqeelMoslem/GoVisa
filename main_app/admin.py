from django.contrib import admin
from .models import Visa
from .models import Message

admin.site.register(Visa)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('subject', 'body', 'sender__username')