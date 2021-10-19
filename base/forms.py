from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from .models import Entry, Feedback

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title','source','topic','link','user_code','optimized_code', 'user_notes']
        
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Title of post', 
                }),
            'source': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Source', 
                'choices': Entry.SOURCE_CHOICES
                }),
            'topic': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Topic', 
                'choices': Entry.TOPIC_CHOICES
                }),
            'link': URLInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Link to question', 
                }),
            'user_code': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; min-height: 600px;',
                'placeholder': 'Your original code'
                }),
            'optimized_code': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; min-height: 600px;',
                'placeholder': 'Optimized code'
                }),
            'user_notes': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; min-height: 600px;',
                'placeholder': 'Takeaways/Reflections'
                }),
        }