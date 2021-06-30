import arcpy.da
arcpy.env.workspace=r"c:\Student\ProgrammingPro\Databases"
try:
    with arcpy.da.SearchCursor("Schools.shp",("Facility","Name"),'"FACILITY"=\'HIGH SCHOOL\'') as cursor:
        for row in sorted(cursor):
            print("High School name:"+row[1])
except Exception as e:
    print ("Error:"+e.args[0])