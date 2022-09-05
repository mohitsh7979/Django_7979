from rest_framework.routers import DefaultRouter


from.views import AddressViewset
from django.urls import path,include

router=DefaultRouter()
router.register('address',AddressViewset)

urlpatterns = [
    path('api/',include(router.urls)),
]