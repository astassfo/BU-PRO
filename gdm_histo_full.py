import ROOT

c = ROOT.TCanvas("c", "", 600, 500)
hist = ROOT.TH1F("GDM", "Mass of Glue Deposited (mg)", 12, 4, 10.3)

with open("gdm_data_full.txt", "r") as file:
    for line in file:
        hist.Fill(float(line))

hist.SetLineColor(ROOT.kRed)

legend = ROOT.TLegend(.15, .75, .27, .85)
legend.AddEntry(hist, "GDM")

hist.Draw("HIST")
legend.Draw("SAME")

ROOT.gApplication.Run()