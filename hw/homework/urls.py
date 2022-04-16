from django.urls import path
from homework.views import MainView

urlpatterns = [
    path('index/', MainView.as_view(), name="form_profile"),
]