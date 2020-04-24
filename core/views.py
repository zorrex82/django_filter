from django.shortcuts import render

def BoostrapFilterView(request):
    return render(request, 'bootstrap_form.html', {})