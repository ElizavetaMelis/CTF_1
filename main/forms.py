from django.contrib.auth import get_user_model
from django import forms

Student = get_user_model()

class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(min_length=8, required=True)

    class Meta:
        model = Student
        fields = ('full_name', 'age', 'email', 'password', 'password_confirmation')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Student.objects.filter(username=username).exists():
            raise forms.ValidationError('User already exists')
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Password don\'t match')
        return data

    def save(self, commit=True):
        # print(self.cleaned_data)
        user = Student.objects.create(**self.cleaned_data)
        return user
