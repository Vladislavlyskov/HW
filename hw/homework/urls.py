from django.urls import path
from homework.views import MainView

urlpatterns = [
    path('name/', MainView.as_view(), name="form_profile"),
]