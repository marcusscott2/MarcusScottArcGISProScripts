import arcpy
import os
try:
    aprx=arcpy.mp.ArcGISProject(r"c:\Student\ProgrammingPro\Chapter6\MapSeries\MapSeries.aprx")
    arcpy.env.workspace=r"C:\Student\ProgrammingPro\Databases\MapBook.gdb"

    outDir=r"C:\Student\ProgrammingPro\Chapter6"
    finalpdf_filename=outDir+r"\MapSeries.pdf"
    if os.path.exists(finalpdf_filename):
        os.remove(finalpdf_filename)
    finalPdf=arcpy.mp.PDFDocumentCreate(finalpdf_filename)

    #Add the title page to the pdf
    print("Adding the title page\n")
    finalPdf.appendPages(outDir+r"\TitlePage.pdf")

    #Add the index map to the pdf
    print("Adding the index page\n")
    finalPdf.appendPages(outDir+r"\MapIndex.pdf")

    with arcpy.da.SearchCursor("GridIndexFeatures", ["PageName","SHAPE@"],sql_clause=(None, 'ORDER BY PageName ASC')) as cursor:
        for row in cursor:
            print(row[0])
            lyt=aprx.listLayouts()[0]
            mf=lyt.listElements('MAPFRAME_ELEMENT',"Detail Map Map Frame")[0]
            mf.panToExtent(row[1].extent)

            print("Creating the map series page\n")
            temp_Filename=outDir+r"\tempMS.pdf"
            if os.path.exists(temp_Filename):
                os.remove(temp_Filename)

            lyt.exportToPDF(temp_Filename)

            print("Appending the map series\n")
            finalPdf.appendPages(temp_Filename)

        finalPdf.updateDocProperties(pdf_open_view="USE_THUMBS",pdf_layout="SINGLE_PAGE")
        finalPdf.saveAndClose()

        #remove the temporary data driven pages file
        if os.path.exists(temp_Filename):
            print("Removing the temporary map series file")
            os.remove(temp_Filename)

except Exception as e:
    print("Error:"+e.args[0])
