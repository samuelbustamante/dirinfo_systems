# -*- coding: utf-8 -*-

from django.views.generic import CreateView, DetailView, ListView
from concourses.models import Professor, Result, ProfessorResult
from django.db.models import Count
import random


class ResultCreateView(CreateView):
    model = Result
    fields = ['title', 'area']

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
                pk__in=professors_elected,
                area=form.cleaned_data['area']
                ).annotate(count=Count('professorresult')).order_by('count')
            # Profesores con el menor número de concursos ganados.
            professors = [x.count for x in professors if (
                x.count == professors[0].count
                )]
            # Profesor elegido al azar y guardado en auxiliar.
            professors_elected.insert(0, random.choice(professor))
            # Guardar la relación entre Professor y Resultado.
            ProfessorResult.objects.create(
                professor=professor_elected[0],
                result=result
                )


class ResultDetailView(DetailView):
    model = Result


class ResultListView(ListView):
    model = Result
