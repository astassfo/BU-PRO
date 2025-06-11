import ROOT
import math

# histogram that compares a uniform histogram distribution to a gaussian dist with mean = 50, std dev = 10

c1 = ROOT.TCanvas("c1", "", 600, 500)
gaushist = ROOT.TH1F("gaussian", "data", 100, 0, 100)
unihist = ROOT.TH1F("uniform", "data", 100, 0, 100)

for i in range(10000):
    gaushist.Fill(ROOT.gRandom.Gaus(50, 10))
    unihist.Fill(ROOT.gRandom.Uniform(0, 100))

gaushist.SetLineColor(ROOT.kBlue)
unihist.SetLineColor(ROOT.kRed)
legend = ROOT.TLegend(.15, .7, .3, .85)
legend.AddEntry(gaushist, "gaussian")
legend.AddEntry(unihist, "uniform")

gaushist.Draw()
unihist.Draw("SAME")
legend.Draw("SAME")

ROOT.gApplication.Run()