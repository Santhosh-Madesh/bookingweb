from django.contrib import admin
from .models import Book, User
# Register your models here.

class BookInline(admin.TabularInline):
    model=Book
    extra=2

class UserAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Username",{'fields':['name']}),
        ("Email",{'fields':['email']}),
        ("Number",{'fields':['number']})
    ]
    inlines=[BookInline]
    search_fields=["name"]
    list_filter=["name"]

admin.site.register(User,UserAdmin)