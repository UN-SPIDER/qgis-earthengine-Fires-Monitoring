import ee
from ee_plugin import Map
########################################################################

# This funtion add feature of theastudy area =(Tunisia)
countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
TUN = countries.filter(ee.Filter.eq('country_na', 'Tunisia'))

# Create an empty image into which to paint the features, cast to byte.
empty = ee.Image().byte()

# Paint all the polygon edges with the same number and 'width', display.
outline = empty.paint(**{
  'featureCollection': TUN,
  'color': 1,
  'width': 1.5
})
Map.addLayer(outline, {'palette': 'FF0000'}, 'Tunisia Limit')

# set Map center using coordinates and zoom
Map.setCenter(9.346, 35.032, 6)
########################################################################

# This funtion add a Sentinel 2 imagen 
imagen = ee.ImageCollection('COPERNICUS/S2') \
  .filterBounds(TUN) \
  .filterDate('2020-04-15', '2020-08-19').median() \
  .divide(10000) \
  .select(
  ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12'],
  ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B08A', 'B11', 'B12']
  )
vis = {'bands': ['B12', 'B08', 'B04'], 'min': 0.05, 'max': 0.5}
Map.addLayer(imagen, vis, 'Sentinel 2 False color')
Map.setCenter(8.7107, 35.2061, 15)
########################################################################

# This function gets FIRMS from MODIS imagery.
collection = ee.ImageCollection('FIRMS')\
  .filterBounds(TUN) \
  .select('T21')\
  .filterDate('2020-04-15', '2020-08-20')\

band_viz = {
  'min': 325,
  'max': 400,
  'palette': ['red', 'orange', 'yellow']
}

Map.addLayer(collection.mean(), band_viz, 'Hot Spots')
########################################################################

##This funtion Visualize the burn area of FireCCI51 for the year 2019
dataset = ee.ImageCollection('ESA/CCI/FireCCI/5_1')\
                  .filterDate('2019-01-01', '2019-12-30')
burnedArea = dataset.select('BurnDate')

##Use a circular palette to assign colors to date of first detection
baVis = {
  'min': 1,
  'max': 366,
  'palette': [
    'ff0000', 'fd4100', 'fb8200', 'f9c400', 'f2ff00', 'b6ff05',
    '7aff0a', '3eff0f', '02ff15', '00ff55', '00ff99', '00ffdd',
    '00ddff', '0098ff', '0052ff', '0210ff', '3a0dfb', '7209f6',
    'a905f1', 'e102ed', 'ff00cc', 'ff0089', 'ff0047', 'ff0004'
  ]
};
maxBA = burnedArea.max()
Map.addLayer(maxBA, baVis, 'Burned Area CCI Fire 2019')
########################################################################

#MCD64A1.006 MODIS Burned Area Monthly Global 500m
collection2 = ee.ImageCollection('MODIS/006/MOD14A1')\
.filterDate('2020-04-15', '2020-08-20')\
  
fireMaskVis = {
  'min': 0.0,
  'max': 6000.0,
  'bands': ['MaxFRP', 'FireMask', 'FireMask']
  }

Map.addLayer(collection2.mean(), fireMaskVis, 'MOD14A')
########################################################################

#This funtion add a MCD64A1.006 MODIS Burned Area Monthly Global 500m
collection3 = ee.ImageCollection('MODIS/006/MCD64A1')\
.select('BurnDate')\
.filterDate('2020-01-01', '2020-06-01')\

fireMaskVis2 = {
  'min': 30.0,
  'max': 341.0,
  'palette': ['4e0400', '951003', 'c61503', 'ff1901']
  }

Map.addLayer(collection3.mean(), fireMaskVis2, 'MCD64A1')
########################################################################

# This function gets pre NBR from Sentinel 2 imagery.
imagen1 = ee.ImageCollection('COPERNICUS/S2') \
  .filterBounds(TUN) \
  .filterDate('2020-04-22', '2020-05-23').median() \
  .divide(10000) \
  .select(
  ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12'],
  ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B08A', 'B11', 'B12']
  )
vis2 = {'bands': ['B12', 'B08', 'B04'], 'min': 0.05, 'max': 0.5}
Map.addLayer(imagen1, vis2, 'Sentinel pre')

# Compute NBR from the pre scene.
nbr1 = imagen1.select('B08').subtract(imagen1.select('B11')) \
        .divide(imagen1.select('B08').add(imagen1.select('B11')))

nbrParams = {'palette': ['#d73027', '#f46d43', '#fdae61',
                          '#fee08b', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850']}

Map.addLayer(nbr1, nbrParams, 'NBR PRE')
# This function gets the post NBR from Sentinel 2 imagery.
imagen2 = ee.ImageCollection('COPERNICUS/S2') \
  .filterBounds(TUN) \
  .filterDate('2020-07-01', '2020-07-23').median() \
  .divide(10000) \
  .select(
  ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12'],
  ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B08A', 'B11', 'B12']
  )
vis3 = {'bands': ['B12', 'B08', 'B04'], 'min': 0.05, 'max': 0.5}
Map.addLayer(imagen2, vis3, 'Sentinel post')

# Compute NBR from the pre scene.
nbr2 = imagen2.select('B08').subtract(imagen2.select('B11')) \
        .divide(imagen2.select('B08').add(imagen2.select('B11')))

nbrParams2 = {'palette': ['#d73027', '#f46d43', '#fdae61',
                          '#fee08b', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850']}

Map.addLayer(nbr2, nbrParams2, 'NBR POST')
# Compute the difference burn index dNBR image.

dNBRDifference = (nbr2.subtract(nbr1)).multiply(1000)
difParams = {'min': -2000, 'max': 2000, 'palette': ['ffffff', 'FF0000', 'ff641b', 'ffaf38', 'fff70b', '0ae042', 'acbe4d', '7a8737' ]}

Map.addLayer(dNBRDifference, difParams, 'dNBR')

# Define an Severity style of discrete intervals to apply to the image.

sld_intervals = \
  '<RasterSymbolizer>' + \
    '<ColorMap type="intervals" extended="false" >' + \
      '<ColorMapEntry color="#ffffff" quantity="-500" label="-500"/>' + \
      '<ColorMapEntry color="#7a8737" quantity="-250" label="-250" />' + \
      '<ColorMapEntry color="#acbe4d" quantity="-100" label="-100" />' + \
      '<ColorMapEntry color="#0ae042" quantity="100" label="100" />' + \
      '<ColorMapEntry color="#fff70b" quantity="270" label="270" />' + \
      '<ColorMapEntry color="#ffaf38" quantity="440" label="440" />' + \
      '<ColorMapEntry color="#ff641b" quantity="660" label="660" />' + \
      '<ColorMapEntry color="#FF0000" quantity="2000" label="2000" />' + \
    '</ColorMap>' + \
  '</RasterSymbolizer>';
# Add the image to the map using the color interval schemes.
Map.addLayer(dNBRDifference.sldStyle(sld_intervals), {}, 'dNBR intervals');
########################################################################