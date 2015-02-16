import sys, os, json

os.environ.setDefault("DJANGO_SETTINGS_MODULE", "VicBikeMap.settings")
from mapApp.models import Incident

# USAGE
# $ python migrateIncidents.py jsonFileToLoad_date.json
def main(argv):
    # Open file
    json_data = open(argv[0]).read()
    data = json.loads(json_data)

    print Incident.objects.all()

    #
    # for f in data['features']:
    #     print json.dumps(f, indent=2, separators=(',', ': '))
    #
    #     # print f['properties']
    #
    #     break


if __name__ == "__main__":
    main(sys.argv[1:])
