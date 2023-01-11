from django.urls import path
from .views import signup, profile, edit_profile, add_profile_number, add_profile_address, edit_profile_number, user_activate, wishlist, delete_profile_contact, delete_profile_address, edit_profile_address


app_name = 'accounts'


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('profile/edit',  edit_profile, name="edit_profile"),
    path('profile/edit/number',  edit_profile_number, name="edit_profile_number"),
    path('profile/edit/address',  edit_profile_address, name="edit_profile_address"),
    path('profile/add/number',  add_profile_number, name="add_profile_number"),
    path('profile/add/address',  add_profile_address, name="add_profile_address"),
    path('profile/delete/contact',  delete_profile_contact, name="delete_profile_contact"),
    path('profile/delete/address',  delete_profile_address, name="delete_profile_address"),
    path('<str:username>/activate', user_activate, name="user_activate"),
    path('wishlist/', wishlist, name="wishlist"),
]
