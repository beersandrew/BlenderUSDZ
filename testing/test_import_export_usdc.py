from io_scene_usdz.crate_file import *

usdcFile = "/Users/andrewbeers/git/projects/BlenderUSDZ/testing/files/convertedNeedleGeometry.usdc"
outputFile = "/Users/andrewbeers/git/projects/BlenderUSDZ/testing/files/python.usdc"
file = open(usdcFile, 'rb')
crate = CrateFile(file)
usdData = crate.readUsd()
file.close()


crateFile = open(outputFile, 'wb')
output_crate = CrateFile(crateFile)
output_crate.writeUsd(usdData)
crateFile.close()