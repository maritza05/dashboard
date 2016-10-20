from django.shortcuts import render, get_object_or_404

from .models import ProjectsProject, UsersUser, UserstoriesUserstory

from .utils import api_handler


def get_all_projects(request):
    projects = ProjectsProject.objects.all()
    all_projects_count = len(projects)
    users_count = len(UsersUser.objects.all())
    closed_userstories_count = len(UserstoriesUserstory.objects.filter(is_closed=False))
    current_projects_count = 0
    for project in projects:
        project_info = api_handler.get_project_stats(project.id)
        closed_points = project_info['total_points'] - project_info['closed_points']
        if closed_points > 0 :
            current_projects_count += 1
            print("Project id: " + str(project.id))
    return render(request, 'projects/index.html',
                            {'projects': projects,
                             'projects_count': all_projects_count,
                             'users_count': users_count,
                             'current_projects_count': current_projects_count,
                             'closed_userstories_count': closed_userstories_count})


def show_charts(request, id):
    project = ProjectsProject.objects.get(id=id)
    data = api_handler.get_project_stats(id)
    sprints = data['milestones']
    print(sprints)


    return render(request, 'projects/charts-area.html', {'project': project})
