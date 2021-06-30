import arcpy
try:
    arcpy.env.workspace=r"C:\Student\ProgrammingPro\Databases\CityOfSanAntonio.gdb"
    desc=arcpy.da.Describe("Burglary")
    print("The shape type is:"+desc['shapeType'])
    for fld in desc['fields']:
        print("Field:"+fld.name)
        print("Type:"+fld.type)
        print("Length"+str(fld.length))
        ext=desc['extent']
        print("XMin:%f"%(ext.XMin))
        print("YMin:%f"%(ext.YMin))
        print("XMax:%f"%(ext.XMin))
        print("YMax:%f"%(ext.YMax))
except Exception as e:
    print ("Error:"+e.args[0])