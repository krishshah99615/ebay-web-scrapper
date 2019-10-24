from django.urls import path
from . import views
urlpatterns = [
    path('',view=views.index,name='index' ),
    path('new_search',view=views.new_search,name='new_search')
]