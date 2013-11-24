from django.contrib import admin
from todolist.models import Todo

class TodoAdmin(admin.ModelAdmin):
  fields = ['title','desc']
  list_display = ['title','created']

admin.site.register(Todo,TodoAdmin)
