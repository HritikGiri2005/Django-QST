from django.urls import path
from Testapp import views

urlpatterns = [
    path('hello/',views.hello_view)
]
