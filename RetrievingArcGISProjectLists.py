import arcpy.mp as map

try:
    aprx = map.ArcGISProject(r"C:\Student\ProgrammingPro\Chapter2\Ex 2A.aprx")
    for m in aprx.listMaps("Street*"):
        print("Map:" + m.name)
        for lyr in m.listLayers():
            print("" + lyr.name)

except Exception as e:
    print("Error:" + e.args[0])
