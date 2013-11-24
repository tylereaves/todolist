#Make our new todo form work in the base template

from todolist.forms import TodoForm

def todo(request):
  form = TodoForm()
  return {'new_form':form}