from django.urls import path
from .views import landing_page

app_name = "leads"

urlpatterns = [
    path('', view=landing_page, name="landing-page"),
]