from django import forms 
from labeler.models import Person 

class PersonRegister(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    likes_law = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    likes_real_estate = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    likes_computer_vision = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        likes_count = sum(cleaned_data.get(like_field, False) for like_field in \
                          ["likes_law", "likes_real_estate", "likes_computer_vision"])
        if likes_count > 1:
            raise forms.ValidationError("You can only select up to 1 category")
        return cleaned_data

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "username", "email", "likes_law", "likes_real_estate", \
                   "likes_computer_vision", "password"]


class PersonLogin(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = Person
        fields = ["username", "password"]


class Answer(forms.Form):
    pixels = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField(required=True)
    class Meta:
        fields = ["answer"]
