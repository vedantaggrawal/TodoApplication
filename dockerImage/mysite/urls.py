from django.contrib import admin
from django.urls import include,path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('todo')),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
