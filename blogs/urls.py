from django.urls import path  #необходима для связывания URL с представлениями 
from . import views #точка говорит что виевс в этой же папке

app_name='приложение'

urlpatterns=[
	#home page
	path ('',views.index,name='индекс'),
	path ('blogs/',views.blogs,name='перечень_блогов'),
	path ('blogs/new_blog/',views.new_blog,name='новый_блог'),
	path ('blogs/edit_blog/<int:blog_id>/',views.edit_blog,name='редактированние_блога'),
	path ('blogs/blog/<int:blog_id>/',views.blog,name='блог'),

]	
