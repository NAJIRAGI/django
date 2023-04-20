from django.urls import path

from accountapp.views import helloworld

app_name = "accountapp"

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),

]