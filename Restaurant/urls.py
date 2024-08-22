from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="Index"),
    path('menu/', views.MenuItemView.as_view(), name="Menu List"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="Single Menu Item View"),
    path('booking/', include(router.urls))
]
