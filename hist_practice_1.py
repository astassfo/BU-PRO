import ROOT
import math
# histogram that compares a uniform histogram distribution to a gaussian dist with mean = 50, std dev = 10
c1 = ROOT.TCanvas("c1", "", 600, 500) # initializing canvas
gaushist = ROOT.TH1F("gaussian", "data;x;y", 100, 0, 100) # data = histo name, x = x-axis name, y = y-axis name (creative)
unihist = ROOT.TH1F("uniform", "data;x;y", 100, 0, 100)
# taking 10,000 random numbers to fill out both gaussian and uniform datasets
for i in range(10000):
    gaushist.Fill(ROOT.gRandom.Gaus(50, 10))
    unihist.Fill(ROOT.gRandom.Uniform(0, 100))
# normalizing the histograms
gaushist.Scale(1.0 / gaushist.Integral())
unihist.Scale(1.0 / unihist.Integral())
# setting histogram colors and making legend
gaushist.SetLineColor(ROOT.kBlue)
unihist.SetLineColor(ROOT.kRed)
legend = ROOT.TLegend(.15, .7, .3, .85)
legend.AddEntry(gaushist, "gaussian")
legend.AddEntry(unihist, "uniform")
# drawing histograms and legend on same plot
gaushist.Draw("HIST") # argument "HIST" to make sure appears as histogram instead of collection of points
unihist.Draw("HIST SAME")
legend.Draw("SAME")
# write histograms to a file
f = ROOT.TFile("histo.root", "RECREATE") # recreate to override existing histo.root
f.cd() # making sure f is current directory
gaushist.Write()
unihist.Write()
f.Close()
# reading back data from histo.root
r = ROOT.TFile("histo.root", "READ")
# prompting user to give name of histogram they are looking for in histo.root
fhist = input("enter the histogram you are trying to locate: ")
lookingfor = r.Get(fhist) # if fhist not in histo.root, then it will hold value "None"
# if statement to see if fhist in histo.root; responds to user if found or not
if lookingfor: 
    print("your histogram was found in histo.root")
else:
    print("your histogram was not found in hist.root")
# listing elements of file
r.ls()
# closing file
r.Close()
# allows histogram to stay open/be interacted with
ROOT.gApplication.Run()
# NOTE: histogram will only appear in python terminal AFTER response to fhist input