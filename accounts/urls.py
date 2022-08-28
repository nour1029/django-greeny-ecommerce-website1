from django.urls import path
from .views import signup, profile, edit_profile, user_activate, wishlist


app_name = 'accounts'


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('<str:username>/activate', user_activate, name="user_activate"),
    path('wishlist/', wishlist, name="wishlist"),
]
