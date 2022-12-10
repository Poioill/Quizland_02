from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=CustomLoginForm), name='login')
]
