import argparse
import matplotlib.pyplot as plt

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXY"

letterToNumber = lambda x: 0.1*(LETTERS.index(x) - 12)

def nextVal( x, y, params ):
    a,b,c,d,e,f = params
    return a + b*x + c*x*x + d*x*y + e*y + f*y*y

def generatePoints(s, num_iter=100000, init=(0.05, 0.05)):
    xparams = list(map(letterToNumber, s[:6]))
    yparams = list(map(letterToNumber, s[6:]))
    
    out = [init]
    x,y = init
    
    for k in range(num_iter):
        x,y = nextVal(x,y,xparams), nextVal(x,y,yparams)
        out.append((x,y))
    
    return out

def main():
    parser = argparse.ArgumentParser(prog="gen_img.py", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('coefficient_string',
                        nargs='+',
                        help='coefficient string for quadratic equations')
    parser.add_argument('filename',
                        nargs='+',
                        help='filename for generated png image (no extension needed)')
    parser.add_argument('-m', '--marker_size',
                        nargs='+',
                        type=float,
                        default=[0.08],
                        metavar='',
                        help='marker size for plotted points \n \
default value: 0.08')
    parser.add_argument('-c', '--color',
                        nargs='+',
                        metavar='',
                        choices=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'],
                        default=['k'],
                        help='COLOR OPTIONS: \n \
    b 	  blue \n \
    g 	  green \n \
    r 	  red \n \
    c 	  cyan \n \
    m 	  magenta \n \
    y 	  yellow \n \
    k 	  black \n \
    w 	  white \n \
default value: k')
    parser.add_argument('-p', '--point_shape',
                        nargs='+',
                        default=['+'],
                        metavar='',
                        choices=['.', ',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','D','d','|','_'],
                        help='POINT SHAPE OPTIONS: \n \
    .     point marker \n \
    ,     pixel marker \n \
    o     circle marker \n \
    v     triangle_down marker \n \
    ^ 	  triangle_up marker \n \
    < 	  triangle_left marker \n \
    > 	  triangle_right marker \n \
    1 	  tri_down marker \n \
    2 	  tri_up marker \n \
    3 	  tri_left marker \n \
    4 	  tri_right marker \n \
    8 	  octagon marker \n \
    s 	  square marker \n \
    p 	  pentagon marker \n \
    P 	  plus (filled) marker \n \
    * 	  star marker \n \
    h 	  hexagon1 marker \n \
    H 	  hexagon2 marker \n \
    + 	  plus marker \n \
    x 	  x marker \n \
    X 	  x (filled) marker \n \
    D 	  diamond marker \n \
    d 	  thin_diamond marker \n \
    | 	  vline marker \n \
    _ 	  hline marker \n \
default value: +')
    parser.add_argument('-i', '--iterations',
                        nargs='+',
                        type=int,
                        metavar='',
                        default=[100000],
                        help='number of iterations (points) \n \
default value: 100,000')
    parser.add_argument('-d', '--dpi',
                        nargs='+',
                        type=int,
                        metavar='',
                        default=[300],
                        help='dpi for saved image \n \
default value: 300')
    args = parser.parse_args()
    points = generatePoints(args.coefficient_string[0], num_iter=args.iterations[0])
    metadata = {"Title": args.coefficient_string[0]}
    x,y = [p[0] for p in points], [p[1] for p in points]
    fig, ax = plt.subplots()
    # figure out how to have more color options? & change background color
    fmtstr = args.color[0] + args.point_shape[0]
    ax.plot(x,y,fmtstr, markersize = args.marker_size[0])
    ax.set_axis_off()
    fn_with_extension = args.filename[0] + ".png"
    fig.savefig(fn_with_extension, dpi=args.dpi[0], metadata=metadata)

if __name__ == "__main__":
    main()