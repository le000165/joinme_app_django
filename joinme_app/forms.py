from django import forms
from .models import Activity, User, Comment

# Create your forms here
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: forms.py
# JoinMe Project


class ActivityForm(forms.ModelForm):
    """
    Activity form will be the form for creating and updating
    inherits from the ModelForm
    """

    class Meta:
        """
        Inner class for the ActivityForm for the purpose of initializing
        """
        model = Activity
        fields = ('activity_name', 'city', 'address',
                  'fees', 'organizer', 'start', 'end',
                  'date', 'num_people', 'email', 'province', 'zip')
        labels = {
            'activity_name': 'Type of Activity',
            'city': 'City',
            'adrress': 'Address',
            'fees': 'Fees (enter number only)',
            'organizer': 'Organizer Name',
            'date': 'Date (YYYY-MM-DD)',
            'start': 'From',
            'end': 'To',
            'num_people': 'People registered',
            'email': 'Email',
            'province': 'Province',
            'zip': 'Zip'
        }

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)


class NewUserForm(forms.ModelForm):
    """
    User form will be the form for creating and updating
    inherits from the ModelForm
    """
    pswd = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """
        Inner class for the ActivityForm for the purpose of initializing
        """
        model = User
        # what fields are for form input
        fields = ('first_name', 'last_name', 'u_email',
                  'pswd', 'birth_date', 'gender')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'u_email': 'Email',
            'pswd': 'New Password',
            'birth_date': 'Birth Date',
            'gender': 'Gender',
        }

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['pswd'].label = "New Password"


class CommentForm(forms.ModelForm):
    """
    CommentForm will be the form for creating the comment
    inherits from the ModelForm
    """
    # body = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, class="form-control"})
    class Meta:
        """
        Inner class for the CommentForm for the purpose of initializing
        """
        model = Comment
        # what fields are for form input
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)


class LoginForm(forms.ModelForm):
    """
    LoginForm will be the form for user login
    inherits from the ModelForm
    """
    # u_email = forms.CharField(widget=forms.TextInput)
    # pswd = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """
        Inner class for the LoginForm for the purpose of initializing
        """
        model = User
        fields = ('u_email', 'pswd')

        widgets = {
            'u_email': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email or Phone Number'}),
            'pswd': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password', 'type': 'password'}),
        }

        # what fields are for login form

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
