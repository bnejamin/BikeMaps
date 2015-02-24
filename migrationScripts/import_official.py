import sys, os, django, json, datetime
from django_setup import import_django

def main(argv):
    import_django("dev")

    from django.contrib.gis.geos import GEOSGeometry
    from mapApp.models import Official

    # Load passed json file
    json_data = open(argv[0]).read()
    data = json.loads(json_data)

    for f in data['features']:
        p = f['properties']
        o = Official(
            # Set fields here
            official_type = "Vehicle collision",
            data_source = "Victoria Police Dept.",
            metadata = "Data available for the City of Victoria from 2008 to 2012",
            who_added = "Taylor",
            geom = GEOSGeometry(json.dumps(f['geometry'])),
            # report_date = AutoNow()
            date = datetime.datetime.strptime((p['ACC_DATE'] + "T" + p['ACC_TIME']), "%Y/%m/%dT%H%M"),
            details = p['ACC_TYPE'].lower().capitalize(),
            p_type = "official",
        )
        print o
        # o.save()


if __name__ == "__main__":
    main(sys.argv[1:])
