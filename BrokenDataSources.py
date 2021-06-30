import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    aprx.updateConnectionProperties(r"C:\Student\ProgrammingPro\Databases\Data\OldData\CityOfSanAntonio.gdb",
                                    "C:\Student\ProgrammingPro\Databases\CityOfSanAntonio.gdb")
    aprx.save()
    #m=aprx.listMaps("Crime*")[0]
    #for lyr in m.listBrokenDataSources():
    #    print(lyr.name)
    #lyrs=aprx.listBrokenDataSources()
    #for lyr in lyrs:
    #    print(lyr.name)
except Exception as e:
    print("Error:"+e.args[0])
