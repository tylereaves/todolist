from django.db import models


class Todo(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField(verbose_name="Description",blank=True)
  created = models.DateTimeField(auto_now_add=True, blank=True)

  def __unicode__(self):
    return self.title

  def form(self):
    #Ugly hack, but nessesary as otherwise Django chockes on the circular import
    import todolist.forms as forms
    return forms.TodoForm(instance=self)

