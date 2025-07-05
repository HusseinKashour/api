from django.contrib import admin
from django.urls import path
from Task.views import TaskViewSet 

urlpatterns = [
    path('admin/', admin.site.urls),
    
   
    path('api/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/tasks/<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]