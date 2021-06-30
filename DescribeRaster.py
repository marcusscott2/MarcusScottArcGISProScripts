import arcpy
try:
    arcpy.env.workspace=r"C:\Student\ProgrammingPro\Databases"
    desc=arcpy.da.Describe("AUSTIN_EAST_NW.sid")
    ext=desc['extent']
    print("XMin:%f"%(ext.XMin))
    print("YMin:%f"%(ext.YMin))
    print("XMax:%f"%(ext.XMin))
    print("YMax:%f"%(ext.YMax))
    sr=desc['spatialReference']
    print(sr.name)
    print(sr.type)
except Exception as e:
    print("Error:"+e.args[0])