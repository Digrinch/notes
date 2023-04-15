from django.contrib import admin
from django.apps import apps
from django.urls import path, include

urlpatterns = [
    path(
        '', include('tasks.urls', namespace=apps.get_app_config('tasks').name)
    ),
    path(
        'auth/',
        include('users.urls', namespace=apps.get_app_config('users').name),
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace=apps.get_app_config('api').name)),
]
