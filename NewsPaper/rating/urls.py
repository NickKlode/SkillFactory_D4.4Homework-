from django.urls import path
from .views import *  

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name='detail'),
    path('search/', NewsSearchView.as_view(), name='search'),
    path('add/', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='delete'),
]