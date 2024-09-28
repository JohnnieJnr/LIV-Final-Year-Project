from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, UserList, AccountDetail

app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_endpoint'),
    path('logout/', LogoutView.as_view(), name='logout_endpoint'),
    path('login/', LoginView.as_view(), name='login_endpoint'),
    path('users/', UserList.as_view(), name='user_list_endpoint'),
    path('users/<int:pk>/', AccountDetail.as_view(), name='user_profile_endpoint'),
    ]