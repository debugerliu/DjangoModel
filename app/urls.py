from django.conf.urls import url

from app import views

urlpatterns = [
    url('add_person', views.add_person),
    url('person_list', views.person_list)
]