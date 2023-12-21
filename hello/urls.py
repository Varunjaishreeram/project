from hello import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:vendor_id>', views.retrieve_vendor, name='retrieve_vendor')
]