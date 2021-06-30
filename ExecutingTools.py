import arcpy
from arcpy import env
env.workspace=r"C:\Student\ProgrammingPro\Databases\Trippville_GIS.gdb"
env.overwriteOutput=True
try:
    arcpy.Buffer_analysis("Lakes and Ponds", "Buffered_Water", "250 Feet", 'FULL', 'ROUND', 'All')
    arcpy.MakeFeatureLayer_management("Parcels", "Parcels_FL")
    arcpy.SelectLayerByLocation_management("Parcels_FL", "intersect", "Buffered_Water")
    arcpy.CopyFeatures_management("Parcels_FL", "Parcels_NearWaterBodies")
except Exception as e:
    print("Error:"+e.args[0])
