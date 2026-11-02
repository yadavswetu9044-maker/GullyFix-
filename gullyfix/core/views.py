from django.shortcuts import render, redirect
from .models import Issue, Category

def home(request):
    cat_filter = request.GET.get('category')
    if cat_filter:
        issues = Issue.objects.filter(category__name__icontains=cat_filter).order_by('-created_at')
    else:
        issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'issues': issues, 'active_cat': cat_filter})

def report(request):
    if not request.user.is_authenticated:
        return redirect('/admin/login/?next=/report/')
    cats = Category.objects.all()
    if request.method == 'POST':
        Issue.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            latitude=request.POST['latitude'],
            longitude=request.POST['longitude'],
            image=request.FILES.get('image'),
            category_id=request.POST['category']
        )
        return redirect('home')
    return render(request, 'report.html', {'cats': cats})

def issue_detail(request, id):
    issue = Issue.objects.get(id=id)
    return render(request, 'detail.html', {'issue': issue})

def stats_view(request):
    total = Issue.objects.count()
    pending = Issue.objects.filter(status='Pending').count()
    fixed = Issue.objects.filter(status='Fixed').count()
    return render(request, 'stats.html', {'total': total, 'pending': pending, 'fixed': fixed})

def leaderboard_view(request):
    return render(request, 'leaderboard.html')

def contact_view(request):
    return render(request, 'contact.html')