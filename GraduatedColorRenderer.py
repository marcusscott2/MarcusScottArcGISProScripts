import arcpy.mp as map
try:
    aprx=map.ArcGISProject("CURRENT")
    for m in aprx.listMaps("Map"):
        for lyr in m.listLayers("Parcels"):
            if lyr.isFeatureLayer:
                sym=lyr.symbology
                sym.updateRenderer('GraduatedColorsRenderer')
                sym.renderer.classificationField="ACRES"
                sym.renderer.classificationMethod="Natural Breaks"
                sym.renderer.breakCount=5
                sym.renderer.colorRamp= \
                aprx.listColorRamps("Reds (5 Classes)")[0]
                lyr.symbology=sym
except Exception as e:
    print("Error"+e.args[0])

