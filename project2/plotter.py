import csv
import matplotlib.pyplot as plt
import math
import sys, re, os

def _main(argv):
    csv_pattern = re.compile('\.csv$')

    if len(argv) != 2: raise Exception('Must specify 2 filenames')
    
    for i, csv_path in enumerate(argv):
        if not os.path.exists(csv_path) or not csv_pattern.search(csv_path):
            raise Exception('File argument %s is not a valid .csv file' % str(i + 1))

    xvals = []
    yvals = []
    # read csv
    with open(argv[0], 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            #         print row
            xvals.append(row[0]); yvals.append(row[1])
            
    yvals_old = []
    with open(argv[1], 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            yvals_old.append(row[1])
                    
    # plot the times
    plt.xlabel('#tiles'); plt.ylabel('Time')
    xpts = [math.sqrt(float(xval)) for xval in xvals]
    # plt.xticks(xpts, [str(sz) for sz in xpts])
    plt.plot(xvals, yvals, 'bo-')
    plt.plot(xvals, yvals_old, 'ro-')
    plt.show()


if __name__ == '__main__':
    _main(sys.argv[1:])
