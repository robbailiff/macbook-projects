from django.shortcuts import render
from projects.models import Project as ProjectModel

# Create your views here.
def project_index(request):
	projects = ProjectModel.objects.all()
	context = {
		'projects': projects
	}
	return render(request, 'project_index.html', context)


def project_detail(request, pk):
	project = ProjectModel.object.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'project_detail.html', context)