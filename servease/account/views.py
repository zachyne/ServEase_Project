from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.models import Service 

# Create your views here.
@login_required
def index(request):
	services = Service.objects.filter(created_by=request.user)

	return render(request, 'account/account.html', {
		'services': services,
		})


