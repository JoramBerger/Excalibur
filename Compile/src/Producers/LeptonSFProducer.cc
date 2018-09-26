#include "Excalibur/Compile/interface/Producers/LeptonSFProducer.h"

#include <boost/algorithm/string.hpp>
#include "TH2.h"
#include "TGraphAsymmErrors.h"

/*
taken from https://twiki.cern.ch/twiki/bin/view/Main/EGammaScaleFactors2012

This producer contains some un-intuitive programming constructs, which are
necessary to account for the different formats of the ROOT files containing
the scale factors (different axes, binning in absolute eta)

needed tags:
- LeptonIDSFVariation           Vary IDSF by error. Choices: up, down, None
- LeptonIsoSFVariation          Vary IsoSF by error. Choices: up, down, None
- LeptonTrackingSFVariation     Vary TrackingSF by error. Choices: up, down, None
- LeptonTriggerSFVariation      Vary TriggerSF by error. Choices: up, down, None

maybe also relevant:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/MultivariateElectronIdentification (SF files for MVA
ID)
https://twiki.cern.ch/twiki/bin/view/CMSPublic/DiLeptonAnalysis#Efficiencies_and_Scale_Factors
https://twiki.cern.ch/twiki/bin/viewauth/CMS/DileptonTriggerResults
http://lovedeep.web.cern.ch/lovedeep/WORK13/TnPRun2012ReReco_2013Oct28/effiPlots.html
*/

//////////////
// LeptonSF //
//////////////

std::string LeptonSFProducer::GetProducerId() const { return "LeptonSFProducer"; }

void LeptonSFProducer::Init(ZJetSettings const& settings)
{
   
    
}

void LeptonSFProducer::Produce(ZJetEvent const& event,
                                 ZJetProduct& product,
                                 ZJetSettings const& settings) const
{
    
}

////////////////
// LeptonIDSF //
////////////////

std::string LeptonIDSFProducer::GetProducerId() const { return "LeptonIDSFProducer"; }

void LeptonIDSFProducer::Init(ZJetSettings const& settings)
{
    m_sffile = settings.GetLeptonIDSFRootfile();
    m_etaonly = settings.GetLeptonSFetaonly();
    double error_multiplier = 0.;
    if (settings.GetLeptonIDSFVariation() == "up") {
        LOG(WARNING) << "LeptonIDSFProducer: varying scale factor UP one sigma";
        error_multiplier = 1.;
    } else if (settings.GetLeptonIDSFVariation() == "down") {
        LOG(WARNING) << "LeptonIDSFProducer: varying scale factor DOWN one sigma";
        error_multiplier = -1.;
    }
    if(settings.GetChannel() == "mm"){
        histoname = settings.GetLeptonIDSFHistogramName();
    }
    else{
        LOG(ERROR) << "LeptonIsoSFProducer not implemented for this channel";
    }
    
    m_etabins = &m_xbins;
    m_ptbins = &m_ybins;
    if (m_etaonly)
        m_absoluteeta = false;
    //m_reversed_axes = true;
    
    // Get file
    LOG(INFO) << "Loading lepton scale factors for ID " << m_id << ": File " << m_sffile
              << ", Histogram " << histoname;
    TFile file(m_sffile.c_str(), "READONLY");
    TH2F* sfhisto = (TH2F*)file.Get(histoname.c_str());

   // Get the pT and eta bin borders
    for (int ix = 0; ix <= sfhisto->GetNbinsX(); ++ix)
        m_xbins.emplace_back(2 * sfhisto->GetXaxis()->GetBinCenter(ix) -
                             sfhisto->GetXaxis()->GetBinLowEdge(ix));
    for (int iy = 0; iy <= sfhisto->GetNbinsY(); ++iy)
        m_ybins.emplace_back(2 * sfhisto->GetYaxis()->GetBinCenter(iy) -
                             sfhisto->GetYaxis()->GetBinLowEdge(iy));
    // Fill the m_sf array with the values from the root histo
    for (int ix = 1; ix <= sfhisto->GetNbinsX(); ix++) {
        for (int iy = 1; iy <= sfhisto->GetNbinsY(); iy++) {
            m_sf[0][ix - 1][iy - 1] = static_cast<float>(
                sfhisto->GetBinContent(ix, iy) + error_multiplier * sfhisto->GetBinError(ix, iy));
        }
    }
    delete sfhisto;
    file.Close();

}

void LeptonIDSFProducer::Produce(ZJetEvent const& event,
                                 ZJetProduct& product,
                                 ZJetSettings const& settings) const
{
    if(product.m_zValid){
        product.m_weights["leptonIDSFWeight"] =
                //some old SF files already include the inverse, make sure you use them the right way!
                //GetScaleFactor(0, *product.m_zLeptons.first) * GetScaleFactor(0, *product.m_zLeptons.second);
                1/GetScaleFactor(0, *product.m_zLeptons.first) * 1/GetScaleFactor(0, *product.m_zLeptons.second);
        product.m_weights["mu1IDSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.first);
        product.m_weights["mu2IDSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.second);
    }
    else
        product.m_weights["leptonIDSFWeight"] = 0;
}

/////////////////
// LeptonIsoSF //
/////////////////

std::string LeptonIsoSFProducer::GetProducerId() const { return "LeptonIsoSFProducer"; }

void LeptonIsoSFProducer::Init(ZJetSettings const& settings)
{
    m_sffile = settings.GetLeptonIsoSFRootfile();
    m_etaonly = settings.GetLeptonSFetaonly();
    double error_multiplier = 0.;
    if (settings.GetLeptonIsoSFVariation() == "up") {
        LOG(WARNING) << "LeptonIsoSFProducer: varying scale factor UP one sigma";
        error_multiplier = 1.;
    } else if (settings.GetLeptonIsoSFVariation() == "down") {
        LOG(WARNING) << "LeptonIsoSFProducer: varying scale factor DOWN one sigma";
        error_multiplier = -1.;
    }
    
    if(settings.GetChannel() == "mm"){
        histoname = settings.GetLeptonIsoSFHistogramName();
    }
    else{
        LOG(ERROR) << "LeptonIsoSFProducer not implemented for this channel";
    }

    m_etabins = &m_xbins;
    m_ptbins = &m_ybins;
    if (m_etaonly)
        m_absoluteeta = false;
    //m_reversed_axes = true;
    
    // Get file
    LOG(INFO) << "Loading lepton scale factors for Isolation " << m_id << ": File " << m_sffile
              << ", Histogram " << histoname;
    TFile file(m_sffile.c_str(), "READONLY");
    TH2F* sfhisto = (TH2F*)file.Get(histoname.c_str());

    // Get the pT and eta bin borders
    for (int ix = 0; ix <= sfhisto->GetNbinsX(); ++ix)
        m_xbins.emplace_back(2 * sfhisto->GetXaxis()->GetBinCenter(ix) -
                             sfhisto->GetXaxis()->GetBinLowEdge(ix));
    for (int iy = 0; iy <= sfhisto->GetNbinsY(); ++iy)
        m_ybins.emplace_back(2 * sfhisto->GetYaxis()->GetBinCenter(iy) -
                             sfhisto->GetYaxis()->GetBinLowEdge(iy));
    // Fill the m_sf array with the values from the root histo
    for (int ix = 1; ix <= sfhisto->GetNbinsX(); ix++) {
        for (int iy = 1; iy <= sfhisto->GetNbinsY(); iy++) {
            m_sf[0][ix - 1][iy - 1] = static_cast<float>(
                sfhisto->GetBinContent(ix, iy) + error_multiplier * sfhisto->GetBinError(ix, iy));
        }
    }
    delete sfhisto;
    file.Close();
}

void LeptonIsoSFProducer::Produce(ZJetEvent const& event,
                                 ZJetProduct& product,
                                 ZJetSettings const& settings) const
{
    if(product.m_zValid){
        product.m_weights["mu1IsoSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.first);
        product.m_weights["mu2IsoSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.second);
        product.m_weights["leptonIsoSFWeight"] =
                //some old SF files already include the inverse, make sure you use them the right way!
                //GetScaleFactor(0, *product.m_zLeptons.first) * GetScaleFactor(0, *product.m_zLeptons.second);
                1/GetScaleFactor(0, *product.m_zLeptons.first) * 1/GetScaleFactor(0, *product.m_zLeptons.second);
    }
    else
        product.m_weights["leptonIsoSFWeight"] = 0;
}

//////////////////////
// LeptonTrackingSF //
//////////////////////

std::string LeptonTrackingSFProducer::GetProducerId() const { return "LeptonTrackingSFProducer"; }

void LeptonTrackingSFProducer::Init(ZJetSettings const& settings)
{
    m_sffile = settings.GetLeptonTrackingSFRootfile();
    double error_multiplier = 0.;
    if (settings.GetLeptonTrackingSFVariation() == "up") {
        LOG(WARNING) << "LeptonTrackingSFProducer: varying scale factor UP one sigma";
        error_multiplier = 1.;
    } else if (settings.GetLeptonTrackingSFVariation() == "down") {
        LOG(WARNING) << "LeptonTrackingSFProducer: varying scale factor DOWN one sigma";
        error_multiplier = -1.;
    }
    
    if(settings.GetChannel() == "mm"){
        histoname = settings.GetLeptonTrackingSFHistogramName();
    }
    else{
        LOG(ERROR) << "LeptonTrackingSFProducer not implemented for this channel";
    }
    
    m_etabins = &m_xbins;
    m_ptbins = &m_ybins;
    m_absoluteeta = false;
    //m_reversed_axes = true;

    // Get file
    LOG(INFO) << "Loading lepton scale factors for Tracking: File " << m_sffile
              << ", Histogram " << histoname;
    TFile file(m_sffile.c_str(), "READONLY");
    TGraphAsymmErrors *sfhisto = (TGraphAsymmErrors*)file.Get(histoname.c_str());

    // Get the pT and eta bin borders
    m_xbins.emplace_back(sfhisto->GetX()[0] - sfhisto->GetErrorXlow(0));
    for (int ix = 0; ix < sfhisto->GetN(); ++ix){
        m_xbins.emplace_back(sfhisto->GetX()[ix] + sfhisto->GetErrorXhigh(ix));
    }
    m_ybins.emplace_back(0);
    m_ybins.emplace_back(10000);
    
    // Fill the m_sf array with the values from the root histos
    for (int ix = 1; ix <= sfhisto->GetN(); ix++) {
        m_sf[0][ix-1][0] = static_cast<float>(sfhisto->GetY()[ix-1] + error_multiplier * sfhisto->GetErrorY(ix-1));
    }
    delete sfhisto;
    file.Close();
}

void LeptonTrackingSFProducer::Produce(ZJetEvent const& event,
                                 ZJetProduct& product,
                                 ZJetSettings const& settings) const
{
    //some old SF files already include the inverse, make sure you use them the right way!
    if(product.m_zValid){
        product.m_weights["mu1TrackingSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.first);
        product.m_weights["mu2TrackingSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.second);
        product.m_weights["leptonTrackingSFWeight"] =
                1/GetScaleFactor(0, *product.m_zLeptons.first) * 1/GetScaleFactor(0, *product.m_zLeptons.second);
    }
    else
        product.m_weights["leptonTrackingSFWeight"] = 0;
}

/////////////////////
// LeptonTriggerSF //
/////////////////////

std::string LeptonTriggerSFProducer::GetProducerId() const { return "LeptonTriggerSFProducer"; }

void LeptonTriggerSFProducer::Init(ZJetSettings const& settings)
{
    m_sffile = settings.GetLeptonTriggerSFRootfile();
    m_etaonly = settings.GetLeptonSFetaonly();
    double error_multiplier = 0.;
    if (settings.GetLeptonTriggerSFVariation() == "up") {
        LOG(WARNING) << "LeptonTriggerSFProducer: varying scale factor UP one sigma";
        error_multiplier = 1.;
    } 
    else if (settings.GetLeptonTriggerSFVariation() == "down") {
        LOG(WARNING) << "LeptonTriggerSFProducer: varying scale factor DOWN one sigma";
        error_multiplier = -1.;
    }
    
    if(settings.GetChannel() == "mm"){
        histoname = settings.GetLeptonTriggerSFHistogramName();
    }
    else{
        LOG(ERROR) << "LeptonTriggerSFProducer not implemented for this channel";
    }
    m_etabins = &m_xbins;
    m_ptbins = &m_ybins;
    if (m_etaonly)
        m_absoluteeta = false;
    //m_reversed_axes = true;
    
    // Get file
    LOG(INFO) << "Loading lepton scale factors for Trigger " << m_id << ": File " << m_sffile
              << ", Histogram " << histoname;
    TFile file(m_sffile.c_str(), "READONLY");
    TH2F* sfhisto = (TH2F*)file.Get(histoname.c_str());
    
    // Get the pT and eta bin borders
    for (int ix = 0; ix <= sfhisto->GetNbinsX(); ++ix){
        m_xbins.emplace_back(2 * sfhisto->GetXaxis()->GetBinCenter(ix) -
                             sfhisto->GetXaxis()->GetBinLowEdge(ix));
    }
    for (int iy = 0; iy <= sfhisto->GetNbinsY(); ++iy){
        m_ybins.emplace_back(2 * sfhisto->GetYaxis()->GetBinCenter(iy) -
                             sfhisto->GetYaxis()->GetBinLowEdge(iy));
    }
    // Fill the m_sf array with the values from the root histo
    for (int ix = 1; ix <= sfhisto->GetNbinsX(); ix++) {
        for (int iy = 1; iy <= sfhisto->GetNbinsY(); iy++) {
            m_sf[0][ix - 1][iy - 1] = static_cast<float>(
            sfhisto->GetBinContent(ix, iy) - error_multiplier * sfhisto->GetBinError(ix, iy));
        }
    }    
    file.Close();
}

void LeptonTriggerSFProducer::Produce(ZJetEvent const& event,
                                 ZJetProduct& product,
                                 ZJetSettings const& settings) const
{
    if(product.m_zValid){
        product.m_weights["mu1TriggerSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.first);
        product.m_weights["mu2TriggerSFWeight"] = 1/GetScaleFactor(0, *product.m_zLeptons.second);
        product.m_weights["leptonTriggerSFWeight"] =
            1/(1-(1-GetScaleFactor(0, *product.m_zLeptons.first)) * (1-GetScaleFactor(0, *product.m_zLeptons.second)));
    }
    else
        product.m_weights["leptonTriggerSFWeight"] = 0;
}
