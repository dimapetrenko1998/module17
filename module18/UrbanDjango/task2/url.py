from django.urls import path
from .views import functional_view, ClassBasedView

urlpatterns = [
    path('func/', functional_view, name='functional_view'),
    path('class/', ClassBasedView.as_view(), name='ClassBasedView'),
]
