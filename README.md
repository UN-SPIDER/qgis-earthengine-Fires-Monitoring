# Monitoring wildfires with the Google Earth Engine plugin for QGIS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<figure><img src='img\S_2_fires.png' alt='Forest Fires in Honduras, April 2020. Image: Copernicus.' style="align:center; width:100%;"></img><figcaption>Forest fires in Honduras in 2020. Image: ESA.</figcaption><figure>
<hr>
  
## 1. Description

The following is an example of using Google Earth Engine [API Documentation](https://developers.google.com/earth-engine/) via the [Google Earth Engine plugin for QGIS](https://github.com/gee-community/qgis-earthengine-plugin) for monitoring and tracking wildfires in QGIS. This script adapts examples for the use of GEE in QGIS from the [Google Earth Engine plugin](https://github.com/gee-community/qgis-earthengine-plugin/tree/master/examples), [qgis-earthengine-examples](https://github.com/giswqs/qgis-earthengine-examples) and [Earth Engine API](https://github.com/google/earthengine-api/tree/master/python/examples) repositories. In addition, it also makes use of the [UN-SPIDER Recommended Practice on burn severity mapping](http://www.un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity-mapping).

## 2. Setup

To use the [script](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/Python/GEE_QGIS_TUNISIA.py) for monitoring wildfires provided below, you will need a [Google Earth Engine account](https://earthengine.google.com/signup/) and a [QGIS](https://qgis.org/) installation. 

### 2.1. Install the Google Earth Engine plugin for QGIS

To connect to Google Earth Engine from within QGIS, install the [Google Earth Engine Plugin for QGIS](https://gee-community.github.io/qgis-earthengine-plugin/). To do this, go to the top menu of QGIS and click on **Add-ons> Manage and install add-ons ...**. In the search box, search for "Google Earth", select the plugin and install it. Once installed, the plugin will verify whether you are authenticated to use GEE. If that is not the case yet, you will be asked to authenticate with your credentials.
<figure><img src='img\gee_QGIS.png' alt='GEE plugin' style="align:center; width:100%;"></img><figcaption> GEE Plugin</figcaption><figure>
<hr>

### 2.2. Add more basemaps to QGIS
It can be helpful to have additional basemaps available for working with QGIS. To add basemaps, you can make use of scripts developed by the QGIS community. For instance: 
* Open the Python Console in QGIS and import this [Python script](https://github.com/klakar/QGIS_resources/blob/master/collections/Geosupportsystem/python/qgis_basemaps.py).
* Click the *Run script* button on the Python Console to execute the script. This will add many basesmaps as XYZ tiles to QGIS. Select and double-click any basemap under XYZ tiles to add it to the QGIS canvas. See the screenshot below.
Alternatively, you can install the QGIS [QuickMapServices](https://plugins.qgis.org/plugins/quick_map_services/) plugin. After installing the plugin, go to _QGIS_ -- _Web_ --_QuickMapServices_ -- _Settings_ -- _More services_ -- _Get contributed pack_ -- _Save_. 

![QGIS Basemaps](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/img/qgis_gee_3.png)

### 2.3. Access Google Earth Engine from QGIS

Once installed and authenticated, you can access the Google Earth Engine plugin for QGIS from the QGIS Python Console to write and run scripts that make use of Google Earth Engine. 
To test if the plugin is installed and authenticated correctly, type the following in the QGIS Python Console:

![Check Install](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/img/hello_w.PNG)

Note that QGIS projects that contain Earth Engine layers can be saved. In this case, the code required to connect to Google Earth Engine is stored in a QGIS project and used to reinitialize these layers when the project is loaded again. Currently, this only works when the plugin is installed in the QGIS installation where these layers are loaded.

Demo:

![qgis-gee-demo](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/img/strm_basem.gif)

The above code asks Google Earth Engine for an image and adds it as an XYZ tile layer to the QGIS canvas.

## 3. Script for wildfire monitoring
The following script uses Earth observation data products available in the Google Earth Engine Data Catalog to identify fire locations and assess the burn severity of an area after a fire.
* Active fire detection product: [FIRMS: Fire Information for Resource Management System](https://developers.google.com/earth-engine/datasets/catalog/FIRMS)
* Burned area products:  
    * [FireCCI51: MODIS Fire_cci Burned Area Pixel product, version 5.1](https://developers.google.com/earth-engine/datasets/catalog/ESA_CCI_FireCCI_5_1)  
    * [MOD14A1.006: Terra Thermal Anomalies & Fire Daily Global 1km](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD14A1)
    * [MCD64A1.006 MODIS Burned Area Monthly Global 500m](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MCD64A1)

In addition, the script processes Sentinel-2 imagery to identify burn severity. For more details, please see the [UN-SPIDER Recommended Practice on burn severity mapping](http://www.un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity-mapping).

**Running the script**
To import the [Python script](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/Python/GEE_QGIS_TUNISIA.py) in QGIS, download it to your hard drive, open the QGIS Python Console and then select it there. Click the "run script" button to execute the script. You can now inspect the results on the QGIS canvas.

The script is also available as a Jupyter Notebook.
* [Jupyter Notebook](https://github.com/Alexanderariza/qgis-earthengine-Fires-Monitoring/blob/master/qgis-earthengine-Fires-Monitoring.ipynb)

<i><p style="text-align:right;">The compilation has been created to support the [UN-SPIDER Knowledge Portal](http://www.un-spider.org/).
