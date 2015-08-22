# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView
    )
from concourses.models import Professor, Result, ProfessorResult
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
import random


class ResultListView(ListView):
    model = Result

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultListView, self).dispatch(*args, **kwargs)


class ResultCreateView(CreateView):
    model = Result
    fields = ['title', 'area']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # Objeto Result
        result = form.save()
        # Auxiliar donde se guardarán los profesores elegidos.
        professors_elected = []
        # Se concursa 6 veces, ya que hay 3 titulares y 3 suplentes
        concourses = 6

        for i in range(concourses):
            # Profesores que no pertenecen al area por el cual se realiza el
            # concurso, ni tampoco a los que salieron ultimamente, con su
            # respectivo número de veces ganadas (count).
            professors = Professor.objects.exclude(
                pk__in=[x.pk for x in professors_elected]
                ).exclude(
                area=form.cleaned_data['area']
                ).annotate(count=Count('professorresult')).order_by('count')
            # Profesores con el menor número de concursos ganados.
            professors = [x for x in professors if (
                x.count == professors[0].count
                )]
            # Profesor elegido al azar y guardado en auxiliar.
            professors_elected.insert(0, random.choice(professors))
            # Guardar la relación entre Professor y Resultado.
            ProfessorResult.objects.create(
                professor=professors_elected[0],
                result=result
                )
        return super(ResultCreateView, self).form_valid(form)


class ResultDetailView(DetailView):
    model = Result

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultDetailView, self).dispatch(*args, **kwargs)


class ResultDeleteView(DeleteView):
    model = Result
    success_url = reverse_lazy('concourses:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultDeleteView, self).dispatch(*args, **kwargs)
