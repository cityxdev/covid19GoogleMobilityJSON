# covid19GoogleMobilityJSON
A way to transform Google's mobility data during the COVID-19 pandemic to a JSON file per country

<h2>New version that breaks dependencies</h2>
<p>As this dataset continues growing, we reached a file size limit of Github. This way, the output structure changed to make files smaller. This was done by moving regional data to individual files instead of being stored in the country file.</p>
<p>The output has now the following structure:</p>

    --data
      |_____countries
      |     |__________google_mobility_data_XX.json
      |     |__________google_mobility_data_XY.json
      |
      |_____subregions1
      |     |__________google_mobility_data_XX-AA.json
      |     |__________google_mobility_data_XX-AB.json
      |     |__________google_mobility_data_XY-subregion1name.json
      |     |__________google_mobility_data_XY-subregion1name.json
      |
      |______subregions2                                                               (currently, only for USA)
             |__________google_mobility_data_XX_subregion1name_subregion2name.json
           
- The two letter code for countries is stable and covers the whole dataset
- The iso_3166_2 code for subregion1 is used where possible. If unavailable, name is used instead
- There are no codes for subregion2. It is also not possible to use the iso_3166_2 code to group subregion2 because it is not provided in the source
<hr/>

<br/>
<p>Reads from the CSV available at https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv
<br/>
More info on this data: https://www.google.com/covid19/mobility/data_documentation.html?hl=en#about-this-data</p>

<p>I will try to run once a day and push an update on fresh data</p>

<br/><br/>
**You can access the data using a URL like:**

```https://cityxdev.github.io/covid19GoogleMobilityJSON/data/countries/google_mobility_data_```[2 letter country code]```.json```
Example: ```https://cityxdev.github.io/covid19GoogleMobilityJSON/data/countries/google_mobility_data_PT.json```
