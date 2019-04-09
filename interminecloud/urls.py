from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from interminecloud.views import UserprofileViewSet,IntermineViewSet
from interminecloud.views import AuthenticateIntermine

router = routers.DefaultRouter()
router.register('user', UserprofileViewSet)
router.register('intermine', IntermineViewSet)


urlpatterns = [
    path('v1/',include(router.urls)),
    path('auth/',AuthenticateIntermine, name='token'),

]