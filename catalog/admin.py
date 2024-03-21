from django.contrib import admin
# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Language)
# admin.site.register(Book)
admin.site.register(Genre)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
class BookAdmin(admin.ModelAdmin):
    list_filter = ('genre', 'author')
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
admin.site.register(Book, BookAdmin)

# class AuthorInstanceInline(admin.TabularInline):
#     model = AuthorAdmin

#...................................................................................................................................................................................
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    class BookInline(admin.TabularInline):
        model = Book
        extra = 0
    inlines = [BookInline]
    
admin.site.register(Author, AuthorAdmin)
    
#...................................................................................................................................................................................    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'imprint', 'status', 'due_back', 'id')
    
    fieldsets = ((
        None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
        )
# admin.site.register(BookInstance, BookInstanceAdmin)






