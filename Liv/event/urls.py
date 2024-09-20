from django.urls import path
from .views import , CreateEvent, ListEventsView

app_name = 'post'

urlpatterns = [
    path('ex/', CreateEvent.as_view(), name='new_ev'),
    path('ls/', ListEventsView.as_view(), name='list_endpoint'),

]