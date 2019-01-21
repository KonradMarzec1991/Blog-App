from django.contrib import admin
from django.urls import re_path, include
from users.views import LoginUser, LogoutUser, RegisterUser

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('posts.urls')),
    re_path(r'^login/$', LoginUser.as_view(), name='login'),
    re_path(r'^logout/$', LogoutUser.as_view(), name='logout'),
    re_path(r'^register/$', RegisterUser.as_view(), name='register'),
]
