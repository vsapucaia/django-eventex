from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView

from eventex.core.models import Speaker, Talk


home = ListView.as_view(template_name='index.html', model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)

# def speaker_detail(request, slug):
#     speaker = get_object_or_404(Speaker, slug=slug)
#     return render(request, 'core/speaker_detail.html', {'speaker': speaker})

# def talk_list(request):
#     # at_morning = list(Talk.objects.at_morning()) + list(Course.objects.at_morning())
#     # at_morning.sort(key=lambda o: o.start)
#     #
#     # at_afternoon = list(Talk.objects.at_afternoon()) + list(Course.objects.at_afternoon())
#     # at_afternoon.sort(key=lambda o: o.start)
#
#     context = {
#         'morning_talks': Talk.objects.at_morning(),
#         'afternoon_talks': Talk.objects.at_afternoon()
#     }
#     return render(request, 'core/talk_list.html', context)


