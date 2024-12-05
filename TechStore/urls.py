"""
URL configuration for TechStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

# Маршруты страниц
urlpatterns = [
    path("", main_views.home_page, name="home_page"),
    path("iphones/", main_views.iphones_page, name="iphones_page"),
    path("reviews/", main_views.all_reviews_page, name="reviews_page"),
    path(
        "reviews/<int:review_id>/",
        main_views.review_detail_page,
        name="review_detail_page",
    ),
    path("reviews/add/", main_views.add_reviews_page, name="add_reviews_page"),
    path("about/", main_views.about_page, name="about_page"),
    path("submit/", main_views.submit_form, name="submit_form"),
    path(
        "callback-request/",
        main_views.callback_request_page,
        name="callback_request_page",
    ),
    path("admin/", admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # маршруты для медиафайлов
