from django.contrib import admin
from .models import Visa
from .models import Message

admin.site.register(Visa)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'receiver', 'read', 'timestamp')
    list_filter = ('read', 'timestamp')
    search_fields = ('subject', 'body', 'sender__username', 'receiver__username')
