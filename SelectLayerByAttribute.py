import arcpy
arcpy.env.workspace="C:/Student/ProgrammingPro/Databases/CityOfSanAntonio.gdb"
try:
    qry='"SVCAREA"=\'North\''
    flayer=arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
    arcpy.SelectLayerByAttribute_management (flayer,"NEW_SELECTION",qry)
    cnt=arcpy.GetCount_management(flayer)
    print("The number of selected records is: "+str(cnt))
except Exception as e:
    print("Error:"+e.args[0])
