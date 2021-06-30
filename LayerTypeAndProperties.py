import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers("Parcels"):
            if lyr.isFeatureLayer:
                if lyr.supports("MINTHRESHOLD"):
                    lyr.minThreshold=50000
                #if lyr.supports("DEFINITIONQUERY"):
                    lyr.definitionQuery="ACRES>5.0"
except Exception as e:
    print("Error"+e.args[0])