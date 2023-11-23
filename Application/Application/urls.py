from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "JC Records"
admin.site.site_title = "JC Records Admin Portal"
admin.site.index_title = "Welcome to JC Records Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
]
