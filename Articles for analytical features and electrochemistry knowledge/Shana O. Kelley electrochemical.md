Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 560
nature reviews bioengineering
Review article
https://doi.org/10.1038/s44222-023-00067-z
 Check for updates
Biomolecular sensors for advanced 
physiological monitoring
Connor D. Flynn    1,2, Dingran Chang    3, Alam Mahmud4, Hanie Yousefi5, Jagotamoy Das    2, Kimberly T . Riordan   2, 
Edward H. Sargent2,4,6 & Shana O. Kelley   1,2,3,5,7,8,9 
Abstract
Body-based biomolecular sensing systems, including wearable, 
implantable and consumable sensors allow comprehensive health-
related monitoring. Glucose sensors have long dominated wearable 
bioanalysis applications owing to their robust continuous detection 
of glucose, which has not yet been achieved for other biomarkers. 
However, access to diverse biological fluids and the development 
of reagentless sensing approaches may enable the design of body-
based sensing systems for various analytes. Importantly, enhancing 
the selectivity and sensitivity of biomolecular sensors is essential 
for biomarker detection in complex physiological conditions. In 
this Review, we discuss approaches for the signal amplification of 
biomolecular sensors, including techniques to overcome Debye and 
mass transport limitations, and selectivity improvement, such as the 
integration of artificial affinity recognition elements. We highlight 
reagentless sensing approaches that can enable sequential real-
time measurements, for example, the implementation of thin-film 
transistors in wearable devices. In addition to sensor construction, 
careful consideration of physical, psychological and security concerns 
related to body-based sensor integration is required to ensure that 
the transition from the laboratory to the human body is as seamless 
as possible.
Sections
Introduction
Strategies for signal 
amplification
Strategies for selectivity 
improvement
Continuous real-time 
monitoring
The biological fluid frontier
Outlook
Citation diversity statement
1Department of Chemistry, Faculty of Arts & Science, University of Toronto, Toronto, ON, Canada. 2Department  
of Chemistry, Weinberg College of Arts & Sciences, Northwestern University, Evanston, IL, USA. 3Department of  
Pharmaceutical Sciences, Leslie Dan Faculty of Pharmacy, University of Toronto, Toronto, ON, Canada.  
4The Edward S. Rogers Sr Department of Electrical and Computer Engineering, University of Toronto, Toronto,  
ON, Canada. 5Department of Biomedical Engineering, McCormick School of Engineering, Northwestern University, 
Evanston, IL, USA. 6Department of Electrical and Computer Engineering, McCormick School of Engineering, 
Northwestern University, Evanston, IL, USA. 7Department of Biochemistry and Molecular Genetics, Feinberg 
School of Medicine, Northwestern University, Evanston, IL, USA. 8International Institute for Nanotechnology, 
Northwestern University, Evanston, IL, USA. 9Chan Zuckerberg Biohub Chicago, Chicago, IL, USA.  e-mail:  
shana.kelley@northwestern.edu

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 561
Review article
analyte and provides some degree of selectivity; the transducer, which 
converts the analyte-recognition element interaction into a readable 
signal; and the analysis system, which interprets the received signals. 
In addition to these physical components, there are several key terms 
that are vital to understanding and comparing sensing schemes: the 
limit of detection (LoD) describes the lowest analyte concentration 
that can be consistently detected by a sensor; sensitivity, though often 
erroneously used interchangeably with LoD, refers to the ability of a 
sensor to differentiate between similar input concentrations; selectiv-
ity describes the ability of a sensor to selectively target certain analytes; 
specificity, which serves as an ultimate form of selectivity, describes the  
ability of a sensor to target a single analyte; linear range describes  
the analyte concentration range over which a sensor produces 
a proportional response; and physiological range describes the 
physiologically relevant concentration range of the analyte, which 
ideally falls within the linear range of the sensor.
The concept of biomolecular sensing existed millennia prior to 
any understanding of the molecular concept (Fig. 1), with the analysis 
of urine being conducted in civilizations as old as Sumer (~4000 BC)2. 
The most considerable and lasting of these findings was the associa -
tion between polyuria and sweet-tasting urine, recorded by the Indian 
physician Sushruta (~600 BC)3. Over the next two millennia, it was not 
uncommon for individuals referred to as water tasters to diagnose 
diabetes-like illness by tasting urine and assessing its sweetness4. The 
connection between diabetes and sweet urine was rediscovered and 
made mainstream in Europe by Thomas Willis (~1679)3. Over the next 
few centuries, scholars discovered that sugar was responsible for the 
sweetness of diabetic urine and established chemical tests to determine 
its presence5. These tests, including Trommer’s test, Fehling’s test and 
Benedict’s test, exploited sugar-assisted reduction of copper species to 
produce colorimetric changes and diagnose diabetes3,5. Although these 
tests were rather non-specific, they can be seen as the predecessors of 
modern biomolecular sensors.
The first modern biomolecular sensor is typically attributed to 
Leland Clark for his 1962 proposal 6 to incorporate glucose oxidase 
enzymes into his previously developed oxygen electrode7. However, the  
Miles–Ames laboratory also made substantial contributions with  
the development of a colorimetric glucose oxidase test strip in 1957 
(ref. 8). In 1970, the same laboratory released the first portable blood 
glucose meter, a landmark achievement in portable biomolecular 
analysis9. Clark eventually commercialized his electrochemical glucose 
monitor in 1975 (ref. 10). In the 1980s, as glucose monitoring became 
more mainstream, many alternative colorimetric glucose systems 
made their way to market 11. Although it was difficult to miniaturize 
them, the first portable electrochemical glucose monitor eventually 
reached the market in 1987 and quickly dominated its colorimetric 
competitors12. This landmark led to market-wide adoption of electro-
chemical sensing, with most companies replacing their colorimetric 
devices with electrochemical ones that are still on the market today. 
Finally, in 1999, the first continuous glucose monitor received US Food 
and Drug Administration (FDA) approval 13, sparking interest in the 
development of body-based sensing platforms.
The twenty-first century has brought with it a new wave of body-
based sensing systems, with many large life sciences companies market-
ing their own continuous glucose monitoring system. While glucose 
measurement remains at the forefront of sensor innovation, the devel-
opment of commercial sensors for alternative analytes has lagged 
behind, with the exception of a few other metabolites (for example, 
cholesterol). However, there is an abundance of other biochemical 
Key points
 • Glucose sensors traditionally dominate the commercial sensing 
market, but sensors for alternative analytes could advance 
personalized health care in coming decades.
 • Body-based biomolecular sensors, including wearable, implantable 
and ingestible sensors, provide simple and continuous access to user 
biomolecular data through various biological fluids.
 • Continuous monitoring requires kinetically favourable receptors 
and sensing mechanisms capable of detecting analytes without user 
intervention.
 • In addition to sensor efficacy, body-based systems require careful 
consideration of physical, psychological and security concerns related 
to device use and data handling.
Introduction
Biomolecular sensing is a rapidly growing interdisciplinary field. By 
combining engineering, chemistry, biology, physics, medicine and 
computational data analytics, sensors have been developed for the 
real-time monitoring of various physiological conditions. However, 
in spite of the identification of new sensing mechanisms and unique 
biomolecular targets, there remains a gap between the number of 
laboratory-developed sensors and commercialized products. Despite 
major advances in analyte targeting, signal amplification and sensor  
portability, it remains challenging to match the practicality and perfor-
mance of simple enzymatic glucose sensors in systems that detect other 
analytes. Glucose sensors use specific enzymes (for example, glucose 
oxidase and glucose dehydrogenase) capable of producing highly 
amplified responses (for example, through high catalytic turnover) 
in a continuous manner, which is not easily achievable for other 
small-molecule, protein and nucleic-acid analytes. The development  
and adoption of body-based biomolecular sensing platforms (for 
example, wearables and implantables) requires continuous-sensing 
mechanisms with sensitivities and specificities comparable to those of 
glucose sensors. Therefore, the continued exploration of these body-
based platforms is key to expanding biomolecular analysis beyond 
simple metabolite detection, to enable comprehensive physiological 
monitoring and inform clinical decision-making.
Historically, biological sensors or biosensors were named for 
their incorporation of a biological component to recognize and detect 
analytes. These biorecognition elements were necessary because the 
intricacy and selectivity of biological macromolecules was difficult  
to imitate. However, advances in the development of synthetic recogni-
tion elements, such as molecularly imprinted polymers and artificial 
enzymes, have enabled sensors to achieve selectivity comparable 
to that of their natural counterparts
1. At present, we use the term 
biomolecular sensor to more generally describe all sensors aimed 
at detecting biomolecules or other biologically relevant molecules, 
shifting the focus away from the origin of the selected recognition 
component, and towards the more relevant nature of the analyte being  
detected.
In terms of composition, biomolecular sensing systems typically 
comprise four main components: the analyte, which is the biomolecule 
being detected; the recognition element, which interacts with the 

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 562
Review article
indicators (for example, proteins and DNA) that can provide invalu-
able information on physiological status. As sensor development 
continues towards new body-based platforms capable of long-term 
measurements, the number of analytes that can be reliably detected 
will hopefully continue to expand and allow these systems to realize 
their diagnostic potential.
This Review summarizes emerging biomolecular sensors, tack -
ling two main challenges. The first challenge is the transition of sen-
sors from laboratory-based assays to body-based systems to develop 
self-contained biomolecular sensors that are wearable, implantable 
or consumable and can easily be incorporated into everyday life. 
The second challenge is to expand biomolecular sensors beyond 
glucose detection, to realize practical and commercial devices for a 
broader range of relevant physiological markers (Box 1). T o overcome 
these challenges requires biomolecular sensing approaches that are 
more sensitive, specific and amenable to continuous monitoring 
than ever before. Here we highlight many of the cutting-edge strate-
gies expected to facilitate the development of new sensing devices. 
In addition, we explore relevant considerations regarding biological 
fluid compatibility and sensor design to ensure seamless lab-to-body 
transition.
Strategies for signal amplification
Sensitivity, specificity and adaptability to new analytes are the major 
challenges for biomolecular analysis14. Therefore, many amplification 
strategies have been developed to enable lower LoDs and higher sen-
sitivities. These strategies can be implemented at any level of sensor 
development to help to achieve practical physiological monitoring.
Intracellular sensors
Intracellular sensors go beyond secreted (for example, insulin) and 
membrane-bound biomarkers (for example, viral surface proteins) 
to provide localized information at the cellular level (for example, 
quantifying mRNA expression in breast cancer cells and detecting 
overexpression of cytosolic cathepsin B in adenocarcinoma cells)15,16. 
They are also sensitivity enhancers, given the small size of the cell and 
the fact that intracellular concentrations often surpass those in bio-
logical fluids. These sensors allow single-cell diagnosis by probing 
cytoplasmic regions and enable access to diverse high-concentration 
biomarkers (Fig. 2a). Intracellular analysis is typically achieved by 
either direct insertion of nanostructures into the cytosol to probe16 
or extract17 its contents, or indirect intake and expression of a genetic 
sensing framework; for example, through reporter gene activation 
upon interaction with intracellular human immunodeficiency virus 
(HIV) proteins18. These intracellular approaches have the potential to 
considerably amplify cell-localized biological phenomena (such as 
cytoplasmic protein overexpression) for diagnostic purposes.
Surrogate biomarkers
Sensor development has long focused on the assessment of biological 
conditions through directly related molecular targets, such as targeting 
viral surface proteins to detect a virus. Yet there is an abundance of addi-
tional targets or surrogate biomarkers (Fig. 2b) that are less intuitive 
but still correlate with physiological conditions19. Surrogate markers 
may also be present at higher concentrations than the direct target, and 
can thus amplify a biochemical signal. Advances in the understanding 
of molecular pathways can reveal new biological relationships and help 
to access a broader library of health indicators. For example, precursor 
or metabolite molecules can be targeted, such as tyrosine as precursor 
to norepinephrine — a neurological indicator 20. Another approach is 
the targeting of indirectly related proteins that show high condition 
correlation, for example, measuring neurofilament light chain protein 
as an indicator of inflammatory brain demyelination21. These simple 
methods can provide precise indirect estimates of trace molecules or 
hidden biological events.
Synthetic biomarkers
The pool of endogenous biomarkers is large, but it is not limitless. 
Alternatively, synthetic biomarkers (Fig. 2c) that are designed to inter-
act with biomolecules can be introduced into the body (for example, 
through injection) to indicate and amplify physiological conditions 
(for example, by reacting with an overexpressed enzyme) 22,23. Syn-
thetic biomarkers can have various configurations; however, all of 
them contain two essential components: a recognition region (for 
example, substrates 24 and promoter sequences 25) to target the bio -
chemical process and a reporter region (for example, volatile organic 
compounds24 and genes25) to signal its presence. Synthetic markers 
can bypass common endogenous biomarker issues (for example, short 
half-lives and low concentrations), and detect previously inaccessi -
ble or subtle health states. For example, volatile reporter molecule-  
linked peptides injected into mice are cleaved by neutrophil 
elastase, to indicate its elevated activity, which is associated with 
several illnesses (such as pulmonary bacterial infections and alpha-1 
antitrypsin  deficiency)
24.
Emerging approaches
• Wearable sensors
• Implantable sensors
• Consumable sensors
4000 BC: First 
evidence of 
urine analysis
2
600 BC: First link 
between urine 
sweetness and 
diabetes-like illness
3
1679: Rediscovery of 
the link between 
between diabetes and 
sweet urine, in Europe 3
1957: First incorporation of 
a biological recognition 
element into a colorimetric 
biomolecular sensor 8
1970: First portable 
biomolecular sensor 
for glucose detection 
in the market 9
1999: FDA approval of 
continuous glucose 
monitor for body-
based sensing 13
1700–1900: Development 
of several methods for 
glucose detection using 
metal salts
3,5
1962: First 
electrochemical 
biomolecular 
sensor 6
1987: First portable 
electrochemical glucose 
sensor in the market 12
Fig. 1 | Timeline of biomolecular sensor development. Timeline of major 
events regarding the evolution of biomolecular sensing, including the first 
evidence of urine analysis
2; the first connection between sweet urine and 
diabetes-like illness3; the rediscovery of the connection between sweet urine 
and diabetes in Europe3; the development of primitive metal salt glucose tests3,5; 
the first incorporation of a biological recognition element into a colorimetric 
biomolecular sensor
8; the first proposed electrochemical biomolecular 
sensor6; the first commercial, portable glucose sensor9; the first commercial 
electrochemical glucose sensor12; and the US Food and Drug Administration 
(FDA) approval of the first continuous glucose monitor13.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 563
Review article
Catalyst-mediated amplification
Enzymes are considered the ideal recognition element owing to their 
excellent selectivity and natural catalytic ability; however, they are 
restricted by the analytes they can target. Therefore, the discovery and 
fabrication of alternative catalysts (Fig. 2d) is important for universal 
high-sensitivity sensing.
Nanozymes are nanomaterials that possess catalytic ability and 
can replace enzymes in biomolecular sensing. These include nanopar-
ticles26, metal–organic frameworks (MOFs)27, and many other nanoma-
terials28 capable of catalysing biochemical reactions and generating 
amplified biomolecular responses. For example, peroxidase-like MOFs 
capable of catalysing o-phenylenediamine to 2,2-diaminoazobenzene 
enable sensitive detection of Staphylococcus aureus with a LoD of only 
6 colony-forming units (CFU) ml–1  (ref. 29). Additionally, single-atom 
nanozymes have atomically dispersed metal active sites that maximize 
catalytic efficiency, allow for tunable selectivity, and enable reaction 
kinetics similar to that of natural enzymes 1,30,31. Moreover, compu-
tational approaches and artificial intelligence can be applied to the 
discovery of artificial catalysts (for example, superoxide-dismutase 
nanozymes and carbon dioxide electrocatalysts)32,33.
DNA catalysts, or DNAzymes, can also amplify biomolecular 
signals and offer alternative catalytic routes for sensing. DNAzymes 
catalyse various reactions, including RNA cleavage, RNA ligation and 
alkyne–azide cycloaddition 34– 36. These reactions can be implemented 
in a variety of ways to detect metal ions, small molecules, nucleic acids 
and proteins through a combination of a catalytic event and a released 
reporter molecule (for example, cleaving of a dye-conjugated RNA 
sequence). For example, DNAzymes selected to react with specific 
bacteria lysates can detect bacteria in single digits per millilitre in 
unprocessed blood samples 37,38. In addition, the complementary 
nature of DNA within DNAzymes allows for programmable capture 
and release of the substrate, and easy integration with other functional 
nucleic acids (for example, extension of the DNAzyme sequence to 
include an aptamer sequence that can bind the analyte and provide 
additional selectivity)34.
Overcoming mass transport limitations
The sensitivities and LoDs of biomolecular sensors do not rely on the 
bulk concentrations of analyte in solution but on the localized amount 
of analyte interacting with the recognition component of the sensor. 
Therefore, maximizing the analyte-recognition element interactions 
is important to ensure sensitive and fast detection. Several strategies 
have been developed to overcome the limitations caused by slow mass 
transport of molecules and thus slow diffusion (Fig. 2e) to improve 
biomolecular recognition and to amplify early signal responses. These 
strategies include designing synthetic nanochannels to maximize 
transport efficiency39, using superhydrophobic surfaces to control 
molecule localization40 and using molecular micromotors to mix solu-
tions and accelerate mass transport41. In addition, DNA nanostructures 
can improve surface probe distribution and reduce probe crowding, 
Box 1
Commercializing biomolecular sensors beyond glucose
As of 2022, the global market for biomolecular sensors exceeded 
US$28 billion and is expected to surpass US$58 billion over the next 
10 years
204. Although the past 50 years of biomolecular sensing have 
seen considerable financial investment and industrial development, 
this has primarily focused on advancing glucose detection. This 
is partly because of the high demand for daily diabetic glucose 
monitoring, but also because of the simple enzymatic detection 
method by which glucose can be measured. There is certainly no 
shortage of sensing mechanisms for other analytes, and many 
sensing approaches have been developed for various fluids, but 
there is a lack of detection schemes that can easily be implemented 
in commercial products. To accommodate biomarkers and enable 
commercialization, several hurdles must be overcome.
Improved understanding of the biochemistry–physiology 
relationship
The broad adoption of glucose monitoring can be attributed  
to the direct link between levels of glucose and health, a link that  
can be difficult to make for other more complex biomarkers. An array 
of analytes have been studied for their association with health condi-
tions, but there is a need for a deeper understanding of how biomark-
ers fluctuate in specific biological fluids, especially in non-blood 
biological fluids, so that physiological conditions can be tracked 
accurately
155. For example, complex biomarkers, such as cytokines,  
have immense potential to inform critical health decisions, but their 
polycausal fluctuations, combined with our still elementary under-
standing of their stimulation, make it difficult to employ them for 
medical assessment.
Developing detection strategies with simplicity comparable 
to glucose sensors
Although enzymatic detection is simple and easily implementable, 
the lack of available enzymes for most analytes necessitates more 
advanced sensing strategies, such as affinity-based approaches. 
However, although affinity-based sensors have shown promise, 
their reliance on affinity interactions makes them more difficult to 
implement in continuous-sensing systems
87. Such sensors must be 
able to reset themselves in a timely manner, maintain sensor integrity 
and avoid biasing bulk analyte concentrations. Further development 
of kinetically controllable recognition elements, robust anti-fouling 
strategies and reliable reagentless detection approaches will help  
to hasten their adoption
86,92,117.
Identification and prediction of societal needs
The translation of biomolecular sensors requires investment of time, 
money and knowledge. Therefore, sensors must address issues that 
are central to current needs. For example, the ongoing SARS-CoV-2 
pandemic has driven considerable development of viral detection 
methods
118. The ability to identify emerging sensing applications is  
an important factor in guiding a sensor to the market.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 564
Review article
allowing for enhanced analyte association42. Microfluidic approaches 
for sample collection and transport can maximize mass transport effi-
ciency, in addition to being compatible with wearable and implantable 
devices43.
Organic electrochemical transistors
Organic electrochemical transistors (OECTs) (Fig. 2f) can act as signal-
amplifying components in biomolecular sensing and other bioelec-
tronic devices44. OECTs contain three main properties which, when 
combined, set them apart from other field-effect transistors. First, 
they possess an organic semiconductor channel (such as poly(3,4-
ethylenedioxythiophene) polystyrene sulfonate, PEDOT:PSS) that 
bridges the source and drain electrodes. Second, they possess an 
electrolyte between the channel and gate electrode. Third and most 
importantly, they allow for full penetration of electrolyte ions into the 
semiconductor channel45. Because semiconductor doping is reliant 
on ion penetration, OECTs can generate very large drain currents with 
small gate voltages, which makes them excellent signal amplifiers for 
biomolecular interactions44,46. For example, an interdigitated OECT 
sensor for adenosine triphosphate (ATP) achieves a LoD of 10 pM, 
which is nearly four orders of magnitude better than an amperomet-
ric transduction approach using the same recognition element47. The 
inexpensive fabrication costs of OECTs, as well as their capacity for 
flexible electronic integration, make these components attractive 
candidates for wearable and implantable devices48.
Reporter multimerization
A simple method of amplifying biomolecular interactions at the trans-
duction level is to increase the amount of signal generated by each 
analyte. Typically, affinity interactions result in a 1:1 ratio between signal 
and interaction. However, this ratio can be increased through simple 
incorporation of multiple reporter molecules (Fig. 2g) into the recogni-
tion element complex. For example, incorporation of multiple methyl-
ene blue redox markers into a C-reactive protein sensor enhances signal 
output and enables a LoD of 1 pM, which is considerably lower than 
that of previous electrochemical and optical approaches using single 
reporter molecules49. Alternatively, secondary reporter complexes 
in the form of oligonucleotide systems or reporter-labelled nanoma-
terials (for example, dendrimers) may be used to produce amplified 
responses50. However, many of these multimerization amplification 
strategies are designed for use in more traditional immunoassays with 
externally added reporter molecules, and thus may not be compatible 
with body-based biomolecular sensing. This encourages the develop-
ment of methods that focus on multimerization of recognition ele -
ments and require no external reagents, which are more compatible 
with continuous in vivo detection.
Overcoming Debye limitations
The screening of surface-bound charges by mobile ions beyond the Debye 
length, which is the effective sensing range, is a key obstacle in the devel-
opment of high-sensitivity electronic sensors51. Although this issue is 
often avoided through alterations to the buffer solution (for example, 
decreased ionic strength), this approach is unrealistic for biofluid analy-
sis52. Thus, several strategies have been introduced to overcome Debye 
length limitations and to amplify biomolecular interactions (Fig. 2h). 
Among these strategies is inducing near-electrode conformational 
changes to signal distant interactions51, using nanostructured materials 
to accelerate electron transfer53, and employing membrane-encapsulated 
ion-free water layers to extend the Debye length54.
Multiplexing and molecular data fusion
Multiplexing or using multiple markers allows the amplification of 
changes in physiological signals by increasing the number of bio -
molecular targets. Thus, sampling of multiple molecular avenues (for 
example, inflammatory, hormonal and metabolic) provides a more 
comprehensive health assessment55. The fusion and analysis of multiple 
molecular data (Fig. 2i) through artificially intelligent approaches, such 
as machine learning, can expand the capability of sensors to identify 
and diagnose physiological conditions faster, earlier and with more 
accuracy than techniques relying on single analyte analysis 56– 58.  
In addition, multiplexed controls (for example, additional sensors with 
non-specific recognition elements) allow better insight into sensor 
stability by providing separate channels to monitor sensor degradation.
Strategies for selectivity improvement
The incorporation of biological recognition elements that selec -
tively detect biologically relevant molecules into molecular sensing 
approaches can improve selectivity6,8. Proteins, DNA and synthetic 
alternatives (such as polymers and nanoparticles) can be applied as reco-
gnition elements for specific analytes59,60. Although enzymes are ideal  
recognition elements owing to their high specificity and natural signal 
amplification through high catalytic turnover, most biomolecular tar-
gets do not have specific enzyme catalysts and thus require alternative 
recognition approaches. Robust affinity recognition elements (affinity 
receptors) that induce highly specific association interactions with 
their target are necessary to develop body-based biomolecular sensors. 
These recognition elements should be able to withstand the presence of 
high concentration interferants in native biofluids, remain stable during 
daily wear and tear, and possess the resolution and dynamic capabili-
ties to capture physiologically relevant changes in biomarker levels. 
Here, we discuss the current state of affinity recognition elements, 
explore strategies to overcome non-specific binding and biofouling, 
and analyse the compatibility of various recognition elements for  
in vivo real-time monitoring.
Natural and artificial affinity receptors
Antibodies are the most popular biological affinity receptors employed 
in sensors (Fig. 3a). They are generated in vivo in response to specific 
immunostimulation to selectively bind targets under physiological 
conditions. Antibodies have high binding affinities, selectivity and 
sensitivity to detect biomarkers at picomolar to nanomolar concentra-
tions. However, antibodies are fragile, highly sensitive to temperature 
and pH changes, exhibit batch-dependent variation, and have high 
production costs, which greatly limits their use in bioelectronic appli-
cations59. Antibody mimetics with high ligand-binding affinity can be 
designed in the form of antibody fragments59 (for example, nanobod-
ies61) and engineered proteins (for example, avimers62, affimers63 and 
affibodies64). Compared to antibodies, these engineered receptors are 
smaller in size, have higher thermal stability, and can be engineered 
as multimers to increase avidity59,61. In addition, in vitro technologies 
such as phage display and ribosome display enable rapid, efficient and 
inexpensive selection of high-affinity protein-based binders65,66. How-
ever, although they are effective, these engineered alternatives often 
fail to outcompete antibodies in assay performance; this is probably 
due to their inability to mimic the glycosylation patterns and post-
translational modifications of antibodies, which confer additional 
selectivity.
Functional nucleic acids are promising affinity recognition ele -
ment alternatives to antibodies. Aptamers are single-stranded nucleic 

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 565
Review article
a  Intracellular sensing b  Surrogate biomarkers c  Synthetic biomarkers
d  Nanozymes and DNAzymes e   Overcoming mass transport limitations f  Organic electrochemical transistors
g  Reporter multimerization h  Overcoming Debye length limitations i   Computational approaches and 
     multiplexed analysis
Analyte
Precursor
Intermediate
Disease-
associated
protease
Substrate
Reporter
Electrolyte
Structure-switching receptors
Membrane-mediated Debye extension
Nanostructure-mediated 
electron transfer
Source Drain
Organic semiconductor
Gate
Analyte (pM)
Precursor (mM)
Potential (V)
Current (nA)
Substrate
Product
Nanozyme
Precursor
Analyte
Micromotor
Analyte-guiding 
nanochannel
Reporter multimerization
Single reporter
Superhydrophobic transport metamaterials
+ +
+
+
–
–
– –
Debye
length
+++ +
––– – – ––
e –
e –
+
–
+
–
+
–
+
+
+
+
–
–
–
–
Reporter
DNAzyme
+ +
+
+ + +
+
– – – –
– – – – –
Biomarker 1
Cancer (90%)
Hepatitis (9%)
Parasite (1%)
Biomarker 2
Biomarker 3
Biomarker 4
To sensor
Extracellular
(low concentration)
Intracellular
(high concentration)
Biological sampling
Biomarker analysis
Nanostructure
Analyte
Analyte
Analyte-containing
droplet

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 566
Review article
acids generated in vitro through the systematic evolution of ligands 
by exponential enrichment (SELEX), in which sequences are selected 
to bind to a specific target, ranging from metal ions to whole cells67,68. 
SELEX allows the generation of affinity receptors for a broad range 
of targets, including toxic, non-immunogenic and small-molecule 
biomarkers that are difficult to target with antibodies 69,70. Aptamers 
are particularly promising for implementation in body-based sen -
sors owing to their simple and inexpensive mass synthesis, minimal 
batch-to-batch variation, high thermal stability, non-immunogenic 
properties and their amenability to site-specific chemical modifica -
tion. As such, aptamers have been demonstrated in several wearable 
and implantable sensors (for example, in continuous cortisol- and 
serotonin-monitoring systems)71,72.
However, aptamers are inherently prone to nonspecific binding 
owing to their intrinsic negative charge and the large variety of RNA- 
and DNA-binding proteins present in body fluids73. In addition, they are 
susceptible to nucleases in biological fluids and sensitive to changes in 
environmental conditions, such as pH, temperature and salt concen-
tration. Alternatively, chemically modified aptamers with non-natural 
nucleic acids can have low nonspecific binding, and improved stability 
and binding affinity (such as SOMAmers74 modified to have slow analyte 
dissociation)75. SELEX approaches run in biological fluids or directly 
in live animals can isolate aptamers that maintain high performance 
under physiological conditions 76,77. Additionally, strategies to resist 
nuclease degradation such as using chemical alterations or surface 
coatings78,79 can minimize probe loss.
Synthetic recognition elements that are not based on biological 
monomers (such as molecularly imprinted polymers 60 and supra -
molecular systems 80) also show promise as selective receptors for   
biomolecular sensors.
Nonspecific binding
A key challenge in the translation of biomolecular sensors is nonspe-
cific binding, which can occur on both the sensor surface (biofouling) 
and the recognition element (cross-reactivity)73. Biofouling is driven 
by the accumulation of cells, proteins or other species on the sensor 
surface through nonspecific interactions. This adsorption process 
hinders the diffusion of analytes to the sensor and leads to signal loss 
over time81. Cross-reactivity arises from recognition elements that 
interact with molecules other than the analyte of interest to produce 
false-positive responses. These interferants may have affinities close 
to that of the analyte, or they may be present in such high concentra-
tions that they associate to a considerable degree at equilibrium. In 
biological fluids, high protein content compared to that of the analyte 
can cause substantial nonspecific binding that may appear as false 
positive signals73. Strategies and approaches, such as using protec-
tive coatings and exploiting kinetic differences between analyte and 
interferant must therefore be developed to minimize these extraneous 
interactions (Fig. 3b).
Generally, anti-fouling strategies aim to either fill the gaps in a 
sensing surface using a blocking agent (for example, bovine serum 
albumin (BSA) and casein) or to coat the entire sensing surface with an 
anti-fouling layer (for example, poly(ethylene glycol) and zwitterionic 
polymers such as derivatized polycarboxybetaine)73,82,83. More com-
plex anti-fouling layers, based on bioinspired materials (for example, 
slippery liquid-infused porous surfaces inspired by pitcher plants)
84, 
hydrogels (for example, polyacrylamide copolymer gels) 85,86 and 
nanocomposites (for example, cross-linked BSA impregnated with 
conducting nanomaterials) 87,88 also show fouling resistance in vivo. 
Additionally, methods have been developed to distinguish analyte 
binding from nonspecific interferent binding. One such approach 
exploits the affinity differences between analyte and interferant to 
physically remove weakly bound entities with an external force, for 
example by using an alternating electric field89. This approach allows 
active removal of interfering species, such as nonspecific IgG without 
ejection of the target HER2 protein. The inclusion of a reference or 
control sensor with a non-specific receptor (for example, scrambled 
aptamer sequence
71) is another way to differentiate between real and 
non-specific signals. Alternatively, the molecular recognition approach 
itself can confer some resistance to nonspecific interactions. Sensing 
mechanisms that rely on an analyte-triggered event (for example, 
structure-switching aptamers51) are less prone to nonspecific signal 
interference than sensors that rely on bulk property changes. Similarly, 
stochastic sensing approaches (for example, solid-state nanopores90) 
that can computationally distinguish between analyte and interferant 
are highly resistant to nonspecific behaviour.
Continuous real-time monitoring
As an alternative to single-use sensors, body-based biomolecular sen-
sors require sensor regeneration and reliability. Thus, sensors must be 
able to detect analytes using reversible molecular interactions, ensure 
minimal time between readings and provide continuous data with 
negligible hysteresis. Continuous monitoring is challenging, especially 
with high-affinity recognition elements that exhibit slow dissociation 
kinetics91; however, there are several solutions to overcoming such limi-
tations (Fig. 3c). A receptor with fast binding kinetics (for example, an 
aptamer selected for high on/off rate) is ideal for continuous monitor-
ing because it allows rapid equilibration with the surrounding fluid92. 
Fig. 2 | Strategies for amplifying biomolecular interactions. a, Intracellular  
sensing allows access to new, high-concentration biomarkers. b, Surrogate bio-
markers can provide alternative detection pathways for trace analytes. c, Synthe tic 
biomarkers can be introduced to the body to amplify biomolecular processes and 
enable their detection. d, Nanozymes and DNAzymes provide alternative catalytic 
routes for analyte monitoring. e, Mass transport advances, including analyte-
guiding nanochannels, superhydrophobic transport metamaterials and analyte 
mixing micromotors increase the rate of interaction between an analyte and its 
recognition element. f, Organic electrochemical transistors serve as powerful 
amplifiers for biomolecular interactions. g, Reporter multimerization enhances the 
signal output from affinity interactions. h, Debye length-manipulating approaches,  
including structure-switching receptors, nanostructure-mediated electron 
transfer and membrane-mediated Debye extension bypass traditional Debye 
limitations to extend transducer influence and increase signal generation.  
i, Computational approaches, combined with multiplexed analysis, may allow 
health state amplification for predictive medicine. Part c is adapted from ref. 22,  
Springer Nature Limited. Part e (analyte-guiding nanochannel) is adapted from  
ref. 39, Springer Nature Limited. Part e (superhydrophobic transport meta-
materials) is adapted from ref. 40, Springer Nature Limited. Part f is adapted 
from ref. 44, Springer Nature Limited. Part h (structure-switching receptor) from 
Nakatsuka, N. et al. Aptamer-field-effect transistors overcome Debye length 
limitations for small-molecule sensing. Science 362, 319–324 (2018)
51. Adapted 
with permission from AAAS. Part h (nanostructure-mediated electron transfer) is 
adapted from ref. 53, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). 
Part h (membrane-mediated Debye extension) is adapted from ref. 54, Springer 
Nature Limited.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 567
Review article
However, as these rapid kinetics edge closer to real-time monitoring, 
this temporal resolution often comes at the cost of sensor LoD. There-
fore, biomolecular sensors that employ such recognition elements 
must also use highly sensitive transduction mechanisms (for example, 
transistor-based approaches) to compensate for sensitivity loss93. In 
addition, a proper fluid-sampling system (for example, microfluidic 
integration) is desirable to provide effective and rapid transport of 
the biological fluid over the sensor to ensure a reproducible, timely 
and accurate signal, along with negligible sample contamination and 
carryover.
Real-time monitoring can also be achieved through the regen -
eration of recognition elements after each measurement, using 
either chemical, thermal or electrochemical approaches94. Chemical 
regeneration methods rely on surface and fluid property alterations 
through the application of acids, bases or other solvents. However, 
these approaches can damage biological receptors and are not com-
patible with body-based biomolecular analysis. Thermal regeneration 
methods are more feasible for body-based sensing, relying on localized 
warming using miniaturized heating elements, and are particularly 
promising for nucleic-acid-based receptors95. Finally, electrochemi-
cal regeneration approaches employ electrical pulses or other wave-
forms to manipulate affinity interactions without risking damage to 
receptors96.
Approaches for continuous monitoring
Continuous monitoring requires complementary sensing approaches 
that enable real-time detection in biological fluids97. Most available bio-
molecular sensing methods rely on secondary reporters (for example, 
sandwich assays), indirect reporters (for example, steric hindrance 
assays) or chromatographic systems (for example, lateral flow assays). 
However, such techniques are incompatible with body-based biomo-
lecular sensing owing to their dependence on external manipulation 
and washing steps. Some approaches avoid the need for such external 
interventions by combining recognition and reporting steps into one 
process. However, these methods typically rely on specialized receptors 
with intrinsic activity such as enzyme catalysts that are only available 
for a small subset of analytes. Thus, the development of universal rea-
gentless platforms that offer versatility in target analysis, and employ 
self-contained reagent-free mechanisms, is crucial for the widescale 
adoption of body-based sensors.
Electrochemical aptamer-based sensors. Electrochemical aptamer-
based (E-AB) sensors (Fig. 4a) allow reagentless, label-free detection 
of small molecules and proteins98. E-AB sensors use electrode-bound 
aptamers with terminal redox reporters to recognize and bind ana-
lytes. Analyte detection is achieved through target-induced proximity 
changes between the redox reporter and the electrode surface, which 
alters the received Faradaic current. E-AB sensors have been optimized 
Receptor regeneration following analyte attachment
c Catalyst-mediated detection
Enzyme
Signal+
 Signal+++
Regeneration
a Protein recognition element
Antibody
Receptor
 Enzyme
 Nanobody
 Avimer
 A/f_f.shortimer
 A/f_f.shortibody
Nucleic acid recognition element
ssDNA/ssRNA
 Aptamer
 Nucleic acid
enzyme
Modi/f.shortied aptamer
For example, SOMAmer
Synthetic recognition element
Molecularly
imprinted polymer
Synthetic
catalyst
Supramolecular
systems
Referencing
No receptor
control
Signal
b
Signal NSBSignal SB
Stochastic sensing High-speci/f.shorticity
recognition elements
Anti-fouling layers
Kinetic control of analyte binding and release
kon
koﬀ
koﬀ
kon
Molecular-switching recognition elements External force
NSB
 NSB
SB
 SB
External force (for
example, alternating
electric /f.shortield)
 Non-speci/f.shortic
receptor control
Analyte Interferant
Analyte changes
receptor conformation
Non-speci/f.shortic
receptor
Fig. 3 | Considerations for biomolecular sensor recognition element selection. 
a, Classes of available recognition elements (protein, DNA and synthetic) including 
both traditional and emerging receptors. b, Strategies for prevention of non- 
specific binding (NSB). c, Recognition-element-based strategies for continuous 
monitoring include catalyst-mediated detection, kinetic control of analyte  
binding and release, and receptor regeneration following analyte attachment. 
koff, dissociation rate constant; kon, association rate constant; SB, specific binding; 
SOMAmer, slow off-rate modified aptamer; ssDNA, single-stranded DNA; ssRNA, 
single-stranded RNA.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 568
Review article
to establish a detailed theoretical framework for their molecular interac-
tions99, and enable their implementation in in vivo systems99– 101. Moreo-
ver, E-AB sensors have excellent temporal resolution upon sequential  
in vivo measurements, for example, for the detection of plasma phenyla-
lanine in rats102. Furthermore, E-AB molecular probes can be incorporated  
into implantable devices to offer non-invasive continuous monitoring. 
For example, an E-AB microelectrode sensor is used for the continuous 
measurement of doxorubicin in mouse tumour tissue 103. Although 
E-AB approaches expand analyte diversity for continuous monitoring, 
they are restricted by the availability of aptamer sequences that can 
bind relevant targets and undergo sufficient conformational changes 
between their unbound and bound states.
Electrochemical DNA sensors.  DNA is an important biomarker for 
the diagnosis of disease and surveillance of physiological conditions. 
Electrochemical DNA (E-DNA) sensors (Fig. 4b) operate in a similar way 
to E-AB sensors, that is, through target-induced proximity changes 
between a terminal redox reporter and an electrode. However, instead 
of aptamers, E-DNA sensors rely on DNA hairpin probes that hybridize 
to nucleic acid analytes 104. Alternatively, E-DNA approaches can use 
strand displacement techniques105. E-DNA sensors can be implemented 
into in vivo systems, for example, for the detection of pM-level DNA 
in whole blood 106. However, these sensors are often susceptible to 
false-positive results owing to probe degradation and non-specific 
interactions. In addition, ultralow concentrations of circulating DNA 
in physiological matrices complicates the commercial adaptation of 
these approaches
107. Ongoing research aims to overcome these chal-
lenges and enable in vivo monitoring through signal amplification 
and advanced probe design (for example, through the incorporation 
of multiple redox reporters per probe)
108.
DNA-scaffold-based sensors.  DNA-scaffold-based sensors enable 
reagentless detection of proteins, nucleic acids and small molecules, 
relying on DNA frameworks (Fig. 4c). These sensors employ a variety 
of small recognition elements such as peptides that are anchored to 
electrodes by DNA sequences. In addition, these systems typically con-
tain redox reporter molecules within the DNA scaffold that enable elec-
trochemical readout109–113 . DNA-scaffold-based detection is achieved 
through differential access to the electrode surface of bound versus 
unbound probes, often through analyte-mediated steric hindrance, 
which leads to differences in faradaic current. DNA-scaffold-based sen-
sors can detect analytes in complex biological fluids, for example, HIV 
and syphilis antibodies in human serum110,113, making them a promising 
chemical approach for body-based sensing. Even though these sen -
sors work well for small receptors, they are incompatible with larger 
recognition elements such as antibodies owing to slow diffusion and 
low baseline currents. Thus, analytes that lack corresponding small 
receptors, such as many large proteins, are difficult to detect with 
this approach. Using protein-binding DNA can be a solution for this 
challenge114, but these methods are also limited by the availability of 
such recognition elements.
Protein-scaffold-based sensors.  Protein-scaffold-based sensors 
(Fig. 4d) operate on principles similar to those of their DNA counter-
parts, enabling reagentless detection through use of amino acid scaf-
folds115,116. Like DNA scaffolds, protein scaffolds contain an electroactive 
reporter that confers electrochemical activity. However, protein-based 
approaches do not typically involve a separate recognition element, with 
the protein scaffold itself acting as the analyte receptor. Upon binding of 
the protein scaffold to its corresponding analyte, conformational changes 
facilitate the alteration of faradaic current received at the electrode. 
Protein-scaffold-based sensors can enable real-time measurements in 
b  Electrochemical DNA sensors
+Target
e–
a  Electrochemical aptamer sensors
e–
+Target
++
+–
+
+
–
+ –
+ –
–
+ +
e  Nanoscale molecular 
 pendulum sensors
+Target
f  Impedimetric sensors
+Target
++ + +
d  Protein scaﬀold sensors
+Target
e–
c  DNA scaﬀold sensors
+Target
g  Thin-/f.shortilm transistors
+
+
+
+
+
Source
Drain
Channel
Dielectric
Gate
Redox reporter
++++ + +
e–
Fig. 4 | Strategies for reagentless biomolecular analysis. a, Electrochemical 
aptamer-based sensors rely on aptamer binding-induced proximity changes between 
a redox reporter and an electrode. b, Electrochemical DNA sensors use hairpin 
DNA structures to detect DNA through binding-induced redox reporter proximity 
changes. c, DNA scaffold sensors rely on steric hindrance from small receptor-bound 
analytes to alter redox readout. d, Protein scaffold sensors use conformational  
changes in redox-tagged protein receptors to detect bound analytes. e, Nanoscale 
molecular pendulum sensors exploit hydrodynamic differences between bound and 
unbound probes to temporally separate redox readout. f, Impedimetric sensors rely 
on interfacial capacitance changes to detect analyte binding. g, Thin-film transistors 
use interaction-mediated alterations in current flow to detect analyte–receptor  
binding. Part a is reproduced with permission from Xiao, Y ., Lubin, A. A., Heeger, A. J.  
& Plaxco, K. W. Label-free electronic detection of thrombin in blood serum by using 
an aptamer-based sensor. Angew. Chem. Int. Edn Engl. 44, 5456–5459 (2005)
98. 
Copyright Wiley-VCH GmbH. Part b is adapted with permission from Fan, C., Plaxco, 
K. W. & Heeger, A. J. Electrochemical interrogation of conformational changes as a 
reagentless method for the sequence-specific detection of DNA. Proc. Natl Acad. Sci. 
USA 100, 9134–9137 (2003)
104. Copyright (2003) National Academy of Sciences, USA. 
Part e is adapted from ref. 117, Springer Nature Limited.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 569
Review article
biological fluids, for example, for the detection of Fyn kinase peptide 
targets in whole blood115. However, their dependence on protein-based 
receptors greatly limits the range of analytes they can detect.
Molecular pendulum-based sensors. Nanoscale molecular pendu-
lums (NMPs) allow reagentless electrochemical sensing for continuous 
biomarker analysis117 (Fig. 4e). NMPs are comprised of two hybridized 
DNA strands, one of which contains a terminal ferrocene redox reporter 
and the other a terminal antibody. Upon application of a sufficiently 
positive potential, the negatively charged NMPs descend towards the 
electrode surface in a motion resembling that of an inverted pendulum. 
When the terminal ends of the NMPs fall close enough to the electrode 
surface, ferrocene oxidizes and produces a measurable faradaic cur-
rent. Detection with NMPs occurs through differential rates of ferro-
cene oxidation, where hydrodynamic differences between bound and 
unbound antibodies dictate the rate of pendulum descent. This method 
allows detection of proteins and peptides (for example, troponin T, 
brain natriuretic peptide and the interleukin IL-6) in a variety of biologi-
cal fluids, including blood, sweat, and saliva117. NMPs can also detect 
SARS-CoV-2 proteins and whole viruses in untreated clinical saliva 
samples118. However, further theoretical development and optimization 
is required prior to the adoption of NMP sensors in biomedical devices.
Impedance spectroscopy-based sensors. Electrochemical imped-
ance spectroscopy (EIS) (Fig. 4f) is a powerful technique for measuring 
interfacial properties related to electrode-localized molecular recogni-
tion events119. Many EIS sensors rely on faradaic impedance, and thus 
require addition of external redox probes. Alternatively, non-faradaic 
impedance approaches enable reagentless detection without the need 
for sample pretreatment120. Given the detail-rich nature of impedance 
measurements, these non-faradaic methods use alternative parameters 
(for example, double-layer capacitance121) to monitor analyte interaction 
with receptor-functionalized surfaces. Non-faradaic methods allow the 
detection of nucleic acids, proteins and many other analytes continuously 
in complex biological fluids (for example, detection of insulin in serum and 
detection of miRNAs in plasma)122,123. However, because of their depend-
ence on interfacial properties, impedance-based sensors are particularly 
susceptible to surface biofouling; thus, further research into anti-fouling 
strategies is required to apply these techniques in body-based systems87.
Thin-film-transistor-based systems. Thin-film transistors (Fig.  4g) 
are a subset of field-effect transistors (FETs) that can be integrated 
into body-based sensors, showing high sensitivity, great flexibility 
and capacity for real-time continuous sensing 124. Similar to impedi -
metric approaches, FETs rely on interfacial property alterations and 
thus do not require external reporter molecules to indicate molecu -
lar interactions. Promising semiconductors for thin-film transistors 
include organic materials, such as PEDOT:PSS45,46, carbon allotropes125 
and metal oxides71. Although these materials differ in their individual 
properties, for example in their conductivity, they can all facilitate con-
tinuous monitoring of a variety of analyte types in complex biological 
fluids. For example, FETs are used for the detection of amino-terminal 
pro-brain natriuretic peptide (NT-proBNP) in human serum and SARS-
CoV-2 RNA in nasopharyngeal samples 46,126,127. In addition, thin-film 
transistors can be implemented in wearable and implantable systems 
for small molecule sensing in vivo (for example, wearable cortisol 
monitoring in human sweat and serotonin monitoring in mice using 
an implanted neural probe)71,72. However, similar to EIS-based sensors, 
thin-film transistors are susceptible to biofouling and environmental 
degradation128.
Alternative transduction approaches. Besides electrochemical and 
electronic detection, optical approaches can be applied for signal trans-
duction. Here, the distance between a fluorophore and quencher are 
exploited, using optical analogues of E-AB sensors129, E-DNA sensors128, 
DNA/protein-scaffold-based sensors130 and NMP sensors131. Advances 
in fibre optics and nanophotonics have enabled optical body-based 
biomolecular sensors132,133.
The biological fluid frontier
A variety of bodily fluids can be assessed for biomolecular analysis 
(Table 1; Fig. 5). Ideally, a biological fluid should be non-invasively col-
lected or sampled, contain diverse analytes, reflect physiologically 
relevant biomarker concentrations, and capture transient fluctuations 
in targeted biomarkers. In addition, biological fluid sampling should 
be compatible with day-to-day life, such that sensors can take readings 
without the need for user handling.
Urine
Urine is a reliable fluid for at-home biomolecular sensing (for exam-
ple, pregnancy tests) owing to its non-invasive and easy collection. 
Because of its direct derivation from blood, urine contains a wealth of 
molecular information, including metabolites, DNA, RNA and proteins, 
that tend to correlate well with blood concentrations134. In addition, 
urine does not typically undergo proteolytic degradation, as with other 
blood-derived fluids, greatly extending protein lifetime and stability135.  
Table 1 | Comparison of biological fluid suitability for various biomolecular sensing applications
Body fluid Correlation with blood Analyte diversity Glucose lag time Invasiveness Body-based compatibility Can be stimulated?
Urine Medium Low Long Low Wearable No
Blood Not applicable Very high Not applicable High Implantable No
Saliva Low Medium 15 min Low Wearable Yes
Sweat Medium Low 10 min Low Wearable Yes
Tears High Medium 13 min Low Wearable Yes
Interstitial fluid Very high High 5–6 min Medium Wearable, implantable No
Breath Unknown Low Not applicable Low Wearable Not applicable
Digestive fluid Unknown Medium Not applicable Medium Consumable Not applicable

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 570
Review article
However, biomolecules tend to exist in urine at much lower concen-
trations than in blood, which can complicate detection134,135. Further-
more, the long filtration process of urine production reflects analyte 
concentrations over long time frames, which makes analysis of transient 
conditions difficult136. The use of urine in biomolecular sensors is rare, 
but it still may be advantageous over other fluids in diagnosing repro-
ductive cancers135, sexually transmitted diseases137 and other urogeni-
tal conditions. Urine has also been explored as a potential fluid for 
wearable sensor analysis (for example, in diapers)138.
Blood
Blood is the most information-rich biological fluid in the body owing 
to its ubiquitous involvement in homeostasis and transport. Because 
of the diverse biomolecular composition of blood, blood analysis has 
long served as the gold standard for physiological diagnosis. Many 
other body fluids, including interstitial fluid (ISF), saliva, tears and urine 
are derived from blood, making it an excellent reference for alternative 
fluid comparison. Blood is being explored as a potential fluid for in vivo 
body-based sensors139; however, its sampling tends to be invasive and 
risks systemic infections. In addition, blood contains high concentra-
tions of cells and proteins, which can cause biofouling and decrease 
the stability and reliability of sensors over time. Although blood still 
serves as an excellent fluid for laboratory-based analysis and sensor 
comparison, blood derivatives are favoured in the development of 
body-based sensors.
Saliva
Saliva can be easily collected or stimulated 140, and has a diverse 
molecular composition. Although saliva is 99% water, it also contains 
an abundance of small molecules, proteins, DNA, and other molecular 
signatures that can be used to monitor physiology and diagnose dis-
ease141. Saliva is derived from blood plasma; however, its biochemical 
composition has little correlation with that of whole blood142. Therefore, 
the use of salivary markers to monitor physiology requires independent 
validation and testing. Saliva–blood glucose comparisons show decent 
similarity, with lag times of approximately 15 minutes143. Body-based 
sensing wearables for the analysis of saliva include mouthguards and 
pacifiers that can continuously monitor small molecules144,145. Unlike 
physiological markers, exogenous analytes, such as those from bacteria 
or viruses, are typically used in presence-based detection, which makes 
saliva an ideal testing fluid for infectious diseases141,146.
Sweat
Sweat can be non-invasively collected for physiological monitoring147. 
Small-molecule concentrations in sweat have demonstrated good 
correlation with blood, with a reported lag time of 10 minutes for glu-
cose148. However, although wearable sweat sensors have been devel-
oped for ions and other small molecules20,55,149, sweat-based detection 
of proteins and other large molecules remains a challenge150. Protein 
concentrations in sweat correlate with blood concentrations in some 
instances151, but have remained difficult to reliably detect owing to 
their trace concentrations, often unexplored physiological correla-
tion, and a lack of biomarker-focused sweat proteomic analyses147,152. 
Despite these hurdles, protein sensing in sweat has had some success 
(for example, in the detection of cytokines
153,154) and has the potential 
to advance considerably as the physiological distribution of proteins 
in sweat becomes clearer
150.
Sweat collection and sampling is straightforward as its secretion 
can be stimulated through heat, stress, chemicals or iontophoresis in 
addition to passive release
147,155. However, the partitioning of analytes 
into sweat varies with the different stimulation approaches155. Further-
more, sweat composition is largely dependent on sweat rate, which 
influences the degree of analyte dilution155. Ionic strength differences 
among sweat collection conditions alter the electric double layer of 
electronic surfaces, which complicates detection schemes that rely 
on stable Debye parameters51,52. Sweat-based wearables can be incor-
porated into everyday life in the form of watches, tattoos or any other 
product in contact with skin
156.
Tears
T ears have gained attention as a non-invasive fluid for biomolecular 
analysis owing to their external secretion and diverse biochemical 
composition, including metabolites, small molecules and proteins157. 
Although tear composition can differ substantially from that of blood, 
many tear-based analytes correlate closely with their corresponding 
blood concentrations158. T ear analyte concentrations lag behind those 
of blood, with a recorded lag time of approximately 13 minutes for 
glucose159. Advances in flexible electronics have allowed the develop-
ment of fully integrated contact lenses that can sample tears without 
user intervention158 for continuous monitoring of tear glucose160,161. 
However, tear-based sensors face several challenges, including small 
sample volumes, fast evaporation rates and variations in tear secretion 
rates and composition depending on their source of stimulation162– 164.
Tears
Contact lenses Breath
Masks
Saliva 
Mouthguards 
and paci/f.shortiers
Sweat
Watches 
and tattoos
Urine 
Diapers
ISF
Arm patches and 
implantables
Digestive /f.shortluid
Pills
Ocular 
health
General 
purpose
• Microbiome
• Digestive 
health
• Respiratory 
diseases
• Infectious 
diseases
• Oral health
• Infectious 
diseases
• Urogenital 
health
• Sexually 
transmitted 
infections
Metabolic 
de/f.shorticiencies
Fig. 5 | Biological fluid considerations for 
body-based sensing systems. Approaches to 
incorporating body-based sensors into everyday  
life, showing frequently used biological fluids and 
specific applications for these fluids (apart from 
general applications that multiple fluids can be used 
for), and existing commercial products that can 
house these fluid-sampling devices.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 571
Review article
Interstitial fluid
ISF is a promising fluid for biomolecular analysis, owing to its compo-
sitional similarity to blood and potential for non-invasive collection165. 
Analyte partitioning between blood and ISF occurs mainly through con-
tinuous capillaries owing to high capillary densities, low flow rates and 
the ability to exchange even very large proteins (up to 1 MDa). There-
fore, many analytes pass easily between these two fluids and have near-
equal concentrations in both155. However, larger analytes (for example, 
proteins >10 kDa) typically exist at lower concentrations in ISF owing 
to their reliance on more complex transport pathways, with their ISF 
concentrations varying inversely with the logarithm of their molecular 
weight166. Analyte changes in blood are also detected quickly in ISF , 
with the lag time for glucose being approximately 5–6 minutes behind 
that of blood167. Although ISF-based continuous glucose monitors have 
been commercialized (for example, Dexcom’s G6 and Abbott’s Free-
Style Libre continuous glucose monitoring system168), there remains 
a demand for robust and simple ISF collection approaches with high 
extraction efficiency and resistance to potential contamination 155. 
Microneedle patches, containing arrays of micrometre-sized nee -
dles, can be used to sample large volumes of ISF non-invasively169,170. 
Although ISF-based glucose sensing has been extensively optimized, 
fundamental research into ISF analyte partitioning, physiological cor-
relation and lag times will be needed to allow the detection of other 
analytes171.
Breath
Breath contains volatile organic compounds, proteins, fatty acids and 
germ particles that can provide valuable information on physiology 
and disease172. Although the diversity and quantity of biologically 
relevant molecules in breath is lower than in other biological fluids, 
biomolecular breath sensors can be applied to detect small molecules, 
proteins and viruses172– 174. In addition, synthetic biomarkers (for exam-
ple, protease-responsive nanoparticles) may enable breath-based 
detection of various physiological conditions (for example, alpha-1 
antitrypsin deficiency)24. Breath analysis can also be implemented in 
wearable sensors (such as masks) that can directly sample analytes 
from exhaled air132.
Digestive fluids
Digestive fluids may be analysed by consumable electronics (for exam-
ple, diagnostic pills). The molecular biomarkers within digestive flu-
ids are still being explored, but contain an abundance of biochemical 
information relating to health (for example, gut microbiota) 175 and 
disease (for example, digestive system cancers)176. Unlike other bodily 
fluids, digestive fluids are characterized by high acidity and abundant 
enzymes, requiring highly resilient sensors 177. Optical and electro-
chemical sensors can continuously monitor analytes within these 
harsh environments (for example, through amperometric detection 
of glucose in gastric and intestinal fluids178) and demonstrate success 
in animal models (for example, detecting gastrointestinal bleeding in 
swine using a wireless optical readout capsule specific for haem)179. 
Such consumable biomolecular sensors may improve access to and 
analysis of the gastrointestinal tract180.
Outlook
Biomolecular sensing has drawn substantial attention during the ongo-
ing SARS-CoV-2 pandemic, with the rapid development and implemen-
tation of viral antigen tests demonstrating the power of such sensors to 
provide easy access to health information. Whereas glucose monitoring 
has traditionally dominated the biomolecular sensing landscape, 
body-based bioelectronic devices have sparked immense interest in 
the development of continuous sensors for alternative analytes that 
can operate in many body fluids180.
The development of body-based biomolecular sensors requires 
flexible and biocompatible electronic materials that can seamlessly 
interface with soft biological tissues and that can be manufactured 
using inexpensive, facile and easily scalable methods 20,181. Materials 
such as conductive hydrogels and laser-engraved graphene can serve 
as sensing platforms20,182. Additionally, plastics and organic materials 
can serve as substrates and semiconductors benefiting from cost-
efficiency, flexibility and potential biodegradability 183. Metals that 
are fluid at room temperature (for example, gallium) also hold great 
promise for soft electronics development184. Application-dependent 
material considerations are also essential in body-based sensor devel-
opment; for example, wearable sensors that can be integrated into 
clothing as smart textiles are non-intrusive and allow dispersed units 
to communicate easily 185,186. Moreover, implantable sensors made 
with biofilm-resistant materials are resilient to internal physiologi -
cal conditions187, and consumable sensors made with edible, biosafe 
materials are safe for user ingestion188. In addition, materials that can 
harvest biochemical or biomechanical energy (for example, biofuel 
cells189, triboelectric generators 190 and piezoelectric generators 191), 
store energy (for example, supercapacitors192), and enable multi-sensor 
communication (for example, surface-plasmon-like metamaterials193) 
will likely prove vital in the evolution of body-based platforms.
However, the clinical translation of biomolecular sensors will 
require proof of safety. Sensors must be sanitized prior to implementa-
tion194, have low component toxicity195 and minimal immunogenicity196. 
Furthermore, sensors must produce minimal irritation and stimuli (for 
example, loud sounds and bright lights) and they should be comfort-
able to wear197. Moreover, devices must be resistant to cyberattacks or 
other intrusive events198 and ensure user data protection199.
Body-based sensing systems will also advance sensing applica -
tions, such as in personalized healthcare to provide tailored diagnoses, 
interventions and management plans through access to real-time, 
patient-specific biomolecular data. Using this technology, it may be 
possible to identify effective drugs for different illnesses200, monitor 
and optimize drug dosages 201, and detect early signs of disease. In 
addition, body-based sensors can provide preventative information, 
through metabolic and nutritional profiles, for example, to improve 
patient health and avoid disease 202. Body-based systems also show 
promise in the development of advanced closed-loop systems, such 
as an artificial pancreas device capable of monitoring and deliver-
ing insulin, for the treatment of diabetes 203. In addition to diabetes, 
these closed-loop systems may allow the treatment of various health 
conditions related to biomolecular deficiencies (for example, neural 
chemical imbalances and iron-deficiency anaemia).
The next generation of biomolecular sensors aims to advance 
biomolecular analysis by using advanced body-based systems to 
detect diverse analytes in complex biological environments. However, 
there are outstanding challenges regarding adequate signal amplifi-
cation (for example, the need for enhanced sensitivity and flexible 
LoDs), practical continuous measurements (for example, the need for  
regenerable sensing approaches), biological fluid composition  
(for example, the need for strategies to overcome interferences in 
complex media), and device integration (for example, the need for reli-
able and practical sensors) that must be addressed prior to widespread  
adoption.

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 572
Review article
Citation diversity statement
We acknowledge that papers authored by scholars from minoritized 
groups are systematically under-cited. Here, we have made every 
attempt to reference relevant papers in a manner that is equitable in 
terms of racial, ethnic, gender and geographical representation.
Published online: 11 May 2023
References
1. Ji, S. et al. Matching the kinetics of natural enzymes with a single-atom iron nanozyme. 
Nat. Catal. 4, 407–417 (2021).
2. Armstrong, J. A. Urinalysis in Western culture: a brief history. Kidney Int. 71, 384–387 
(2007).
3. Karamanou, M., Protogerou, A., Tsoucalas, G., Androutsos, G. & Poulakou-Rebelakou, E. 
Milestones in the history of diabetes mellitus: the main contributors. World J. Diabetes 7, 
1–7 (2016).
4. Thomas, M. C., Jandeleit-Dahm, K. & Bonnet, F. Beyond glycosuria: exploring the 
intrarenal effects of SGLT-2 inhibition in diabetes. Diabetes Metab. 40, S17–S22 (2014).
5. Guthrie, D. W. & Humphreys, S. S. Diabetes urine testing: an historical perspective. 
Diabetes Educ. 14, 521–525 (1988).
6. Clark, L. C. Jr & Lyons, C. Electrode systems for continuous monitoring in cardiovascular 
surgery. Ann. NY Acad. Sci. 102, 29–45 (1962).  
This article describes the first electrochemical sensing platform that incorporates a 
biorecognition element to provide selectivity for an analyte.
7. Clark, L. C., Kaplan, S., Matthews, E. C., Edwards, F. K. & Helmsworth, J. A. Monitor and 
control of blood oxygen tension and pH during total body perfusion. J. Thorac. Surg. 36, 
488–496 (1958).
8. Free, A. H., Adams, E. C., Kercher, M. L., Free, H. M. & Cook, M. H. Simple specific test for 
urine glucose. Clin. Chem. 3, 163–168 (1957).  
This article describes the first time a biorecognition element was incorporated into a 
sensing mechanism, despite this feat being usually misattributed to Clark and Lyons 
(1962).
9. Mazzaferri, E. L., Skillman, T. G., Lanese, R. R. & Keller, M. P. Use of test strips with colour 
meter to measure blood-glucose. Lancet 295, 331–333 (1970).
10. Chua, K. S. & Tan, I. K. Plasma glucose measurement with the Yellow Springs glucose 
analyzer. Clin. Chem. 24, 150–152 (1978).
11. Clarke, S. F. & Foster, J. R. A history of blood glucose meters and their role in self-
monitoring of diabetes mellitus. Br. J. Biomed. Sci. 69, 83–93 (2012).
12. Matthews, D. R. et al. Pen-sized digital 30-second blood glucose meter. Lancet 329, 
778–779 (1987).
13. Ginsberg, B. H. The FDA panel advises approval of the first continuous glucose sensor. 
Diabetes Technol. Ther. 1, 203–204 (1999).
14. Kelley, S. O. et al. Advancing the speed, sensitivity and accuracy of biomolecular 
detection using multi-length-scale engineering. Nat. Nanotechnol. 9, 969–980 (2014).
15. Sero, J. E. & Stevens, M. M. Nanoneedle-based materials for intracellular studies.  
In Bio-Nanomedicine For Cancer Therapy 191–219 (Springer, 2021).
16. Chiappini, C. et al. Mapping local cytosolic enzymatic activity in human esophageal 
mucosa with porous silicon nanoneedles. Adv. Mater. 27, 5147–5152 (2015).
17. Cao, Y. et al. Nondestructive nanostraw intracellular sampling for longitudinal cell 
monitoring. Proc. Natl Acad. Sci. USA 114, E1866–E1874 (2017).
18. Siciliano, V. et al. Engineering modular intracellular protein sensor–actuator devices.  
Nat. Commun. 9, 1881 (2018).
19. Poste, G. Bring on the biomarkers. Nature 469, 156–157 (2011).
20. Yang, Y. et al. A laser-engraved wearable sensor for sensitive detection of uric acid and 
tyrosine in sweat. Nat. Biotechnol. 38, 217–224 (2020).
21. Weinhofer, I. et al. Neurofilament light chain as a potential biomarker for monitoring 
neurodegeneration in X-linked adrenoleukodystrophy. Nat. Commun. 12, 1816 (2021).
22. Kwong, G. A. et al. Synthetic biomarkers: a twenty-first century path to early cancer 
detection. Nat. Rev. Cancer 21, 655–668 (2021).  
This review describes the development of synthetic biomarkers, including their function 
at the physiological level, their design and how they advance biomolecular sensing.
23. Nishihara, T. et al. Beta-galactosidase-responsive synthetic biomarker for targeted tumor 
detection. Chem. Commun. 54, 11745–11748 (2018).
24. Chan, L. W. et al. Engineering synthetic breath biomarkers for respiratory disease.  
Nat. Nanotechnol. 15, 792–800 (2020).
25. Aalipour, A. et al. Engineered immune cells as highly sensitive cancer diagnostics.  
Nat. Biotechnol. 37, 531–539 (2019).
26. Chen, J. et al. Glucose-oxidase like catalytic mechanism of noble metal nanozymes.  
Nat. Commun. 12, 3375 (2021).
27. Liu, S. et al. Metal–organic frameworks and their derivatives as signal amplification 
elements for electrochemical sensing. Coord. Chem. Rev. 424, 213520 (2020).
28. Huang, Y., Ren, J. & Qu, X. Nanozymes: classification, catalytic mechanisms, activity 
regulation, and applications. Chem. Rev. 119, 4357–4412 (2019).
29. Hu, W.-C. et al. Ultrasensitive detection of bacteria using a 2D MOF nanozyme-amplified 
electrochemical detector. Anal. Chem. 93, 8544–8552 (2021).
30. Huang, L., Chen, J., Gan, L., Wang, J. & Dong, S. Single-atom nanozymes. Sci. Adv. 5, 
eaav5490 (2019).
31. Jiao, L. et al. Single-atom catalysts boost signal amplification for biosensing. Chem. Soc. 
Rev. 50, 750–765 (2021).
32. Wang, Z. et al. Accelerated discovery of superoxide-dismutase nanozymes via high-
throughput computational screening. Nat. Commun. 12, 6866 (2021).
33. Zhong, M. et al. Accelerated discovery of CO
2 electrocatalysts using active machine 
learning. Nature 581, 178–183 (2020).
34. McConnell, E. M. et al. Biosensing with DNAzymes. Chem. Soc. Rev. 50, 8954–8994 
(2021).
35. Borggräfe, J. et al. Time-resolved structural analysis of an RNA-cleaving DNA catalyst. 
Nature 601, 144–149 (2022).
36. Liu, K., Lat, P. K., Yu, H.-Z. & Sen, D. CLICK-17, a DNA enzyme that harnesses ultra-low 
concentrations of either Cu+ or Cu2+ to catalyze the azide–alkyne ‘click’ reaction in water. 
Nucleic Acids Res. 48, 7356–7370 (2020).
37. Liu, M. et al. Programming a topologically constrained DNA nanostructure into a sensor. 
Nat. Commun. 7, 12074 (2016).
38. Kang, D.-K. et al. Rapid detection of single bacteria in unprocessed blood using 
integrated comprehensive droplet digital detection. Nat. Commun. 5, 5427 (2014).
39. Shen, J., Liu, G., Han, Y. & Jin, W. Artificial channels for confined mass transport at the 
sub-nanometre scale. Nat. Rev. Mater. 6, 294–312 (2021).
40. de Angelis, F. et al. Breaking the diffusion limit with super-hydrophobic delivery of 
molecules to plasmonic nanofocusing SERS structures. Nat. Photon. 5, 682–687 (2011).
41. Morales-Narváez, E., Guix, M., Medina-Sánchez, M., Mayorga-Martinez, C. C. & Merkoçi, 
A. Micromotor enhanced microarray technology for protein detection. Small 10, 
2542–2548 (2014).
42. Lin, M. et al. Programmable engineering of a biosensing interface with tetrahedral DNA 
nanostructures for ultrasensitive DNA detection. Angew. Chem. 127, 2179–2183 (2015).
43. Zhang, P. et al. Ultrasensitive detection of circulating exosomes with a 3D-nanopatterned 
microfluidic chip. Nat. Biomed. Eng. 3, 438–451 (2019).
44. Rivnay, J. et al. Organic electrochemical transistors. Nat. Rev. Mater. 3, 17086 (2018).  
This review describes the evolution of organic electrochemical transistors, including 
their fabrication, various configurations and their ability to amplify biochemical 
signals.
45. Rivnay, J. et al. Organic electrochemical transistors with maximum transconductance at 
zero gate bias. Adv. Mater. 25, 7010–7014 (2013).
46. Pappa, A. M. et al. Direct metabolite detection with an n-type accumulation mode 
organic electrochemical transistor. Sci. Adv. 4, eaat0911 (2018).
47. Liang, Y., Wu, C., Figueroa-Miranda, G., Offenhäusser, A. & Mayer, D. Amplification 
of aptamer sensor signals by four orders of magnitude via interdigitated organic 
electrochemical transistors. Biosens. Bioelectron. 144, 111668 (2019).
48. Ersman, P. A. et al. All-printed large-scale integrated circuits based on organic 
electrochemical transistors. Nat. Commun. 10, 5053 (2019).
49. Jarczewska, M., Rębiś, J., Górski, Ł. & Malinowska, E. Development of DNA aptamer-
based sensor for electrochemical detection of C-reactive protein. Talanta 189,  
45–54 (2018).
50. Reiber, T., Zavoiura, O., Dose, C. & Yushchenko, D. A. Fluorophore multimerization as an 
efficient approach towards bright protein labels. Eur. J. Org. Chem. 2021, 2817–2830 
(2021).
51. Nakatsuka, N. et al. Aptamer-field-effect transistors overcome Debye length limitations 
for small-molecule sensing. Science 362, 319–324 (2018).
52. Kesler, V., Murmann, B. & Soh, H. T. Going beyond the Debye length: overcoming 
charge screening limitations in next-generation bioelectronic sensors. ACS Nano 14, 
16194–16201 (2020).
53. Fu, K. et al. Accelerated electron transfer in nanostructured electrodes improves the 
sensitivity of electrochemical biosensors. Adv. Sci. 8, 2102495 (2021).
54. Lee, D. et al. Ionic contrast across a lipid membrane for Debye length extension: towards 
an ultimate bioelectronic transducer. Nat. Commun. 12, 3741 (2021).
55. Gao, W. et al. Fully integrated wearable sensor arrays for multiplexed in situ perspiration 
analysis. Nature 529, 509–514 (2016).
56. Cui, F., Yue, Y., Zhang, Y., Zhang, Z. & Zhou, H. S. Advancing biosensors with machine 
learning. ACS Sens. 5, 3346–3364 (2020).
57. King, R. C. et al. Application of data fusion techniques and technologies for wearable 
health monitoring. Med. Eng. Phys. 42, 1–12 (2017).
58. Habib, C., Makhoul, A., Darazi, R. & Salim, C. Self-adaptive data collection and fusion for 
health monitoring based on body sensor networks. IEEE Trans. Ind. Inf. 12, 2342–2352 
(2016).
59. Yu, X., Yang, Y.-P., Dikici, E., Deo, S. K. & Daunert, S. Beyond antibodies as binding 
partners: the role of antibody mimetics in bioanalysis. Annu. Rev. Anal. Chem. 10, 
293–320 (2017).
60. Belbruno, J. J. Molecularly imprinted polymers. Chem. Rev. 119, 94–119 (2019).
61. Muyldermans, S. Nanobodies: natural single-domain antibodies. Annu. Rev. Biochem. 82, 
775–797 (2013).
62. Silverman, J. et al. Multivalent avimer proteins evolved by exon shuffling of a family of 
human receptor domains. Nat. Biotechnol. 23, 1556–1561 (2005).
63. Tiede, C. et al. Affimer proteins are versatile and renewable affinity reagents. eLife 6, 
e24903 (2017).
64. Löfblom, J. et al. Affibody molecules: engineered proteins for therapeutic, diagnostic 
and biotechnological applications. FEBS Lett. 584, 2670–2680 (2010).
65. Bratkovič, T. Progress in phage display: evolution of the technique and its applications. 
Cell. Mol. Life Sci. 67, 749–767 (2010).

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 573
Review article
66. Bradbury, A. R. M., Sidhu, S., Dübel, S. & McCafferty, J. Beyond natural antibodies: the 
power of in vitro display technologies. Nat. Biotechnol. 29, 245–254 (2011).
67. Tuerk, C. & Gold, L. Systematic evolution of ligands by exponential enrichment: RNA 
ligands to bacteriophage T4 DNA polymerase. Science 249, 505–510 (1990).
68. Ellington, A. D. & Szostak, J. W. In vitro selection of RNA molecules that bind specific 
ligands. Nature 346, 818–822 (1990).
69. Qian, S., Chang, D., He, S. & Li, Y. Aptamers from random sequence space: 
accomplishments, gaps and future considerations. Anal. Chim. Acta 1196, 339511 (2022).
70. Yu, H., Alkhamis, O., Canoura, J., Liu, Y. & Xiao, Y. Advances and challenges in small-
molecule DNA aptamer isolation, characterization, and sensor development. Angew. 
Chem. Int. Edn 60, 16800–16823 (2021).
71. Wang, B. et al. Wearable aptamer-field-effect transistor sensing system for noninvasive 
cortisol monitoring. Sci. Adv. 8, eabk0967 (2022).  
This article demonstrates a fully integrated body-based sensing platform for the 
continuous detection of cortisol using field-effect transistors and aptamer recognition 
elements.
72. Zhao, C. et al. Implantable aptamer-field-effect transistor neuroprobes for in vivo 
neurotransmitter monitoring. Sci. Adv. 7, eabj7422 (2021).
73. Frutiger, A. et al. Nonspecific binding — fundamental concepts and consequences for 
biosensing applications. Chem. Rev. 121, 8095–8160 (2021).  
This review provides a detailed analysis of non-specific binding, including its history, 
physiological causes and solutions to overcome its effects.
74. Gawande, B. N. et al. Selection of DNA aptamers with two modified bases. Proc. Natl 
Acad. Sci. USA 114, 2898–2903 (2017).
75. Yoshikawa, A. M. et al. Discovery of indole-modified aptamers for highly specific 
recognition of protein glycoforms. Nat. Commun. 12, 7106 (2021).
76. Wang, J. et al. Multiparameter particle display (MPPD): a quantitative screening method 
for the discovery of highly specific aptamers. Angew. Chem. Int. Edn Engl. 129, 762–765 
(2017).
77. Zhou, J. & Rossi, J. Aptamers as targeted therapeutics: current potential and challenges. 
Nat. Rev. Drug. Discov. 16, 181–202 (2017).
78. Gerling, T., Kube, M., Kick, B. & Dietz, H. Sequence-programmable covalent bonding of 
designed DNA assemblies. Sci. Adv. 4, eaau1157 (2018).
79. Anastassacos, F. M., Zhao, Z., Zeng, Y. & Shih, W. M. Glutaraldehyde cross-linking of 
oligolysines coating DNA origami greatly reduces susceptibility to nuclease degradation. 
J. Am. Chem. Soc. 142, 3311–3315 (2020).
80. Biedermann, F. & Schneider, H.-J. Experimental binding energies in supramolecular 
complexes. Chem. Rev. 116, 5216–5300 (2016).
81. Bixler, G. D. & Bhushan, B. Biofouling: lessons from nature. Phil. Trans. R. Soc. A 370, 
2381–2417 (2012).
82. Ostuni, E. et al. Self-assembled monolayers that resist the adsorption of proteins and the 
adhesion of bacterial and mammalian cells. Langmuir 17, 6336–6343 (2001).
83. Liu, S. & Guo, W. Anti-biofouling and healable materials: preparation, mechanisms, and 
biomedical applications. Adv. Funct. Mater. 28, 1800596 (2018).
84. Li, S. et al. Slippery liquid-infused microphase separation surface enables highly robust 
anti-fouling, anti-corrosion, anti-icing and anti-scaling coating on diverse substrates. 
Chem. Eng. J. 431, 133945 (2022).
85. Zhang, L. et al. Zwitterionic hydrogels implanted in mice resist the foreign-body reaction. 
Nat. Biotechnol. 31, 553–556 (2013).
86. Chan, D. et al. Combinatorial polyacrylamide hydrogels for preventing biofouling on 
implantable biosensors. Adv. Mater. 34, 2109764 (2022).
87. del Río, J. S., Henry, O. Y. F., Jolly, P. & Ingber, D. E. An antifouling coating that enables 
affinity-based electrochemical biosensing in complex biological fluids.  
Nat. Nanotechnol. 14, 1143–1149 (2019).
88. Timilsina, S. S. et al. Ultrarapid method for coating electrochemical sensors with 
antifouling conductive nanomaterials enables highly sensitive multiplexed detection  
in whole blood. Adv. Healthc. Mater. 11, 2102244 (2022).
89. Shiddiky, M. J. A., Vaidyanathan, R., Rauf, S., Tay, Z. & Trau, M. Molecular nanoshearing:  
an innovative approach to shear off molecules with AC-induced nanoscopic fluid flow. 
Sci. Rep. 4, 3716 (2014).
90. Xue, L. et al. Solid-state nanopore sensors. Nat. Rev. Mater. 5, 931–951 (2020).
91. Yang, B., Jiang, X., Fang, X. & Kong, J. Wearable chem-biosensing devices: from basic 
research to commercial market. Lab Chip 21, 4285–4310 (2021).
92. Fercher, C., Jones, M. L., Mahler, S. M. & Corrie, S. R. Recombinant antibody engineering 
enables reversible binding for continuous protein biosensing. ACS Sens. 6, 764–776 (2021).
93. Wilson, B. D. & Soh, H. T. Re-evaluating the conventional wisdom about binding assays. 
Trends Biochem. Sci. 45, 639–649 (2020).
94. Goode, J. A., Rushworth, J. V. H. & Millner, P. A. Biosensor regeneration: a review of 
common techniques and outcomes. Langmuir 31, 6267–6276 (2015).
95. Delport, F. et al. Real-time monitoring of DNA hybridization and melting processes using 
a fiber optic sensor. Nanotechnology 23, 065503 (2012).
96. Gilles, P. N., Wu, D. J., Foster, C. B., Dillon, P. J. & Chanock, S. J. Single nucleotide 
polymorphic discrimination by an electronic dot blot assay on semiconductor 
microchips. Nat. Biotechnol. 17, 365–370 (1999).
97. Clifford, A. et al. Strategies for biomolecular analysis and continuous physiological 
monitoring. J. Am. Chem. Soc. 143, 5281–5294 (2021).
98. Xiao, Y., Lubin, A. A., Heeger, A. J. & Plaxco, K. W. Label-free electronic detection of 
thrombin in blood serum by using an aptamer-based sensor. Angew. Chem. Int. Edn Engl. 
44, 5456–5459 (2005).
99. Arroyo-Currás, N. et al. Real-time measurement of small molecules directly in awake, 
ambulatory animals. Proc. Natl Acad. Sci. USA 114, 645–650 (2017).
100. Dauphin-Ducharme, P., Ploense, K. L., Arroyo-Currás, N., Kippin, T. E. & Plaxco, K. W. 
Electrochemical aptamer-based sensors: a platform approach to high-frequency 
molecular monitoring in situ in the living body. Biomed. Eng. Technol. 2393, 479–492 
(2022).
101. Ferguson, B. S. et al. Real-time, aptamer-based tracking of circulating therapeutic agents 
in living animals. Sci. Transl. Med. 5, 213ra165 (2013).
102. Idili, A., Gerson, J., Kippin, T. & Plaxco, K. W. Seconds-resolved, in situ measurements 
of plasma phenylalanine disposition kinetics in living rats. Anal. Chem. 93, 4023–4032 
(2021).
103. Seo, J. W. et al. Real-time monitoring of drug pharmacokinetics within tumor tissue in live 
animals. Sci. Adv. 8, eabk2901 (2022).  
This article describes the real-time monitoring of doxorubicin in animal tumour tissue, 
demonstrating the effectiveness of reagentless sensing approaches in animal models.
104. Fan, C., Plaxco, K. W. & Heeger, A. J. Electrochemical interrogation of conformational 
changes as a reagentless method for the sequence-specific detection of DNA. Proc. Natl 
Acad. Sci. USA 100, 9134–9137 (2003).
105. Xiao, Y., Lubin, A. A., Baker, B. R., Plaxco, K. W. & Heeger, A. J. Single-step electronic 
detection of femtomolar DNA by target-induced strand displacement in an electrode-
bound duplex. Proc. Natl Acad. Sci. USA 103, 16677–16680 (2006).
106. Li, C. et al. Design of DNA nanostructure-based interfacial probes for the electrochemical 
detection of nucleic acids directly in whole blood. Chem. Sci. 9, 979–984 (2018).
107. Yu, H. L. L., Maslova, A. & Hsing, I.-M. Rational design of electrochemical DNA biosensors 
for point-of-care applications. ChemElectroChem 4, 795–805 (2017).
108. Wang, M. et al. A reagentless triplex DNA junctions-based electrochemical DNA sensor 
using signal amplification strategy of CHA and tetraferrocene. Sens. Actuators B 358, 
131496 (2022).
109. Ranallo, S., Porchetta, A. & Ricci, F. DNA-based scaffolds for sensing applications.  
Anal. Chem. 91, 44–59 (2019).
110. Parolo, C. et al. E-DNA scaffold sensors and the reagentless, single-step, measurement  
of HIV-diagnostic antibodies in human serum. Microsyst. Nanoeng. 6, 13 (2020).
111. Cash, K. J., Ricci, F. & Plaxco, K. W. An electrochemical sensor for the detection of 
protein–small molecule interactions directly in serum and other complex matrices.  
J. Am. Chem. Soc. 131, 6955–6957 (2009).
112. White, R. J. et al. Wash-free, electrochemical platform for the quantitative, multiplexed 
detection of specific antibodies. Anal. Chem. 84, 1098–1103 (2012).
113. Ogden, N. E., Kurnik, M., Parolo, C. & Plaxco, K. W. An electrochemical scaffold sensor for 
rapid syphilis diagnosis. Analyst 144, 5277–5283 (2019).
114. Ricci, F., Bonham, A. J., Mason, A. C., Reich, N. O. & Plaxco, K. W. Reagentless, 
electrochemical approach for the specific detection of double- and single-stranded DNA 
binding proteins. Anal. Chem. 81, 1608–1614 (2009).
115. Kurnik, M., Pang, E. Z. & Plaxco, K. W. An electrochemical biosensor architecture based 
on protein folding supports direct real-time measurements in whole blood. Angew. 
Chem. Int. Edn 59, 18442–18445 (2020).
116. Kang, D. et al. New architecture for reagentless, protein-based electrochemical 
biosensors. J. Am. Chem. Soc. 139, 12113–12116 (2017).
117. Das, J. et al. Reagentless biomolecular analysis using a molecular pendulum. Nat. Chem. 
13, 428–434 (2021).
118. Yousefi, H. et al. Detection of SARS-CoV-2 viral particles using direct, reagent-free 
electrochemical sensing. J. Am. Chem. Soc. 143, 1722–1727 (2021).
119. Bertok, T. et al. Electrochemical impedance spectroscopy based biosensors: mechanistic 
principles, analytical examples and challenges towards commercialization for assays of 
protein cancer biomarkers. ChemElectroChem 6, 989–1003 (2019).
120. Flauzino, J. M. R. et al. Label-free and reagentless electrochemical genosensor based  
on graphene acid for meat adulteration detection. Biosens. Bioelectron. 195, 113628 
(2022).
121. Cecchetto, J., Fernandes, F. C. B., Lopes, R. & Bueno, P. R. The capacitive sensing of NS1 
Flavivirus biomarker. Biosens. Bioelectron. 87, 949–956 (2017).
122. Capaldo, P. et al. Circulating disease biomarker detection in complex matrices: real-time, 
in situ measurements of DNA/miRNA hybridization via electrochemical impedance 
spectroscopy. ACS Sens. 1, 1003–1010 (2016).
123. Luo, X., Xu, M., Freeman, C., James, T. & Davis, J. J. Ultrasensitive label free electrical 
detection of insulin in neat blood serum. Anal. Chem. 85, 4129–4134 (2013).
124. Kergoat, L., Piro, B., Berggren, M., Horowitz, G. & Pham, M.-C. Advances in organic 
transistor-based biosensors: from organic electrochemical transistors to electrolyte-
gated organic field-effect transistors. Anal. Bioanal. Chem. 402, 1813–1826 (2012).
125. Hajian, R. et al. Detection of unamplified target genes via CRISPR–Cas9 immobilized  
on a graphene field-effect transistor. Nat. Biomed. Eng. 3, 427–437 (2019).
126. Wang, L. et al. Rapid and ultrasensitive electromechanical detection of ions, 
biomolecules and SARS-CoV-2 RNA in unamplified samples. Nat. Biomed. Eng. 6, 
276–285 (2022).
127. Tai, T. Y. et al. Design and demonstration of tunable amplified sensitivity of AlGaN/GaN 
high electron mobility transistor (HEMT)-based biosensors in human serum. Anal. Chem. 
91
, 5953–5960 (2019).
128. Tyagi, S., Bratu, D. P. & Kramer, F. R. Multicolor molecular beacons for allele 
discrimination. Nat. Biotechnol. 16, 49–53 (1998).
129. Tuleuova, N. et al. Development of an aptamer beacon for detection of interferon-gamma. 
Anal. Chem. 82, 1851–1857 (2010).

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575 574
Review article
130. Bai, Y., Shu, T., Su, L. & Zhang, X. Functional nucleic acid-based fluorescence 
polarization/anisotropy biosensors for detection of biomarkers. Anal. Bioanal. Chem. 412, 
6655–6665 (2020).
131. Kruse, M. et al. Measuring influenza A virus and peptide interaction using electrically 
controllable DNA nanolevers. Adv. Mater. Technol. 7, 2101141 (2021).
132. Nguyen, P. Q. et al. Wearable materials with embedded synthetic biology sensors for 
biomolecule detection. Nat. Biotechnol. 39, 1366–1374 (2021).
133. Oh, S.-H. et al. Nanophotonic biosensors harnessing van der Waals materials. Nat. 
Commun. 12, 3824 (2021).
134. Aitekenov, S., Gaipov, A. & Bukasov, R. Review: Detection and quantification of proteins  
in human urine. Talanta 223, 121718 (2021).
135. Ploussard, G. & de La Taille, A. Urine biomarkers in prostate cancer. Nat. Rev. Urol. 7, 
101–109 (2010).
136. Gray, M. et al. Implantable biosensors and their contribution to the future of precision 
medicine. Vet. J. 239, 21–29 (2018).
137. Soler, M. et al. Multiplexed nanoplasmonic biosensor for one-step simultaneous 
detection of Chlamydia trachomatis and Neisseria gonorrhoeae in urine. Biosens. 
Bioelectron. 94, 560–567 (2017).
138. Zhang, J. et al. A wearable self-powered biosensor system integrated with diaper  
for detecting the urine glucose of diabetic patients. Sens. Actuators B 341, 130046 
(2021).
139. Lager, W. et al. Implantable electrocatalytic glucose sensor. Horm. Metab. Res. 26, 
526–530 (1994).
140. Topkas, E., Keith, P., Dimeski, G., Cooper-White, J. & Punyadeera, C. Evaluation of saliva 
collection devices for the analysis of proteins. Clin. Chim. Acta 413, 1066–1070 (2012).
141. Zhang, C.-Z. et al. Saliva in the diagnosis of diseases. Int. J. Oral. Sci. 8, 133–137 (2016).
142. Bel’skaya, L. V., Sarf, E. A. & Kosenok, V. K. Age and gender characteristics of the 
biochemical composition of saliva: correlations with the composition of blood plasma.  
J. Oral Biol. Craniofac. Res. 10, 59–65 (2020).
143. Lin, C. et al. Toward the development of a glucose dehydrogenase-based saliva glucose 
sensor without the need for sample preparation. J. Diabetes Sci. Technol. 12, 83–89 
(2018).
144. Arakawa, T. et al. Mouthguard biosensor with telemetry system for monitoring of saliva 
glucose: a novel cavitas sensor. Biosens. Bioelectron. 84, 106–111 (2016).
145. García-Carmona, L. et al. Pacifier biosensor: toward noninvasive saliva biomarker 
monitoring. Anal. Chem. 91, 13883–13891 (2019).
146. Kevadiya, B. D. et al. Diagnostics for SARS-CoV-2 infections. Nat. Mater. 20, 593–605 
(2021).
147. Bariya, M., Nyein, H. Y. Y. & Javey, A. Wearable sweat sensors. Nat. Electron. 1, 160–171 
(2018).
148. la Count, T. D., Jajack, A., Heikenfeld, J. & Kasting, G. B. Modeling glucose transport from 
systemic circulation to sweat. J. Pharm. Sci. 108, 364–371 (2019).
149. He, W. et al. Integrated textile sensor patch for real-time and multiplex sweat analysis. 
Sci. Adv. 5, eaax0649 (2019).
150. Pérez, D. & Orozco, J. Wearable electrochemical biosensors to measure biomarkers with 
complex blood-to-sweat partition such as proteins and hormones. Microchim. Acta 189, 
127 (2022).
151. Cizza, G. et al. Elevated neuroimmune biomarkers in sweat patches and plasma of 
premenopausal women with major depressive disorder in remission: the P.O.W.E.R. study. 
Biol. Psychiat. 64, 907–911 (2008).
152. Qiao, L., Benzigar, M. R., Subramony, J. A., Lovell, N. H. & Liu, G. Advances in sweat 
wearables: sample extraction, real-time biosensing, and flexible platforms. ACS Appl. 
Mater. Interf. 12, 34337–34361 (2020).
153. Jagannath, B. et al. Novel approach to track the lifecycle of inflammation from 
chemokine expression to inflammatory proteins in sweat using electrochemical 
biosensor. Adv. Mater. Technol. 7, 2101356 (2022).
154. Jagannath, B. et al. Temporal profiling of cytokines in passively expressed sweat for 
detection of infection using wearable device. Bioeng. Transl. Med. 6, e10220 (2021).
155. Heikenfeld, J. et al. Accessing analytes in biofluids for peripheral biochemical 
monitoring. Nat. Biotechnol. 37, 407–419 (2019).  
This review discusses opportunities and challenges for biomolecular sensing in 
various biological fluids, with information on biological fluid generation, analyte 
partitioning and sampling technologies.
156. Kaya, T. et al. Wearable sweat sensors: background and current trends. Electroanalysis 
31, 411–421 (2019).
157. You, J. et al. Tear fluid protein biomarkers. Adv. Clin. Chem. 62, 151–196 (2013).
158. Farandos, N. M., Yetisen, A. K., Monteiro, M. J., Lowe, C. R. & Yun, S. H. Contact lens 
sensors in ocular diagnostics. Adv. Healthc. Mater. 4, 792–810 (2015).
159. la Belle, J. T. et al. Self-monitoring of tear glucose: the development of a tear based 
glucose sensor as an alternative to self-monitoring of blood glucose. Chem. Commun. 
52, 9197–9204 (2016).
160. Kim, J. et al. Wearable smart sensor systems integrated on soft contact lenses for 
wireless ocular diagnostics. Nat. Commun. 8, 14997 (2017).
161. Elsherif, M., Hassan, M. U., Yetisen, A. K. & Butt, H. Wearable contact lens biosensors for 
continuous glucose monitoring using smartphones. ACS Nano 12, 5452–5462 (2018).
162. Kim, J., Campbell, A. S., de Ávila, B. E. F. & Wang, J. Wearable biosensors for healthcare 
monitoring. Nat. Biotechnol. 37, 389–406 (2019).
163. Sempionatto, J. R., Jeerapan, I., Krishnan, S. & Wang, J. Wearable chemical sensors: 
emerging systems for on-body analytical chemistry. Anal. Chem. 92, 378–396 (2020).
164. Stuchell, R. N., Feldman, J. J., Farris, R. L. & Mandel, I. D. The effect of collection 
technique on tear composition. Invest. Ophthalmol. Vis. Sci. 25, 374–377 (1984).
165. Kim, Y. & Prausnitz, M. R. Sensitive sensing of biomarkers in interstitial fluid. Nat. Biomed. 
Eng. 5, 3–5 (2021).
166. Vermeer, B. J., Reman, F. C. & van Gent, C. M. The determination of lipids and proteins in 
suction blister fluid. J. Investig. Dermatol. 73, 303–305 (1979).
167. Basu, A. et al. Time lag of glucose from intravascular to interstitial compartment in 
humans. Diabetes 62, 4083–4087 (2013).
168. Soni, A. et al. A practical approach to continuous glucose monitoring (rtCGM) and 
FreeStyle Libre systems (isCGM) in children and young people with type 1 diabetes. 
Diabetes Res. Clin. Pract. 184, 109196 (2022).
169. Samant, P. P. et al. Sampling interstitial fluid from human skin using a microneedle patch. 
Sci. Transl. Med. 12, eaaw0285 (2020).
170. Samant, P. P. & Prausnitz, M. R. Mechanisms of sampling interstitial fluid from skin using a 
microneedle patch. Proc. Natl Acad. Sci. USA 115, 4583–4588 (2018).
171. Friedel, M. et al. Opportunities and challenges in the diagnostic utility of dermal 
interstitial fluid. Nat. Biomed. Eng. https://doi.org/10.1038/s41551-022-00998-9 (2023).  
This Perspective provides a detailed analysis of the opportunities and challenges 
related to interstitial-fluid-based sensing and provides a roadmap for future interstitial 
fluid sensor development.
172. Vasilescu, A., Hrinczenko, B., Swain, G. M. & Peteu, S. F. Exhaled breath biomarker 
sensing. Biosens. Bioelectron. 182, 113193 (2021).
173. Chen, H. et al. Automated in vivo nanosensing of breath-borne protein biomarkers.  
Nano Lett. 18, 4716–4726 (2018).
174. Ates, H. C. & Dincer, C. Wearable breath analysis. Nat. Rev. Bioeng. 1, 80–82 (2023).
175. McBurney, M. I. et al. Establishing what constitutes a healthy human gut microbiome: 
state of the science, regulatory considerations, and future directions. J. Nutr. 149, 
1882–1895 (2019).
176. Melton, S. D., Genta, R. M. & Souza, R. F. Biomarkers and molecular diagnosis of 
gastrointestinal and pancreatic neoplasms. Nat. Rev. Gastroenterol. Hepatol. 7, 620–628 
(2010).
177. Salama, R., Arshavsky-Graham, S., Sella-Tavor, O., Massad-Ivanir, N. & Segal, E. Design 
considerations of aptasensors for continuous monitoring of biomarkers in digestive tract 
fluids. Talanta 239, 123124 (2022).
178. Ruiz-Valdepeñas Montiel, V. et al. Direct electrochemical biosensing in gastrointestinal 
fluids. Anal. Bioanal. Chem. 411, 4597–4604 (2019).
179. Mimee, M. et al. An ingestible bacterial-electronic system to monitor gastrointestinal 
health. Science 360, 915–918 (2018).
180. Beardslee, L. A. et al. Ingestible sensors and sensing systems for minimally invasive 
diagnosis and monitoring: the next frontier in minimally invasive screening. ACS Sens. 5, 
891–910 (2020).
181. Yang, Y. & Gao, W. Wearable and flexible electronics for continuous molecular 
monitoring. Chem. Soc. Rev. 48, 1465–1491 (2019).
182. Wang, L., Xu, T. & Zhang, X. Multifunctional conductive hydrogel-based flexible wearable 
sensors. TrAC Trends Anal. Chem. 134, 116130 (2021).
183. Someya, T., Bao, Z. & Malliaras, G. G. The rise of plastic bioelectronics. Nature 540, 
379–385 (2016).
184. Park, Y.-G. et al. Liquid metal-based soft electronics for wearable healthcare. Adv. 
Healthc. Mater. 10, 2002280 (2021).
185. Libanori, A., Chen, G., Zhao, X., Zhou, Y. & Chen, J. Smart textiles for personalized 
healthcare. Nat. Electron. 5, 142–156 (2022).
186. Wang, L. et al. Functionalized helical fibre bundles of carbon nanotubes as 
electrochemical sensors for long-term in vivo monitoring of multiple disease biomarkers. 
Nat. Biomed. Eng. 4, 159–171 (2020).
187. Shah, S. R., Tatara, A. M., D’Souza, R. N., Mikos, A. G. & Kasper, F. K. Evolving strategies  
for preventing biofilm on implantable materials. Mater. Today 16, 177–182 (2013).
188. Kim, J. et al. Edible electrochemistry: food materials based electrochemical sensors.  
Adv. Healthc. Mater. 6, 1700770 (2017).
189. Yin, L. et al. A passive perspiration biofuel cell: high energy return on investment. Joule 5, 
1888–1904 (2021).
190. Hinchet, R. et al. Transcutaneous ultrasound energy harvesting using capacitive 
triboelectric technology. Science 365, 491–494 (2019).
191. Ali, F., Raza, W., Li, X., Gul, H. & Kim, K.-H. Piezoelectric energy harvesters for biomedical 
applications. Nano Energy 57, 879–902 (2019).
192. Jeong, Y. R., Lee, G., Park, H. & Ha, J. S. Stretchable, skin-attachable electronics with 
integrated energy storage devices for biosignal monitoring. Acc. Chem. Res. 52, 91–99 
(2019).
193. Hajiaghajani, A. et al. Textile-integrated metamaterials for near-field multibody area 
networks. Nat. Electron. 4, 808–817 (2021).
194. Chung, J., Sepunaru, L. & Plaxco, K. W. On the disinfection of electrochemical aptamer-
based sensors. ECS Sens. Plus 1, 011604 (2022).
195. Zhang, Y., Bindra, D. S., Barrau, M.-B. & Wilson, G. S. Application of cell culture toxicity 
tests to the development of implantable biosensors. Biosens. Bioelectron. 6, 653–661 
(1991).
196. Avula, M. N., Rao, A. N., McGill, L. D., Grainger, D. W. & Solzbacher, F. Foreign body 
response to subcutaneous biomaterial implants in a mast cell-deficient Kit(w-Sh) murine 
model. Acta Biomater. 10, 1856–1863 (2014).
197. Fang, Y.-M. & Chang, C.-C. Users’ psychological perception and perceived readability  
of wearable devices for elderly people. Behav. Inf. Technol. 35, 225–232 (2016).

Nature Reviews Bioengineering | Volume 1 | August 2023 | 560–575
 575
Review article
198. Pycroft, L. & Aziz, T. Z. Security of implantable medical devices with wireless 
connections: the dangers of cyber-attacks. Expert Rev. Med. Devices 15, 403–406  
(2018).
199. Sadowski, J., Viljoen, S. & Whittaker, M. Everyone should decide how their digital data are 
used — not just tech companies. Nature 595, 169–171 (2021).
200. Teymourian, H. et al. Wearable electrochemical sensors for the monitoring and screening 
of drugs. ACS Sens. 5, 2679–2700 (2020).
201. Goud, K. Y. et al. Wearable electrochemical microneedle sensor for continuous 
monitoring of Levodopa: toward Parkinson management. ACS Sens. 4, 2196–2204 
(2019).
202. Sempionatto, J. R., Montiel, V. R.-V., Vargas, E., Teymourian, H. & Wang, J. Wearable and 
mobile sensors for personalized nutrition. ACS Sens. 6, 1745–1760 (2021).
203. Thabit, H. & Hovorka, R. Coming of age: the artificial pancreas for type 1 diabetes. 
Diabetologia 59, 1795–1805 (2016).
204. Biosensors market size by type (wearable, non-wearable), by technology (electrochemical, 
optical, thermal, piezoelectric), by medical application (blood glucose testing, cholesterol 
testing, blood gas analysis, pregnancy testing, drug discovery. Global Market Insights 
https://www.gminsights.com/industry-analysis/biosensors-market (2022).
Acknowledgements
The authors thank A. Jiao for her illustrative contributions to the manuscript.
Author contributions
All authors contributed to the writing of the manuscript. C.D.F. and S.O.K. edited the 
manuscript.
Competing interests
S.O.K. and H.Y. are cofounders and equity holders in Arma Biosciences, which is 
commercializing new sensing technologies.
Additional information
Peer review information Nature Reviews Bioengineering thanks Chunhai Fan and the other, 
anonymous, reviewer(s) for their contribution to the peer review of this work.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this 
article under a publishing agreement with the author(s) or other rightsholder(s); author self-
archiving of the accepted manuscript version of this article is solely governed by the terms  
of such publishing agreement and applicable law.
© Springer Nature Limited 2023