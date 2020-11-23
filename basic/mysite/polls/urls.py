from django.urls import path

from . import views

# path(routing, view, ??)
urlpatterns = [
    path('', views.index, name='index'),        # /polls
]

