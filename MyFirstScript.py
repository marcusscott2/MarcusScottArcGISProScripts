import arcpy
try:
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    for m in aprx.listMaps():
        print("Map:"+ m.name)
        for lyr in m.listLayers ():
            print(""+lyr.name)

except Exception as e:
    print("Error:" + e.args[0])
