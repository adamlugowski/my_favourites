from django.urls import path
from .views import index, add_post, my_posts


app_name = 'posts'
urlpatterns = [
    path('', index, name='index'),
    path('add_post', add_post, name='add_post'),
    path('my_posts', my_posts, name='my_posts')
]
