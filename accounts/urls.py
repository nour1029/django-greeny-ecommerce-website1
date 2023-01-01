from django.urls import path
from .views import signup, profile, edit_profile, add_profile_number, add_profile_address, edit_profile_number, user_activate, wishlist


app_name = 'accounts'


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('profile/edit',  edit_profile, name="edit_profile"),
    path('profile/edit/number',  edit_profile_number, name="edit_profile_number"),
    path('profile/add/number',  add_profile_number, name="add_profile_number"),
    path('profile/add/address',  add_profile_address, name="add_profile_address"),
    path('<str:username>/activate', user_activate, name="user_activate"),
    path('wishlist/', wishlist, name="wishlist"),
]
