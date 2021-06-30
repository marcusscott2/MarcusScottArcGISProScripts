import arcpy
arcpy.env.workspace="C:/Student/ProgrammingPro/Databases/CityOfSanAntonio.gdb"
try:
    flayer=arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
    arcpy.SelectLayerByLocation_management (flayer,"WITHIN_A_DISTANCE","EdgewoodSD","1 MILES")
    arcpy.CopyFeatures_management
    (flayer,"EDGEWOOD_BURGLARIES")
    cnt=arcpy.GetCount_management(flayer)
    print("The number of selected records is: "+str(cnt))
except Exception as e:
    print("Error:"+e.args[0])