from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from recipe.views import *

urlpatterns = [
    path('', splash_screen, name='splash_screen'),
    path("recipe_view/", recipe_view, name="recipe-view"),
    path("delete_recipe/<id>/", delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>/", update_recipe, name="update_recipe"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

urlpatterns += staticfiles_urlpatterns()
