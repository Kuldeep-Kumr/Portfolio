"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import Views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.home, name="home"),
    path('about', Views.about, name="about"),
    path('certi', Views.certi, name="certificates"),
    path('pp', Views.pp, name="personal_project"),
    path('skills', Views.skills, name="skills"),
    path('work', Views.work, name="work"),
    path('home', Views.home, name="home"),
    path('resume', Views.resume, name="resume"),
    path('badges', Views.Badges, name="badges"),

    path('DAIBM', Views.DAIBM, name="badges"),
    path('DSIBM', Views.DSIBM, name="badges"),
    path('BPY', Views.DSIBM, name="badges"),
    path('BSQL', Views.DSIBM, name="badges"),

    path('FF', Views.ff, name="FlitFare"),
    path('HCP', Views.hcp, name="HousingCost"),
    path('LAP', Views.lap, name="LoanAcceptance"),
    path('INP', Views.inp, name="IrisName"),
    path('NA', Views.na, name="NotebookApp"),
    path('RA', Views.ra, name="RenterApp"),
    path('OSW', Views.osw, name="OnlineShoppingWebsite"),
    path('AAS', Views.aas, name="AutomatedAttendanceSystem"),

    path('github', Views.github, name="github"),
    path('linked', Views.linked, name="linkedin"),
    path('gmail', Views.gmail, name="gmail"),
    path('twitter', Views.twitter, name="twitter"),
    path('fb', Views.fb, name="facebook"),
    path('insta', Views.insta, name="instagram"),
]
urlpatterns += staticfiles_urlpatterns()
