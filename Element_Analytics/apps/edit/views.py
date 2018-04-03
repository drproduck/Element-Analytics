from django.shortcuts import render, redirect
from apps.edit.forms import EditProfileForm

# Create your views here.
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/userprof/')
    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request,'edit/edit.html', args)

