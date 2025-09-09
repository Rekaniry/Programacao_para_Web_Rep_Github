from django.urls import path
from Contatos import views

app_name = 'Contatos'

urlpatterns = [
    path('', views.home_page_contatos, name='home-page-contatos'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('cria_contato/', views.ContatoCreateView.as_view(), name='cria-contato'),
]
