from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet


router = SimpleRouter()

router.register('cats', CatViewSet, basename='tiger')

urlpatterns = [
    path('cat/', ..., name='tiger-list'),
    path('cat/<int:pk>/', ..., name='tiger-detail'),
]


