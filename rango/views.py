from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category,Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required	
from datetime import datetime  			#to implement counter
@login_required
def add_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
			return redirect('/',request = request)
		else:
			print form.errors
			print "I have printed errors !\n"
			return render(request,'rango/add_category.html',{'form':form})
	else:
		form = CategoryForm()
	return render(request,'rango/add_category.html',{'form':form})

@login_required
def add_page(request,category_name_url):
	try:
		cat = Category.objects.get(slugs = category_name_url)
	except Category.DoesNotExist:
		print "DNE Category"
		cat = None
	print "I am inside Add_Page view"
	if request.method == "POST":
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit = False)
				page.category = cat
				page.views = 0
				page.save()
				return category(request,category_name_url)
		else:
			print form.errors
	else:
		form = PageForm()
	context = {'form':form,'category':cat}
	return render(request,'rango/add_page.html',context)

def register(request):
	if request.session.test_cookie_worked():
		print ">>>>Test cookie worked !!!"
		request.session.delete_test_cookie()
	registered = False
	if request.method == "POST":
		user_form  = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			print "Part 1 done"
			
			profile = profile_form.save(commit = False)
			profile.user = user
			print "Part 1.5 done"
			if 'pic' in request.FILES:
				profile.pic = request.FILES['pic']
			profile.save()
			print "Part 2 done"
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		print "Part 3 executing"
		user_form = UserForm()
		profile_form = UserProfileForm()
	print "registered =  ",registered
	return render(request, 
		'rango/register.html',
		{'user_form': user_form, 'profile_form':profile_form, 'registered': registered })

def user_login(request):
	context = {}
	if request.method=="POST":
		#print request.GET.next
		#redirect_to = request.POST.get('next', '')
		#print redirect_to, "Here"
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username,password = password)
		if user:
			if user.is_active:
				login(request,user)
				if 'next' in request.POST:
					return HttpResponseRedirect(request.POST['next'])

				return HttpResponseRedirect('/rango/')
			else:
				return HttpResponse("Your Account is disabled !")
		else:
			print "Invalid login details: {0} {1}".format(username,password)
			context = {'error':'Invalid Login Credentials !'}
	else:
		if 'next' in request.GET:
			context['next']=request.GET['next']

	return render(request,'rango/login.html',context)

@login_required
def restricted(request):
	return render(request,'rango/restricted.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rango/')
	
def index(request):
	request.session.set_test_cookie()		##to test cookies in browser !!
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context = {'categories': category_list,'pages':page_list}

	"""visits = int(request.COOKIES.get('visits','1'))
	recent_last_visit_time = False
	
	if 'last_visit' in request.COOKIES:
		last_visit = request.COOKIES['last_visit']
		print 'I am here !',last_visit
		last_visit_time = datetime.strptime(last_visit[:-7],"%Y-%m-%d %H:%M:%S")
		if (datetime.now()-last_visit_time).days>0:
			visits = visits +1
			recent_last_visit_time = True
	else:
		recent_last_visit_time = True

	print 'visits = ',visits
	context['visits']=visits
	response = render(request,'rango/index.html',context)
	if recent_last_visit_time:
		response.set_cookie('last_visit',datetime.now())
		response.set_cookie('visits',visits)
	return response

	return render(request,'rango/index.html',context)"""		##Using client side cookies for count !

	visits = request.session.get('visits')
	if not visits:
		visits = 1
	recent_last_visit_time = False
	last_visit = request.session.get('last_visit')

	if last_visit:
		print last_visit
		last_visit_time = datetime.strptime(last_visit[:-7],"%Y-%m-%d %H:%M:%S")
		print last_visit_time
		if (datetime.now()-last_visit_time).days>0:
			visits = visits +1
			recent_last_visit_time = True
	else:
		recent_last_visit_time = True
	if recent_last_visit_time:
		request.session['visits'] = visits
		request.session['last_visit'] = str(datetime.now())
	context['visits'] = visits

	response = render(request,'rango/index.html',context)
	return response

def about(request):
	count = request.session.get('visits')
	if not count:
		count = 0
	print "count = ",count
	context = {'msg': 'This is because of django temp var !', 'visits':count}
	return render(request,'rango/about.html',context)

def category(request,category_name_url):
	context = {} #Contect dictionary empty
	try:
		category = Category.objects.get(slugs = category_name_url)
		context['category_name'] = category.name
		pages = Page.objects.filter(category = category)
		context['pages'] = pages
		context['category'] = category
	except Category.DoesNotExist:
		pass
	return render(request,'rango/category.html',context)