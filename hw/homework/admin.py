from django.contrib import admin
from homework.models import Student, Book

@admin.register(Book)
class AdminContactInfo(admin.ModelAdmin):
    list_display = ('title', 'number_of_pages', 'student')

@admin.register(Student)
class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'book')

    def full_name(self, obj):
        return f'{obj.firstname}  {obj.lastname}'

# admin.site.register(Customer)
# admin.site.register(Book)



