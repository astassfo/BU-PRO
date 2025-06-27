import ROOT
import math
from array import array
# code that approximates graph of sin(x) with random numbers
c1 = ROOT.TCanvas("c1", "", 600, 500)
numentries = int(input("please enter how many entries you would like to add: ")) # asking user to supply numentries
# making arrays for x and y values with numentries
x = array("f", [0.0] * numentries)
y = array("f", [0.0] * numentries)
# initializing histogram
xyhist = ROOT.TH2F("sin(x)", "", 1000, -10, 10, 1000, -1.1, 1.1)
# filling out x values and corresponding values of sin(x) on y-axis
for i in range(numentries):
    x[i] = ROOT.gRandom.Uniform(-10, 10)
    y[i] = math.sin(x[i])
    xyhist.Fill(x[i], y[i])
# drawing histogram
xyhist.Draw()
# allows histogram to stay open/be interacted with
ROOT.gApplication.Run()