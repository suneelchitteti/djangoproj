from django import forms
from .models import registration
class registrationform(forms.ModelForm):
    class Meta:
        model=registration
        widgets={'Pwd':forms.PasswordInput()}
        fields=('User','Pwd','FirstName','LastName','email','Dob','phone')
class Loginform(forms.Form):
    user=forms.CharField(max_length=20)
    Pwd=forms.CharField(widget=forms.PasswordInput())
