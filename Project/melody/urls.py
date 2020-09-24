from django.urls import path
from . import views

app_name='melody'
urlpatterns=[
    path('index', views.MelodyIndexView.as_view(), name="melody_index_view"),
    path('customerRegistration', views.MelodyCustomerRegistrationView.as_view(), name="melody_customerRegistration_view"),
    path('productDashboard', views.MelodyProductDashboardView.as_view(), name="melody_productDashboard_view"),
    path('customerDashboard', views.MelodyCustomerDashboardView.as_view(), name="melody_customerDashboard_view"),
    path('songRegistration', views.MelodySongRegistrationView.as_view(), name="melody_songRegistration_view"),
]