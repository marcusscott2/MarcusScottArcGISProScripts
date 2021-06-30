import arcpy.mp  as map
try:
    aprx=map.ArcGISProject(r"C:\Student\ProgrammingPro\Chapter2\Ex 2A.aprx")
    aprx.saveACopy(r"C:\Student\ProgrammingPro\Chapter2\Ex 2A Copy.aprx")
    print("Finished saving a copy of the file")

except Exception as e:
    print("Error:" + e.args[0])