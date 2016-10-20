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

def get_completed_points(id):
    data = api_handler.get_milestones_stats(id)
    # Calculate the progress through completed points
    total_points = data['total_points']
    completed_points = data['completed_points']
    sum_total_points = sum([point for point in total_points.values()])
    sum_completed_points = sum([point for point in completed_points])
    points_percent = (sum_completed_points * 100) / sum_total_points
    print("This is the porcent of points: " + str(points_percent))
    return points_percent


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
    milestones = milestones.order_by('id')
    milestones2 = [(milestone, get_completed_points(milestone.id)) for milestone in milestones]

    max_point = max([sprint['optimal'] for sprint in sprints ])
    max_point = (int(max_point/100)) + 1
    print("This is the max_point: " + str(max_point))
    milestone_data = [api_handler.get_milestones(milestone.id) for milestone in milestones]
    milestones_data = []
    for milestone in milestone_data:
        data = dict()
        data['name']= milestone['name']
        if milestone['closed_points'] == None:
            data['closed_points'] = 0
        elif milestone['total_points'] == None:
            data['total_points'] = 0
        else:
            data['closed_points'] = milestone['closed_points']
            data['total_points'] = milestone['total_points']
        milestones_data.append(data)
    velocities = []
    for i in range(0, len(sprints)):
        if i == 0:
            last = sprints[i]
            actual = sprints[i]
        else:
            last = sprints[i-1]
            actual = sprints[i]
        print("--> Points" + str(actual['name']) + " last: " + str(last['evolution']) + " actual: " + str(actual['evolution']) + " = " + str(last['evolution'] - actual['evolution']))
        velocities.append({'name': actual['name'], 'velocity': last['evolution'] - actual['evolution'] })
    velocity_team = sum([v['velocity'] for v in velocities])/len(velocities)
    data2 = api_handler.get_project_stats(id)
    print("Closed points: " + str(data2['closed_points']))
    print("Total points: " + str(data2['total_points']) )
    try:
     avg_points = (data2['closed_points'] * 100) / data2['total_points']
    except:
     avg_points = 0


    return render(request, 'projects/charts-area.html', {'project': project,
                                                        'sprints': sprints,
                                                        'milestones': milestones,
                                                        'max_point': max_point,
                                                        'velocities': velocities,
                                                        'velocity_team': velocity_team,
                                                        'avg_points': avg_points,
                                                        'milestones2': milestones2})

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
    print("This is the porcent of points: " + str(points_percent))




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


def calculate_probability(request, points, id):
    project = ProjectsProject.objects.get(id=id)
    data = api_handler.get_project_stats(id)
    sprints = data['milestones']
    previous = next_ = None
    label = "Insufficient Data"
    l = len(sprints)
    for index, sprint in enumerate(sprints):
        if index > 0:
            previous = sprints[index - 1]
        sprint['client_increment'] = sprint.pop('client-increment')
        sprint['team_increment'] = sprint.pop('team-increment')
        if sprint['evolution'] == None:
            sprint['evolution'] = previous['evolution']
    velocities = []
    for i in range(0, len(sprints)):
        if i == 0:
            last = sprints[i]
            actual = sprints[i]
        else:
            last = sprints[i-1]
            actual = sprints[i]
        print("--> Points" + str(actual['name']) + " last: " + str(last['evolution']) + " actual: " + str(actual['evolution']) + " = " + str(last['evolution'] - actual['evolution']))
        velocities.append({'name': actual['name'], 'velocity': last['evolution'] - actual['evolution'] })
    for velocity in velocities:
        try:
            name = velocity['name']
            milestone = MilestonesMilestone.objects.get(project=project, name__contains=name)
            print("-- Milestone: " + milestone.name)
            velocity['id'] = milestone.id
        except:
            velocity['id'] = -1
    print("*** Velocities: " + str(velocities))
    milestones = MilestonesMilestone.objects.all().filter(project=project, id__in=[v['id'] for v in velocities], closed=True)
    avg = 0
    for milestone in milestones:
        for velocity in velocities:
            if milestone.id == velocity['id']:
                avg += milestone['velocity']
    print("Average: " + str(avg))



    return render(request, 'projects/probability.html', {'label': label})
