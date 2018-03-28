import json
import requests

def get_json( url ):
    r = requests.get(url=url)
    if r.status_code != 200:
    	return None

    output_json = r.json()
    return output_json

def parse_json(data):
	final_structure = []
	for feature in data["features"]:
		lat = feature["geometry"]["coordinates"][1]
		lng = feature["geometry"]["coordinates"][0]
		properties = feature["properties"]
		struct = properties
		struct["LAT"] = lat
		struct["LONG"] = lng
		final_structure.append(struct)
	print(final_structure[0])

water_info = get_json("https://www.water.ie/site-files/cms-templates/utils/proxy/index.xml?https://services2.arcgis.com/OqejhVam51LdtxGa/ArcGIS/rest/services/WaterAdvisoryCR021/FeatureServer/0/query?returnGeometry=true&where=STATUS!%3D%27Closed%27&outFields=*&orderByFields=STARTDATE%20DESC&outSR=4326&returnIdsOnly=false&f=pgeojson")

parsed_data = parse_json(water_info)

