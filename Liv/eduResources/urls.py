from django.urls import path
from .views import ListEduresources, CreateEduresource

app_name = 'eduResources'

urlpatterns = [
    path('ls/', ListEduresources.as_view(), name='listedu_endpoint'),
    path('create/', CreateEduresource.as_view(), name='new_edu_endpoint'),

]
