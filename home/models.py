from django.db import models
from django.shortcuts import render
from django import forms
from django.core.validators import RegexValidator

from wagtail.models import Page


class HomePage(Page):
    
    """Template"""
    template = "home/home_page.html"

    """Form processing"""
    def serve(self, request):
        if request.method == "POST":
            form = CustomForm(request)
            
            if form.is_valid():
                return render(request, self.template, {
                    "page": self,
                    "form": form,
                    "success": True
                })
        else:
            form = CustomForm()

        return render(request, self.template, {
            "page": self,
            "form": form
        })
    


class CustomForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={
            "placeholder": "Enter Your Name",
            "class": ""
            })
        )
    
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            "placeholder": "Enter Your Email",
            "class": ""
            })
    )

    phone = forms.CharField(
        max_length=15,
        validators = [RegexValidator(r'^\+?1?\d{9,15}$', 'Enter Your Phone')],
        widget = forms.TextInput(attrs={
            "placeholder": "Enter Your Phone",
            "tyipe": "tel",
            "class": ""
            })
    )

    date = forms.DateField(
        widget = forms.DateInput(attrs={
            "type": "date",
            "class": ""
        })
    )

    time = forms.DateField(
        widget = forms.TimeInput(attrs={
            "type": "time",
            "class": ""
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Describe Your Problem",
            "class": ""
            })
    )
    
