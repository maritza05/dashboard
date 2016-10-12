from django.shortcuts import render, get_object_or_404

from .models import ProjectsProject, UsersUser, UserstoriesUserstory, MilestonesMilestone

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
    previous = next_ = None
    l = len(sprints)
    for index, sprint in enumerate(sprints):
        if index > 0:
            previous = sprints[index - 1]
        sprint['client_increment'] = sprint.pop('client-increment')
        sprint['team_increment'] = sprint.pop('team-increment')
        if sprint['evolution'] == None:
            sprint['evolution'] = previous['evolution']
    milestones = MilestonesMilestone.objects.all().filter(project=project)

    return render(request, 'projects/charts-area.html', {'project': project,
                                                        'sprints': sprints,
                                                        'milestones': milestones})

def get_milestones_stats(request, id):
    print("ID: " + str(id))
    milestone = MilestonesMilestone.objects.get(id=id)
    data = api_handler.get_milestones_stats(id)
    days = data['days']
    completed_userstories = data['completed_userstories']
    total_userstories = data['total_userstories']
    userstories_percent = (completed_userstories * 100) / total_userstories
    return render(request, 'projects/iterations.html', {'milestone': milestone,
                                                        'days': days,
                                                        'userstories_percent': userstories_percent})
