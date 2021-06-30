import arcpy.mp as map
try:
    aprx = map.ArcGISProject("CURRENT")
    lyt = aprx.listLayouts("Crime")[0]
    for el in lyt.listElements("TEXT_ELEMENT", "Title"):
        el.text="Crime and It\'s Impact on School Test Performance-2009"
        outFile=r"C:\Student\ProgrammingPro\My Projects\ImportedCrime\Layout.pdf"
        lyt.exportToPDF(outFile, image_quality="BEST", embed_fonts=True)
        print("Exported Layout to PDF")
except Exception as e:
    print("Error: " + e.args[0])