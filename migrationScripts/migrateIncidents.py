import sys, os, django, json

# Get Django settings and shell commands
sys.path.append( os.path.dirname(os.getcwd()) )
os.environ['DJANGO_SETTINGS_MODULE'] = 'VicBikeMap.settings.dev'
django.setup()

from django.contrib.gis.geos import GEOSGeometry

from mapApp.models import Incident

# USAGE
# $ python migrateIncidents.py jsonFileToLoad_date.json
def main(argv):
    # Open file
    json_data = open(argv[0]).read()
    data = json.loads(json_data)

    for f in data['features']:
        # print json.dumps(f, indent=2, separators=(',', ': '))
        # Set properties
        p = f['properties']
        incident = Incident(
            geom = GEOSGeometry(json.dumps( f['geometry'] )),

            report_date = p["date"],

            date = p["incident_date"],
            incident_type = p["incident"],
            incident_with = p["incident_with"],
            injury = p["injury"],
            trip_purpose = p["trip_purpose"],

            road_conditions = p["road_conditions"],
            sightlines = p["sightlines"],
            cars_on_roadside = p["cars_on_roadside"],
            riding_on = p["riding_on"],
            bike_lights = p["bike_lights"],
            terrain = p["terrain"],
            direction = p["direction"],
            turning = p["turning"],

            details = p["incident_detail"],

            age = p["age"],
            birthmonth = p["birthmonth"],
            sex = p["sex"],
            regular_cyclist = p["regular_cyclist"],
            helmet = p["helmet"],
            intoxicated = p["intoxicated"],

            weather = p["weather"],

            p_type = getIncidentType(p["incident"]),
        )
        incident.save()

def getIncidentType(usr_choice):
	for t,choice in Incident.INCIDENT_CHOICES:
		for p,q in choice:
			if p == usr_choice:
				return t.replace(" ", "").lower()

if __name__ == "__main__":
    main(sys.argv[1:])
