import ROOT
import math
from array import array

# appx area of quarter circ w monte carlo method, also outputs png

numentries = 200000
rngarray = array("f", [0.0] * numentries)
for i in range(numentries):
    rngarray[i] = ROOT.gRandom.Uniform()

canv = ROOT.TCanvas("c1", "", 500, 500)
histo = ROOT.TH2F("circle", "", 100, 0, 1, 100, 0, 1)
ROOT.gStyle.SetPalette(ROOT.kCool)
ROOT.gStyle.SetOptStat(0)


circ = 0
for i in range(0, numentries - 1, 2):
    if rngarray[i]**2 + rngarray[i+1]**2 <= 1:
        circ += 1
        histo.Fill(rngarray[i], rngarray[i+1])

area = circ/(numentries/2) #dividing numentries by 2 b/c iterated over every other numentry in for loop
print(area)
histo.Draw()

ROOT.gApplication.Run()