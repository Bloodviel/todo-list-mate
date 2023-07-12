from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "tags"]
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def complete_task(request, pk):
    task = Task.objects.get(id=pk)

    if task.mark_task:
        task.mark_task = False
    else:
        task.mark_task = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:index"))

