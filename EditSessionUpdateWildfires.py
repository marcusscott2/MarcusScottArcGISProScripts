import arcpy

try:
    arcpy.env.workspace = r"C:\Student\ProgrammingPro\Databases\WildlandFires.gdb"
    edit = arcpy.da.Editor(r"C:\Student\ProgrammingPro\Databases\WildlandFires.gdb")
    edit.startEditing(True)
    with arcpy.da.UpdateCursor("FireIncidents", ("CONFIDENCEVALUE", "CONFID_RATING")) as cursor:
        cntr = 1
        for row in cursor:
            # update the confid_rating field
            if row[0] > 40 and row[0] <= 60:
                row[1] = 'GOOD'
            elif row[0] > 60 and row[0] <= 85:
                row[1] = 'BETTER'
            else:
                row[1] = 'BEST'
            cursor.updateRow(row)
            print("Record number " + str(cntr) + " updated")
            cntr = cntr + 1
    edit.stopEditing(True)
except Exception as e:
    print("Error: " + e.args[0])