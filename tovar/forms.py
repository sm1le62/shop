# -*- coding: utf-8 -*-

from django import forms
from .models import Tovar

class TagListForm(forms.Form):
    tag_list = forms.CharField(label='new', required=False)

class TovarForm(forms.Form):
    title = forms.CharField(label='Name', max_length=256)
    article = forms.CharField(label='Article', max_length=256)
    quantity = forms.IntegerField(label='In stock', min_value=0)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    
    

class TovarModelForm(forms.ModelForm):
    
    #form creating here, if it need
    class Meta:
        model = Tovar
        fields = ['title', 'article', 'quantity', 'description']
