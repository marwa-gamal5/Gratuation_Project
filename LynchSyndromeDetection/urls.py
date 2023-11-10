"""
URL configuration for LynchSyndromeDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Recona import views
from django.conf import settings
from django.conf.urls.static import static
from Upload import views
from Recona import views as recona_views
from Upload import views as upload_views
from Accounts import views as Accounts_views

app_name = 'Recona'  # For the Recona app
app_name = 'Upload'  # For the Upload app
from Recona import views as home
from Recona import views as abo
from Recona import views as res
from Upload import views as add_folder
from Upload import views as Uploadfiles
from Upload import views as run_docker
from Upload import views as file_view
urlpatterns = [
path('admin/', admin.site.urls),
path('', recona_views.home, name='homee'),
path('abo/', recona_views.abo, name='my_view'),
path('res/', recona_views.res, name='res'),
#path('Upload/', upload_views.add_folder, name='x'),
path('Uploadfiles/', upload_views.Uploadfiles, name='Uploadfiles'),
path('run_docker/', upload_views.run_docker, name='run_docker'),
path('Login/', Accounts_views.Login, name='login'),
path('sign_up/', Accounts_views.sign_up, name='sign_up'),
path('download/', upload_views.download, name='download'),
path('view/', upload_views.view, name='view'),
path('file_view/', upload_views.file_view, name='file_view'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
