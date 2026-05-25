from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Car, Brand
from .forms import LeadForm


def index(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка принята! Свяжемся с вами.')
            return redirect('index')
    return render(request, 'cars/index.html', {
        'featured_cars': Car.objects.filter(is_featured=True)[:6],
        'form': form,
        'total_cars': Car.objects.count(),
        'services': [
            ('credit-card-2-front', 'Автокредит', 'Одобрение за 1 час. Ставка от 3.9%.', 'credit'),
            ('arrow-left-right', 'Trade-in', 'Обмен старого авто с выгодой до 500 000 ₸.', 'tradein'),
            ('shield-check', 'Страхование', 'КАСКО и ОСАГО в автосалоне.', 'contacts'),
            ('tools', 'Сервис', 'Официальный сервисный центр.', 'contacts'),
        ],
    })


def catalog(request):
    cars = Car.objects.all()
    if request.GET.get('brand'):    cars = cars.filter(brand_id=request.GET['brand'])
    if request.GET.get('condition'):cars = cars.filter(condition=request.GET['condition'])
    if request.GET.get('body'):     cars = cars.filter(body=request.GET['body'])
    if request.GET.get('fuel'):     cars = cars.filter(fuel=request.GET['fuel'])
    if request.GET.get('price_min'):cars = cars.filter(price__gte=request.GET['price_min'])
    if request.GET.get('price_max'):cars = cars.filter(price__lte=request.GET['price_max'])

    page_obj = Paginator(cars, 9).get_page(request.GET.get('page'))
    return render(request, 'cars/catalog.html', {
        'page_obj': page_obj,
        'brands': Brand.objects.all(),
        'total': cars.count(),
        'filters': request.GET,
    })


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = LeadForm(initial={'car': car})
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка принята!')
            return redirect('car_detail', pk=pk)
    return render(request, 'cars/car_detail.html', {
        'car': car,
        'similar': Car.objects.filter(body=car.body).exclude(pk=pk)[:3],
        'form': form,
    })


def tradein(request):
    steps = [
        ('Оставьте заявку',    'Заполните форму — займёт 2 минуты.'),
        ('Оценка автомобиля',  'Специалист оценит ваш авто по рыночной стоимости.'),
        ('Выбор нового авто',  'Выберите автомобиль из нашего каталога.'),
        ('Оформление сделки',  'Зачтём стоимость вашего авто в счёт нового.'),
    ]
    form = LeadForm(initial={'request_type': 'tradein'})
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.request_type = 'tradein'
            lead.save()
            messages.success(request, 'Заявка на Trade-in принята!')
            return redirect('tradein')
    return render(request, 'cars/tradein.html', {'form': form, 'steps': steps})


def credit(request):
    form = LeadForm(initial={'request_type': 'credit'})

    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.request_type = 'credit'
            lead.save()

            messages.success(request, 'Заявка на кредит принята!')
            return redirect('credit')

    return render(request, 'cars/credit.html', {
        'form': form,
        'credit_stats': [
            ('3.9%', 'Ставка от'),
            ('1 час', 'Одобрение'),
            ('11', 'Банков-партнёров'),
            ('7 лет', 'Срок кредита до'),
        ],
    })


def about(request):
    return render(request, 'cars/about.html')


def contacts(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено!')
            return redirect('contacts')
    return render(request, 'cars/contacts.html', {'form': form})