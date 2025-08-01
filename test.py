import ROOT
import math

# Create canvas
c = ROOT.TCanvas("c", "", 600, 500)

# Create histograms
hist1 = ROOT.TH1F("GDM", "GDM", 50, 0, 12)
hist2 = ROOT.TH1F("TECH", "TECH", 50, 0, 12)

# Fill first histogram
with open("gdm_data.txt", "r") as file1:
    for line in file1:
        hist1.Fill(float(line))

# Fill second histogram
with open("garrett_data.txt", "r") as file2:
    for line in file2:
        hist2.Fill(float(line))

# Style histograms
hist1.SetLineColor(ROOT.kGreen)
hist2.SetLineColor(ROOT.kRed)

# Draw first histogram and get stats box
hist1.Draw("HIST")
c.Update()
stats1 = hist1.GetListOfFunctions().FindObject("stats")
# stats1.SetX1NDC(0.6)  # move right box
# stats1.SetX2NDC(0.8)
# stats1.SetY1NDC(0.7)
# stats1.SetY2NDC(0.9)

# Draw second histogram and get stats box
hist2.Draw("HIST SAME")
c.Update()
stats2 = hist2.GetListOfFunctions().FindObject("stats")
# stats2.SetTextColor(ROOT.kRed)  # match color
# stats2.SetX1NDC(0.6)  # move left box
# stats2.SetX2NDC(0.8)
# stats2.SetY1NDC(0.5)
# stats2.SetY2NDC(0.7)

# Draw legend
legend = ROOT.TLegend(.15, .7, .3, .85)
legend.AddEntry(hist1, "GDM")
legend.AddEntry(hist2, "TECH")
legend.Draw("SAME")

c.Modified()
c.Update()

ROOT.gApplication.Run()