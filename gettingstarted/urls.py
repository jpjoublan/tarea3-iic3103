from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("tarea3/", hello.views.tarea3, name="tarea3"),
    path("film/", hello.views.film, name="film"),
    path("characters/", hello.views.characters, name="characters"),
    path("planets/", hello.views.planets, name="planets"),
    path("starships/", hello.views.starships, name="starships"),
    path("admin/", admin.site.urls),

]
