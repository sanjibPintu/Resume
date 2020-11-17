from django.shortcuts import render

# Create your views here.
def skill(request):
    print('skill page is running')
    return render(request ,'edu/skill.html',{'skill':'active'})