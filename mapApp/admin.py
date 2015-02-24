from django.contrib.gis import admin

# Register models
from mapApp.models import Point
from mapApp.models import Incident
from mapApp.models import Hazard
from mapApp.models import Theft
# from mapApp.models import AlertArea
# from mapApp.models import IncidentNotification, HazardNotification, TheftNotification

from spirit.models import User
admin.site.register(User)


class IncidentAdmin(admin.OSMGeoAdmin):
	class Meta:
		model = Incident

	# Map options
	default_lon = -13745000
	default_lat = 6196000
	default_zoom = 10

	# Allow for filtering of report date
	list_filter = ['report_date', 'date', 'p_type']

	list_display = ('pk','report_date','date','time','incident_type', 'incident_with','was_published_recently')

	fieldsets = [
	    ('Location', {'fields': ['geom']}),
	    ('Incident', {'fields': ['date','time','incident_type', 'incident_with', 'injury', 'trip_purpose']}),
	    ('Detail', {'fields': ['details'], 'classes':['collapse']}),
	    ('Personal', {'fields': ['age', 'birthmonth', 'sex', 'regular_cyclist', 'helmet', 'intoxicated'], 'classes':['collapse']}),
	    ('Conditions', {'fields': ['road_conditions', 'sightlines', 'cars_on_roadside', 'riding_on', 'bike_lights', 'terrain', 'direction', 'turning'], 'classes':['collapse']}),
	]
admin.site.register(Incident, IncidentAdmin)

class HazardAdmin(admin.OSMGeoAdmin):
	class Meta:
		model = Hazard

	# Map options
	default_lon = -13745000
	default_lat = 6196000
	default_zoom = 10

	# Allow for filtering of report date
	list_filter = ['report_date', 'date']

	list_display = ('pk','report_date','date','time','hazard_type','was_published_recently')

	fieldsets = [
	    ('Location', {'fields': ['geom']}),
	    ('Hazard', {'fields': ['date','time','hazard_type']}),
	    ('Detail', {'fields': ['details'], 'classes':['collapse']}),
	    ('Personal', {'fields': ['age', 'birthmonth', 'sex', 'regular_cyclist'], 'classes':['collapse']})
	]
admin.site.register(Hazard, HazardAdmin)

class TheftAdmin(admin.OSMGeoAdmin):
	# Map options
	default_lon = -13745000
	default_lat = 6196000
	default_zoom = 10

	# Allow for filtering of report date
	list_filter = ['report_date', 'date']

	list_display = ('pk','report_date','date','time','theft_type','was_published_recently')

	fieldsets = [
	    ('Location', {'fields': ['geom']}),
	    ('Theft', {'fields': ['date', 'time','theft_type', 'how_locked', 'lock', 'locked_to', 'lighting', 'traffic', 'police_report', 'insurance_claim']}),
	    ('Detail', {'fields': ['details'], 'classes':['collapse']}),
	    ('Personal', {'fields': ['regular_cyclist'], 'classes':['collapse']})
	]
admin.site.register(Theft, TheftAdmin)

class PointAdmin(admin.OSMGeoAdmin):
	# Map options
	default_lon = -13745000
	default_lat = 6196000
	default_zoom = 10

	# Allow for filtering of report date
	list_filter = ['report_date', 'date', 'p_type']

	list_display = ('pk','p_type','report_date','date','time','was_published_recently')

	fieldsets = [
	    ('Location', {'fields': ['geom']}),
	    ('Point', {'fields': ['date',  'p_type']}),
	    ('Detail', {'fields': ['details'], 'classes':['collapse']}),
	    ('Personal', {'fields': ['age', 'birthmonth', 'sex', ], 'classes':['collapse']})
	]
admin.site.register(Point, PointAdmin)


# class AlertAreaAdmin(admin.OSMGeoAdmin):
# 	# Map options
# 	default_lon = -13745000
# 	default_lat = 6196000
# 	default_zoom = 10

# 	list_display = ('pk', 'user', 'email', 'date')

# 	fieldsets = [
# 		('Area',	{'fields': ['geom']}),
# 		('User',	{'fields': ['user','email']})
# 	]
# admin.site.register(AlertArea, AlertAreaAdmin)


# admin.site.register(IncidentNotification)
# admin.site.register(HazardNotification)
# admin.site.register(TheftNotification)
