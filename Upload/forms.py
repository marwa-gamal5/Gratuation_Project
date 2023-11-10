

from django import forms
from .models import Folder
from .models import OneFolder

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name', 'file1', 'file2')

class FolderOneForm(forms.ModelForm):
    class Meta:
        model = OneFolder
        fields = ('name', 'file1')
