from io_scene_usdz.crate_file import *

usdcFile = "/Users/andrewbeers/git/projects/BlenderUSDZ/testing/files/reference/converted.usdc"
outputFile = "/Users/andrewbeers/git/projects/BlenderUSDZ/testing/files/reference/result.usdc"
file = open(usdcFile, 'rb')
crate = CrateFile(file)
usdData = crate.readUsd()
file.close()




print("Python - Exporting...")
crateFile = open(outputFile, 'wb')
output_crate = CrateFile(crateFile)
output_crate.writeUsd(usdData)
crateFile.close()

print("Python - DONE")