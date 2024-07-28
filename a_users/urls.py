from django.urls import path
from .views import *


urlpatterns = [
    path("",profile_view,name='profile'),
    path("edit/",profile_edit_view,name='profile-edit'),
    path('onboarding/',profile_edit_view,name='profile-onboarding'),
    path('profile_settings/',profile_settings_view,name='profile_settings'),
    path('emailchange/',profile_emailchange,name='profile-emailchange'),
    path('emailverify/',profile_emailverify,name='profile-emailverify'),
    path('delete/',profile_delete_view,name='profile-delete'),
]
