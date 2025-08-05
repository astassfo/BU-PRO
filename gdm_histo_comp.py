import ROOT
# code that puts data from gluing trials into histogram; overlays 3 data sets
c = ROOT.TCanvas("c", "", 600, 500)
hist1 = ROOT.TH1F("GDM", "Normalized Mass of Glue Deposited (mg)", 100, 2, 11)
hist2 = ROOT.TH1F("TECH", "TECH", 100, 2, 11)
# filling histogram with data
with open("gdm_data_part.txt", "r") as file1:
    for line in file1:
        hist1.Fill(float(line))

hist1.SetLineColor(616) # magenta
hist1.Scale(1.0 / hist1.Integral())
hist1.Draw("HIST")

with open("garrett_data.txt", "r") as file2:
    for line in file2:
        hist2.Fill(float(line))

hist2.SetLineColor(418) # green
hist2.Scale(1.0 / hist2.Integral())
hist2.Draw("HIST SAME")

legend = ROOT.TLegend(.15, .7, .3, .85)
legend.AddEntry(hist1, "GDM")
legend.AddEntry(hist2, "TECH")

legend.Draw("SAME")

ROOT.gApplication.Run()