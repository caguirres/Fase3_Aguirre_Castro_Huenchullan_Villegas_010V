from django.urls import path
from . import views

urlpatterns=[
	path('',views.inicio,name='inicio'),
	path('galeria',views.galeria,name='galeria'),
	path('qs',views.qs,name='qs'),
	path('form_suscrip',views.suscrip, name='form_suscrip'),
	


]

	


