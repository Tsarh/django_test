from django.contrib import admin
from .models import Book,Author

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('info manga',{"fields":["title","author"]}),
        ('info magasin',{"fields":["quantity"]})
    ]
    list_display = ("title","author")

class AuthorAdmim(admin.ModelAdmin):
    list_display = ("name","id")
    search_fields = ["name"]
    list_filter = ['name']
    

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmim)
