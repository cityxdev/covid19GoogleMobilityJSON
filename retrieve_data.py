import urllib2
import json
from datetime import datetime
import csv



csvdata = urllib2.urlopen("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")

countries = {}

fieldnames = (
	"country_region_code",
	"country_region",
	"sub_region_1",
	"sub_region_2",
	"date",
	"retail_and_recreation_percent_change_from_baseline",
	"grocery_and_pharmacy_percent_change_from_baseline",
	"parks_percent_change_from_baseline",
	"transit_stations_percent_change_from_baseline",
	"workplaces_percent_change_from_baseline",
	"residential_percent_change_from_baseline"
)
reader = csv.DictReader(csvdata, fieldnames)
i = 0;
for row in reader:
	i+=1
	if i==1:
		continue

	countrykey=row["country_region_code"]
	if not countries.get(countrykey):
		countries[countrykey]={
			"country":[],
			"regions":{}
		}

	values={
		"date":row["date"],
		"retail_and_recreation_percent_change_from_baseline":row["retail_and_recreation_percent_change_from_baseline"],
		"grocery_and_pharmacy_percent_change_from_baseline":row["grocery_and_pharmacy_percent_change_from_baseline"],
		"parks_percent_change_from_baseline":row["parks_percent_change_from_baseline"],
		"transit_stations_percent_change_from_baseline":row["transit_stations_percent_change_from_baseline"],
		"workplaces_percent_change_from_baseline":row["workplaces_percent_change_from_baseline"],
		"residential_percent_change_from_baseline":row["residential_percent_change_from_baseline"]
	}

	if row["sub_region_1"]!='':
		regionkey = row["sub_region_1"]+(('_'+row["sub_region_2"]) if row["sub_region_2"]!='' else '')
		if not countries[countrykey]["regions"].get(regionkey):
			countries[countrykey]["regions"][regionkey]=[]
		countries[countrykey]["regions"][regionkey].append(values)
	else:
		countries[countrykey]["country"].append(values)


for key in countries:
	jsonfile = open('data/google_mobility_data_'+key+'_'+datetime.today().strftime('%Y-%m-%d')+'.json', 'w')
	json.dump(countries[key], jsonfile, sort_keys=True, indent=4)

