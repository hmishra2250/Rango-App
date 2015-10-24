from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	"""name = forms.CharField(max_length = 128, help_text = "Please enter the Category Name")
	views = forms.IntegerField(widget = forms.HiddenInput(),initial = 0)
	likes = forms.IntegerField(widget = forms.HiddenInput(),initial = 0)
	slugs = forms.CharField(max_length = 128,required = False)"""

	class Meta:
		model = Category
		fields = ('name','views','likes','slugs')
		widgets = {
		'name': forms.Textarea(attrs={'cols': 40, 'rows': 1}),
		'views': forms.HiddenInput(attrs={'initial' : 0}),
		'likes': forms.HiddenInput(attrs = {'initial' : 0}),
		'slugs': forms.Textarea(attrs = {'required' : False,'cols' : 40 , 'rows' : 1}),
		}
		help_texts = {
		'name': "Please enter the Category Name",
		'slugs': "Please enter the URL          "
		}

class PageForm(forms.ModelForm):
	"""title = forms.CharField(max_length = 128,help_text = "Please enter a title for the page")
	url = forms.URLField(max_length = 200,help_text = "Please eneter the URL for the page")
	views = forms.IntegerField(widget = forms.HiddenInput(),initial = 0)"""	

	class Meta:	
		model = Page
		exclude = ('category',)
		widgets = {
		'title':forms.Textarea(attrs={'cols':40,'rows':1}),
		'url':forms.URLInput(attrs = {'cols':40,'rows':1}),
		'views': forms.HiddenInput(attrs = {'initial':0})
		}
		help_texts = {
		'title': "Please Enter title of the page",
		'url': "Please Enter the URL of the page"
		}

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		if url and not url.startswith('http://'):
			url = 'http://'+url
			cleaned_data['url'] = url
		return cleaned_data

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','email','password')
		widgets = {
		'password': forms.PasswordInput()
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website','pic')