from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Workspace
from .forms import ContributorForm

# Create your views here.


def welcome(request):
	'''this function is to redirect from login page to workspace list passing the username 
	of the logged in user as a parameter'''
	username = request.user.username
	if username == '':
		return render(request, 'workspace/landing_page.html', {'title': 'Ace'})
	else:
		return redirect('user-workspace', username)



class WorkspaceCreateView(LoginRequiredMixin, CreateView):
	model = Workspace
	fields = ['title', 'description', 'image']

	def form_valid(self, form):
		print(self.kwargs)
		form.instance.head = self.request.user
		return super().form_valid(form)


class UserWorkspaceListView(ListView):
	model = Workspace
	template_name = 'workspace/workspace_list.html'
	context_object_name = 'workspaces'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Workspace.objects.filter(head=user).order_by('-updated_at')

class WorkspaceDetailView(DetailView):
	model = Workspace

class WorkspaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Workspace
	fields = ['title', 'description', 'image']

	def form_valid(self, form):
		form.instance.head = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		user = self.request.user
		if user == post.head:
			return True
		return False

class WorkspaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Workspace
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		user = self.request.user
		if user == post.head:
			return True
		return False

class AddContributor(View):
	def get(self, request, pk, *args, **kwargs):
		form = ContributorForm()
		context = {
		'form':form,
		}
		return render(self.request, "workspace/contributor_form.html", context)

	def post(self, request, pk, *args, **kwargs):
		workspace =  get_object_or_404(Workspace, pk=self.kwargs.get('pk'))
		form = ContributorForm(self.request.POST or None)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			contributor = get_object_or_404(User, email= email)
			workspace.contributors.add(contributor)
			workspace.save()
			return redirect("workspace-details", pk)

def ContributorsListView(request, pk):
	workspace = Workspace.objects.get(pk=pk)
	contributors = workspace.contributors.all()
	context = {
		'head': workspace.head,
		'contributors':contributors,
		}
	return render(request, 'workspace/contributors_list.html', context )


def About(request):
	return render(request, 'workspace/about.html', {'title': 'About'})