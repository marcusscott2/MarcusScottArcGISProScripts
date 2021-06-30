import arcpy.mp as map
try:
    #Exercise 3C
    aprx = map.ArcGISProject("CURRENT")
    m = aprx.listMaps("Map")[0]
    parcelLyr = m.listLayers("Parcels")[0]

    lyt = aprx.listLayouts("Park Layout")[0]
    mf = lyt.listElements("MAPFRAME_ELEMENT")[0]

    ext = mf.getLayerExtent(parcelLyr,False)
    mf.panToExtent(ext)
except Exception as e:
    print("Error: " + e.args[0])