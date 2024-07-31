from django.urls import path
from .views import TestUserAdd, TestUserList, GenerateImageView

urlpatterns = [
    path('test/', TestUserAdd.as_view(), name='test_user_list_create'),
    path('users/', TestUserList.as_view(), name='test_user_list'),
    path('generate-image/', GenerateImageView.as_view(), name='generate_image'),
]