from django.urls import path
from .views import ListCommentView

app_name = 'comment'

urlpatterns = [
    path('cs/', ListCommentView.as_view(), name='listcomment_endpoint'),

]