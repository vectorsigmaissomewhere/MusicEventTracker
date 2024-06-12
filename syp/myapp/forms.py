from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback,AddEvent

"""Inheritts functionality of UserCreationForm
model = User means the form should use the User model
field means it should include the username , password1 and password2
"""
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # the field should use render html input element of type password


class FeedbackForm(forms.ModelForm):
    class Meta:
        # specifies that the form is tied to the Feedback model
        model = Feedback
        fields = ['feedback_text']
        # custom widgets for feedback_text
        widgets = {
            'feedback_text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Enter your feedback here...'})
        }

class AddEventForm(forms.ModelForm):
    """specifies the form is tied to AddEvent Model"""
    class Meta:
        model = AddEvent
        fields = ['your_artist_name', 'your_event_place', 'your_event_time', 'your_event_district', 'your_event_ticket','your_event_free']
