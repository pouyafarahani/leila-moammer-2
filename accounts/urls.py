from django.urls import path

from .views import signup, login_view, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', ProfileView, name='profile'),
]
