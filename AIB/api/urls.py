"""AIB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path
from api import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^api/agreement$', views.AddAgreement),
    re_path(r'^api/agreement/(?P<id>[0-9])', views.GetAgreement),
    re_path(r'^api/agreement/all$', views.getAllAgreements),
    re_path(r'^api/invoice$', views.AddInvoice),
    re_path(r'^api/invoice/all$', views.getAllInvoice),
    re_path(r'^api/invoice/(?P<id>[0-9])', views.GetInvoice),
    re_path(r'^api/login/(?P<email>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)/(?P<passw>.*)', views.GetLogin),
    re_path(r'^api/img$', views.AddPdf)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
