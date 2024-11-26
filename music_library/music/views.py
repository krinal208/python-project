from django.shortcuts import render,HttpResponse,get_object_or_404
from music.models import Contact

# Create your views here.
def index(request):
	return render(request,"index.html")
	# return HttpResponse("India is Great Country")

def read(request):
	data = Contact.objects.all()
	return render(request,"read.html",{'data':data})

def contact(request):
	if request.method == 'GET':
		srno = request.GET.get('srno')
		album_title = request.GET.get('album_title')
		album_artist = request.GET.get('album_artist')
		album_genre = request.GET.get('album_genre')
		album_relese_year = request.GET.get('album_relese_year')
		song_title = request.GET.get('song_title')
		song_artist = request.GET.get('song_artist')
		song_genre = request.GET.get('song_genre')
		song_relese_year = request.GET.get('song_relese_year')

		contact = Contact(srno=srno,album_title=album_title, album_artist=album_artist,
						  album_genre=album_genre,album_relese_year=album_relese_year,
						  song_title=song_title,song_artist=song_artist,
						  song_genre=song_genre,song_relese_year=song_relese_year)
		contact.save()
	return render(request,'index.html')

def update(request):
	return render(request,'update.html')

def update_data(request):
	srno = request.GET.get('srno')
	contact = get_object_or_404(Contact, srno = srno)
	if request.method == 'GET':
		new_album_title = request.GET.get('album_title')
		new_album_artist = request.GET.get('album_artist')
		new_album_genre = request.GET.get('album_genre')
		new_album_relese_year = request.GET.get('album_relese_year')
		new_song_title = request.GET.get('song_title')
		new_song_artist = request.GET.get('song_artist')
		new_song_genre = request.GET.get('song_genre')
		new_song_relese_year = request.GET.get('song_relese_year')

		contact.album_title = new_album_title
		contact.album_artist = new_album_artist
		contact.album_genre = new_album_genre
		contact.album_relese_year = new_album_relese_year
		contact.song_title = new_song_title
		contact.song_artist = new_song_artist
		contact.song_genre = new_song_genre
		contact.song_relese_year = new_song_relese_year

		contact.save()
	return render(request,'update.html')

def search(request):
	return render(request,'search.html')

def search_data(request):
	if request.method =='GET':
		srno = request.GET.get('srno')
		data = Contact.objects.filter(srno = srno)
		return render(request,'read.html',{'data':data})
	else:
		return render(request,'search.html')

def delete(request):
	return render(request,'delete.html')

def delete_data(request):
	srno = request.GET.get('srno')
	contact = get_object_or_404(Contact, srno=srno)
	if request.method =='GET':
		contact.delete()
	return render(request,'delete.html')
