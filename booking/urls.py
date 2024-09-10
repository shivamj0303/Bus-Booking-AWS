from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_bus, name='search_bus'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('agency_id/<int:agency_id>/', views.agency_id, name='agency_id'),
    path('book/<int:bus_id>/', views.book_seat, name='book_seat'),
    path('register_bus/', views.register_bus, name='register_bus'),
    path('register_agency/', views.register_agency, name='register_agency'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
