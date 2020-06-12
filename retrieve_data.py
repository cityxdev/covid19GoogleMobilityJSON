import csv
import json

import urllib2

csvdata = urllib2.urlopen("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")

countries = {}

fieldnames = (
    "country_region_code",
    "country_region",
    "sub_region_1",
    "sub_region_2",
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
i = 0;
for row in reader:
    i += 1
    if i == 1:
        continue

    countrykey = row["country_region_code"]
    if not countries.get(countrykey):
        countries[countrykey] = {
            "country": [],
            "regions": {}
        }

    values = {
        "date": row["date"],
        "retail_and_recreation_percent_change_from_baseline": float(
            row["retail_and_recreation_percent_change_from_baseline"]) if row[
                                                                              "retail_and_recreation_percent_change_from_baseline"] != '' else None,
        "grocery_and_pharmacy_percent_change_from_baseline": float(
            row["grocery_and_pharmacy_percent_change_from_baseline"]) if row[
                                                                             "grocery_and_pharmacy_percent_change_from_baseline"] != '' else None,
        "parks_percent_change_from_baseline": float(row["parks_percent_change_from_baseline"]) if row[
                                                                                                      "parks_percent_change_from_baseline"] != '' else None,
        "transit_stations_percent_change_from_baseline": float(row["transit_stations_percent_change_from_baseline"]) if
        row["transit_stations_percent_change_from_baseline"] != '' else None,
        "workplaces_percent_change_from_baseline": float(row["workplaces_percent_change_from_baseline"]) if row[
                                                                                                                "workplaces_percent_change_from_baseline"] != '' else None,
        "residential_percent_change_from_baseline": float(row["residential_percent_change_from_baseline"]) if row[
                                                                                                                  "residential_percent_change_from_baseline"] != '' else None
    }

    if row["sub_region_1"] != '':
        regionkey = row["sub_region_1"] + (('_' + row["sub_region_2"]) if row["sub_region_2"] != '' else '')
        if not countries[countrykey]["regions"].get(regionkey):
            countries[countrykey]["regions"][regionkey] = []
        countries[countrykey]["regions"][regionkey].append(values)
    else:
        countries[countrykey]["country"].append(values)

for key in countries:
    jsonfile = open('data/google_mobility_data_' + key + '.json', 'w')
    json.dump(countries[key], jsonfile)
