import ROOT
import math
# code that puts data from gluing trials into histogram; overlays 3 data sets
c = ROOT.TCanvas("c", "", 600, 500)
hist1 = ROOT.TH1F("GDM", "GDM", 50, 0, 10)
# open file w/ data
file1 = open("gdm_data.txt", "r")
# filling histogram with data
for line in file1:
    line_flt = float(line)
    hist1.Fill(line_flt)

hist1.Draw("HIST")

ROOT.gApplication.Run()