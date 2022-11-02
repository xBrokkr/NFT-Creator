#    dMMMMb  dMMMMb  .aMMMb  dMP dMP dMP dMP dMMMMb
#   dMP"dMP dMP.dMP dMP"dMP dMP.dMP dMP.dMP dMP.dMP
#  dMMMMK" dMMMMK" dMP dMP dMMMMK" dMMMMK" dMMMMK"
# dMP.aMF dMP"AMF dMP.aMP dMP"AMF dMP"AMF dMP"AMF
#dMMMMP" dMP dMP  VMMMP" dMP dMP dMP dMP dMP dMP



import matplotlib.pyplot as plt
from samila import GenerativeImage, Projection
import math
import random

def f1(x, y):
    result = random.uniform(-1,1) * x**2 - math.sin(y**2) + abs(y-x)
    return result
def f2(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

#loop for saving
for i in range(500): #quantity to be produced
    g = GenerativeImage(f1, f2)
    g.generate(start=-2*math.pi, step=0.03)

    #Types; POLAR, AITOFF, HAMMER, LAMBERT
    g.plot(projection=Projection.POLAR, color="cyan", bgcolor="black", alpha=0.4) #for looking colors: https://matplotlib.org/2.0.1/api/colors_api.html

#If NFT Storage upload is requested, enter your api key.
    g.nft_storage(api_key="")

    #saving area
    fname = f'arts/projectname_{i}' #export
    g.save_image(fname + '.png', depth=5)
    #g.save_data(fname + '.json')