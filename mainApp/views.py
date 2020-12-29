from django.shortcuts import render

def index(request):
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	context={'num_visits': num_visits,}
	return render(request, 'mainApp/homePage.html', context)

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['Звоните и заказывайте по телефону:', '+7(778) 247-46-29', 'Даулетбаева Жансая Камбаркызы']})