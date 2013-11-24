# Create your view

from django.http import HttpResponse
from django.utils import simplejson
from todolist.forms import TodoForm
from django.template.loader import render_to_string
from todolist.models import Todo


#https://coderwall.com/p/k8vb_a
def json_response(func):
  """
  A decorator thats takes a view response and turns it
  into json. If a callback is added through GET or POST
  the response is JSONP.
  """
  def decorator(request, *args, **kwargs):
    objects = func(request, *args, **kwargs)
    if isinstance(objects, HttpResponse):
      return objects
    try:
      data = simplejson.dumps(objects)
      if 'callback' in request.REQUEST:
        # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    except:
      data = simplejson.dumps(str(objects))
    return HttpResponse(data, "application/json")
  return decorator

@json_response
def create(request):
  f = TodoForm(request.POST)
  if f.is_valid():
    t = f.save()
    return {"status":"ok",
            "id":t.id,
            "html":render_to_string("partials/todo.html",{'todo':t}),
            "formhtml":render_to_string("partials/form.html",{'form':TodoForm()})
          }
  else:
    return {"status":"error",
            "formhtml":render_to_string("partials/form.html",{'form':f})}

@json_response
def delete(request, id):
  try:
    t = Todo.objects.get(pk=id)
  except Todo.DoesNotExist:
    return {"status":"notfound"}
  t.delete()
  return {"status":"ok","id":id, "formhtml":""}

@json_response
def edit(request, id):
  try:
    t = Todo.objects.get(pk=id)
  except Todo.DoesNotExist:
    return {"status":"notfound"}
  f = TodoForm(request.POST,instance=t)
  if f.is_valid():
    t = f.save()
    return {"status":"ok",
            "id":t.id,
            "html":render_to_string("partials/todo.html",{'todo':t})}
  else:
    return {"status":"error",
            "id":t.id,
            "formhtml":render_to_string("partials/form.html",{'form':f})}