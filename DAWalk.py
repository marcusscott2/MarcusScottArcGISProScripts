import arcpy
import os
try:
    arcpy.env.workspace=r"C:\Student\ProgrammingPro\Databases"
    for dirpath, dirnames,filenames in arcpy.da.Walk(arcpy.env.workspace, datatype="FeatureClass"):
        for filename in filenames:
            print(os.path.join(dirpath,filename))
except Exception as e:
    print("Error:"+e.args[0])