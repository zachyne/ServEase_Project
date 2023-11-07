from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import Service, Category
from .forms import NewServiceForm, EditServiceForm


# Create your views here.

def services(request):
	query = request.GET.get('query', '')
	services = Service.objects.filter(is_sold=False)
	categories = Category.objects.all()
	category_id = request.GET.get('category', 0)

	if query:
		services = services.filter(Q(name__icontains=query) | Q(description__icontains=query))


	if category_id:
		services = services.filter(category_id=category_id)


	return render(request, 'service/services.html', {
		'services': services,
		'query': query,
		'categories': categories,
		'category_id': int(category_id),
		})


def detail(request, pk):
	service = get_object_or_404(Service, pk=pk)
	related_services = Service.objects.filter(category=service.category, is_sold=False).exclude(pk=pk)[0:3]


	return render(request, 'service/detail.html', {'service': service, 'related_services': related_services})


@login_required
def new(request):
	if request.method == 'POST':
	    form = NewServiceForm(request.POST, request.FILES)

	    if form.is_valid():
	        service = form.save(commit=False)
	        service.created_by = request.user
	        service.save()  # Save the service instance to the database

	        return redirect('service:detail', pk=service.id)
	else:
	    form = NewServiceForm()  # Instantiate the form

	return render(request, 'service/form.html', {
	    'form': form,
	    'title': 'New Service'
	})


@login_required
def delete(request, pk):
	service = get_object_or_404(Service, pk=pk, created_by=request.user)
	service.delete()

	return redirect('account:index')


@login_required
def edit(request, pk):
    service = get_object_or_404(Service, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()

            return redirect('service:detail', pk=service.id)
    else:
        form = EditServiceForm(instance=service)

    return render(request, 'service/form.html', {
        'form': form,
        'title': 'Edit Service'
    })
