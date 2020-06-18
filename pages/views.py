from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
from.models import Contact ,Catagory,  Posts, PostsForm


'''Create your views here.
these are function and procedural based urls pattrens
def home(request):
    return HttpResponse("<h1>hii Iam in side the h1 tag</h1>")
def contact(request):
    return HttpResponse("<h2>Hii Iam INSIDE the Contact Page</h2>")
'''
'''these are class based urls
class index(View):
    def get(self, request):
        return HttpResponse("<h1>hii Iam in side the h1 tag</h1>")
class About(View):
    def get(self, request):
        return HttpResponse("<h2>Hii Iam INSIDE the About Page</h2>")

'''

# for using include function
def home(req):
    qs = {'title':'Home page Title'}
    return render(req, 'home.html',qs)
def contact(request):
    if (request.method == 'GET' and request.GET.get('method') == 'delete' and request.GET.get('id')):
        rec = Contact.objects.filter(id= request.GET.get('id'))
        rec.delete()
    if(request.method == 'GET' and request.GET.get('method') == 'edit' and request.GET.get('id')):
        cnt = Contact.objects.filter(id= request.GET.get('id')).get()
        return render(request, 'edit.html', {'row':cnt})
    if (request.method == 'POST'):
        if(request.GET.get('method') == 'edit' and request.GET.get('id')):
            cnt = Contact.objects.filter(id=request.GET.get('id')).get()
            cnt.update(
                name = request.POST['name'],
                email = request.POST['email'],
                # image_of_person = request.POST['image_of_person'],
                city = request.POST['city'],
                state = request.POST['state'],
                zipcode = request.POST['zip'],

            )
            return HttpResponseRedirect('/contact')
        else:

            data = Contact(

                name = request.POST['name'],
                email = request.POST['email'],
                city = request.POST['city'],
                state = request.POST['state'],
                zipcode = request.POST['zip'],

            )
        data.save()
    cnt = Contact.objects.all()
    qs = {'title':'contact page Title' , 'rows':cnt}
    return render(request, 'contact.html',qs )

def index(request):

    if(request.method == 'GET' and request.GET.get('method') == 'delete' and request.GET.get('id')):
        rec = Posts.objects.filter(id = request.GET.get('id'))
        rec.delete()

    form = PostsForm()
    data = Posts.objects.all()
    catagories = Catagory.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')


    return render(request, 'post.html', {'title':'postpage', 'form':form, 'rows':data, 'catagories':catagories})






def about(request):
    qs = {'title':'About page Title'}
    return render(request,'about.html',qs)
'''def teams(request, team_id, mem_id):
    if(request.method == 'GET' and 'team_id' in request.GET and 'mem_id' in request.GET):
        return HttpResponse("we are in the team so team ID:{} AND my member ID:{}".format(request.GET.get('team_id'), request.GET.get('mem_id')))
    else:
        return HttpResponse("<h2>Iam in the team pages on the</h2>")'''
