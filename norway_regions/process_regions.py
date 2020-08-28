"""
SatsKred processing regions were drawn using QGIS and saved as shapefile. CRS while drawing is UTM33.
Data needs to be re-projected to CRS:4326 (Lat/Lon) before saving. satskred init works only with lat/lon.
Regions with ID 1000-1999 contain A-forecasting regions (daily forecasting). regions with ID 2000-2999 contain B-forecasting regions (emergency regions).
"""

import geopandas as gpd
import json
from shapely.geometry import mapping

regions = gpd.read_file("N:\Prosjekter\SatSkred\Dev\GIS\satskred_regions.shp")
print("Original CRS is: {0}".format(regions.crs))
regions.head()

regions['area_km2'] = regions.area / 1e6
regions['length_km'] = regions.length / 1e3

print("\nRegion sorted by ID")
print(regions.filter(['ID', 'area_km2', 'length_km']).sort_values(by=['ID']))

print("\nRegions sorted by area (sq.km)")
print(regions.filter(['ID', 'area_km2', 'length_km']).sort_values(by=['area_km2'], ascending=False))

regions.to_crs(epsg=4326, inplace=True)
print("\nChanged CRS to lat/lon: {0}".format(regions.crs))

for index, reg in regions.iterrows():
    _json_str = mapping(reg.geometry)
    _json_file = 'satskred_region_{0}.geojson'.format(reg['ID'])
    print('Writing {0}... '.format(_json_file), end='')
    with open(_json_file, 'w') as fid:
        json.dump(_json_str, fid)
    print('Done')

print("\nExport to GEOJSON complete!")
