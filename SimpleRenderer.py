import arcpy.mp as map

try:
    aprx = map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers("Parcels"):
            if lyr.isFeatureLayer:
                sym = lyr.symbology
                sym.renderer.symbol.applySymbolFromGallery\
                ("Extent Transparent Wide Gray")
                sym.renderer.symbol.color = \
                {'RGB': [255, 255, 190, 25]}
                sym.renderer.symbol.outlineColor = \
                {'CMYK': [25, 50, 75, 25, 100]}
                sym.renderer.symbol.size = 1.0
                lyr.symbology = sym
except Exception as e:
    print("Error" + e.args[0])
