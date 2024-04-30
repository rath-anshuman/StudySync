from django.shortcuts import render
from adminnotes.models import Notes
from adminnotice.models import Notice




def home(request):
    # objects = Notes.objects.using('newdb').all()
    # for obj in objects:
    #     obj.pk = None  # Reset the primary key to create a new object
    #     obj.save(using='default')
    #     print(f'saved {obj}')

    # objectss = Notice.objects.using('newdb').all()
    # for obj in objectss:
    #     obj.pk = None  # Reset the primary key to create a new object
    #     obj.save(using='default')
    #     print(f'saved {obj}')
    return render(request,'home.html')

def tryy(request):
    return render(request,'try.html')

def add(request):
    return render(request,'add.html')