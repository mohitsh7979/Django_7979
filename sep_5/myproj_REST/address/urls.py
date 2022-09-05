from rest_framework.routers import DefaultRouter

from myproj_REST.address.models import Address
from.views import AddressViewset, path,include

router=DefaultRouter()
router.register('address',AddressViewset)

urlpatterns = [
    path('api/',include(router.urls)),
]