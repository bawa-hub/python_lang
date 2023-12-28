from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

# from .import views,hod_views,staff_views,student_views
# from .views import BASE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', view=base, name='base'),
    path('login/', view=login, name='login')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
