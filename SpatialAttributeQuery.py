import arcpy
arcpy.env.workspace="C:/Student/ProgrammingPro/Databases/CityOfSanAntonio.gdb"
try:
    qry='"DOW"=\'Mon\''
    flayer=arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
    arcpy.SelectLayerByLocation_management(flayer,"COMPLETELY_WITHIN","EdgewoodSD")
    arcpy.SelectLayerByAttribute_management(flayer,"SUBSET_SELECTION",qry)
    cnt=arcpy.GetCount_management(flayer)
    print("The number of selected records is: "+str(cnt))
except Exception as e:
    print("Error:"+e.args[0])