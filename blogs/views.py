from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Topic
from .forms import TopicForm
from django.http import Http404
# Create your views here.

def index(request):
	"домашняя страница application"	
	
	return render (request,'blogs/index.html')

@login_required
def blogs(request):
	blogs=Topic.objects.filter(owner=request.user).order_by('date_added')
	
	context={'blogs':blogs}

	return render (request,'blogs/blogs.html',context)
@login_required
def blog(request,blog_id):
	#ВЫводит одну теmу и все ее записи
	topic=Topic.objects.get(id=blog_id)	
	context={'topic':topic} #в щаблоне перебираются значения,но передает ключ.
	return render (request,'blogs/blog.html',context) 


@login_required
def new_blog(request):
	"""определяет новую форму"""
	if request.method!='POST': #проверяем тип запроса
		#данные не отправляются,создается пустая форма
		form=TopicForm() #создаем топик и сохранили в переменной его

	else:
		#отправлены данные POST. обработать данные
		form=TopicForm(data=request.POST) #передаем данные введенные пользователем , хранящиеся в request.POST.

		if form.is_valid():
			NEW_TOPIC=form.save(commit=False)
			NEW_TOPIC.owner=request.user

			 #проверяет запоненны ли все обязательные поля. Априори стоят все обязятельные
			NEW_TOPIC.save() #если все заполненно,то сохраняет в базу данных
			return redirect('приложение:перечень_блогов') #перенаправляет данную страницу


	#вывести пустую или недействительную форму
	context={'form':form}
	return render(request,'blogs/new_blog.html',context)
@login_required
def edit_blog(request,blog_id):
	BLOG=Topic.objects.get(id=blog_id)

	if request.method!='POST':
		form=TopicForm(instance=BLOG)


	else:
		form=TopicForm(instance=BLOG,data=request.POST)

		if form.is_valid():
			form.save()
			return redirect ('приложение:перечень_блогов')

	context={'BLOG':BLOG,'form':form}
	return render (request,'blogs/edit_blog.html',context)
