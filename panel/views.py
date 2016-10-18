from django.shortcuts import render, get_object_or_404

from .models import ProjectsProject, UsersUser, UserstoriesUserstory, MilestonesMilestone, ProjectsMembership

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
    max_point = max([sprint['optimal'] for sprint in sprints ])
    max_point = (int(max_point/100)) + 1
    print("This is the max_point: " + str(max_point))

    return render(request, 'projects/charts-area.html', {'project': project,
                                                        'sprints': sprints,
                                                        'milestones': milestones,
                                                        'max_point': max_point})

def get_milestones_stats(request, id):
    print("ID: " + str(id))
    milestone = MilestonesMilestone.objects.get(id=id)
    data = api_handler.get_milestones_stats(id)
    days = data['days']

    completed_userstories = data['completed_userstories']
    total_userstories = data['total_userstories']
    userstories_percent = (completed_userstories * 100) / total_userstories
    print('Porcent of userstories: ' + str(int(userstories_percent)))

    # Calculate the progress through completed points
    total_points = data['total_points']
    completed_points = data['completed_points']
    sum_total_points = sum([point for point in total_points.values()])
    sum_completed_points = sum([point for point in completed_points])
    points_percent = (sum_completed_points * 100) / sum_total_points




    return render(request, 'projects/iterations.html', {'milestone': milestone,
                                                        'days': days,
                                                        'userstories_percent': int(userstories_percent),
                                                        'progress_points': int(points_percent)})



def show_panel(request, id):
    project = ProjectsProject.objects.get(id=id)
    milestones = MilestonesMilestone.objects.all().filter(project=project)
    memberships = ProjectsMembership.objects.all().filter(project=project)
    users = [ membership.user for membership in memberships ]

    milestones_count = len(milestones)
    users_count = len(users)

    return render(request, 'projects/sidebar.html', {'actual_project': project,
                                                     'milestones': milestones,
                                                     'users': users,
                                                     'milestones_count': milestones_count,
                                                     'users_count': users_count })
