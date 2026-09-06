from django import forms
from .models import Note,Document,Password,Event,Task,Transaction,User


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = ['title', 'content']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Note Title'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your note here...',
                'rows': 8
            }),

        }

from django import forms
from .models import Note, Document


# ==========================
# NOTE FORM
# ==========================

class NoteForm(forms.ModelForm):

    class Meta:

        model = Note

        fields = ['title', 'content']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),

        }


# ==========================
# DOCUMENT FORM
# (Dashboard Upload)
# ==========================

class DocumentForm(forms.ModelForm):

    class Meta:

        model = Document

        fields = [

            'title',

            'category',

            'file',

            'description'

        ]

        widgets = {

            'title': forms.TextInput(attrs={

                'class': 'form-control',

                'placeholder': 'Document Title'

            }),

            'category': forms.Select(attrs={

                'class': 'form-select'

            }),

            'description': forms.Textarea(attrs={

                'class': 'form-control',

                'rows': 4

            })

        }


# ==========================
# CATEGORY DOCUMENT FORM
# (Folder Upload)
# ==========================

class CategoryDocumentForm(forms.ModelForm):

    class Meta:

        model = Document

        fields = [

            'title',

            'file',

            'description'

        ]

        widgets = {

            'title': forms.TextInput(attrs={

                'class': 'form-control',

                'placeholder': 'Document Title'

            }),

            'description': forms.Textarea(attrs={

                'class': 'form-control',

                'rows': 4

            })

        }

# ==========================
# PASSWORD FORM
# ==========================

class PasswordForm(forms.ModelForm):

    class Meta:

        model = Password

        fields = [

            'title',

            'website',

            'username',

            'password',

            'notes'

        ]

        widgets = {

            'password': forms.PasswordInput(attrs={

    'class': 'form-control',

    'id': 'id_password',

    'placeholder': 'Enter Password'

}),

            'website': forms.URLInput(attrs={

                'class':'form-control',

                'placeholder':'https://'

            }),

            'username': forms.TextInput(attrs={

                'class':'form-control',

                'placeholder':'Email or Username'

            }),

            'password': forms.PasswordInput(attrs={

                'class':'form-control',

                'placeholder':'Enter Password'

            }),

            'notes': forms.Textarea(attrs={

                'class':'form-control',

                'rows':4,

                'placeholder':'Optional Notes'

            }),

        }

# ==========================================
# EVENT FORM
# ==========================================

class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [

            'title',

            'description',

            'date',

            'location',

            'color'

        ]

        widgets = {

            'title': forms.TextInput(attrs={

                'class':'form-control',

                'placeholder':'Event Title'

            }),

            'description': forms.Textarea(attrs={

                'class':'form-control',

                'rows':4

            }),

            'date': forms.DateInput(attrs={

                'class':'form-control',

                'type':'date'

            }),

            'location': forms.TextInput(attrs={

                'class':'form-control',

                'placeholder':'Location'

            }),

            'color': forms.Select(attrs={

                'class':'form-select'

            }),

        }      

# ==========================================
# TASK FORM
# ==========================================

class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = [

            'title',

            'description',

            'due_date',

            'priority',

        ]

        widgets = {

            'title': forms.TextInput(attrs={

                'class': 'form-control',

                'placeholder': 'Task Title'

            }),

            'description': forms.Textarea(attrs={

                'class': 'form-control',

                'rows': 4,

                'placeholder': 'Description'

            }),

            'due_date': forms.DateInput(attrs={

                'class': 'form-control',

                'type': 'date'

            }),

            'priority': forms.Select(attrs={

                'class': 'form-select'

            }),

        }  

# ==========================================
# TRANSACTION FORM
# ==========================================

class TransactionForm(forms.ModelForm):

    class Meta:

        model = Transaction

        fields = [

            'transaction_type',

            'title',

            'category',

            'amount',

            'date',

            'description'

        ]

        widgets = {

            'transaction_type': forms.Select(attrs={

                'class':'form-select'

            }),

            'title': forms.TextInput(attrs={

                'class':'form-control',

                'placeholder':'Transaction Title'

            }),

            'category': forms.Select(attrs={

                'class':'form-select'

            }),

            'amount': forms.NumberInput(attrs={

                'class':'form-control',

                'placeholder':'Amount'

            }),

            'date': forms.DateInput(attrs={

                'class':'form-control',

                'type':'date'

            }),

            'description': forms.Textarea(attrs={

                'class':'form-control',

                'rows':4,

                'placeholder':'Description'

            }),

        }

class EditProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [

            'first_name',
            'last_name',
            'email',

        ]

        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }