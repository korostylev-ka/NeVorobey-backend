from django.contrib import admin

from main.models import Word, HiddenWord

# Register your models here.
admin.site.register(Word)
admin.site.register(HiddenWord)
