from django.contrib.auth.views import login
from django.urls import path
from mainsite import views

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', view=views.logout, name="logout"),
    path('signup/', view=views.signup, name="signup"),
]
