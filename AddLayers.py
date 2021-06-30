import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name=="Zoning":
                m.removeLayer(lyr)
except Exception as e:
    print("Error:"+e.args[0])