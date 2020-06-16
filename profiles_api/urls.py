from django.contrib import admin
from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('user-info',views.UserInfoViewList)

urlpatterns = [

    path('login/',views.UserLoginViewSet.as_view()),
    path('',include(router.urls)),
]