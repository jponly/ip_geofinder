import geoip2.database

reader = geoip2.database.Reader('./GeoLite2-City_20200218/Geolite2-City.mmdb')

response = reader.city('98.155.130.10')
print("response.country.iso_code: {}".format(response.country.iso_code))
print("response.subdivisions.most_specific.name: {}".format(response.subdivisions.most_specific.name))
print("response.subdivisions.most_specific.iso_code: {}".format(response.subdivisions.most_specific.iso_code))
print("response.city.name: {}".format(response.city.name))
print("response.postal.code {}".format(response.postal.code))

reader.close() 