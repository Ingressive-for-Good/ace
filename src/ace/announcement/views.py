from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Announcement
from announcement.models import Profile
# Create your views here.

@login_required
def create_announcement(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['content']:
            announcement = Announcement()
            announcement.title = request.POST['title']
            announcement.content = request.POST['content']
            # announcement.image = request.FILES['image']
            announcement.author = Profile.objects.get(user=request.user)
            announcement.save()
            return redirect('landing_page') #temporarily because there's no workspace page to redirect to yet
        else:
            return HttpResponse('Error: Announcement creation failed')
    else:
        return render(request, 'announcement/create_announcement.html')


@login_required
def delete_announcement(request, pk):
    query = Announcement.objects.get(pk=pk)
    query.delete()
    return HttpResponse('Delete operation successful')
    