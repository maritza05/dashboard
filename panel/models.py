# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AttachmentsAttachment(models.Model):
    object_id = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    attached_file = models.CharField(max_length=500, blank=True, null=True)
    is_deprecated = models.BooleanField()
    description = models.TextField()
    order = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    name = models.CharField(max_length=500)
    size = models.IntegerField(blank=True, null=True)
    sha1 = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'attachments_attachment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CustomAttributesEpiccustomattribute(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=16)
    order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'custom_attributes_epiccustomattribute'
        unique_together = (('project', 'name'),)


class CustomAttributesEpiccustomattributesvalues(models.Model):
    version = models.IntegerField()
    attributes_values = models.TextField()  # This field type is a guess.
    epic = models.ForeignKey('EpicsEpic', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'custom_attributes_epiccustomattributesvalues'


class CustomAttributesIssuecustomattribute(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'custom_attributes_issuecustomattribute'
        unique_together = (('project', 'name'),)


class CustomAttributesIssuecustomattributesvalues(models.Model):
    version = models.IntegerField()
    attributes_values = models.TextField()  # This field type is a guess.
    issue = models.ForeignKey('IssuesIssue', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'custom_attributes_issuecustomattributesvalues'


class CustomAttributesTaskcustomattribute(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'custom_attributes_taskcustomattribute'
        unique_together = (('project', 'name'),)


class CustomAttributesTaskcustomattributesvalues(models.Model):
    version = models.IntegerField()
    attributes_values = models.TextField()  # This field type is a guess.
    task = models.ForeignKey('TasksTask', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'custom_attributes_taskcustomattributesvalues'


class CustomAttributesUserstorycustomattribute(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'custom_attributes_userstorycustomattribute'
        unique_together = (('project', 'name'),)


class CustomAttributesUserstorycustomattributesvalues(models.Model):
    version = models.IntegerField()
    attributes_values = models.TextField()  # This field type is a guess.
    user_story = models.ForeignKey('UserstoriesUserstory', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'custom_attributes_userstorycustomattributesvalues'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjmailMessage(models.Model):
    uuid = models.CharField(primary_key=True, max_length=40)
    from_email = models.CharField(max_length=1024)
    to_email = models.TextField()
    body_text = models.TextField()
    body_html = models.TextField()
    subject = models.CharField(max_length=1024)
    data = models.TextField()
    retry_count = models.SmallIntegerField()
    status = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    created_at = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    exception = models.TextField()

    class Meta:
        managed = False
        db_table = 'djmail_message'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.ForeignKey(EasyThumbnailsThumbnail, models.DO_NOTHING, unique=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class EpicsEpic(models.Model):
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField()
    is_blocked = models.BooleanField()
    blocked_note = models.TextField()
    ref = models.BigIntegerField(blank=True, null=True)
    epics_order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    subject = models.TextField()
    description = models.TextField()
    client_requirement = models.BooleanField()
    team_requirement = models.BooleanField()
    assigned_to = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name='epics_asigned')
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    status = models.ForeignKey('ProjectsEpicstatus', models.DO_NOTHING, blank=True, null=True)
    color = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'epics_epic'


class EpicsRelateduserstory(models.Model):
    order = models.BigIntegerField()
    epic = models.ForeignKey(EpicsEpic, models.DO_NOTHING)
    user_story = models.ForeignKey('UserstoriesUserstory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'epics_relateduserstory'
        unique_together = (('user_story', 'epic'),)


class ExternalAppsApplication(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    icon_url = models.TextField(blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    next_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'external_apps_application'


class ExternalAppsApplicationtoken(models.Model):
    auth_code = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    application = models.ForeignKey(ExternalAppsApplication, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'external_apps_applicationtoken'
        unique_together = (('application', 'user'),)


class FeedbackFeedbackentry(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=255)
    comment = models.TextField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feedback_feedbackentry'


class HistoryHistoryentry(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    is_snapshot = models.NullBooleanField()
    key = models.CharField(max_length=255, blank=True, null=True)
    diff = models.TextField(blank=True, null=True)  # This field type is a guess.
    snapshot = models.TextField(blank=True, null=True)  # This field type is a guess.
    values = models.TextField(blank=True, null=True)  # This field type is a guess.
    comment = models.TextField(blank=True, null=True)
    comment_html = models.TextField(blank=True, null=True)
    delete_comment_date = models.DateTimeField(blank=True, null=True)
    delete_comment_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_hidden = models.NullBooleanField()
    comment_versions = models.TextField(blank=True, null=True)  # This field type is a guess.
    edit_comment_date = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'history_historyentry'


class IssuesIssue(models.Model):
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField()
    is_blocked = models.BooleanField()
    blocked_note = models.TextField()
    ref = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    finished_date = models.DateTimeField(blank=True, null=True)
    subject = models.TextField()
    description = models.TextField()
    assigned_to = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name='issue_asigned_to')
    milestone = models.ForeignKey('MilestonesMilestone', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    priority = models.ForeignKey('ProjectsPriority', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    severity = models.ForeignKey('ProjectsSeverity', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('ProjectsIssuestatus', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('ProjectsIssuetype', models.DO_NOTHING, blank=True, null=True)
    external_reference = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'issues_issue'


class LikesLike(models.Model):
    object_id = models.IntegerField()
    created_date = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'likes_like'
        unique_together = (('content_type', 'object_id', 'user'),)


class MilestonesMilestone(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    estimated_start = models.DateField()
    estimated_finish = models.DateField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    closed = models.BooleanField()
    disponibility = models.FloatField(blank=True, null=True)
    order = models.SmallIntegerField()
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'milestones_milestone'
        unique_together = (('name', 'project'), ('slug', 'project'),)


class NotificationsHistorychangenotification(models.Model):
    key = models.CharField(max_length=255)
    created_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField()
    history_type = models.SmallIntegerField()
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications_historychangenotification'
        unique_together = (('key', 'owner', 'project', 'history_type'),)


class NotificationsHistorychangenotificationHistoryEntries(models.Model):
    historychangenotification = models.ForeignKey(NotificationsHistorychangenotification, models.DO_NOTHING)
    historyentry = models.ForeignKey(HistoryHistoryentry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications_historychangenotification_history_entries'
        unique_together = (('historychangenotification', 'historyentry'),)


class NotificationsHistorychangenotificationNotifyUsers(models.Model):
    historychangenotification = models.ForeignKey(NotificationsHistorychangenotification, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications_historychangenotification_notify_users'
        unique_together = (('historychangenotification', 'user'),)


class NotificationsNotifypolicy(models.Model):
    notify_level = models.SmallIntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications_notifypolicy'
        unique_together = (('project', 'user'),)


class NotificationsWatched(models.Model):
    object_id = models.IntegerField()
    created_date = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notifications_watched'
        unique_together = (('content_type', 'object_id', 'user', 'project'),)


class ProjectsEpicstatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    order = models.IntegerField()
    is_closed = models.BooleanField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_epicstatus'
        unique_together = (('project', 'slug'), ('project', 'name'),)


class ProjectsIssuestatus(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    is_closed = models.BooleanField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'projects_issuestatus'
        unique_together = (('project', 'name'), ('project', 'slug'),)


class ProjectsIssuetype(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_issuetype'
        unique_together = (('project', 'name'),)


class ProjectsMembership(models.Model):
    is_admin = models.BooleanField()
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    token = models.CharField(max_length=60, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)
    role = models.ForeignKey('UsersRole', models.DO_NOTHING)
    invited_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name='membership_invited_by')
    invitation_extra_text = models.TextField(blank=True, null=True)
    user_order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'projects_membership'
        unique_together = (('user', 'project'),)


class ProjectsPoints(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_points'
        unique_together = (('project', 'name'),)


class ProjectsPriority(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey('ProjectsProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_priority'
        unique_together = (('project', 'name'),)


class ProjectsProject(models.Model):
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    total_milestones = models.IntegerField(blank=True, null=True)
    total_story_points = models.FloatField(blank=True, null=True)
    is_backlog_activated = models.BooleanField()
    is_kanban_activated = models.BooleanField()
    is_wiki_activated = models.BooleanField()
    is_issues_activated = models.BooleanField()
    videoconferences = models.CharField(max_length=250, blank=True, null=True)
    videoconferences_extra_data = models.CharField(max_length=250, blank=True, null=True)
    anon_permissions = models.TextField(blank=True, null=True)  # This field type is a guess.
    public_permissions = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_private = models.BooleanField()
    tags_colors = models.TextField(blank=True, null=True)  # This field type is a guess.
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    creation_template = models.ForeignKey('ProjectsProjecttemplate', models.DO_NOTHING, blank=True, null=True)
    default_issue_status = models.ForeignKey(ProjectsIssuestatus, models.DO_NOTHING, unique=True, blank=True, null=True)
    default_issue_type = models.ForeignKey(ProjectsIssuetype, models.DO_NOTHING, unique=True, blank=True, null=True)
    default_points = models.ForeignKey(ProjectsPoints, models.DO_NOTHING, unique=True, blank=True, null=True)
    default_priority = models.ForeignKey(ProjectsPriority, models.DO_NOTHING, unique=True, blank=True, null=True)
    default_severity = models.ForeignKey('ProjectsSeverity', models.DO_NOTHING, unique=True, blank=True, null=True)
    default_task_status = models.ForeignKey('ProjectsTaskstatus', models.DO_NOTHING, unique=True, blank=True, null=True)
    default_us_status = models.ForeignKey('ProjectsUserstorystatus', models.DO_NOTHING, unique=True, blank=True, null=True)
    issues_csv_uuid = models.CharField(max_length=32, blank=True, null=True)
    tasks_csv_uuid = models.CharField(max_length=32, blank=True, null=True)
    userstories_csv_uuid = models.CharField(max_length=32, blank=True, null=True)
    is_featured = models.BooleanField()
    is_looking_for_people = models.BooleanField()
    total_activity = models.IntegerField()
    total_activity_last_month = models.IntegerField()
    total_activity_last_week = models.IntegerField()
    total_activity_last_year = models.IntegerField()
    total_fans = models.IntegerField()
    total_fans_last_month = models.IntegerField()
    total_fans_last_week = models.IntegerField()
    total_fans_last_year = models.IntegerField()
    totals_updated_datetime = models.DateTimeField()
    logo = models.CharField(max_length=500, blank=True, null=True)
    looking_for_people_note = models.TextField()
    blocked_code = models.CharField(max_length=255, blank=True, null=True)
    transfer_token = models.CharField(max_length=255, blank=True, null=True)
    is_epics_activated = models.BooleanField()
    default_epic_status = models.ForeignKey(ProjectsEpicstatus, models.DO_NOTHING, unique=True, blank=True, null=True)
    epics_csv_uuid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_project'


class ProjectsProjectmodulesconfig(models.Model):
    config = models.TextField(blank=True, null=True)  # This field type is a guess.
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'projects_projectmodulesconfig'


class ProjectsProjecttemplate(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    default_owner_role = models.CharField(max_length=50)
    is_backlog_activated = models.BooleanField()
    is_kanban_activated = models.BooleanField()
    is_wiki_activated = models.BooleanField()
    is_issues_activated = models.BooleanField()
    videoconferences = models.CharField(max_length=250, blank=True, null=True)
    videoconferences_extra_data = models.CharField(max_length=250, blank=True, null=True)
    default_options = models.TextField(blank=True, null=True)  # This field type is a guess.
    us_statuses = models.TextField(blank=True, null=True)  # This field type is a guess.
    points = models.TextField(blank=True, null=True)  # This field type is a guess.
    task_statuses = models.TextField(blank=True, null=True)  # This field type is a guess.
    issue_statuses = models.TextField(blank=True, null=True)  # This field type is a guess.
    issue_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    priorities = models.TextField(blank=True, null=True)  # This field type is a guess.
    severities = models.TextField(blank=True, null=True)  # This field type is a guess.
    roles = models.TextField(blank=True, null=True)  # This field type is a guess.
    order = models.BigIntegerField()
    epic_statuses = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_epics_activated = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'projects_projecttemplate'


class ProjectsSeverity(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_severity'
        unique_together = (('project', 'name'),)


class ProjectsTaskstatus(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    is_closed = models.BooleanField()
    color = models.CharField(max_length=20)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'projects_taskstatus'
        unique_together = (('project', 'slug'), ('project', 'name'),)


class ProjectsUserstorystatus(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    is_closed = models.BooleanField()
    color = models.CharField(max_length=20)
    wip_limit = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    slug = models.CharField(max_length=255)
    is_archived = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'projects_userstorystatus'
        unique_together = (('project', 'name'), ('project', 'slug'),)


class ReferencesReference(models.Model):
    object_id = models.IntegerField()
    ref = models.BigIntegerField()
    created_at = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'references_reference'
        unique_together = (('project', 'ref'),)


class TasksTask(models.Model):
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField()
    is_blocked = models.BooleanField()
    blocked_note = models.TextField()
    ref = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    finished_date = models.DateTimeField(blank=True, null=True)
    subject = models.TextField()
    description = models.TextField()
    is_iocaine = models.BooleanField()
    assigned_to = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name='task_asigned_to')
    milestone = models.ForeignKey(MilestonesMilestone, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    status = models.ForeignKey(ProjectsTaskstatus, models.DO_NOTHING, blank=True, null=True)
    user_story = models.ForeignKey('UserstoriesUserstory', models.DO_NOTHING, blank=True, null=True)
    taskboard_order = models.BigIntegerField()
    us_order = models.BigIntegerField()
    external_reference = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tasks_task'


class TimelineTimeline(models.Model):
    object_id = models.IntegerField()
    namespace = models.CharField(max_length=250)
    event_type = models.CharField(max_length=250)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING, blank=True, null=True)
    data = models.TextField()  # This field type is a guess.
    data_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, related_name='timeline_content_type')

    class Meta:
        managed = False
        db_table = 'timeline_timeline'


class UsersAuthdata(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=300)
    extra = models.TextField()  # This field type is a guess.
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_authdata'
        unique_together = (('key', 'value'),)


class UsersRole(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    permissions = models.TextField(blank=True, null=True)  # This field type is a guess.
    order = models.IntegerField()
    computable = models.BooleanField()
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_role'
        unique_together = (('slug', 'project'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField()
    full_name = models.CharField(max_length=256)
    color = models.CharField(max_length=9)
    bio = models.TextField()
    photo = models.CharField(max_length=500, blank=True, null=True)
    date_joined = models.DateTimeField()
    lang = models.CharField(max_length=20, blank=True, null=True)
    timezone = models.CharField(max_length=20, blank=True, null=True)
    colorize_tags = models.BooleanField()
    token = models.CharField(max_length=200, blank=True, null=True)
    email_token = models.CharField(max_length=200, blank=True, null=True)
    new_email = models.CharField(max_length=254, blank=True, null=True)
    is_system = models.BooleanField()
    theme = models.CharField(max_length=100, blank=True, null=True)
    max_private_projects = models.IntegerField(blank=True, null=True)
    max_public_projects = models.IntegerField(blank=True, null=True)
    max_memberships_private_projects = models.IntegerField(blank=True, null=True)
    max_memberships_public_projects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'


class UserstorageStorageentry(models.Model):
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)  # This field type is a guess.
    owner = models.ForeignKey(UsersUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userstorage_storageentry'
        unique_together = (('owner', 'key'),)


class UserstoriesRolepoints(models.Model):
    points = models.ForeignKey(ProjectsPoints, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(UsersRole, models.DO_NOTHING)
    user_story = models.ForeignKey('UserstoriesUserstory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userstories_rolepoints'
        unique_together = (('user_story', 'role'),)


class UserstoriesUserstory(models.Model):
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField()
    is_blocked = models.BooleanField()
    blocked_note = models.TextField()
    ref = models.BigIntegerField(blank=True, null=True)
    is_closed = models.BooleanField()
    backlog_order = models.BigIntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    finish_date = models.DateTimeField(blank=True, null=True)
    subject = models.TextField()
    description = models.TextField()
    client_requirement = models.BooleanField()
    team_requirement = models.BooleanField()
    assigned_to = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name='userstory_assigned_to')
    generated_from_issue = models.ForeignKey(IssuesIssue, models.DO_NOTHING, blank=True, null=True)
    milestone = models.ForeignKey(MilestonesMilestone, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    status = models.ForeignKey(ProjectsUserstorystatus, models.DO_NOTHING, blank=True, null=True)
    sprint_order = models.BigIntegerField()
    kanban_order = models.BigIntegerField()
    external_reference = models.TextField(blank=True, null=True)  # This field type is a guess.
    tribe_gig = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userstories_userstory'


class VotesVote(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'votes_vote'
        unique_together = (('content_type', 'object_id', 'user'),)


class VotesVotes(models.Model):
    object_id = models.IntegerField()
    count = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'votes_votes'
        unique_together = (('content_type', 'object_id'),)


class WebhooksWebhook(models.Model):
    url = models.CharField(max_length=200)
    key = models.TextField()
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'webhooks_webhook'


class WebhooksWebhooklog(models.Model):
    url = models.CharField(max_length=200)
    status = models.IntegerField()
    request_data = models.TextField()  # This field type is a guess.
    response_data = models.TextField()
    webhook = models.ForeignKey(WebhooksWebhook, models.DO_NOTHING)
    created = models.DateTimeField()
    duration = models.FloatField()
    request_headers = models.TextField()  # This field type is a guess.
    response_headers = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webhooks_webhooklog'


class WikiWikilink(models.Model):
    title = models.CharField(max_length=500)
    href = models.CharField(max_length=500)
    order = models.BigIntegerField()
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wiki_wikilink'
        unique_together = (('project', 'href'),)


class WikiWikipage(models.Model):
    version = models.IntegerField()
    slug = models.CharField(max_length=500)
    content = models.TextField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    last_modifier = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(UsersUser, models.DO_NOTHING, blank=True, null=True, related_name='wikipedia_owner')
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wiki_wikipage'
        unique_together = (('project', 'slug'),)
