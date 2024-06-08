from django import forms
from student.models import student,course

class Studentform(forms.ModelForm):
    class Meta:
        model = student
        fields="__all__"

class Courseform(forms.ModelForm):
    class Meta:
        model= course
        fields = "__all__"

        