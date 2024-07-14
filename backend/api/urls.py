from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.IndexApi.as_view(), name='example'),
    path('logout/', views.SendData.as_view(), name='oalah'),
    path('company_reg/', views.CompanyRegestration.as_view(), name='CompanyRegistration'),
    path('companies/', views.CompanyList.as_view(), name='company-list'),
]
