from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

#custom signup form SignUpForm that inherits from 
#UserCreationForm and is associated with your custom User model. 
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1','password2',)
        


class Loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password',)