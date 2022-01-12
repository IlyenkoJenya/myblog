from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):  #Простейшая версия ModelForm состоит из вложенного класса Meta, 
#который сообщает Django, на какой модели должна базироваться форма и какие поля на ней 
#должны находиться.
	class Meta:
		model=Topic  #форма создается на базе модели Topic
		fields=['text'] #размещается только поле text
		labels={'text':''} 
		widgets={'text':forms.Textarea(attrs={'cols':80})}