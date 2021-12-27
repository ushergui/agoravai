from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from .models import Estado, Cidade, Bairro, Logradouro, Proprietario, Terreno, Produtividade

#Método para redirecionar o usuário após ele efetuar um cadastro
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin #Importa views que protege o acesso de usuário não autenticado
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

#Primeiro criei uma view que é uma herança de CreateView
#Utilizo o nome da classe junto com a função para facilitar
#Ela tem três atributos: Modelo (classe), Fields (campos), Template_name
# e sucess_url (redirecionamento)

########################### CREATE ###########################
class ProdutividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produtividade
    fields = ['descricao', 'pdf_teste']
    template_name = 'form-upload.html'
    success_url = reverse_lazy('listar-produtividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Para personalizar a aparência para o usuário
        context['titulo'] = "Cadastro de produtividade"
        context['botao'] = "Cadastrar"

        return context

    def form_valid(self, form):
        #Vou pegar os dados dos usuário no formulário
        form.instance.usuario = self.request.user #Está pegando o usuário que está logado
        #Antes do super a Protudividade não foi criada
        url = super().form_valid(form)
        #Depois do super a Produtividade foi criada
        #Quando chega neste ponto ele salvou no banco de dados da produtividade

        #self.object.descricao += " [TESTE]"
        #self.object.save()

        #Posso pegar qualquer atributo e mudar ainda
        return url

class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nome_estado', 'sigla_estado']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estados')

class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome_cidade', 'estado']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidades')

class BairroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Bairro
    fields = ['bairro', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-bairros')

class LogradouroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Logradouro
    fields = ['logradouro', 'bairro', 'cep']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-logradouros')

class ProprietarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Proprietario
    fields = ['nome_proprietario', 'logradouro_proprietario', 'numero_proprietario', 'complemento_proprietario']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-proprietarios')

class TerrenoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Terreno
    fields = ['inscricao', 'logradouro_terreno','numero_terreno','complemento_terreno',
              'proprietario', 'lote','quadra','area','logradouro_correspondencia',
              'numero_correspondencia','complemento_correspondencia']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-terrenos')

########################### UPDATE ###########################
class ProdutividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produtividade
    fields = ['descricao', 'pdf_teste']
    template_name = 'form-upload.html'
    success_url = reverse_lazy('listar-produtividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Para personalizar a aparência para o usuário
        context['titulo'] = "Editar cadastro de produtividade"
        context['botao'] = "Salvar"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Produtividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nome_estado', 'sigla_estado']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estados')

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome_cidade', 'estado']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidades')

class BairroUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Bairro
    fields = ['bairro', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-bairros')

class LogradouroUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Logradouro
    fields = ['logradouro', 'bairro', 'cep']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-logradouros')

class ProprietarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Proprietario
    fields = ['nome_proprietario', 'logradouro_proprietario']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-proprietarios')

class TerrenoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Terreno
    fields = ['inscricao', 'logradouro_terreno','numero_terreno','complemento_terreno',
              'proprietario', 'lote','quadra','area','logradouro_correspondencia',
              'numero_correspondencia','complemento_correspondencia']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-terrenos')

########################### DELETE ###########################
class ProdutividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Produtividade
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-produtividades')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Produtividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-estados')

class CidadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cidades')

class BairroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Bairro
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-bairros')

class LogradouroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Logradouro
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-logradouros')

class ProprietarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Proprietario
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-proprietarios')

class TerrenoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Terreno
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-terrenos')

########################### LISTA ###########################

class EstadoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'listar-estados.html'

class CidadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'listar-cidades.html'

class BairroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Bairro
    template_name = 'listar-bairros.html'

class LogradouroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Logradouro
    template_name = 'listar-logradouros.html'

class ProprietarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Proprietario
    template_name = 'listar-proprietarios.html'

class TerrenoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Terreno
    template_name = 'listar-terrenos.html'
#pra fazer uma lista onde

class ProdutividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produtividade
    template_name = 'listar-produtividades.html'

    def get_queryset(self):
        #self.object_list = Produtividade.object.all()
        #Estou listando todos os objetos do tipo Produtividade
        self.object_list = Produtividade.objects.filter(usuario=self.request.user)
        return self.object_list
