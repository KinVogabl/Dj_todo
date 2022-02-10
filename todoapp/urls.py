from todoapp.views import AboutView
from django.urls import path

urlpatterns = [
    path('',AboutView.as_view() )
]
