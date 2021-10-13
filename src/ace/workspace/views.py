from django.shortcuts import render

# Create your views here.


def welcome(request):
	'''this function is to redirect from login page to workspace list passing the username 
	of the logged in user as a parameter'''
	username = request.user.username
	if username == '':
		return render(request, 'workspace/landing_page.html', {'title': 'Ace'})
	else:
		return redirect('user-workspace', username)