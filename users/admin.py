from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_preview', 'followers_count', 'following_count')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email', 'bio')
    readonly_fields = ('created_at', 'updated_at', 'followers_count', 'following_count')
    filter_horizontal = ('following',)  # Nice UI for ManyToMany field
    fieldsets = (
        ('User Info', {
            'fields': ('user',)
        }),
        ('Profile Details', {
            'fields': ('bio', 'avatar')
        }),
        ('Social', {
            'fields': ('following', 'followers_count', 'following_count')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse by default
        }),
    )
    
    def bio_preview(self, obj):
        return obj.bio[:50] + '...' if obj.bio and len(obj.bio) > 50 else obj.bio or '(no bio)'
    bio_preview.short_description = 'Bio'
    
    def followers_count(self, obj):
        return obj.followers.count()
    followers_count.short_description = 'Followers'
    
    def following_count(self, obj):
        return obj.following.count()
    following_count.short_description = 'Following'


admin.site.register(Profile, ProfileAdmin)
