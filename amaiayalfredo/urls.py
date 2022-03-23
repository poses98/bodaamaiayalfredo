
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the main application
from django.urls import include
# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('boda/', include('boda.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='boda/', permanent=True)),
]
