from django.contrib import admin
from .models import Notes
# Register your models here.


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('subject_name','branch','year','semester','uploaded_at')
    list_filter = ('year','semester','branch')
    search_fields = ('subject_name','branch')
