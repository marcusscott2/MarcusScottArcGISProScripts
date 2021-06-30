import arcpy.mp as map
try:
    aprx=map.ArcGISProject(r"C:\Student\ProgrammingPro\Chapter2\Ex 2A.aprx")
    geo=aprx.defaultGeodatabase
    tool=aprx.defaultGeodatabase
    home=aprx.homeFolder
    version=aprx.documentVersion
    dtSaved=aprx.dateSaved
    print("Default geodatabase:%s\n Default toolbox:%s\n Home Folder: %s" % (geo,tool,home))
    print("ArcGIS Pro Document version: %s \n Last Date Saved: %s" (version, dtSaved))

except Exception as e:
    print("Error:" + e.args[0])





