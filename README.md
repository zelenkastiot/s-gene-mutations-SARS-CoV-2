# s-gene-mutations-SARS-CoV-2
 *Phd. Nevena Ackovska* | *Kiril Zelenkovski*

Code for my Bioinformatics project where I analyzed GISAID SARS-CoV-2 emerging variants data and generated a language model using Transformers. The model semantically captures masked glycoprotein amino acid mutations in emerging variants of the SARS-CoV2-virus and gives appropriate scores for each potential aa change.



## Abstract 
This mini project exporles the idea of using Natural
Language Processing in the filed of genetics and virus tracking.
Hence, the case study explores the potential of Transformers
architecture and its ability to captures amino-acid mutations.
The study is based around building a grammar from sequences,
that are genetically different glycoprotein peptides, which serve
as an input-sentences. The model then trains to tell apart which
sequences are biologically correct and results showcase this
the best. With a low evaluation loss, the model was able to
successfully distinct which masked regions especially ACE2
binding cites which play a crucial role in drug resistance
development.

<p align="center">
<img src="https://raw.githubusercontent.com/zelenkastiot/s-gene-mutations-SARS-CoV-2/main/report/IEEE%20_Template/images/fig8-architecture.jpg" width=45%;></img> <br>
Fig1. The Transformer model architecture <a href='https://arxiv.org/abs/1706.03762'>[1]</a>
</p>


## Data

The proposed idea of building a grammar in a way
modeled the dataset, its final appearance is a result of
the way these models learn and train. For the part of
creating a dataset with biologically correct variants, huge
acknowledgement goes to the GISAID platform [12], who
have made tremendous effort to organize the data and create
beautiful documentation of its features. There are several
sections on the main GISAID website and all of them can
be useful in some way for the dataset creation. Since our
main focus was variants, the data was from the ”Emerging
Variants” section. This section of the page helps to monitor
new variants of COVID-19 that may become relevant due to
signs of increased proliferation (estimated by changing the
number of sites) in combination with potential effects on
receptor or antibody binding, commented in CoVsurver 

<p align="center">
<img src="https://raw.githubusercontent.com/zelenkastiot/s-gene-mutations-SARS-CoV-2/main/report/IEEE%20_Template/images/fig7-aligment_chart.png" width=45%;></img> <br>
Fig2. Bio-Dash as an alignment chart for the five most common lineages
</p>

## Results 

For trainging the model we used a Google Colab enviroment, with a Nvidia K80s, with 24 GB of GDDR5
memory. The training took 2h 12min to complete and resulted with a evaluation loss of only 6% (evaluationloss =
0.0655). Three different expirements were tried: 
- With only important binding and ACE2 mutations (Variant column) 
- With mutations from Variant column + Co-occuring changes (only 3) 
- With all possible mutations (Trainging loss is Fig3)

Aside from looking at the training and eval losses going
down, the easiest way to check whether our language model
is learning anything interesting is via the FillMaskPipeline.



<p align="center">
<img src="https://raw.githubusercontent.com/zelenkastiot/s-gene-mutations-SARS-CoV-2/main/loss.png" width=45%;></img> <br>
Fig3. Learning loss taking account the co-occuring changes
</p>



Pipelines are simple wrappers around tokenizers and models,
and the ’fill-mask’ one will let you input a sequence containing a masked token (here, ¡mask¿) and return a list of
the most probable filled sequences, with their probabilities.
Now we start masking the amino acids locations we
desire to see and see if our model captures them. We started
by masking the first location, 0 which is 100% the amino
acid M, and our model caught it with a probscore = 0.9999.
But, this was an easy one so we tried testing one of the 2
most lethal mutations [27], which are the N501Y and the
D614G.
Figure 4 shows the scores that the model returned as outputs: 



<p align="center">
<img src="https://raw.githubusercontent.com/zelenkastiot/s-gene-mutations-SARS-CoV-2/main/report/IEEE%20_Template/images/fig10-freq_transformer.png" width=45%;></img> <br>
Fig4. Transformer catches for frequency of amino acid in dataset
sequences at locations 501 and 614 in the Spike protein
</p>



<hr>
<p align="center">
<img src="https://raw.githubusercontent.com/zelenelez/images/master/finki.jpg" width=50%;></img> <br>
Summer, 2021
</p>
