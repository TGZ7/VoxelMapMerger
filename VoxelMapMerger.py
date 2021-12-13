from PIL import Image
'''
Put this script in the same folder with a folder "images" with the VoxelMap images
'''
regions = []

for i in range(-200,200):
    y = i
    for i in range(-200,200):
        try:
            filename = "images/" + str(i) + "," + str(y) + ".png"
            im = Image.open(filename)
            regions.append((i,y))
        except IOError:
            pass

minRegion, maxRegion = min(regions) , max(regions)

minCoords, maxCoords = (minRegion[0]*256,minRegion[1]*256), (maxRegion[0]*256,maxRegion[1]*256)

totalRegionResolution = (maxRegion[0]-minRegion[0]+1,maxRegion[1]-minRegion[1]+1)
pixelResolution = (totalRegionResolution[0]*256,totalRegionResolution[1]*256)

canvas = Image.new("RGB", pixelResolution, "black")
canvas.format = "PNG"

for j in regions:
    filename = "images/" + str(j[0]) + "," + str(j[1]) + ".png"
    openRegion = Image.open(filename)
    canvas.paste(openRegion, ((j[0]-minRegion[0])*256,(j[1]-minRegion[1])*256))

canvas.show()
canvas.save('compiledMap.png')