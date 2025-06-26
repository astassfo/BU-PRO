import ROOT
import math
from array import array

# code that approximates graph of sin(x) with random numbers

c1 = ROOT.TCanvas("c1", "", 600, 500)
numentries = 10000
x = array("f", [0.0] * numentries)
y = array("f", [0.0] * numentries)
xyhist = ROOT.TH2F("sin(x)", "", 100, -10, 10, 100, -1.1, 1.1)

for i in range(numentries):
    x[i] = ROOT.gRandom.Uniform(-10, 10)
    y[i] = math.sin(x[i])
    xyhist.Fill(x[i], y[i])

xyhist.Draw()

ROOT.gApplication.Run()