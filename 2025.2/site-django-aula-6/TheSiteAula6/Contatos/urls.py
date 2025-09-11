from django.urls import path
from Contatos import views

app_name = 'Contatos'

urlpatterns = [
    path('', views.home_page_contatos, name='home-page-contatos'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('cria_contato/', views.ContatoCreateView.as_view(), name='cria-contato'),
    path('atualiza_contato/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualiza-contato'),
    path('deleta_contato/<int:pk>/', views.ContatoDeleteView.as_view(), name='deleta-contato'),
]
