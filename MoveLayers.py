import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Streets and Railroads"):
        for lyr in m.listLayers():
            if lyr.name=='Street_Centerlines':
                insertLayer=lyr
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name=="Creek and Streams":
                refLayer=lyr
    m.insertLayer(refLayer,insertLayer,"BEFORE")
except Exception as e:
    print("Error"+e.args[0])
    