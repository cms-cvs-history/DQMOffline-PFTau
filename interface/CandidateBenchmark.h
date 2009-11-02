#ifndef RecoParticleFlow_Benchmark_CandidateBenchmark_h
#define RecoParticleFlow_Benchmark_CandidateBenchmark_h

#include "DQMOffline/PFTau/interface/Benchmark.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"

/// To plot Candidate quantities
class CandidateBenchmark : public Benchmark {

 public:


  CandidateBenchmark(Mode mode) : Benchmark(mode) {}
  virtual ~CandidateBenchmark();

  /// book histograms
  void setup();

  template< class C>
  void fill( const C& candidates); 
  
  /// fill histograms with a given particle
  void fillOne( const reco::Candidate& candidate); 

 protected:
  

  TH1F*   pt_; 
  TH1F*   eta_; 
  TH1F*   phi_; 
  TH1F*   charge_; 

};

template< class C>
void CandidateBenchmark::fill(const C& candCollection) {

  for (unsigned int i = 0; i < candCollection.size(); i++) {
    const reco::Candidate& cand = candCollection[i];
    fillOne(cand);
  }
}


#endif 
