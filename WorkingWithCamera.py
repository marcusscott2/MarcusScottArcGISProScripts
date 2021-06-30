import arcpy.mp as map
try:
    aprx = map.ArcGISProject("CURRENT")
    m = aprx.listMaps("Union City")[0]

    lyt = aprx.listLayouts("Union City Layout")[0]
    mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
    camera = mf.camera

    if camera.mode == "LOCAL":  #check to make sure it's 3D
        camera.pitch = -90.00
        camera.roll = 0.00
        camera.heading = 0.00

except Exception as e:
    print("Error: " + e.args[0])