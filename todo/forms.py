from django.forms import ModelForm

from .models import ToDo

# Create your models here.

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['text']
        labels = {'text':''}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'todo', 'class':'form-control'})