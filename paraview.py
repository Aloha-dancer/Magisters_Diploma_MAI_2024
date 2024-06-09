import paraview
from paraview.simple import *


spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')
data_set_time = 0
timeKeeper1 = GetTimeKeeper()

# get active source.
slice1 = GetActiveSource()

# get display properties
slice1Display = GetDisplayProperties(slice1, view=spreadSheetView1)
animeScene = GetAnimationScene()

while data_set_time <= 1:
    animeScene.AnimationTime = data_set_time
    csv_time = str(data_set_time).replace('.', '')
    ExportView(f'/mnt/c/Users/popov/Documents/openFOAM/test_data/gpu_{csv_time}.csv', view = spreadSheetView1)
    data_set_time += 1


