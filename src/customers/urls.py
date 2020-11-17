from rest_framework import routers
from .views import CustomersViewSet

routers = routers.DefaultRouter()
routers.register('customers', CustomersViewSet, 'customers')

urlpatterns = routers.urls
