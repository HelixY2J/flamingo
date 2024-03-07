from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm




# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST) # pasting form data here'
        
        # print(form['username'].value())
        # print(form['email'].value())

        
        if form.is_valid():  # doing some input validation on its own
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['email'])
            print("i am in form ")
            # print(form.instance.my_field)
            user = form.save()

              # saving form data in user
            authenticate(username=user.username, password=user.password)
            # used authen. clas to check this
            if user is not None:
                login(request,user)
                return redirect('/')
        else:
            print(form.is_valid())
            print(form.errors)
        


    else:
        form = SignupForm()
        
    return render(request,'accounts/signup.html',
                  {'form':form
                   })
        

    