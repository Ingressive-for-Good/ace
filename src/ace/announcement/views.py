from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Announcement
from announcement.models import Profile
from .forms import ApproveForm, AnnouncementUpdateForm
from workspace.models import Workspace
from django.contrib import messages

# Create your views here.



class AnnouncementListView(View):
    def get(self, request, pk, *args, **kwargs):
        form = ApproveForm()

        announcement = Announcement.objects.filter(workspace=pk)
        workspace = get_object_or_404(Workspace, pk=pk)
        context = {
        'pk':pk,
        'form':form,
        'objects':announcement,
        'workspace':workspace
        }
        return render(self.request, "announcement/announcement_list.html", context)
    
    def post(self, request, pk, *args, **kwargs):
        announcement_qs = Announcement.objects.filter(workspace=pk)
        for announcement in announcement_qs:
            form = AnnouncementUpdateForm(self.request.POST)
            if form.is_valid():
                approved = form.cleaned_data.get('approved')
                announcement.approved = approved
                announcement.save()
        messages.success(request, f'The Announcement has been updated!')
        return redirect('workspace-details', pk)



class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'image', 'expiry_date']
    
    def form_valid(self, form,):
        form.instance.author = get_object_or_404(Profile, user=self.request.user)
        form.instance.workspace = get_object_or_404(Workspace, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class AnnouncementDetailView(DetailView):
    model = Announcement
    # def get(self, request, pk, a_pk, *args, **kwargs):
    #   announcement = Announcement.objects.filter(workspace=pk, pk=a_pk)[0]
    #   context = {'object': announcement}
    #   return render(request, "message/announcement_detail.html", context)




class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = get_object_or_404(Profile, user=self.request.user)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        user = get_object_or_404(Profile, user=self.request.user)
        if user == post.author:
            return True
        return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        user = get_object_or_404(Profile, user=self.request.user)
        if user == post.author:
            return True
        return False

def Approve(request, pk, a_pk):
    announcement = get_object_or_404(Announcement, pk=a_pk)
    announcement.approved = True
    announcement.save()
    messages.info(request, "You have approved this announcement")
    return redirect("announcements", pk)


def Unapprove(request, pk, a_pk):
    announcement = get_object_or_404(Announcement, pk=a_pk)
    announcement.approved = False
    announcement.save()
    messages.info(request, "You have unapproved this announcement")
    return redirect("announcements", pk)






















# @login_required
# def create_announcement(request):
#     if request.method == 'POST':
#         if request.POST['title'] and request.POST['content']:
#             announcement = Announcement()
#             announcement.title = request.POST['title']
#             announcement.content = request.POST['content']
#             # announcement.image = request.FILES['image']
#             announcement.author = Profile.objects.get(user=request.user)
#             announcement.save()
#             return redirect('landing_page') #temporarily because there's no workspace page to redirect to yet
#         else:
#             return HttpResponse('Error: Announcement creation failed')
#     else:
#         return render(request, 'announcement/create_announcement.html')


# @login_required
# def delete_announcement(request, pk):
#     query = Announcement.objects.get(pk=pk)
#     query.delete()
#     return HttpResponse('Delete operation successful')
#     