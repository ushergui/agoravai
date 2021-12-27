from django.urls import path #Estou pegando do módulo django
from .views import EstadoCreate, CidadeCreate, BairroCreate, LogradouroCreate, \
    ProprietarioCreate, TerrenoCreate, ProdutividadeCreate
from .views import EstadoUpdate, CidadeUpdate, BairroUpdate, LogradouroUpdate, \
    ProprietarioUpdate, TerrenoUpdate, ProdutividadeUpdate
from .views import EstadoDelete, CidadeDelete, BairroDelete, LogradouroDelete, \
    ProprietarioDelete, TerrenoDelete, ProdutividadeDelete
from .views import EstadoList, CidadeList, BairroList, LogradouroList, \
    ProprietarioList, TerrenoList, ProdutividadeList

#padrão de url que tem lá na outra url, ele funciona como se fosse um vetor

urlpatterns = [
    path('cadastrar/produtividade/', ProdutividadeCreate.as_view(), name="cadastrar-produtividade"),
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/bairro/', BairroCreate.as_view(), name="cadastrar-bairro"),
    path('cadastrar/logradouro/', LogradouroCreate.as_view(), name="cadastrar-logradouro"),
    path('cadastrar/proprietario/', ProprietarioCreate.as_view(), name="cadastrar-proprietario"),
    path('cadastrar/terreno/', TerrenoCreate.as_view(), name="cadastrar-terreno"),

    #Para edição é necessário colocar o ID

    path('editar/produtividade/<int:pk>/', ProdutividadeUpdate.as_view(), name="editar-produtividade"),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/bairro/<int:pk>/', BairroUpdate.as_view(), name="editar-bairro"),
    path('editar/logradouro/<int:pk>/', LogradouroUpdate.as_view(), name="editar-logradouro"),
    path('editar/proprietario/<int:pk>/', ProprietarioUpdate.as_view(), name="editar-proprietario"),
    path('editar/terreno/<int:pk>/', TerrenoUpdate.as_view(), name="editar-terreno"),

    # Para deletar é necessário colocar o ID

    path('deletar/produtividade/<int:pk>/', ProdutividadeDelete.as_view(), name="deletar-produtividade"),
    path('deletar/estado/<int:pk>/', EstadoDelete.as_view(), name="deletar-estado"),
    path('deletar/cidade/<int:pk>/', CidadeDelete.as_view(), name="deletar-cidade"),
    path('deletar/bairro/<int:pk>/', BairroDelete.as_view(), name="deletar-bairro"),
    path('deletar/logradouro/<int:pk>/', LogradouroDelete.as_view(), name="deletar-logradouro"),
    path('deletar/proprietario/<int:pk>/', ProprietarioDelete.as_view(), name="deletar-proprietario"),
    path('deletar/terreno/<int:pk>/', TerrenoDelete.as_view(), name="deletar-terreno"),

    # Para listar
    path('listar-produtividade/', ProdutividadeList.as_view(), name="listar-produtividade"),
    path('listar-estados/', EstadoList.as_view(), name="listar-estados"),
    path('listar-cidades/', CidadeList.as_view(), name="listar-cidades"),
    path('listar-bairros/', BairroList.as_view(), name="listar-bairros"),
    path('listar-logradouros/', LogradouroList.as_view(), name="listar-logradouros"),
    path('listar-proprietarios/', ProprietarioList.as_view(), name="listar-proprietarios"),
    path('listar-terrenos/', TerrenoList.as_view(), name="listar-terrenos"),


]