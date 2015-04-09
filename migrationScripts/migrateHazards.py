# Used to migrate old bikeDB hazards model to newer database that uses multi-table inheritance
# Written by Taylor Denouden, Feb 16, 2015

import sys, os, django, json

# Get Django settings and shell commands
sys.path.append( os.path.dirname(os.getcwd()) )
os.environ['DJANGO_SETTINGS_MODULE'] = 'VicBikeMap.settings.prod'
django.setup()

from django.contrib.gis.geos import GEOSGeometry

from mapApp.models import Hazard

# USAGE
# $ python migrateIncidents.py jsonFileToLoad_date.json
def main(argv):
    # Open file
    json_data = open(argv[0]).read()
    data = json.loads(json_data)

    for f in data:
        p = f['fields']

        hazard = Hazard(
            geom = GEOSGeometry(p['geom']),

            report_date = p["date"],

            date = p["hazard_date"],
            hazard_type = p["hazard"],

            details = p["hazard_detail"],

            age = p["age"],
            birthmonth = p["birthmonth"],
            sex = p["sex"],
            regular_cyclist = p["regular_cyclist"],

            p_type = "hazard",
        )
        hazard.save()

if __name__ == "__main__":
    main(sys.argv[1:])
