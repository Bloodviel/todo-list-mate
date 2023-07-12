from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    mark_task = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["mark_task", "-date_time"]

    def __str__(self):
        return f"{self.content[:20]}..."
