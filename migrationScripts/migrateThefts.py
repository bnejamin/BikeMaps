# Used to migrate old bikeDB thefts model to newer database that uses multi-table inheritance
# Written by Taylor Denouden, Feb 16, 2015

import sys, os, django, json

# Get Django settings and shell commands
sys.path.append( os.path.dirname(os.getcwd()) )
os.environ['DJANGO_SETTINGS_MODULE'] = 'VicBikeMap.settings.prod'
django.setup()

from django.contrib.gis.geos import GEOSGeometry

from mapApp.models import Theft

# USAGE
# $ python migrateIncidents.py jsonFileToLoad_date.json
def main(argv):
    # Open file
    json_data = open(argv[0]).read()
    data = json.loads(json_data)

    for f in data:
        p = f['fields']

        theft = Theft(
            geom = GEOSGeometry(p['geom']),

            report_date = p["date"],

            date = p["theft_date"],
            theft_type = p["theft"],
            how_locked = p["how_locked"],
            lock = p["lock"],
            locked_to = p["locked_to"],
            lighting = p["lighting"],
            traffic = p["traffic"],

            details = p["theft_detail"],

            regular_cyclist = p["regular_cyclist"],
            police_report = p["police_report"],
            police_report_num = p["police_report_num"],
            insurance_claim = p["insurance_claim"],
            insurance_claim_num = p["insurance_claim_num"],

            p_type = "theft",
        )

        theft.save()

if __name__ == "__main__":
    main(sys.argv[1:])
