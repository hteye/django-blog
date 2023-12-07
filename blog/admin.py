from django.contrib import admin

<<<<<<< HEAD
=======
# noinspection PyUnresolvedReferences
>>>>>>> 1d6145c53db21e8bc17c72aafa7c9796ba0bd4b4
from blog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
