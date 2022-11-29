from django.urls import path
from .views import bot

urlpatterns = [
    path('', bot)
        # path('', RedirectView.as_view(url='http://0.0.0.0:9000/js/walker_run')),

]