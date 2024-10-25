from django.views import View
from django.shortcuts import render


def functional_view(request):
    return render(request, 'second_task/func_template.html')


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
