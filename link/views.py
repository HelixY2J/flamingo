from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


from .forms import CategoryForm,LinkForm

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        
        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()

            return redirect('/')
    
    else:
        form = LinkForm()

    

    return render(request,'link/create_link.html', {
        'form': form,
    })



@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect('/')
    
    else:
        form = CategoryForm()

    

    return render(request,'link/create_category.html', {
        'form': form,
    })