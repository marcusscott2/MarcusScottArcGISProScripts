import arcpy
try:
    arcpy.env.workspace=r"C:\Student\ProgrammingPro\Databases\WildlandFires.gdb"
    with arcpy.da.UpdateCursor("FireIncidents", ("CONFID_RATING"), 'CONFID_RATING=\'POOR\'') as cursor:
        cntr=1
        for row in cursor:
            cursor.deleteRow()
            print("Record number"+str(cntr)+"deleted")
            cntr=cntr+1
except Exception as e:
    print("Error:"+ e.args[0])
