from django.contrib import admin
from .models import ProfileModel,Post,LikePost,Followers

# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Followers)