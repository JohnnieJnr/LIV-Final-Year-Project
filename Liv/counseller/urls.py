from django.urls import path
from .views import ListCounsellorView, CreateCounsellorView

app_name = 'counseller'

urlpatterns = [
    path('cs/', ListCounsellorView.as_view(), name='listco_endpoint'),
    path('create/', CreateCounsellorView.as_view(), name='new_co_endpoint'),

]
