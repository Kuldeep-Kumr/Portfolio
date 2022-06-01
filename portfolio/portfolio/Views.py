from django.shortcuts import render
from django.contrib import messages
import webbrowser
from .models import Dest

certificate = [
    ('HACKERPSI', 'Problem Solving'),
    ('HACKERRAPII', 'REST API '),
    ('HACKERPY', 'Python Basic'),
    ('HACKERSQL', 'SQL'),
    ('HACKERPSB', 'Problem Solving'),
    ('SAYLOR', 'Introduction To Python'),
    ('IBM', 'Data Analysis'),
    ('IBMDS', 'Data Science'),
    ('GUVIWR', 'World Record Participation'),
    ('UDEMYB2A', 'Basic To Advance Python'),
    ('UDEMYBOOT', 'Boot camp for Python'),
]

pr = [
    ('OSW', 'Shopping Website'),
    ('AAS', 'Automated Attendance System'),
    ('FF', 'Flight Fare'),
    ('HCP', 'Housing Cost'),
    ('INP', 'Iris Name'),
    ('RA', 'Renter App'),
    ('NA', 'Notebook App'),

]

skill = [
    ('PY', 'Python'),
    ('DJ', 'Django'),
    ('MYSQL', 'MYSQL'),
    ('DS', 'Data Structure'),
    ('ML', 'Machine Learning'),
    ('C', 'C Programing'),
    ('JAVA', 'Java'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JS', 'Java Script'),
    ('BT', 'Bootstrap'),
    ('FB', 'Firebase'),
    ('SQL', ' PL/sSQL'),
    ('DSC', 'Data Science')
]

services = [
    ('CC', 'Competitive Coding'),
    ('SDE', 'Software Developer'),
    ('WD', 'Web Development'),
    ('AD', 'Android Development'),
    ('ML', 'Machine Learning'),
]

bd = [
    ('BPY', 'Python'),
    ('DAIBM', 'Data Analysis'),
    ('DSIBM', 'Data Science'),
]


def home(request):
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def resume(request):
    webbrowser.open_new('https://drive.google.com/file/d/1PF4Hi3_LvIWJItutnumwSziRyDaZpuCj/view?usp=sharing')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def certi(request):
    items = []
    for q in range(len(certificate)):
        itemi = Dest()
        itemi.cimg = certificate[q][0] + '.JPG'
        itemi.cname = certificate[q][1]
        items.append(itemi)
    return render(request, 'certi.html', {'items': items})


def pp(request):
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def skills(request):
    items = []
    for q in range(len(skill)):
        itemi = Dest()
        itemi.cimg = skill[q][0] + '.JPG'
        itemi.cname = skill[q][1]
        items.append(itemi)
    return render(request, 'skills.html', {'items': items})


def work(request):
    return render(request, 'work.html')


def Badges(request):
    items = []
    for q in range(len(bd)):
        itemi = Dest()
        itemi.pid = bd[q][0]
        itemi.cimg = bd[q][0] + '.JPG'
        itemi.cname = bd[q][1]
        items.append(itemi)
    return render(request, 'Badges.html', {'items': items})


# Badges details


def DAIBM(request):
    webbrowser.open_new('https://www.credly.com/badges/751cef9d-6502-4092-a299-3e088d7f38ae/public_url')
    items = []
    for q in range(len(bd)):
        itemi = Dest()
        itemi.pid = bd[q][0]
        itemi.cimg = bd[q][0] + '.JPG'
        itemi.cname = bd[q][1]
        items.append(itemi)
    return render(request, 'Badges.html', {'items': items})


def DSIBM(request):
    webbrowser.open_new('https://www.credly.com/earner/earned/badge/f2c04322-6cde-4a19-b34b-0af2c2ad2f2b')
    items = []
    for q in range(len(bd)):
        itemi = Dest()
        itemi.pid = bd[q][0]
        itemi.cimg = bd[q][0] + '.JPG'
        itemi.cname = bd[q][1]
        items.append(itemi)
    return render(request, 'Badges.html', {'items': items})


def BPY(request):
    webbrowser.open_new('https://www.hackerrank.com/kuldeepkumar0329')
    items = []
    for q in range(len(bd)):
        itemi = Dest()
        itemi.pid = bd[q][0]
        itemi.cimg = bd[q][0] + '.JPG'
        itemi.cname = bd[q][1]
        items.append(itemi)
    return render(request, 'Badges.html', {'items': items})


def BSQL(request):
    webbrowser.open_new('https://www.hackerrank.com/kuldeepkumar0329')
    items = []
    for q in range(len(bd)):
        itemi = Dest()
        itemi.pid = bd[q][0]
        itemi.cimg = bd[q][0] + '.JPG'
        itemi.cname = bd[q][1]
        items.append(itemi)
    return render(request, 'Badges.html', {'items': items})


# Personal project

def ff(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Ml-Filght_fare_prediction')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def hcp(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/ML-Housing_cost_prediction')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def inp(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Portfolio')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def na(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Portfolio')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def ra(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Portfolio')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def osw(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Portfolio')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


def aas(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr/Portfolio')
    items = []
    for q in range(len(pr)):
        itemi = Dest()
        itemi.pid = pr[q][0]
        itemi.cimg = pr[q][0] + '.JPG'
        itemi.cname = pr[q][1]
        items.append(itemi)
    return render(request, 'pp.html', {'items': items})


# Contacts Details


def github(request):
    webbrowser.open_new('https://github.com/Kuldeep-Kumr')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def linked(request):
    webbrowser.open_new('https://www.linkedin.com/in/kuldeep-kumar-singh/')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def gmail(request):
    webbrowser.open_new('https://mail.google.com/mail/u/0/?hl=en-GB&tf=cm&fs=1&to=kuldeepkumar0329@gmail.coms')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def twitter(request):
    webbrowser.open_new('https://twitter.com/_Kuldeep_Kumar_')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def fb(request):
    webbrowser.open_new('https://www.facebook.com/profile.php?id=100066244071308')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})


def insta(request):
    webbrowser.open_new('https://www.instagram.com/_.kuldeep._kumar._/')
    messages.info(request, 'Portfolio of Mr. Kuldeep Kumar Singh')
    items = []
    for q in range(len(services)):
        itemi = Dest()
        itemi.cimg = services[q][0] + '.JPG'
        itemi.cname = services[q][1]
        items.append(itemi)
    return render(request, 'home.html', {'items': items})
