import ROOT
import math
# code that puts data from gluing trials into histogram; overlays 3 data sets
c = ROOT.TCanvas("c", "", 600, 500)
hist1 = ROOT.TH1F("GDM", "GDM", 100, 0, 12)
hist2 = ROOT.TH1F("TECH", "TECH", 100, 0, 12)
# open file w/ data
file1 = open("gdm_data.txt", "r")
file2 = open("garrett_data.txt", "r")
# filling histogram with data
for line in file1:
    hist1.Fill(float(line))
file1.close()

hist1.SetLineColor(ROOT.kGreen)
hist1.Draw("HIST")

for line in file2:
    hist2.Fill(float(line))
file2.close()

hist2.SetLineColor(ROOT.kRed)
hist2.Draw("HIST SAME")

legend = ROOT.TLegend(.15, .7, .3, .85)
legend.AddEntry(hist1, "GDM")
legend.AddEntry(hist2, "TECH")

legend.Draw("SAME")

ROOT.gApplication.Run()