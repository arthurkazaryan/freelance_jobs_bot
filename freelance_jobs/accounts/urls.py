from django.urls import path
from accounts.views import RegisterUser, LoginUser, ProfilePage, SettingsPage, logout_user


urlpatterns = [
    path('profile/', ProfilePage.as_view(), name='accounts-profile'),
    path('settings/', SettingsPage.as_view(), name='accounts-settings'),
    path('register/', RegisterUser.as_view(), name='accounts-register'),
    path('login/', LoginUser.as_view(), name='accounts-login'),
    path('logout/', logout_user, name='accounts-logout')
]
