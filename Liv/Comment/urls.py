from django.urls import path
from .views import ListCommentView, CreateComment

app_name = 'comment'

urlpatterns = [
    path('cs/', ListCommentView.as_view(), name='listcomment_endpoint'),
    path('create/', CreateComment.as_view(), name='new_comment_endpoint'),

]