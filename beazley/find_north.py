from xml.etree.ElementTree import parse

daves_latitude = 41.98062
daves_longitude = -87.668452

data = parse('rt22.xml')

for bus in data.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat > daves_latitude:
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print lat, direction