from django.contrib import admin
from home.models import *

# Register your models here.
class InlineImage(admin.TabularInline):
    model = Studentimage
    extra =1
class StudentAdmin(admin.ModelAdmin):
    fields = ['st_lienkhoa','st_lop','st_ten','st_sdt','st_img']
    inlines = [InlineImage]
admin.site.register(Student,StudentAdmin)

class classAdmin(admin.ModelAdmin):
    fields = ['interlock_name','class_name']
admin.site.register(Class,classAdmin)

class interlockAdmin(admin.ModelAdmin):
    fields = ['interlock_name']
admin.site.register(Interlock,interlockAdmin)


