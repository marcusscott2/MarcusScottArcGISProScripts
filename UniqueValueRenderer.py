import arcpy.mp as map

try:
    aprx = map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Streets and Railroads"):
        for lyr in m.listLayers("Street_Centerlines"):
            if lyr.isFeatureLayer:
                sym = lyr.symbology
                sym.updateRenderer('UniqueValueRenderer')
                sym.renderer.fields = ["Condition"]
                for grp in sym.renderer.groups:
                    for itm in grp.items:
                        if itm.label=='poor':
                            itm.symbol.color=\
                            {'RGB':[255,0,0,100]}
                        elif itm.label=='Fair':
                            itm.symbol.color=\
                            {'RGB':[0,92,230,100]}
                        elif itm.label=='Good':
                            itm.symbol.color=\
                            {'RGB':[38,115,0,100]}

                lyr.symbology = sym
except Exception as e:
    print("Error:" + e.args[0])
