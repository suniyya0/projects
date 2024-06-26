from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Project, Skill, Education, Certification
from .forms import UserProfileForm, ProjectForm, SkillForm, EducationForm, CertificationForm
from django.shortcuts import render

@login_required
def create_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  # Redirect to view_profile or any other appropriate view
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'create_profile.html', context)

@login_required
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def view_profile(request):
    user_profile = request.user.userprofile  # Assuming UserProfile is linked to User
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'base.html', context)

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Optionally, redirect to a success page or another URL
    else:
        form = ProjectForm()

    # Retrieve all projects for display
    projects = Project.objects.all()

    context = {
        'form': form,
        'projects': projects,
    }
    return render(request, 'add_project.html', context)
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user_profile = request.user.userprofile
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

def home(request):
    # Example view function for the root path
    context = {
        'message': 'Welcome to our profile management system!'
    }
    return render(request, 'home.html', context)