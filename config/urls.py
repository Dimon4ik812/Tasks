from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка Django
    path('admin/', admin.site.urls),

    # Маршруты для API задач
    path('api/', include('task.urls')),  # Подключаем urls.py приложения tasks
]