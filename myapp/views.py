from django.shortcuts import render
from .models import Expenses

# Create your views here.
def index(request):
    add = 0  # Initialize add outside the if block

    if request.method == 'POST':
        desk = request.POST['expense-description']
        amount = request.POST['expense-amount']
        date = request.POST['expense-date']

        ex = Expenses.objects.create(description=desk, Amount=amount, date=date)
        ex.save()
        dd=Expenses.objects.all()
        for expense in dd:
            add += expense.Amount
        return render(request, 'index.html', {'dd': dd, 'add': add})
    return render(request,'index.html')
