from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order
from .forms import CustomerForm, OrderForm

def customer_list(request):
    customers = Customer.objects.all()
    form = CustomerForm()

    return render(request, 'clientes/customer_list.html', {
        'customers': customers,
        'form': form 
    })

def order_list(request):
    orders = Order.objects.select_related('customer').all()
    return render(request, 'clientes/order_list.html', {'orders': orders})



def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'clientes/customer_form.html', {'form': form})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            customer_id = request.POST.get('customer')
            return redirect('customer_orders', id=customer_id)
    else:
        form = OrderForm()
    return render(request, 'clientes/order_form.html', {'form': form})



def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'clientes/customer_form.html', {'form': form})

def order_update(request, id):
    order = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'clientes/order_form.html', {'form': form})



def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('customer_list')

def order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('order_list')



def customer_orders(request, id):
    customer = get_object_or_404(Customer, id=id)
    orders = customer.orders.all()  # usando el related_name
    return render(request, 'clientes/customer_orders.html', {
        'customer': customer,
        'orders': orders
    })