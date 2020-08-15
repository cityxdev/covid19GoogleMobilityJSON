# covid19GoogleMobilityJSON - v2.1 - 2020-07-29 - https://github.com/cityxdev/covid19GoogleMobilityJSON

import csv
import json

import urllib2

csvdata = urllib2.urlopen("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")

countries = {}
subregions1 = {}
subregions2 = {}
metros = {}

fieldnames = (
    "country_region_code",
    "country_region",
    "sub_region_1",
    "sub_region_2",
    "metro_area",
    "iso_3166_2_code",
    "census_fips_code",
    "date",
    "retail_and_recreation_percent_change_from_baseline",
    "grocery_and_pharmacy_percent_change_from_baseline",
    "parks_percent_change_from_baseline",
    "transit_stations_percent_change_from_baseline",
    "workplaces_percent_change_from_baseline",
    "residential_percent_change_from_baseline"
)

reader = csv.DictReader(csvdata, fieldnames)
i = 0
for row in reader:
    i += 1
    if i == 1:
        continue

    countrykey = row["country_region_code"]
    if not countries.get(countrykey):
        countries[countrykey] = []

    subregion1key = None
    subregion2key = None
    metrokey = None
    if row["sub_region_1"] != '':
        subregion1key = (row["iso_3166_2_code"] if row["iso_3166_2_code"] != '' else countrykey+"_"+row["sub_region_1"]).replace("/","-")
        if not subregions1.get(subregion1key):
            subregions1[subregion1key] = []
        if row["sub_region_2"] != '':
            subregion2key = (subregion1key+"_"+row["sub_region_2"]).replace("/","-")
            if not subregions2.get(subregion2key):
                subregions2[subregion2key] = []
    else:
        if row["metro_area"] != '':
            metrokey = (row["iso_3166_2_code"] if row["iso_3166_2_code"] != '' else countrykey+"_"+row["metro_area"]).replace("/","-")
            if not metros.get(metrokey):
                metros[metrokey] = []

    values = {
        "date": row["date"],

        "retail_and_recreation_percent_change_from_baseline":
            float(row["retail_and_recreation_percent_change_from_baseline"])
            if row["retail_and_recreation_percent_change_from_baseline"] != ''
            else None,

        "grocery_and_pharmacy_percent_change_from_baseline":
            float(row["grocery_and_pharmacy_percent_change_from_baseline"])
            if row["grocery_and_pharmacy_percent_change_from_baseline"] != ''
            else None,

        "parks_percent_change_from_baseline":
            float(row["parks_percent_change_from_baseline"])
            if row["parks_percent_change_from_baseline"] != ''
            else None,

        "transit_stations_percent_change_from_baseline":
            float(row["transit_stations_percent_change_from_baseline"])
            if row["transit_stations_percent_change_from_baseline"] != ''
            else None,

        "workplaces_percent_change_from_baseline":
            float(row["workplaces_percent_change_from_baseline"])
            if row["workplaces_percent_change_from_baseline"] != ''
            else None,

        "residential_percent_change_from_baseline":
            float(row["residential_percent_change_from_baseline"])
            if row["residential_percent_change_from_baseline"] != ''
            else None
    }

    if subregion1key:
        if subregion2key:
            subregions2[subregion2key].append(values)
        else:
            if metrokey:
                metros[metrokey].append(values)
            else:
                subregions1[subregion1key].append(values)
    else:
        countries[countrykey].append(values)

for key in countries:
    jsonfile = open('data/countries/google_mobility_data_' + key + '.json', 'w')
    json.dump(countries[key], jsonfile)

for key in subregions1:
    jsonfile = open('data/subregions1/google_mobility_data_' + key + '.json', 'w')
    json.dump(subregions1[key], jsonfile)

for key in subregions2:
    jsonfile = open('data/subregions2/google_mobility_data_' + key + '.json', 'w')
    json.dump(subregions2[key], jsonfile)

for key in metros:
    jsonfile = open('data/metro_areas/google_mobility_data_' + key + '.json', 'w')
    json.dump(metros[key], jsonfile)
