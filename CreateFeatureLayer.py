import arcpy
arcpy.env.workspace="C:/Student/ProgrammingPro/Databases/CityOfSanAntonio.gdb"
try:
    flayer=arcpy.MakeFeatureLayer_management ("Burglary","Burglary_Layer")
    tView=arcpy.MakeTableView_management("Crime2009Table","Crime2009TView")
except Exception as e:
    print("Error:"+e.args[0])