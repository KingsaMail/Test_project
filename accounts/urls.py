from django.urls import path
from .views import SignUp

#app_name = 'app_signup'
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]