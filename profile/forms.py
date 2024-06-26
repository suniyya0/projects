from django import forms
from .models import UserProfile, Project, Skill, Education, Certification

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact_phone', 'contact_email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name']
