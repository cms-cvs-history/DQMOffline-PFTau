import FWCore.ParameterSet.Config as cms

process = cms.Process("pfTauDQM")

# import of standard configurations for RECOnstruction
# of electrons, muons and tau-jets with non-standard isolation cones
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_cff')
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('MC_36Y_V7A::All')

process.load("DQMOffline.PFTau.pfTauDQM_cfi")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.DQM.collectorHost = ''

process.dqmSaver.workflow = cms.untracked.string('/Physics/Run Summary/PFTau')

process.dqmSimpleSaver = cms.EDAnalyzer("DQMSimpleFileSaver",
    outputFileName = cms.string('pfTauDQM.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # Z --> tau+ tau- RelVal Monte Carlo
        #'/store/relval/CMSSW_3_1_3/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0003/04567ECF-EBA9-DE11-BA70-001D09F24FBA.root',
        #'/store/relval/CMSSW_3_1_3/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0002/96E4E0AA-A6A9-DE11-8A4A-001D09F24FEC.root',
        #'/store/relval/CMSSW_3_1_3/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0002/4C6AF2CD-A4A9-DE11-A29C-001D09F2A49C.root',
        #'/store/relval/CMSSW_3_1_3/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0002/02C022B1-A3A9-DE11-AF02-001D09F28F25.root'
        #'/store/relval/CMSSW_3_8_2/RelValZTT/GEN-SIM-RECO/START38_V9-v1/0018/FECE93E1-B8AF-DF11-B813-0018F3D096B6.root'
        #'/store/relval/CMSSW_3_8_2/RelValZTT/GEN-SIM-RECO/START38_V9-v1/0018/FECE93E1-B8AF-DF11-B813-0018F3D096B6.root'
        '/store/relval/CMSSW_3_9_0_pre5/RelValZTT/GEN-SIM-RECO/START39_V0-v1/0029/2CF5CD62-EFC8-DF11-96A8-003048D15E14.root',
        
        # real (first) Data !!
        #'rfio:/castor/cern.ch/user/l/lusito/BSC_activity.root'
        #'rfio:/castor/cern.ch/user/v/veelken/CMSSW_3_6_x/skims/tauCommissioning/data/muTauSkim_1_1.root'
        #'rfio:/castor/cern.ch/user/v/veelken/CMSSW_3_6_x/skims/tauCommissioning/data/muTauSkim_1_1.root'
        # small Z --> muon + tau-jet sample for testing purposes
        #'file:/afs/cern.ch/user/v/veelken/scratch0/CMSSW_3_1_4/src/TauAnalysis/Configuration/test/muTauSkim_1.root'
    )
)

process.load("DQMServices.Components.DQMStoreStats_cfi")

process.p = cms.Path(
    process.pfTauDQM
  #+ process.dqmSaver 
   + process.dqmSimpleSaver
   + process.dqmStoreStats
)

# print-out all python configuration parameter information
#print process.dumpPython()
