from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signup/', views.signup, name='signup'),
    path('form/', views.user_form, name='form_page'),
    path('thanks/', views.confirmation_page, name='confirmation_page'),
]

