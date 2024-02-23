from django.contrib.auth.decorators import login_required,permission_required, user_passes_test
from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import SomeForm


"""

    user.has_perm()
        .all()
        .add(<perm1>, ... )
        .remove(<perm1>, ... )
        .clear()
        .set([])   
        
    
    user.groups.set([gr1,gr2])
    user.groups.add("Visiteurs")
    user.groups.remove("Visiteur")
    user.groups.clear()
    
"""

def is_visitors(user):
    return user.groups.filter(name = "utilisateurs").exists()

def index(request):
    content = {"books": Book.objects.order_by('title')}
    return render(request,"page/index.html",content)

@user_passes_test(is_visitors)
def show(request,book_id):
    content = {"book": get_object_or_404(Book, pk = book_id)}
    return render(request,"page/show.html",content)

@permission_required('myapp.add_book')
def add(request):
    if request.method == "POST":
        form = SomeForm(request.POST)
        
        if form.is_valid():
            form.save();
            return redirect('myapp:index')
    else :
        form = SomeForm()
    
    return render(request,"page/form.html",{"form": form})

@permission_required('myapp.change_book')
def edit(request, book_id):
    maj = Book.objects.get(pk = book_id)
    if request.method == "POST":
        form = SomeForm(request.POST, instance=maj)
        
        if form.is_valid():
            form.save()
            return redirect("myapp:index")
    else:
        form = SomeForm(instance=maj)
        content = {"form": form}
    return render(request,"page/form.html",content)

@permission_required('myapp.delete_book', raise_exception= True)
def supp(request,book_id):
    remove = Book.objects.get(pk = book_id)
    remove.delete()
    return redirect('myapp:index')