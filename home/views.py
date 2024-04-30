from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse, get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    context={'success': False}
    if request.method =="POST":
        #Handle the form
        title=request.POST['title']
        desc= request.POST['desc']
        print(title,desc)
        ins=Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={'success': True}

    return render(request,'index.html', context)

def tasks(request):
    allTasks= Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context= {'tasks': allTasks}
    return render(request,'tasks.html', context)

def search_results(request):
    query = request.POST.get('query', '')  # Get the search query from the request
    results = Task.objects.filter(taskTitle__icontains=query)  # Perform search
    context={'results': results, 'query': query}
    return render(request, 'search_results.html',context)

# update function
def updateTask(request,pk):
    task=get_object_or_404(Task,id=pk)

    if request.method=='POST':
        task.taskTitle= request.POST.get('taskTitle')
        task.taskDesc= request.POST.get('taskDesc')
        task.save()
        messages.success(request,'Task Successfully Updated')
        return redirect('/tasks/')
    
    return render(request,'update.html',{'task':task})

# Delete function
def deleteTask(request,pk):
    task=get_object_or_404(Task,id=pk)
    task.delete()
    messages.success(request,'Task Successfully Deleted')
    return redirect('/tasks/')
 