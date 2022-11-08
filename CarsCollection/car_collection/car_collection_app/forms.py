from django import forms
from car_collection.car_collection_app.models import Profile, Car


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarDeleteForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
