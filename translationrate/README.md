##Calculate traditional protein synthesis rate
    - Input as codon sequence with cap structure
        
        
    - mRNA degradation
        1. [https://www.kaggle.com/c/stanford-covid-vaccine](https://www.kaggle.com/c/stanford-covid-vaccine) 
        2. [https://towardsdatascience.com/what-i-learned-from-stanfords-covid-mrna-vaccine-kaggle-competition-98d3f454eef](https://towardsdatascience.com/what-i-learned-from-stanfords-covid-mrna-vaccine-kaggle-competition-98d3f454eef) 
        3. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8237341/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8237341/) 
    - initiation process of translational machinery
    - elgonation of coding sequence
    
    `Analysis and Prediction of Translation Rate Based on Sequence and Functional Features of mRNA`
    
    - protein concentrations depend on mRNA level + translation rate and degredation rate → predicting mRNA's translation rate wprovides valuable info for in-depth undestanding of translation mechanism and dynamic proteome → developed model by 1) integrated various sequence-derived and functional features 2) applied maximum relevance and minimum redundancy method + incremental feature selection to select features to optimize prediction model 3) predict translation rate of RNA into high or low translation rate category
        - key features: codon usage frequency, gene ontology enrichment sources, number of RNA binding proteins, coding sequence length, protein abundance, 5'UTR free energy
    - translation rate/efficiency = normalized read density of translation [footprints] / normalized read density of transcription [mRNA]
        - [ratio of ribosome footprints to mRNA fragments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4917602/) = rae of protein synthesis