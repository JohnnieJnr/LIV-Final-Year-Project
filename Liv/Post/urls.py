from django.urls import path
from .views import CreatePost, ListPostView

app_name = 'post'

urlpatterns = [
    path('ps/', CreatePost.as_view(), name='new_post'),
    path('ls/', ListPostView.as_view(), name='list_endpoint'),

]