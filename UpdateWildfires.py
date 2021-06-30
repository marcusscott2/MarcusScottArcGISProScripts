import arcpy

try:
    arcpy.env.workspace = r"C:\Student\ProgrammingPro\Databases\WildlandFires.gdb"
    arcpy.AddField_management("FireIncidents", "CONFID_RATING", "TEXT", "10")
    print("CONFID_RATING field added to FireIncidents")
    with arcpy.da.UpdateCursor("FireIncidents", ("CONFIDENCEVALUE", "CONFID_RATING")) as cursor:
        cntr = 1
        for row in cursor:
            # update the confid_rating field
            if row[0] <= 40:
                row[1] = 'POOR'
            elif row[0] > 40 and row[0] <= 60:
                row[1] = 'FAIR'
            elif row[0] > 60 and row[0] <= 85:
                row[1] = 'GOOD'
            else:
                row[1] = 'EXCELLENT'
            cursor.updateRow(row)
            print("Record number " + str(cntr) + " updated")
            cntr = cntr + 1
except Exception as e:
    print("Error: " + e.args[0])