from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="Index"),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemView.as_view(), name="Menu List"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="Single Menu Item View"),
    path('booking/', include(router.urls))
]
