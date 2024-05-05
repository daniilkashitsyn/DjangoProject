from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    all_bugs_list = reverse('quality_control:bug_list')
    features_list = reverse('quality_control:feature_list')
    all_bugs = reverse('quality_control:all_bugs')
    all_requests = reverse('quality_control:all_request')
    html = '<h1 align=center>Система контроля качества</h1>'
    html += f'<h2><a href={all_bugs}>Отобразить все баги</h2>'
    html += f'<h2><a href={all_requests}>Отобразить все запросы</h2>'
    html += f'<p><a href={all_bugs_list}>Список багов</p>'
    html += f'<p><a href={features_list}>Запросы на улучшение</p>'
    return HttpResponse(html)

def bug_list(request):
    html = '<h1>Список отчетов об ошибках</h1><ul>'
    all_bug_reports = BugReport.objects.all()
    for bug in all_bug_reports:
        html += f'<li><a href={bug.id}>{bug.title}</li>'
    html += '</ul>'
    return HttpResponse(html)

def feature_list(request):
    html = '<h1>Списко запросов на улучшение</h1><ul>'
    all_features = FeatureRequest.objects.all()
    for feature in all_features:
        html += f'<li><a href={feature.id}>{feature.title}</li>'
    html += '</ul>'
    return HttpResponse(html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    html = f'<h1>Детали бага {bug_id}</h1>'
    html += f'<h2>{bug.title}</h2>'
    html += f'<ul><li>Описание: {bug.description}</li>'
    html += f'<li>Приоритет: {bug.priority}</li>'
    html += f'<li>Статус: {bug.status}</li></ul>'
    return HttpResponse(html)

def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    html = f'<h1>Детали улучшения {feature_id}</h1>'
    html += f'<h2>{feature.title}</h2>'
    html += f'<ul><li>Описание: {feature.description}</li>'
    html += f'<li>Приоритет: {feature.priority}</li>'
    html += f'<li>Статус: {feature.status}</li></ul>'
    return HttpResponse(html)

def all_bugs(request):
    all_bugs_list = BugReport.objects.all()
    html = f'<h1>Список всех багов</h1><ol>'
    for bug in all_bugs_list:
        html += f'<li><a href={bug.id}>{bug.title}: {bug.status}</li>'
    html += '</ol>'
    return HttpResponse(html)

def all_request(request):
    all_requests = FeatureRequest.objects.all()
    html = f'<h1>Список всех запросов</h1><ol>'
    for request in all_requests:
        html += f'<li><a href={request.id}>{request.title}: {request.status}</li>'
    html += '</ol>'
    return HttpResponse(html)