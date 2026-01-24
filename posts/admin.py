from django.contrib import admin
from .models import Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ('image', 'uploaded_at')
    readonly_fields = ('uploaded_at',)
    can_delete = True


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_preview', 'author', 'image_count', 'likes_count', 'date')
    list_filter = ('date', 'author')
    search_fields = ('body', 'author__username')
    readonly_fields = ('date', 'likes_count')
    exclude = ('title',)  # Hide title field from admin
    inlines = [PostImageInline]  # Add images inline
    
    def body_preview(self, obj):
        return obj.body[:100] + '...' if len(obj.body) > 100 else obj.body
    body_preview.short_description = 'Content'
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'
    
    def likes_count(self, obj):
        return obj.total_likes()
    likes_count.short_description = 'Likes'


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_preview', 'image_thumbnail', 'uploaded_at')
    list_filter = ('uploaded_at', 'post__author')
    search_fields = ('post__body', 'post__author__username')
    readonly_fields = ('uploaded_at', 'image_display')
    
    def post_preview(self, obj):
        return obj.post.body[:50] + '...' if len(obj.post.body) > 50 else obj.post.body
    post_preview.short_description = 'Post'
    
    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />'
        return '-'
    image_thumbnail.short_description = 'Thumbnail'
    image_thumbnail.allow_tags = True
    
    def image_display(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 300px;" />'
        return '-'
    image_display.short_description = 'Preview'
    image_display.allow_tags = True


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)