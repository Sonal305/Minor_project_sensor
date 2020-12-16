from django.urls import include, path
# from rest_framework import routers
# # from .views import UserListView,UserDetailView
# from .views import UserViewSet
#
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
#
# urlpatterns = [
#     # path("",UserListView.as_view(),name='list'),
#     # path('<int:pk>',UserDetailView.as_view(),name='detail')
#      path("", include(router.urls)),
#      path('auth',include('rest_framework.urls',namespace='rest_framework'))
# ]

from . import views
urlpatterns = [
    path('', views.homeListView.as_view()),
    path('<int:pk>/', views.homeDetailView.as_view()),

    path('damage/', views.damageListView.as_view()),
    path('damage/<int:pk>/', views.damageDetailView.as_view()),

    path('damageList/<str:home_add>/',views.DamageHomeListView.as_view()),
    #path('damagesdetails/<str:home_add>/',views.DamageHomeDetailView.as_view()),

]
