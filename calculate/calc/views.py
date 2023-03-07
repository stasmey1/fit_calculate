from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy


def profile_list(request):
    profile_list = Profile.objects.all()
    template = 'profile/profile_list.html'
    return render(request, template, locals())


def profile_add(request):
    template = 'profile/profile_change.html'
    if request.method == "POST":
        form = ProfileAddForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save()
            return redirect(reverse_lazy('profile', kwargs={'slug': new_profile.slug}))
        else:
            form = ProfileAddForm(request.POST, request.FILES)
            return render(request, template, locals())
    else:
        form = ProfileAddForm()
        return render(request, template, locals())


def profile_change(request, slug):
    template = 'profile/profile_change.html'
    profile = get_object_or_404(Profile, slug=slug)
    form = ProfileAddForm(instance=profile)
    if request.method == "POST":
        form = ProfileAddForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'slug': profile.slug}))
        else:
            form = ProfileAddForm(request.POST, request.FILES, instance=profile)
    return render(request, template, locals())


def profile_delete(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    template = 'profile/profile_delete.html'
    if request.method == "POST":
        profile.delete()
        return redirect('profile_list')
    return render(request, template, locals())


def profile_ditail(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    body_mass_index = profile.body_mass_index()
    normal_weight = profile.normal_weight()

    if profile.target == '1':
        deficit_calories = profile.deficit_calories()
        deficit_protein_fat_carbohydrate = profile.deficit_protein_fat_carbohydrate()
    else:
        normal_calories = profile.normal_calories()
        normal_protein_fat_carbohydrate = profile.normal_protein_fat_carbohydrate()

    template = 'profile/profile_ditail.html'
    return render(request, template, locals())
