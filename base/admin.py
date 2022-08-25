from django.contrib import admin
from . models import Image, ImageType

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('price', 'image_type', 'original_url')
    list_filter = ('image_type',)

admin.site.register(Image, ImageAdmin)
admin.site.register(ImageType)