import matplotlib.pyplot as plt
import attractor

"""
plan:
use similar structure to gen_img, but with certain predetermined parameters
(automate) commit to GH with new image - use GH LFS
update page to just be the image
use GH page url for arena api req
"""

# create and save a plot
def plot(points, s, ms = 0.05):
    metadata = {"Title": s}
    x,y = [p[0] for p in points], [p[1] for p in points]
    fig, ax = plt.subplots()
    ax.plot(x,y,'k+', markersize = ms)
    ax.set_axis_off()
    fig.savefig('image.png', dpi=300, metadata=metadata)

# if string is given, save plot of that string
# otherwise find a chaotic string and save plot
def go(s = None):
    while s == None:
        s = attractor.generateAttractor()
        
    out = attractor.generatePoints(s)
    
    plot(out, s)

    return s

go()