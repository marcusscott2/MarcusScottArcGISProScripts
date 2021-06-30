import arcpy.mp as map
try:
    aprx = map.ArcGISProject(r"c:\Student\ProgrammingPro\My Projects\ImportedCrime\ImportedCrime.aprx")
    aprx.importDocument(r"c:\Student\ProgrammingPro\Databases\Crime.mxd")
    aprx.save()
    print("Finished importing")

except Exception as e:
    print("Error: " + e.args[0])