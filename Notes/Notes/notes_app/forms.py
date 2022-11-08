from django import forms
from Notes.notes_app.models import Profile, Note


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNote(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = '__all__'
