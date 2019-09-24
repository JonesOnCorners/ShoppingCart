from django.urls import path
from display.views import ItemDisplayView, ItemCreateView
from django.conf.urls import url

urlpatterns = [
    path('items/',ItemDisplayView.as_view()),     
    path('items/create',ItemCreateView.as_view()),     
]