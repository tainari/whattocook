from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('recipes',views.RecipeViewSet,basename='recipes')
urlpatterns = router.urls
# urlpatterns = [
#     path("__debug__/", include("debug_toolbar.urls")),
#     path('', views.index, name='index')
# ]
