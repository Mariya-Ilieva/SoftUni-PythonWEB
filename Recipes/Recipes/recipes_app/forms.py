from django import forms
from Recipes.recipes_app.models import Recipe


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'ingredients': forms.TextInput(
                attrs={'placeholder': "Each ingredient should be separated by a comma!"}),
        }


class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipe(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
