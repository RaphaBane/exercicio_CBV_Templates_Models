"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from info_app.views import WelcomeView, GoodbyeView, TimeView, GreetView, AgeCategoryView, SumView, AboutView, PeopleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', WelcomeView.as_view(), name="welcome"),
    path('goodbye', GoodbyeView.as_view(), name="goodbye"),
    path('time', TimeView.as_view(), name="time"),
    path('greet', GreetView.as_view(), name="greet"),
    path('age-category', AgeCategoryView.as_view(), name="age_category"),
    path('sum/<num1>/<num2>', SumView.as_view(), name="sum"),
    path('about', AboutView.as_view(), name="about"),
    path('people', PeopleView.as_view(), name="people")
]