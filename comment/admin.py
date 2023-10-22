# from django.contrib import admin
# from .models import Comment

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['comment','content_type','commenter','commenter']
#     search_fields = ['content_type','commenter']
#     list_filter = ['content_type']

#     def has_add_permission(self, request):
#         return False
    
#     def has_change_permission(self, request, obj=None):
#         return False
    
#     def has_delete_permission(self, request, obj=None):
#         return False

#     def save_model(self, request, obj, form, change):
#         pass

#     def delete_model(self, request, obj):
#         pass
