from django.views.generic.edit import CreateView, UpdateView, DeleteView,  BaseDetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView


from .models import Estado, Cidade, Bairro, Logradouro, Proprietario, Terreno, Protocolo, Infracao, Inspecao, Fiscal #Produtividade

#Método para redirecionar o usuário após ele efetuar um cadastro
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin #Importa views que protege o acesso de usuário não autenticado
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect

#Primeiro criei uma view que é uma herança de CreateView
#Utilizo o nome da classe junto com a função para facilitar
#Ela tem três atributos: Modelo (classe), Fields (campos), Template_name
# e sucess_url (redirecionamento)

########################### CREATE ###########################
#class ProdutividadeCreate(LoginRequiredMixin, CreateView):
    #login_url = reverse_lazy('login')
   ## model = Produtividade
    #fields = ['descricao', 'pdf_teste']
   # template_name = 'form-upload.html'
  #  success_url = reverse_lazy('listar-produtividades')

   # def get_context_data(self, *args, **kwargs):
      #  context = super().get_context_data(*args, **kwargs)

        #Para personalizar a aparência para o usuário
      #  context['titulo'] = "Cadastro de produtividade"
     #   context['botao'] = "Cadastrar"

      #  return context

   # def form_valid(self, form):
   #     #Vou pegar os dados dos usuário no formulário
    #    form.instance.usuario = self.request.user #Está pegando o usuário que está logado
        #Antes do super a Protudividade não foi criada
    #    url = super().form_valid(form)
        #Depois do super a Produtividade foi criada
        #Quando chega neste ponto ele salvou no banco de dados da produtividade

        #self.object.descricao += " [TESTE]"
        #self.object.save()

        #Posso pegar qualquer atributo e mudar ainda
    #    return url

def get_queryset(self):
    txt_nome = self.request.GET.get('nome')

    if txt_nome:
        terrenos = Terreno.objects.filter(inscricao__icontains=txt_nome)
    else:
        terrenos = Terreno.objects.all()

    return terrenos



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

class ProtocoloCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Protocolo
    fields = ['protocolo','solicitante_protocolo','logradouro','descricao_protocolo','ouvidoria','status_protocolo','entrada_protocolo','encerramento_protocolo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-protocolos')

class FiscalCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fiscal
    fields = ['nome_fiscal','matricula_fiscal','nivel','primeiro_nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-fiscais')

class InspecaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Inspecao
    fields = ['protocolo','data_inspecao1','horario_inspecao1','foto_inspecao_1','data_relatorio1','fiscal', 'mato','entulho','terreno']
    template_name = 'form-upload.html'
    success_url = reverse_lazy('listar-inspecoes')

class InfracaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Infracao
    fields = ['inspecao','data_auto','rastreio_infracao','status_rastreio','data_entrega_autuacao','nome_recebedor', 'defendeu']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-infracoes')



########################### UPDATE ###########################
#class ProdutividadeUpdate(LoginRequiredMixin, UpdateView):
   # login_url = reverse_lazy('login')
  #  model = Produtividade
 #   fields = ['descricao', 'pdf_teste']
  #  template_name = 'form-upload.html'
 #   success_url = reverse_lazy('listar-produtividade')

  #  def get_context_data(self, *args, **kwargs):
  #      context = super().get_context_data(*args, **kwargs)

    #    #Para personalizar a aparência para o usuário
   #     context['titulo'] = "Editar cadastro de produtividade"
    #    context['botao'] = "Salvar"

     #   return context

  #  def get_object(self, queryset=None):
   #     self.object = get_object_or_404(Produtividade, pk=self.kwargs['pk'], usuario=self.request.user)
   #     return self.object


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

class ProtocoloUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Protocolo
    fields = ['protocolo', 'solicitante_protocolo', 'logradouro', 'descricao_protocolo', 'ouvidoria',
              'status_protocolo', 'entrada_protocolo', 'encerramento_protocolo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-protocolos')

class FiscalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fiscal
    fields = ['nome_fiscal','matricula_fiscal','nivel','primeiro_nome']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-fiscais')

class InspecaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Inspecao
    fields = ['protocolo','data_inspecao1','horario_inspecao1','foto_inspecao_1','data_relatorio1','fiscal', 'mato','entulho','terreno']
    template_name = 'form-upload.html'
    success_url = reverse_lazy('listar-inspecoes')

class InfracaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Infracao
    fields = ['inspecao','data_auto','rastreio_infracao','status_rastreio','data_entrega_autuacao','nome_recebedor', 'defendeu']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-infracoes')

########################### DELETE ###########################
#class ProdutividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
   # group_required = u"Administrador"
   # login_url = reverse_lazy('login')
  #  model = Produtividade
  #  template_name = 'form-excluir.html'
  #  success_url = reverse_lazy('listar-produtividades')

    #def get_object(self, queryset=None):
     #   self.object = get_object_or_404(Produtividade, pk=self.kwargs['pk'], usuario=self.request.user)
     #   return self.object


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

class ProtocoloDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Protocolo
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-protocolos')

class FiscalDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fiscal
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-fiscais')

class InspecaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Inspecao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-inspecoes')

class InfracaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Inspecao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-infracoes')







########################### LISTA ###########################

class EstadoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'listar-estados.html'
    paginate_by = 10
    ordering = ['nome_estado']

    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            estados = Estado.objects.filter(nome_estado__icontains=txt_nome)
        else:
            estados = Estado.objects.all()

        return estados



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

class ProtocoloList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Protocolo
    template_name = 'listar-protocolos.html'

class FiscalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fiscal
    template_name = 'listar-fiscais.html'

class InspecaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Inspecao
    template_name = 'listar-inspecoes.html'

class InfracaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Infracao
    template_name = 'listar-infracoes.html'



#pra fazer uma lista onde

#class ProdutividadeList(LoginRequiredMixin, ListView):
 #   login_url = reverse_lazy('login')
  #  model = Produtividade
   # template_name = 'listar-produtividades.html'

    #def get_queryset(self):
        #self.object_list = Produtividade.object.all()
        #Estou listando todos os objetos do tipo Produtividade
     #   self.object_list = Produtividade.objects.filter(usuario=self.request.user)
      #  return self.object_list


########################### GERAÇÕES ################################

def gerar_relatorio(request,pk,template_name="gerar_relatorio.html"):
    inspecao = get_object_or_404(Inspecao, pk=pk)
    return render(request, template_name, {'inspecao':inspecao})


def EstadoDetailView(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    return render(request, 'estado_detalhe.html', context={'estado': estado})

