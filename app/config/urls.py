from django.contrib import admin
from django.urls import path, include

from assets.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', include('users.urls', namespace='users')),
]
