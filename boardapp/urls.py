from . import views
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, Boardcreate, Healthcreate

urlpatterns = [
    path("", loginfunc, name="index"),
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', Boardcreate.as_view(), name='create'),
    path('health/', Healthcreate.as_view(), name='health')
]
