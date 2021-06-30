import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    lyt=aprx.listLayouts("Park Layout")[0]
    mf=lyt.listElements("MAPFRAME_ELEMENT")[0]
    bkmks=mf.map.listBookmarks()
    for bkmk in bkmks:
        mf.zoomToBookmark(bkmk)
        lyt.exportToPDF(r"C:\Student\ProgrammingPro\Scripts"+"\\"+bkmk.name+".pdf")
except Exception as e:
    print("Error:"+e.args[0])
    