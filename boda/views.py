from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from boda.models import *
from .forms import *


def password_view(request):

    form = WebPasswordForm(request.GET or None)
    if form.is_valid():
        password = request.GET.get('password')
        if password == WebPassword.objects.all()[0].password:
            request.session['password'] = True
            return redirect("index")
    else:
        print("form is not valid")

    return render(request, 'password.html')


def password_check(request):
    if WebPassword.objects.all()[0].is_required:
        check = True
        try:
            if request.session['password']:
                check = False
        except:
            check = True
        return check
    else:
        return False


def index(request):
    if password_check(request):
        return redirect("password")

    """View function for home page of site."""
    # Nombres novios
    nombres_pareja = NombresPareja.objects.all()[0]
    # Fecha boda
    fecha_boda = FechaDeBoda.objects.all()[0]
    # Mes boda humanized
    mes_boda = getMonth(fecha_boda.get_month())
    # Lugar boda
    lugar_boda = LugarDeLaBoda.objects.all()[0]
    # Autobuses
    autobuses = Autobus.objects.all()

    buses_ida = Autobus.objects.filter(site_type='i')
    buses_vuelta = Autobus.objects.filter(site_type='v')
    context = {
        'nombres_pareja': nombres_pareja,
        'fecha_boda': fecha_boda,
        'mes_boda': mes_boda,
        'lugar_boda': lugar_boda,
        'buses_ida': buses_ida,
        'buses_vuelta': buses_vuelta,
    }

    return render(request, 'index.html', context=context)


def SuccessForm(request):
    return render(request, 'inscripcion_realizada.html')


# FORMULARIOS
def confirmacion_create_view(request):
    if password_check(request):
        return redirect("password")
    form = ConfirmacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ConfirmacionForm()
        return HttpResponseRedirect(reverse('form_success'))
    context = {
        'form': form
    }
    return render(request, 'boda/confirmacion_create.html', context=context)


def confirmacion_search_view(request):
    if password_check(request):
        return redirect("password")

    form = SearchConfirmacion(request.GET or None)
    datos = None
    if request.method == 'GET':
        if form.is_valid():
            datos = Confirmacion.objects.filter(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname')).first()
    return render(request, 'boda/confirmacion_search.html', {'form': form, 'datos': datos})


def confirmacion_edit_view(request):
    if password_check(request):
        return redirect("password")
    datos = Confirmacion.objects.filter(
        name=request.GET.get('name'),
        surname=request.GET.get('surname')).first()
    form = ConfirmacionForm(instance=datos)
    check = False
    if datos:
        check = True
    if request.method == "POST":
        form = ConfirmacionForm(request.POST, instance=datos)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.save()
            SuccessForm(request)
    context = {
        "form": form,
        "check": check
    }
    return render(request, "boda/confirmacion_edit.html", context=context)


def SuccessForm(request):
    return render(request, 'inscripcion_realizada.html')


def getMonth(monthNumber):
    """Function that returns the month in Spanish with a given month number."""
    MESES = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }
    return MESES[monthNumber]
