
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Venda, Produto
from .forms import ClienteForm, VendaForm
from django.db.models import F
from django.utils.timezone import datetime

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})

def venda_list(request):
    vendas = Venda.objects.select_related('cliente', 'produto').all()
    cliente_id = request.GET.get('cliente')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if cliente_id:
        vendas = vendas.filter(cliente_id=cliente_id)
    if data_inicio:
        vendas = vendas.filter(data_venda__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data_venda__lte=data_fim)

    clientes = Cliente.objects.all()
    return render(request, 'vendas/venda_list.html', {
        'vendas': vendas,
        'clientes': clientes,
        'filtro_cliente': cliente_id,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    })

def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm()
    return render(request, 'vendas/venda_form.html', {'form': form})

def venda_update(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'vendas/venda_form.html', {'form': form})

def venda_delete(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('venda_list')
    return render(request, 'vendas/venda_confirm_delete.html', {'venda': venda})
