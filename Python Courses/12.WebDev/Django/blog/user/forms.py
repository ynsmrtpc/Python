from distutils.command.clean import clean
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label='Kullanıcı adı')
    email = forms.CharField(label='E-Mail Adresi',widget=forms.EmailInput)
    password = forms.CharField(max_length=20,label='Parola',widget=forms.PasswordInput)
    confirm  = forms.CharField(max_length=20,label='Parolayı doğrula',widget=forms.PasswordInput)
    
    # class eklemek için;
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm'].widget.attrs['class'] = 'form-control'
        
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        email = self.cleaned_data.get('email')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar Eşleşmiyor!')
        values = {
            'username' : username,
            'email'    : email,
            'password' : password
        }
        return values