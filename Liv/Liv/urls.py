"""Liv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="The HIV FRAMEWORK API",
        default_version='v1',
        description="HIV API documentation ",
        contact=openapi.Contact(email="ahwirengfiifi@gmail.com"),

    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('Post.urls')),
    path('comm/', include('Comment.urls')),
    path('col/', include('counseller.urls')),
    path('edu/', include('eduResources.urls')),
    path('eve/', include('event.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


