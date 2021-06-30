import arcpy.mp as map
try:
    aprx=map.ArcGISProject(r"c:\Student\ProgrammingPro\Chapter2\Ex 2A.aprx")
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers("C*"):
            print(lyr.name)
except Exception as e:
    print("Error:"+e.args[0])
