Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 346
nature reviews bioengineering
Review article
https://doi.org/10.1038/s44222-023-00032-w
 Check for updates
Device integration of 
electrochemical biosensors
Jie Wu    1,4, Hong Liu    2,4, Weiwei Chen1,3, Biao Ma2 & Huangxian Ju    1 
Abstract
Electrochemical biosensors incorporate a recognition element and 
an electronic transducer for the highly sensitive detection of analytes 
in body fluids. Importantly, they can provide rapid readouts and they 
can be integrated into portable, wearable and implantable devices for 
point-of-care diagnostics; for example, the personal glucose meter 
enables at-home assessment of blood glucose levels, greatly improving 
the management of diabetes. In this Review, we discuss the principles 
of electrochemical biosensing and the design of electrochemical 
biosensor devices for health monitoring and disease diagnostics, with 
a particular focus on device integration into wearable, portable and 
implantable systems. Finally, we outline the key engineering challenges 
that need to be addressed to improve sensing accuracy, enable 
multiplexing and one-step processes, and integrate electrochemical 
biosensing devices in digital health-care pathways.
Sections
Introduction
Electrochemical sensing  
of biomarkers
Device integration
Outlook
1State Key Laboratory of Analytical Chemistry for Life Science, School of Chemistry and Chemical Engineering, 
Nanjing University, Nanjing, China. 2State Key Laboratory of Bioelectronics, School of Biological Science and 
Medical Engineering, Southeast University, Nanjing, China. 3School of Geographic and Biologic Information, 
Nanjing University of Posts and Telecommunications, Nanjing, China. 4These authors contributed equally:  
Jie Wu, Hong Liu.  e-mail: hxju@nju.edu.cn

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 347
Review article
diagnosis in the daily routines of individual patients and consumers. 
Thus, POC diagnostics are expected to play a key role in revolutionizing 
the diagnosis and treatment of major global diseases. For example, the  
electrochemical glucose meter, the most successful commercial 
POC biosensing device, has been widely used across the globe to help 
patients with diabetes.
However, the market for electrochemical biosensing devices is 
currently limited to the detection of some small molecules or ions 
(Supplementary Table 1), which can be detected directly by electro -
chemical signals through oxidation, reduction or affinity interactions 
at the electrode surface. By contrast, the detection of large biomark-
ers, such as proteins, nucleic acids, bacteria or cells, mainly relies on 
affinity recognition and, thus, requires multiple steps to produce a 
detectable signal. Several transduction principles may promote the 
integration of fully automated electrochemical biosensing devices 
for affinity biomarkers, including the relation of affinity recognition 
events with the generation and consumption of glucose 6– 10, one-
step affinity-sensing mechanisms, such as binding-induced folding 
sensing and proximity binding-based affinity sensing11,12, and integra-
tion with automatic fluidic systems such as pump-assisted fluidics, 
paper-based microfluidics and polydimethylsiloxane (PDMS)-based 
microfluidics13– 15. In addition, owing to the low concentration of dis -
ease markers in body fluids, in particular, in the early stages of disease 
(femtomolar or attomolar level), signal amplification strategies are 
required to increase detection sensitivity, which can be achieved by 
implementing nanotechnology-based and biotechnology-based strate-
gies, such as amplification strategies based on nanotags, nanocatalysis, 
and nanocarriers and assembly-based and polymerase-based DNA 
amplification strategies16,17.
Efficient health-care management requires electrochemical bio-
sensors to achieve minimally invasive or non-invasive continuous 
measurement of physiological molecules. Advances in microelec
-
tronic engineering, semiconductor precision-machining, flexible and 
stretchable bioelectronics and wireless communication technologies 
have spearheaded the integration of electrochemical biosensors in 
wearable and implantable devices18– 21. T o achieve long-term detection 
of molecules in different biofluids (for example, cerebrospinal fluid, 
interstitial fluid, sweat, saliva, tears and urine), electrochemical biosen-
sors can also be integrated into flexible films, textiles, glasses, teeth and 
diapers. Furthermore, combining sensors with smartphones and other 
mobile devices allows continuous monitoring of dynamic physiologi-
cal processes, and the integration of intelligent or digital processing 
modules into devices enables the connection of sensors to the Internet 
of Things and cloud computing for large-scale medical data mining.
In this Review, we discuss key innovations in electrochemical 
biosensing for preventive and personalized POC diagnostic devices. 
We discuss the design and integration of amperometric, voltammetric, 
potentiometric, organic electrochemical transistor (OECT), photo -
electrochemical and electrochemiluminescent biosensors (Table 1) for 
disease diagnosis, health management, cell monitoring and neurosci-
ence. In addition, we examine the fabrication, fluidic manipulation, 
signal amplification and readout, signal processing algorithms, and 
result visualization of integrated biosensors.
Electrochemical sensing of biomarkers
In electrochemical biosensors, the signal is typically triggered by elec-
tron or ion transfer on a conductive transducer through a biorecogni-
tion process. Signals can involve current (i), potential (E), impedance, 
conductivity, capacitance and light (I). Among these, impedimetric 
Key points
 • Electrochemical biosensors are self-contained, analytical devices, 
in which a biological recognition element is in direct contact with 
an electrochemcial transduction element to allow the sensitive and 
specific detection of analytes.
 • Depending on the design and sensor type, health-related and 
disease-related biomarkers, such as carbohydrates, proteins, nucleic 
acids and cells, can be rapidly analysed in different body fluids, 
including blood, saliva and tears.
 • Electrochemical biosensors, including amperometric, 
voltammetric, potentiometric, organic electrochemical transistor, 
photoelectrochemical and electrochemiluminescent sensors, can be 
integrated into wearable, portable and implantable devices to enable 
point-of-care diagnostics and health monitoring.
 • Commercialization and broad point-of-care applicability of 
integrated electrochemical biosensors will require improvements in 
stability, sensitivity, reproducibility, multiplexing, and digitalization and, 
importantly, low-cost materials and easy fabrication methods.
Introduction
Biosensors have been widely applied in clinical, industrial, environ-
mental and agricultural analyses since Leland Clark Jr introduced the 
amperometric glucose enzyme electrode in 1962 (ref. 1). According to 
the definition by the International Union of Pure and Applied Chem-
istry2, a biosensor is a self-contained, integrated, analytical device, 
in which a biological recognition element (biochemical receptors, 
including enzymes, antibodies, antigens, peptides, DNA, aptamers 
or living cells) is retained in direct spatial contact with a transduction 
element (such as electrochemical, optical and mechanical transducers). 
Biosensors were initially developed for point-of-care (POC) testing of 
biomolecular targets in the hope of extending clinical analysis from 
specialized laboratories to public settings, including hospitals, non-
hospital nursing settings or home settings2. Although various biosen-
sors have been developed for the sensitive and selective detection of a 
range of disease-related molecules, clinical translation of biosensors 
remains limited owing to difficulties in integrating and miniaturizing 
biosensors into portable devices.
Among the different biosensing platforms, electrochemical bio-
sensors, which integrate the biorecognition element in an electrochem-
ical transducer (for example, an electrode or field-effect transistor) are 
particularly suitable for device integration3– 5 (Fig. 1a) because they can 
be easily miniaturized, batch fabricated and integrated with an elec -
tronic acquisition module on a single chip. In addition, electrochemi-
cal signals, such as electrical current and potential, can be collected 
by simple, portable and low-cost peripheral instruments with low 
power consumption. Moreover, the signal produced through affinity 
recognition of the target analyte by the biorecognition element can be 
amplified by physical, chemical or biological strategies, which greatly 
improves detection sensitivity. As such, electrochemical biosensors 
hold great promise for the development of POC diagnostic devices. 
The World Health Organization stipulates that POC biosensors should 
be affordable, sensitive, specific, user-friendly, rapid, robust, equip-
ment free and deliverable to end users to enable on-site testing and 

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 348
Review article
biosensors are theoretically favoured for POC diagnostics and device 
integration because they can directly detect biorecognition events by 
measuring the non-faradaic resistance and capacitance properties of 
the sensing electrode; however, their practical implementation suffers 
from non-specific binding of non-target compounds, which leads to 
low sensitivity and selectivity. In addition, although impedimetric 
• 
• P rinte d  cir c u i t  boa r d
• Sof t w a r e
• D a t a  collect ion,  
p r oce s s ing and  anal y s i s
• B luetooth
• W i r e l e s s
• P owe r
• Smar t p hone
a  Electrochemical biosensors
g
c  Potentiometric biosensing d  Organic electrochemical 
        transistor biosensing
f  Electrochemiluminescence 
      biosensing
e  Photoelectrochemical 
       biosensing
P eptid eD N A
A ntib o d y A p t ame r
E l e c t r ochemica l
t r a n s d u c e r
DNA E n z yme Ant ibody Apt amer P e ptide
Nucle i c
acid
Cell B a cte ria P r o tei n Me t a b olit e Io n
Electrochemical biosensorsAnalyteDetection probe
Tag
Liq uid  
cont a c t
S o l id 
cont act
A l l -s o l i d  
s t ate
E
t
IE CL
t or E
ip c
tt
Ion- s elec t i ve
memb r a n e
Cond uct ing la y e r
Fi l m elec t r o d e
b  
E n z yme
Ta r g e t
P r odu cts
Med OX Med r e dW E
Amperometric biosensing
i
t Binding -induc e d
f olding sen s ing
Ta r g e t
W E
e –i
P r o ximity binding-ba s ed 
W E
 e –
i
a n d
W E
i i
Voltammetric biosensing
i
E
Mu l t istep sandwich sen s ing
i
Channe lS D
G
i
ichannel
P MT or
c a m e r a
W E
e –
h +
Light
s our c e
Nanoma t e ria l
RE
CE
Print ing  or micr o f abricat ion
Implantable WearablePortable
W E
 e –
Fig. 1 | Electrochemical biosensors. a, Schematic representation of 
electrochemical biosensors based on different biochemical receptors and 
detection probes. b, Amperometric biosensing of metabolite targets based on 
an enzyme electrode, including the current–time (i– t) curve and the i signal 
for quantification. Voltammetric biosensing of proteins or nucleic acids using 
an antibody-modified or nucleic acid-modified electrode through multistep 
sandwich sensing, one-step binding-induced folding sensing or one-step 
proximity binding-based affinity sensing, including the current–potential 
(i–E ) curve and i signal for target quantification. c, Ion-selective electrodes 
with three different structures, including recording of the potential (E) for 
target quantification. d, Two types of organic electrochemical transistor 
sensors prepared by immobilizing the recognition element on the channel 
surface or on the gate electrode (G) for sandwich immunoassays of proteins, 
including recording of the channel current (i
channel) for target quantification. 
e, Photoelectrochemistry biosensing based on a three-electrode system and a 
light source, including recording of the photoelectrode photocurrent (ipc) upon 
target recognition for quantification. f, Electrochemiluminescence biosensing 
of cells based on an aptamer-modified electrode through a sandwich-sensing 
format, including light intensity (I
ECL) at excited potential by a photomultiplier 
tube (PMT) or imaging using a camera for target quantification. g, Integration 
of electrochemical biosensors in portable, wearable and implantable devices. 
CE, counter electrode; D, drain electrode; Med
ox, oxidized form of mediator; 
Medred, reduced form of mediator; RE, reference electrode; S, source electrode; 
WE, working electrode.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 349
Review article
biosensors have been greatly improved during the COVID-19 pandemic, 
for example, using molecular imprinting technology to fabricate virus-
imprinted impedimetric biosensors for sensitive detection of whole 
virus particles22 or by applying a dielectrophoresis force to improve 
the detection sensitivity of impedimetric immunosensors fabricated 
on Au micro-interdigitated electrodes23, their proof-of-concept per-
formance is often only demonstrated using artificial physiological 
samples instead of clinically relevant samples.
Amperometric and voltammetric biosensors
Amperometric and voltammetric biosensors are operated with a 
three-electrode system, which contains a biosensor as a working elec-
trode (WE) for target recognition, a counter electrode as the current 
source, and a reference electrode to apply a stable potential. Current 
signals are generated by electrochemical reactions on the WE under 
an applied potential for target quantification. The difference between 
the two techniques is their applied potential, which is constant for 
amperometric measurements and variable for voltammetric detection. 
According to the potential change modes, the latter can be performed 
with various techniques, including cyclic voltammetry, differential 
pulse voltammetry, square wave voltammetry and anodic stripping 
voltammetry.
Amperometric biosensors are the most popular sensors for the 
detection of metabolites (for example, glucose, lactate and uric acid). 
In amperometric biosensors, a target-specific enzyme (for example, 
glucose oxidase (GOx), lactate oxidase or uricase) is immobilized on 
the WE to catalyze the oxidation of the target at a constant potential3; 
for example, glucose meters are typically constructed with ampero -
metric biosensors that use GOx to catalyze the oxidation of glucose 
by a redox mediator (for example, ferricyanide, ferrocene derivative 
and transition-metal complexes) (Fig. 1b); alternatively, amperomet-
ric glucose sensors can rely on the enzymatic oxidation of glucose 
with natural oxygen to generate and detect hydrogen peroxide using 
a mediator such as Prussian blue 24. Amperometric biosensors are 
simple to fabricate, and have high sensitivity and selectivity in target 
detection, making them suitable for wearable applications. As the 
concentration of metabolites in non-blood fluids is lower than that in 
blood (for example, the concentration of sweat glucose (10–200 μM) 
and tear glucose (0–2 mM) are, respectively, 100-fold and 10-fold 
lower than that of blood glucose (1–20 mM)), nanomaterials, such as 
metallic nanoparticles, carbon nanotubes and graphene, can be added 
to the biosensing interface to facilitate electron transfer to increase 
the sensitivity and decrease the detection limit25. For example, Au–Pt 
bimetallic nanocatalysts in combination with nanoporous hydrogels 
enable GOx immobilization and glucose detection with a sensitivity of 
180 μA cm–2  mmol–1  and a detection limit of 0.01 mg dl− 1 (0.56 μM), mak-
ing such a biosensor suitable for integration with a smart contact lens 
for tear glucose measurement26. In addition, nanomaterials with enzy-
matic properties (that is, artificial nanoenzymes) can be implemented 
in amperometric biosensors to avoid denaturation of natural enzymes; 
for example, using a laser-induced graphene array, co-decorated with 
Cu2O and Au nanoparticles, a miniaturized, electrochemical, flex -
ible, non-enzymatic biosensor was designed, offering stable sensing 
signals upon bending back-and-forth 25 times; its integration with a 
smartphone-based portable station for glucose monitoring has been 
verified with commercial blood testing devices
27.
Metabolites can be detected by enzymatic recognition; by con -
trast, disease biomarkers, such as proteins and nucleic acids, are 
detected by affinity recognition, which cannot directly generate 
electron transfer on the biosensing surface. Thus, an additional 
Table 1 | Electrochemical biosensors
Sensor type Main target Sensing 
mechanism
Detection performance Technical 
challenges
Future directions Device 
integration
Amperometric Metabolites Enzymatic 
reaction
Good sensitivity (180 μA cm
–2  
mmol–1 for glucose detection)26;  
medium stability (~1 month)57
Improvement 
of stability and 
sensitivity
Robust and highly sensitive 
sensors for point-of-care 
diagnostics in different 
environments, including 
wearable sweat monitoring
Portable and 
wearable
Voltammetric Proteins and 
nucleic acids
Bio-affinity 
recognition
Good sensitivity and low LOD 
(10 fM for insulin
44, ~1 pg ml–1 for 
glycoproteins47,48 and ~100 fM 
for DNA50); easy reuse44,48
Simplification and 
automation of 
multistep affinity 
reactions
Simple, rapid, cost-effective 
biosensing systems by 
designing automatic fluidics or 
one-step sensing mechanisms
Portable
Potentiometric Electrolytes Ion-selective 
penetration
Good stability (more than 
1 month) and medium sensitivity 
(~60 mV per decade)
57
Miniaturization and 
flexibility of sensors
Stable all-solid-state sensing 
electrodes
Portable and 
wearable
Organic 
electrochemical 
transistor
Small 
molecules, 
proteins and 
nucleic acids
Bio-affinity 
recognition
Good sensitivity and low LOD 
(30 nM for glucose
58, 10 pM 
for DNA62 and 1 pg ml–1 for 
proteins64)
Batch preparation 
of sensing 
electrodes
Batch production and portable 
data processing systems
Portable and 
wearable
Photoelectrochemistry Bio-affinity 
recognition
Good sensitivity and low 
LOD
73 (~1 μM for lactate, ~1 fM 
for DNA and ~1 pg ml–1 for 
glycoproteins)
Equipped with  
a light source
Miniaturized, implantable 
sensing devices for in vivo 
applications
Portable and 
implantable
ECL Bio-affinity 
recognition
Good sensitivity (LOD of ~3 pM 
for microRNA
83, microimaging 
of membrane proteins on single 
cells85 and sensing of dopamine 
released by a single cell86)
Efficient ECL 
reactions and 
probes; equipped 
with an ECL 
collection module
Highly sensitive ECL imaging 
systems for high-throughput 
detection and single-cell 
analysis
Portable and 
implantable
ECL, electrochemiluminescence; LOD, limit of detection.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 350
Review article
electroactive label is needed for target sensing such as enzymes 
(for example, horseradish peroxidase and alkaline phosphatase), 
nanomaterials (for example, nanoparticles, nanotubes and quantum 
dots) and electroactive molecules (for example, ferrocene and meth-
ylene blue). These labels are typically detected by cyclic voltammetry, 
differential pulse voltammetry, square wave voltammetry and anodic 
stripping voltammetry, and therefore, most affinity sensors are voltam-
metric biosensors. Such sensors can be fabricated by immobilizing 
capture biomolecules (for example, antibodies, antigens, aptamers 
and DNA) on the WE to enable the detection of proteins or nucleic 
acids using a sandwich assay format (Fig. 1b). Here, sequential incuba-
tions with the target, detection molecules and electrochemical nano-
tags are required3,4, limiting device integration of affinity biosensors. 
T o simplify this operation, automatic fluidic systems can be applied; for 
example, biosensors fabricated on screen-printed carbon electrodes 
can be coupled with a flow-injection system to automatically detect 
multiple protein biomarkers28– 30. However, the large size and high cost 
of this apparatus may limit commercialization.
Microfluidics allows the manipulation of fluids in micrometre-scale 
channels by integrated fluidic control units such as microvalves, pumps 
and reactors31. Therefore, multistep liquid processing workflows can 
be integrated into a single chip for fully automated sample-to-answer 
analysis
32,33. Coupling electrochemical biosensors with microfluidics 
enables continuous and high-throughput detection of multiple trace 
analytes in complex samples such as human serum and blood samples. 
Several electrochemical biosensing devices have been commercialized 
(for example, Cue Reader from Cue Health, ePlex RP2 from GenMark 
Diagnostics, Binx io from Binx Health) for chip-based or cartridge-
based detection of SARS-CoV-2 nucleic acids, respiratory viral and bac-
terial organisms, and Chlamydia trachomatis based on the integration 
of digital microfluidics (such as electrowetting) with amperometric 
or voltammetric affinity biosensors (Supplementary Table 1). These 
products enable at-home testing of disease biomarkers but are very 
expensive. Alternatively, cheaper and highly sensitive electrochemical 
biosensing systems can be designed by combining amperometric or 
voltammetric biosensors with paper-based microfluidics with self-
pumping ability. These systems can integrate multiplex sensing elec-
trodes for differential pulse voltammetry or square wave voltammetry 
detection of protein and nucleic acid biomarkers13,15. For example, an 
origami paper-based aptamer and antibody biosensing chip enables 
simultaneous detection of C-reactive protein (CRP) and pre-albumin 
down to the picogram per millilitre level34. By integrating amperomet-
ric or voltammetric biosensors with PDMS-based microfluidics, which 
can be fabricated by high-precision micromachining technologies, 
including soft lithography, casting, imprinting, injection moulding 
and laser ablation, the automation, miniaturization and array size of 
devices can be improved
35–37 . For example, 16 three-electrode biosen-
sors integrated with a PDMS chip with separate chambers and reser-
voirs of reagents and samples allow the high-throughput detection of 
three protein markers of breast cancer38.
Merging biosensors with automatic fluidic systems simplifies 
detection; however, device integration remains difficult owing to the 
requirement of pumps and reservoirs. One-step affinity sensors pro-
vide a simpler alternative; for example, a binding-induced folding elec-
trochemical biosensor can be fabricated by site-specific modification 
of a redox-tagged probe DNA on the WE11. The detection of the target 
then relies on the binding-induced change in rigidity of the probe DNA 
(Fig. 1b), causing the redox tags to move close or away from the elec-
trode surface, resulting in a respective increase or decrease of the 
current signal for target biosensing. Such binding-induced folding 
electrochemical biosensors can achieve sample-in-answer-out sensing 
of nucleic acids or sensing of some specific proteins using aptamer 
receptors; however, they suffer from low sensitivity. The signal can 
be amplified using DNA hybridization strategies39,40; for example, an 
electrochemical DNA sensor based on target-induced CRISPR–Cas12a 
cleaving of interfacial single-stranded DNA with methylene blue as the 
signal tag can detect human papillomavirus 16 (HPV16) and parvovirus 
B19 (PB19) down to the picomolar level41. The sensitivity of this DNA 
sensor can be further improved using a hairpin DNA probe42.
Proximity binding-based affinity electrochemical biosensors are 
particularly suited for protein biomarker detection because they can 
transfer a protein immunoassay to DNA detection 12. In such biosen-
sors, a pair of antibody-DNA affinity probes dually recognizes a target 
protein, which leads to the formation of proximity ligation products 
that initiate DNA assembly, causing the ‘on’ or ‘off’ state of the electro-
active molecule-tagged probe DNA on the electrode surface (Fig. 1b). 
A wash-free and separation-free square wave voltammetry biosen -
sor based on a proximity binding-induced ‘on’ state of methylene 
blue–DNA on the electrode surface allows direct detection of insulin43. 
By introducing uracils in the DNA sequence, this biosensor can be made 
reusable, enabling repeated protein quantitation within 3 min (ref. 44). 
The sensitivity of proximity binding-based affinity electrochemical 
biosensors can be further improved by DNA amplification strategies; 
for example, introducing an electrochemical ratiometric readout45,46, 
nuclease-mediated or DNAzyme-mediated cycle amplification 47,48, 
surface programmatic chain reaction49, or DNA walker amplification50 
enables the one-step detection of glycoprotein markers (for example, 
carcinoembryonic antigen (CEA), prostate-specific antigen (PSA) and 
thrombin) down to picogram per millilitre or sub-picomolar levels 
(Supplementary Table 2).
Potentiometric biosensors
Potentiometric biosensors are typically operated with a two-electrode 
system consisting of a sensing electrode and a reference electrode, 
allowing direct detection of targets by measuring the potential sig-
nal related to the change of surface charge upon target recognition 
on the sensing electrode. Typically, ion-selective electrodes made 
of ion-selective membranes and a liquid contact structure are used 
as potentiometric sensing electrodes (Fig. 1c). Glass membrane ion-
selective electrodes (for example, pH electrode), solid membrane  
ion-selective electrodes (for example, crystalline membrane electrodes 
for F− , Ag+, Cl−  and S2− ), and liquid membrane ion-selective electrodes (for  
example, electrodes based on ionophores (selective host molecules) 
for H
+, K+, Na+, NH4
+, Ca2+) are commercially available. Solid and liquid 
membrane electrodes can further be integrated into clinical analyz-
ers for the detection of blood electrolytes (for example, Na+, K+, Ca2+, 
H+ and Cl− ). Enzymes, nucleic acids and proteins can be detected by 
integrating the biological element on the ion-selective electrode to 
catalyze the reaction that forms the ions or by combining the target 
biorecognition event with an ionic reaction51– 54.
Solid-contact ion-selective electrodes, which can be made with sol-
vent polymeric membranes, do not contain internal solutions (Fig. 1c) 
and benefit from ruggedness (thus, morphological diversity) and 
easy fabrication, modification and miniaturization. Solid-contact ion-
selective electrodes allow protein and nucleic acid analysis through the 
detection of ions released from nanoparticle-tagged probes; for exam-
ple, a miniaturized solid-contact Ag ion-selective electrode can detect 
DNA targets at the femtomolar level in microlitre-volume samples55.  

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 351
Review article
In addition, all-solid-state ion-selective electrodes can be made with 
conducting polymers or nanomaterials to establish a solid contact 
beneath the ion-selective and reference membranes (Fig.  1c). Such 
ion-selective electrodes have been implemented in two commer -
cial portable devices for POC detection of electrolytes and blood 
gases (i-STAT from Abbott and BGA-102 from Wondfo Biotech) 
(Supplementary Table 1). A paper-based potentiometric biosensor 
based on an all-solid-state butyrylcholine-sensitive ion-selective elec-
trode and a 3D origami paper-based fluidic system can detect butyryl-
cholinesterase activity and organophosphate pesticides and, by further 
integrating a USB-controlled miniaturized electrochemical analyzer, 
allows the design of a handheld potentiometric device56. All-solid-state 
ion-selective electrodes can also be integrated into wearable devices 
for ionic detection in biofluids 18– 21; for example, a wearable ‘smart 
wristband’ with Na+ and K+ ion-selective electrodes on a flexible sensing 
array enables in situ analysis of Na+ and K+ in sweat57.
Organic electrochemical transistor biosensors
OECT biosensors are organic thin-film transistors that consist of gate 
(G), drain (D) and source (S) electrodes, with an organic semiconduc-
tor film between the D and S electrodes. A change in the potential 
drop or capacitance of the gate–electrolyte or channel–electrolyte 
interface sensitively changes the channel current. Thus, OECT bio -
sensors can be fabricated by immobilizing the recognition element 
on the G electrode or on the channel surface (Fig. 1d); here, the spe-
cific reactions of the OECT biosensor with the target influence the 
interface potential, resulting in a channel current response for target 
quantification.
OECT biosensors benefit from high sensitivity, low cost, 
flexibility, easy fabrication and low working voltage (<1 V), allowing 
the detection of both electroactive (for example, dopamine, glucose 
and epinephrine) 58– 60 and electro-inactive (for example, cortisol 61, 
DNA62, proteins63,64, bacteria65, cells66 and glycans67– 70) molecules or 
biomacromolecules through electrostatic interactions or affinity 
binding between targets and the sensing interface71.
OECT biosensors can be easily miniaturized, integrated into 
devices and designed as arrays because their detection performance 
does not degrade if their size is reduced at a fixed channel width per 
length ratio. For example, a ‘lab on a chip’ system based on an OECT 
biosensor integrated into a flexible microfluidic system allows label-
free detection of DNA with a detection limit of 10 pM; here, the microflu-
idic device is deposited on a flexible substrate that contains a thiolated 
DNA probe immobilized on the Au gate electrode62. OECT microarrays 
can also be fabricated by solution processes for high-throughput 
sensing. The flexibility and robustness of OECT biosensors make them 
suitable for the non-invasive detection of biomolecules in wearable 
devices. For example, a fabric OECT biosensor, fabricated by weaving 
the sensor with cotton yarns, can be embedded in a diaper to monitor 
glucose in artificial urine, with the sensing signals collected on a mobile 
phone through Bluetooth72.
Photoelectrochemical biosensors
Photoelectrochemistry studies the effect of light on photoelectrodes 
or interfacial materials and the conversion of light energy into electrical 
power. Photoelectrochemical biosensing combines photoelectrochem-
istry with sensor-based bioanalysis; here, light serves as the excitation 
source and current as the readout. Photoelectrochemical biosens -
ing systems typically consist of a three-electrode system and a light 
source (Fig. 1e). Detection is based on the change of photocurrent upon 
target recognition at the biosensor surface, which induces a charge or 
energy transfer owing to the photoelectrochemical reaction between 
an electron donor and acceptor, and a photoactive material on the 
electrode surface upon light irradiation73.
Photoelectrochemical biosensors combine the advantages  
of optical and electrochemical assays, in particular, for the detection of  
disease-related molecules such as glutathione, lactate, DNA, microRNA 
(miRNA), protein tumour markers and cells 73. Light stimuli can be 
applied contactless rather than through bias voltage, making photo-
electrochemical biosensors biocompatible and suitable for in vivo 
sensing. In addition, separation of the excitation source (light) and 
detection signal (electricity) and their different energy forms result in 
low background noise and high sensitivity. Therefore, photoelectro-
chemical microbiosensors allow in vivo or single-cell analysis 74,75;  
for example, using a fluorescence resonance energy transfer (FRET) 
process, a photoelectrochemical microbiosensing system can selec-
tively monitor SO2, a potential marker of cerebral ischaemia (reperfu-
sion) and related brain injury, in the brain of living rats 76. Here, FRET 
is implemented based on upconversion nanoparticles (UCNPs) as the 
energy donor and an organic dye as the energy acceptor. The biosens-
ing interface is then constructed by co-immobilization of the UCNP and 
dye FRET pair, and CdT e quantum dots on a microelectrode. In the brain 
of a rat model of cerebral ischaemia-reperfusion and febrile seizure, the 
presence of SO2 blocks the FRET process and recovers UCNP emission, 
which, in turn, modulates the photocurrent of the photoactive material, 
allowing the detection of SO2.
Electrochemiluminescence biosensing and bioimaging
Electrochemiluminescence is an electrochemically triggered energy-
relaxation process, in which a luminophore undergoes electron transfer 
reactions to form excited states that emit light. Electrochemilumines-
cence biosensing enables the quantitative detection of target molecules 
through electrochemiluminescence emission signals that are associ-
ated with a target biorecognition-induced change in electrochemilu-
minescence active species. Similar to amperometric and voltammetric 
biosensors, electrochemiluminescence biosensors also operate with a 
three-electrode system, in which the WE is modified with the recogni-
tion element to serve as the biosensing electrode (Fig. 1f). Owing to the 
combination of electrochemistry and spectroscopy, electrochemilumi-
nescence biosensing does not require a light source and has negligible 
background noise, high sensitivity, good reproducibility, and high 
spatial and temporal control, making it a powerful analytical tool for 
the detection of a range of disease molecules, including DNA, miRNA, 
proteins and tumour cells77– 79.
A commercialized microbead-based electrochemiluminescence 
biosensing system (that is, Elecsys 1010/2010/E170, Roche Diagnostics) 
is used as the gold-standard detection system in hospitals for many 
glycoprotein tumour markers79; however, this instrument is large and 
bulky. Alternatively, a portable electrochemiluminescence device, 
integrating a screen-printed carbon electrode-based electrochemilu-
minescence biosensor, paper microfluidics and a mobile phone camera, 
can detect 2-(dibutylamino)-ethanol and NADH80. A portable electro-
chemiluminescence biosensing system has also been designed for the 
detection of miRNA-21 by combining a magnetic bead-based switch-on 
electrochemiluminescence molecular beacon sensing strategy with a 
portable potentiostat and a mobile phone camera readout81.
Electrochemiluminescence biosensing strategies can be com -
bined with a charge-coupled device camera and a conventional micro-
scope for electrochemiluminescence bioimaging. This system allows 

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 352
Review article
simultaneous detection of multiple biomarkers through spatial or 
potential resolution; for example, a bead-based electrochemilumines-
cence immunosensing array enables simultaneous detection of three 
antigens by individually imaging the microbeads located in a microwell 
array82. Similarly, electrochemiluminescent polymer dots (Pdots), 
luminol-doped Pdots and diethylamine-coupled Pdots can be exploited 
for potential-resolved and colour-resolved electrochemiluminescence 
bioimaging for the high-throughput detection of miRNAs83. Here, lumi-
nol-doped Pdots show blue electrochemiluminescence emission at 
+0.6 V, whereas diethylamine-coupled Pdots show red electrochemilu-
minescence emission at +1.0 V. On the sensing array, the electrochemi-
luminescence of two Pdots is initially inhibited by quencher-labelled 
capture DNAs. After recognition of target miRNAs, the quencher is 
released through DNA cleaving, and the electrochemiluminescence of 
Pdots is recovered for target detection. Compared to potential-resolved 
electrochemiluminescence biosensors, this potential-resolved and col-
our-resolved bioimaging system prevents interference of the threshold 
produced by the low potential emitter at high potentials.
Electrochemiluminescence bioimaging is well suited for cell 
analysis because it can provide both morphological and quantitative 
information84. Electrochemiluminescence cell bioimaging strategies 
have been developed for different targets, including small molecules 
released from cells and membrane proteins on the cell surface. 
Electrochemiluminescence imaging of membrane proteins is typi -
cally achieved by labelling cells with electrochemiluminescence probes 
through affinity reactions. However, this approach only allows observa
-
tion of the cell periphery in contact with the electrode or requires mem-
brane permeability treatment. Alternatively, a dual-intramolecular 
electron transfer strategy can be applied; for example, co-reactant-
embedded Pdots with strong electrochemiluminescence emission 
enable in situ imaging of the membrane protein human epidermal 
growth factor receptor 2 (HER2) on single living cells 85. T o quantify 
detection, the biosensing interface, that is, a Pdot-modified-indium tin 
oxide (ITO) glass electrode sheet, can be combined with a single-cell-
capture microfluidic chip, enabling high-throughput quantification 
of dopamine secreted by a single cell86.
Device integration
Electrochemical biosensors can be integrated into portable, wearable 
or implantable devices (Table 1), including microfluidics, printed circuit 
boards, software, signal processing units, communication units and 
power units (Fig. 1g). Amperometric biosensors are the most devel-
oped and most commonly used sensors for metabolites. Owing to 
the specific enzyme reaction, they usually exhibit good selectivity. 
In addition, the enzymatic catalytic signal can be further enhanced 
by nanomaterials, leading to high sensitivity. Most importantly, these 
enzyme sensors can be prepared in batches with good reproducibil-
ity; however, enzyme activity can be affected by the environment. 
Thus, robust sensing electrodes are required for work in different 
environments. Potentiometric biosensors can be integrated for 
wearable sweat monitoring, in particular, for the detection of elec -
trolytes. Using ion-selective membranes, potentiometric biosensors 
show good selectivity, reproducibility and stability; however, their 
sensitivity is low. Alternatively, a flexible, all-solid-state, wearable, 
ion-selective electrode could achieve continuous sweat monitoring. 
Voltammetric, OECT, photoelectrochemical and electrochemilumi-
nescent biosensors allow the detection of proteins and nucleic acids, 
showing good selectivity and high sensitivity. However, such affinity 
biosensors typically require the specific assembly of bioreceptors on 
the electrode surface, making their fabrication more complicated than 
that of enzyme electrodes.
Portable electrochemical biosensing devices
Portable electrochemical sensors have initially been developed for 
the monitoring of blood glucose levels in patients with diabetes87. The 
personal glucose meter is a portable electrochemical biosensor that 
provides rapid quantification of blood glucose levels for personal gly-
caemic control. The glucose meter, which is typically an amperometric 
biosensor based on a redox enzyme, consists of a disposable test strip 
and a pocket-sized handheld electrochemical reader (Fig. 2a). The 
disposable test strips can be fabricated by printing and cutting at a 
large scale using low-cost materials such as plastics and conductive 
pastes; for example, the thin-film electrodes on the test strips can be 
produced by screen-printing technology, which allows mass production 
at low cost88. The sensing layer containing the enzyme and the electron 
mediator is immobilized on the WE for the detection of glucose. Once 
the blood sample is introduced to the small chamber (electrochemi-
cal cell) formed by the spacer layer on the test strip, blood glucose is 
oxidized by the redox mediator, which is catalyzed by GOx (Fig. 2a). 
The reduced mediator is then oxidized on the electrode, producing a 
measurable current signal89, which is converted to glucose concentra-
tion by a handheld detector. The personal glucose meter is a result of 
continuous engineering advances to increase its accuracy, reliability, 
user-friendliness and affordability90,91 since the first concept of glucose 
enzyme electrodes was proposed in the 1960s1.
The personal glucose meter can also detect metal ions, drugs, 
organic metabolites, enzymes, proteins, DNA and influenza viruses by 
relating target recognition events with the generation or consumption 
of glucose92– 97. For example, the personal glucose meter can quantify 
cocaine, adenosine and uranium in blood through the target-induced 
release of invertase, from a DNA–invertase conjugate, that catalyzes 
the conversion of sucrose to glucose92. Moreover, the device can quan-
titatively detect SARS-CoV-2 antigen in human saliva for COVID-19 
screening97; here, antigen-binding events are translated into glucose 
signals using an aptamer-based competitive mechanism that leads to 
invertase release to catalyze sucrose hydrolysis. This on-site test can 
be accomplished within 1 h with a picomolar limit of detection.
For complex samples that require pre-treatment, signal ampli -
fication and continuous analysis, electrochemical biosensors can be 
combined with microfluidic systems98,99, for example, for the detection 
of SARS-CoV-2 RNA100. In this device, RNA is detected by a reconfig -
urable enzyme–DNA nanostructure, which comprises DNA strands 
with inhibitor and inverter sequences that are bound to a Taq DNA 
polymerase through a cascading molecular circuitry enhancement; 
here, the biorecognition of target RNA by inverter sequences activates 
polymerase activity for downstream DNA amplification, labelling and 
electrochemical detection. The entire assay is automatically completed 
by a pressure-actuated microfluidic device with embedded sensing 
electrodes. Electrochemical biosensors can also be integrated with 
paper microfluidic devices by directly printing electrodes on paper. 
Paper-based microfluidics is cheap, biodegradable, easy to fabricate 
and allows pumpless fluidic transport by capillary actions 101,102. In 
addition, paper can be folded (origami) to assemble 3D devices and 
control fluidic and electrical connectivity for programmed analytical 
processes103– 105; for example, paper with patterned fluidic channels  
and electrodes can be assembled into a 3D configuration by folding and 
lamination for the detection of adenosine 104 (Fig. 2b). In this device, 
the adenosine sample is first split into two symmetrical channels.  

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 353
Review article
In one channel, adenosine binds an aptamer immobilized on micro -
beads, which causes the release of GOx-labelled DNA and leads to 
the conversion of [Fe(CN)6]3−  to [Fe(CN)6]4− . In the other channel, the 
microbeads do not contain the aptamer, leading to different redox con-
centrations in the cells, allowing the quantitative analysis of adenosine 
in a portable digital multimeter.
Miniaturized electrochemical analyzers can also be connected 
to smartphones for powering, processing and storage of data and to  
display results106. In addition, the test results can be uploaded to mobile 
health services107. For example, an open-source portable electrochemical 
detector that can establish wireless communication with a smartphone  
can be combined with electrochemical biosensors106,108.
Integration into wearable devices
Wearable sensors can be integrated with smartwatches, bracelets and 
glasses for physiological monitoring, for example, of heart rate, elec-
trocardiogram and electroencephalogram109. Such wearable biosen-
sors also allow non-invasive and continuous monitoring of analytes 
in body fluids (Fig. 3a), providing invaluable data for diagnostics and 
health management109–111 . For example, the concentrations of glucose 
in non-blood body fluids, such as sweat and tears, can be converted 
to their corresponding blood levels through a correlation coefficient 
obtained from a correlation study between glucose concentration in 
blood and non-blood biofluids
26,112, considering time lags for glucose 
secretion in different biofluids113– 115. Compared to portable electro-
chemical biosensors, of which some have already been commercialized 
(Supplementary Table 1), wearable electrochemical biosensors are not 
yet at the same development stage.
Thus far, wearable electrochemical biosensors have mainly been 
explored for glucose monitoring because glucose can be detected in 
sweat, saliva and tears116– 118. Compared to the conventional finger-prick 
test, wearable glucose analysis allows non-invasive and continuous 
monitoring, even during sleep, enabling timely feedback for diabetes 
management. A wearable integrated sensing array allows multiplexed 
detection of sweat biomarkers, including metabolites and electrolytes 
(such as glucose, lactate, Na+ and K+); here, signal conditioning, process-
ing and wireless data transmission for in situ sweat analysis are achieved 
by flexible printed circuit boards57. Such integrated wearable electro-
chemical biosensors allow non-invasive and dynamic monitoring of the 
health status at the molecular level, for example, for in situ monitoring 
of wound healing119, therapeutic drugs, drug abuse120, nutrition121 and 
the diagnosis of cystic fibrosis114. Wearable electrochemical biosensors 
can also be incorporated into robots to sense hazardous materials and 
pathogens for agriculture, security and public health applications122.
Sampling plays an important role in wearable biosensing. The con-
centration of biochemical analytes in secreted body fluids is affected 
by various factors, including reabsorption, evaporation, secretion rate, 
interfering substances and metabolism of the secretion glands109,113,123. 
Microfluidic devices can be applied for sample collection; for exam -
ple, sweat can be enriched and transported to a sensor module in a 
microfluidic device, reducing sweat reabsorption and evaporation, 
and allowing real-time continuous monitoring. Moreover, a micro -
fluidic sweat sampling device can be designed to collect small volumes 
of sweat, enabling continuous sweat monitoring at rest by entrap -
ping thermoregulatory-generated sweat in a microfluidic channel124. 
This design may facilitate wearable sweat sensing platforms that do 
not require large sweat volumes, for example, during exercise or at 
high ambient temperatures, making sweat sensing compatible with 
daily activities. Microfluidic devices with fluidic valves further allow 
in situ manipulation of collected biofluids, for example, to achieve 
a  Portable glucose meter b  Micro/f.shortluidic paper-based electrochemical biosensor
Cover layer
Spacer layer
Electrode layer
Test strip Handheld detector
Glucose
Gluconic acid
Enzyme (ox)
Enzyme (red)
Mediator (ox)
Mediator (red)
Working
electrode Capillary
/f.shortilling
of blood
Electrode
Folding
lamination
Digital multimeter Capacitor
Sample
Microbeads
Glucose oxidase
Biotin
Streptavidin
DNA
Adenosine
Glucose
Gluconic acid
Flow direction
[Fe(CN) 6]4– [Fe(CN) 6]3–
Fig. 2 | Portable electrochemical biosensing devices. a, Portable blood glucose 
meter consisting of a handheld electrochemical detector and disposable test 
strips. The test strip contains a bottom electrode layer, an adhesive spacer layer 
and a hydrophilic cover layer. The blood sample is introduced to the reaction 
chamber by capillary force. b, A paper-based microfluidic electrochemical 
biosensor for the detection of adenosine through aptamer-based affinity 
sensing. In one channel, adenosine is recognized by aptamer-functionalized 
microbeads (blue), resulting in the release of glucose oxidase-labelled DNA to 
catalyze the oxidation of glucose, which leads to the conversion of [Fe(CN)
6]3−  
to [Fe(CN)6]4− . In the other channel, the microbeads are not functionalized 
(purple), allowing quantification of adenosine concentration. The current 
signal from the discharging of the capacitor is collected by a portable digital 
multimeter. ox, oxidation; red, reduction. Part b reprinted with permission from 
ref. 
104, Wiley.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 354
Review article
chrono-sampling of sweat for time-dependent analysis of biomarker 
variation125. An epidermal microfluidic device with thermo-responsive 
hydrogel valves enables active control of sweat126, that is, on-demand 
delivery of sweat to the sensing electrode, thereby eliminating the 
influence of flow rate variability on the sensor response and allowing 
scheduled sweat analysis. Although promising for on-body biofluid 
detection, electrochemical bioassays in this device remain difficult 
because they require multistep operations for incubation, amplifica-
tion and washing, limiting its use to monitor protein and nucleic acid 
biomarkers in sweat. Therefore, innovative fluidic control units are 
needed to automate multistep bioassays.
A power source is indispensable for continuous electrochemical 
analysis in wearable devices. Self-powered devices can generate energy 
from human motion127–129  using a piezoelectric nanogenerator130,131 or 
a triboelectric nanogenerator132– 134 that converts mechanical energy 
into electrical energy. For example, a self-powered wearable device 
based on a triboelectric nanogenerator printed on a flexible circuit 
board enables continuous monitoring of H+ and Na+ in sweat135; here, 
the output of the power source (~416 mW m–2 ) can power the multi -
plexed biosensor and the design allows miniaturization. A triboelectric 
self-powered sweat sensor based on nanocellulose hydrogels with self-
healing ability can monitor ions (Na+, K+, Ca2+) in sweat136. Alternatively, 
biofuel cells can power wearable biosensors by harvesting energy 
from redox substances in biological fluids through bioelectrocatalytic 
reactions128,137,138; for example, using ascorbate in tears as the fuel,  
a self-powered contact lens can monitor tear glucose levels 139. Simi-
larly, a self-powered wireless sensing system based on glucose and 
lactate biofuel cells can monitor sweat glucose and lactate levels 140. 
If a single power source is insufficient to power the device, a micro -
grid system incorporating biofuel cells, triboelectric generators and 
supercapacitors can provide higher power output
141.
Long-term wearable electrochemical biosensors can be designed 
with flexible electrode materials (for example, metals, conductive poly-
mers and low-dimensional materials) that resist mechanical deforma-
tion (for example, strain and bending) and that can be self-healing142. 
In addition, flexible, printed circuit boards that contain full-featured 
microcontrollers and other components, such as communication 
modules, can be designed by commercial software, such as the Altium 
Designer, and fabricated by commercially printed circuit board manu-
facturers143. Wireless information communication technologies, such 
as Bluetooth57,144 and near-field communication145,146, have low power 
consumption and acceptable communication distance, allowing sens-
ing devices to communicate with remote electronic systems such as 
smartphones, which can analyze, display and store data (Fig. 3b).
However, the performance of wearable biosensors is limited by 
variations in connectivity and impedances caused by human physical 
activities that can lead to detection errors. Signal processing and cali-
bration algorithms can be applied to correct for such artefacts147; for 
example, electrochemical signals that are affected by pH, temperature 
and flow rate can be calibrated by a multiplexed sensing strategy using 
lookup tables for real-time and automated calibration57. T o reduce sig-
nal variation, an accelerometer can further be integrated and the signal 
can be filtered using short-time fast Fourier transform. More advanced 
frequency-domain algorithms, such as the wavelet-transform projec-
tion, can be employed to decouple motions from the electrochemical 
measurement148. Furthermore, the relative change in electrochemical 
signal (for example, Nernstian shift) can be used instead of the absolute 
signal value to decrease measurement errors149.
Integration into implantable devices
Finger-prick blood tests using portable electrochemical devices are 
usually highly accurate but require frequent, invasive sample collec-
tion150. Wearable electrochemical biosensing is non-invasive but suffers 
from low analytical accuracy, which is a particular concern in diag -
nostic applications151,152. Alternatively, implantable electrochemical 
biosensors combine the high accuracy of invasive finger-prick tests and 
the long-term monitoring capability of non-invasive wearable analy-
sis153,154. Implantable electrochemical biosensors have been particularly 
explored for continuous glucose monitoring and in vivo monitoring of 
biomarkers, such as neurochemicals, in the brain155–158  (Fig. 4).
• PENG
• TENG
• BFC
• BC
• Glucose
• K
+
• Uric acid
• Lactate
• Cortisol
• Na
+
Wristband
Saliva
Sweat
Sweat
Mouthguard
a  Wearable electrochemical biosensors b  Wearable biosensor-integrated health management
Tears
Contact lenses
Flexible patch
Big data
analysis
Health
management
1 Electrochemical analysis
2 Power supply
3 Wireless continuous monitoring
Fig. 3 | Integration of electrochemical biosensors in wearable devices.  
a, Wearable sensors can be applied to monitor health-related or disease- 
related analytes in different body fluids, including tears, saliva and sweat.  
b, Health management can be based on continuous monitoring using  
wearable devices, including electrochemical biosensors, power supply  
and wireless communication modules. BC, biocapacitor; BFC, biofuel cell;  
PENG, piezoelectric nanogenerator; TENG, triboelectric nanogenerator.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 355
Review article
In electrochemical biosensors, the detection reaction occurs 
on the surface of the electrodes and, thus, such sensors can easily 
be integrated with circuitry and incorporated into a small capsule 
for implantation 159,160. Implantable electrochemical biosensors (for 
example, subcutaneous or intravascular) can provide dynamic informa-
tion on glucose levels to guide therapy adjustments157,161–163 . Similarly, 
spatiotemporal electrochemical sensing of neurochemicals, such 
as dopamine and acetylcholine, in the brain can indicate neuronal 
activity164–166 .
Most implantable electrodes are made of Au, Pt and Ir, which 
are electrochemically stable and, in principle, biocompatible 155,167,168. 
However, as foreign bodies, implantable devices are subject to bio -
fouling and the foreign body response, compromising their analyti -
cal performance 169. Therefore, the electrode has to be coated with 
multiple functional layers, including an inner sensing layer consisting 
of redox polymer and enzyme, a middle layer to improve stability, 
and an outer biocompatible layer to prevent fouling of the sensor170,171 
(Fig. 4a). For example, NO-releasing polymer coatings can improve 
the biocompatibility of implantable biosensors (for example, intra -
vascular sensors) because the endogenous gas molecule NO inhibits 
platelet adhesion and activation, inflammatory responses, and bacte-
rial growth148,172. In addition, implantable devices need to be sterilized; 
thus, the coating layers need to withstand sterilization treatments 
such as irradiation173.
The mechanical mismatch between soft tissues and implantable 
electrodes may lead to inflammatory responses and/or device failure. 
Therefore, implantable electrodes should be soft and stretchable to 
seamlessly interface with soft tissues. For example, a soft implantable 
neurotransmitter sensor can monitor the dynamics of monoamine in 
the brain and gut of mice 174; here, the soft, elastic and thin electrode 
is fabricated by embedding laser-induced graphene nanofibres in an 
elastomer matrix, minimizing damage to intestinal tissue and not 
disturbing the peristaltic movement of the gastrointestinal tract.
Implantable biosensors typically remain in the body for long time 
periods, which requires an adequate power supply 175 with high volu-
metric energy density (that is, the energy stored per unit of volume) 
owing to the constraint of the device size 152,155. Batteries have high 
energy densities but require periodic replacement, which may risk 
infection and additional costs 176. Alternatively, implantable electro-
chemical biosensors could be made self-powered using piezoelectric 
materials, triboelectric materials or fuel cells156,177– 180. In addition, near-
field communication may enable wireless power generation and data 
transmission159,181.
Alternative to implantable devices that typically require surgery, 
partially implantable electrochemical biosensors have been commer-
cialized (for example, Freestyle Libre from Abbott and G6 CGM system 
from Dexcom)154,182 (Supplementary Table 1). Such partially implant -
able biosensors only require subcutaneous insertion of a small probe 
(for example, a flexible needle) or a probe array, leaving most com -
ponents, including the power source, readout circuitry and wireless 
communication modules, on the surface of the skin151,162. For example, 
minimally invasive biosensors for glucose detection allow continuous 
glucose monitoring for about 2 weeks and can then be replaced by the 
patient161,183. However, these glucose biosensors are limited to single 
analyte analysis and may cause discomfort owing to the long needles 
(5–11 mm) that need to be inserted to access interstitial fluid. T o achieve 
multiplexed analysis of biomarkers and discomfort-free operation, an 
integrated microneedle array can be applied that allows continuous 
monitoring of two analytes (for example, lactate and glucose, or alco-
hol and glucose) in interstitial fluid184. This device integrates reusable 
Implantable 
continuous
biomarker 
monitoring
a  Implantable electrochemical biosensors b  Implantable-biosensor based health monitoring
Glucose
Anti-
biofouling
Gluconic
acid
Mediator
Cells
Proteins
e –
Biocompatible
layer
Sensing
layer
Working
electrode
Electrochemical signals
Time
Neurochemical
sensing
V
Mass transport
limiting layer
Fig. 4 | Integration of electrochemical biosensors in implantable devices.  
a, Microneedle-based implantable electrochemical biosensors for the 
monitoring of analytes in interstitial fluid. The working electrode is modified 
with multiple functional layers, including an inner sensing layer consisting of 
a redox polymer and an enzyme, a mass transport-limiting layer to improve 
stability, and an outer biocompatible layer to prevent fouling of the sensor.  
b, Implantable electrochemical biosensors allow continuous glucose monitoring 
and in vivo detection of neurochemicals in the brain.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 356
Review article
electronics to acquire and wirelessly transmit the electrochemical 
signals to a smartphone for data analysis and visualization.
Outlook
Electrochemical biosensors are powerful tools to quantitatively analyze 
biochemical analytes in body fluids, providing digital data of dynamic 
physiological processes for fundamental research and health-care 
applications. The integration of electrochemical biosensors in port-
able, wearable and implantable devices enables decentralized POC 
detection185– 187, which has the potential to revolutionize diagnostics 
and health management188, particularly in low-resource settings (Box 1). 
Batch fabrication and integration of disposable, flexible and multi- 
electrode electrochemical biosensors with different substrates, 
including plastics, flexible films, textiles and paper, can be achieved 
by printing (for example, screen28–30 , inkjet122, roll-to-roll189 and trans-
fer190 printing) and microfabrication (for example, photolithography57, 
evaporation124, electron beam evaporation114,119 and laser cutter121); 
however, engineering challenges remain to be addressed for integrated 
electrochemical biosensors to make a real impact in POC diagnostics; 
for example, signal transduction, conditioning (amplification and filter-
ing), processing and wireless transmission need to be improved57; all 
functional controllers and modules should be integrated on one circuit 
board; packaging of soft electronics and chipsets needs to be opti -
mized; and microminiaturization, networking and intellectualization 
of devices needs to be realized191 (Box 2).
Beyond glucose sensing, electrochemical biosensing devices 
could also allow the POC detection of proteins, nucleic acids, viruses 
and cells; however, this will require automated multistep and multi-
solution technology. Digital microfluidics may enable full-automatic 
on-chip measurements but requires high-precision instruments, 
limiting its applications in low-resource settings. Therefore, simple, 
cheap, robust and stable microfluidic systems need to be developed, 
for example, using paper or hydrophilic and hydrophobic polymers, 
which can be folded and/or printed into low-cost, disposable devices. 
Importantly, electrochemical biosensors need to be engineered that 
achieve one-step biosensing to avoid complex handling processes. In 
addition, although amperometric, voltammetric, potentiometric and 
electrochemiluminescent biosensor devices have been commercial-
ized, these are often invasive portable devices rather than non-invasive 
wearable and implantable devices, in particular, OECT, photoelectro-
chemical and electrochemiluminescent bioimaging biosensors are still 
at an early stage. Thus, electrochemical sensors need to be developed 
according to their specific properties; for example, OECT sensors 
can be developed for miniaturized wearable devices and photoelec -
trochemical sensors can be developed for miniaturized composite 
implantable devices (Table 1).
Smartphones, 5G communication and cloud computing will allow 
the digitalization of health-related information obtained by integrated 
electrochemical biosensors. For example, physical sensors connected 
Box 1
Low-resource considerations
To achieve point-of-care analysis of health-related molecules in  
low-resource settings, electrochemical biosensing devices need 
to be portable, cheap, simple to operate and provide rapid readout 
and data analysis. In addition, storage and long-term stability  
should be considered. For example, electrochemical biosensors 
can be designed as disposable test strips and results can be 
detected with a handheld reader. The test strips (for example,  
blood glucose test strip) often have a shelf life of several months  
at room temperature in dry conditions, allowing transportation and 
storage without requiring a cold chain. Such a simple design is also 
compatible with large-scale industrial manufacturing workflows, 
which lowers the cost. Devices designed as test strips provide 
accurate and rapid sample-to-answer detection for point-of-care 
applications without requiring trained personnel. In addition, 
integration of electrochemical biosensors in smartphones, watches 
and wristbands enables at-home measurement of biophysiological 
molecules for health monitoring and disease diagnosis.
Box 2
Translational considerations
The clinical translation of electrochemical biosensors for point-of-
care diagnostic devices requires the establishment of diagnostic 
criteria for the evaluation of test results in different sample types. 
For example, diagnostic criteria for glucose tests have been well-
established for blood samples; however, diagnostic criteria for 
other body fluids, such as sweat, saliva and tears, are more difficult 
to define. In addition, compared with blood samples, these biofluid 
samples may be affected by sampling location (for example, saliva 
in different positions in the mouth, sweat from different sweat 
glands) and by the environment (for example, before and after 
exercise or water drinking). Therefore, the comparison of test 
results and validation of test criteria remains challenging. Thus, the 
translational process of biosensing devices for non-blood samples 
may differ from that of blood samples, requiring the standardization 
of body fluid sampling and additional sensing units to monitor the 
dynamic change in pH, temperature and flow rate of the body fluid 
for calibration. In addition, commercialization of the blood glucose 
meter was originally based on blood glucose measurements 
in hospital settings, outlining the criteria for the design of the 
device; by contrast, new electrochemical biosensor-based devices 
intended for other body fluids may not be based on experience 
in hospital settings but may instead be tested and validated as 
consumer devices for early health warning and health management 
in lifestyle and fitness.
The translation of electrochemical biosensors will further 
depend on their ability to perform full-automatic electrochemical 
biosensing of affinity analytes. This can be achieved by the 
integration of test strips with automatic microfluidic systems. 
However, microfluidic systems are typically fabricated using high-
cost materials and microfabrication technologies (for example, 
soft lithography)
125,194–196. Cheap but robust and stable microfluidic 
systems (for example, paper-based microfluidics) should thus be 
further developed to promote the application of biosensor devices 
in health monitoring.

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 357
Review article
and/or integrated into smartphones, watches or wristbands allow the 
daily monitoring of vital signs such as heart rate, electrocardiogram 
and electroencephalogram. Similarly, electrochemical biosensors can 
be integrated into wearable devices for the non-invasive monitoring of 
specific analytes in body fluids related to health management.
Engineering efforts are often dedicated to improving the sensitivity,  
selectivity and multiplex capability of electrochemical biosensors, 
making these devices increasingly complex and prone to failure. 
However, detection sensitivity and selectivity mainly depend on the 
recognition reaction at the delicate electrolyte–electrode interface, 
which is affected by a range of factors, such as the friction between 
electrodes and tissues, and the dynamic change of pH, flow rate 
and temperature of the body fluid, particularly in wearable devices. 
Therefore, more robust and maintenance-free electrochemical biosen-
sors need to be designed that allow long-term health monitoring; for 
example, enzyme-based sensing chemistry can be replaced by nano-
material-based catalytic sensing chemistry, which is less influenced by 
environmental conditions such as temperature, pH and ionic strength. 
In addition, the accuracy and reliability of electrochemical biosensors 
could be improved by implementing biosensor arrays that enable mul-
tiple detections in different environmental conditions. Such arrays can 
be built using all-solid-state electrodes, which can easily be integrated 
into printed circuit boards. The convoluted signals measured by the 
array can then be deconvoluted using algorithms, such as Fourier and 
wavelet transformation, to achieve simultaneous, multiplex detec -
tion. Furthermore, sensing accuracy could be improved by applying 
techniques commonly used in electrocardiograms, electromyograms 
and magnetic resonance imaging; for example, compressed sensing, 
which enables sub-Nyquist processing of sparse signals
192,193.
Commercialization and broad applicability of integrated electro-
chemical biosensors will require concerted efforts in refining sensing 
techniques and flexible materials and in consolidating electronics, 
wireless electronics, data processing and data mining.
Published online: 24 February 2023
References
1. Clark, L. C. Jr & Lyons, C. Electrode systems for continuous monitoring in cardiovascular 
surgery. Ann. NY Acad. Sci. 102, 29–45 (1962).
2. Lambrianou, A., Demin, S. & Hall, E. A. H. Biosensing for the 21st Century (eds Renneberg, R., 
& Lisdat, F.) 65–95 (Springer, 2007).
3. Labib, M., Sargent, E. H. & Kelley, S. O. Electrochemical methods for the analysis of 
clinically relevant biomolecules. Chem. Rev. 116, 9001–9090 (2016).  
This review introduces electrochemical sensors fabricated with different recognition 
elements for the detection of small molecules, nucleic acids and proteins.
4. Wu, J., Fu, Z. F., Yan, F. & Ju, H. X. Biomedical and clinical applications of immunoassays 
and immunosensors for tumor markers. Trends Anal. Chem. 26, 679–688 (2007).
5. Minteer, S. D. Advances in electroanalytical chemistry. J. Am. Chem. Soc. 140, 2701–2703 
(2018).
6. Zhang, J. J., Xiang, Y., Wang, M., Basu, A. & Lu, Y. Dose-dependent response of 
personal glucose meters to nicotinamide coenzymes: applications to point-of-care 
diagnostics of many non-glucose targets in a single step. Angew. Chem. Int. Ed. 128, 
742–746 (2016).
7. Das, A., Cui, X. K., Chivukula, V. & Iyer, S. S. Detection of enzymes, viruses, and bacteria 
using glucose meters. Anal. Chem. 90, 11589–11598 (2018).
8. Gong, S. H., Li, J. J., Pan, W., Li, N. & Tang, B. Duplex-specific nuclease-assisted CRISPR-
Cas12a strategy for microRNA detection using a personal glucose meter. Anal. Chem. 93, 
10719–10726 (2021).
9. Liu, R., Hu, Y. S., He, Y., Lan, T. & Zhang, J. J. Translating daily COVID-19 screening  
into a simple glucose test: a proof of concept study. Chem. Sci. 12, 9022–9030 (2021).
10. Cao, Y. Z. et al. Portable and sensitive detection of non-glucose target by enzyme-
encapsulated metal-organic-framework using personal glucose meter. Biosens. 
Bioelectron. 198, 113819 (2022).
11. Lubin, A. A. & Plaxco, K. W. Folding-based electrochemical biosensors: the case for 
responsive nucleic acid architectures. Acc. Chem. Res. 43, 496–505 (2010).  
This review of folding-based electrochemical biosensors research opens up ways to 
fabricate one-step response affinity biosensors for nucleic acid and protein targets.
12. Zhang, H. Q., Li, F., Dever, B., Li, X. F. & Le, X. C. DNA-mediated homogeneous binding 
assays for nucleic acids and proteins. Chem. Rev. 113, 2812–2841 (2013).  
This review introduces proximity binding-based affinity sensing mechanisms for  
one-step, homogenous detection of nucleic acid and protein targets.
13. Liu, B. W., Du, D., Hua, X., Yu, X. Y. & Lin, Y. H. Paper-based electrochemical biosensors: 
from test strips to paper-based microfluidics. Electroanalysis 26, 1214–1223 (2014).
14. Sassa, F., Biswas, G. C. & Suzuki, H. Microfabricated electrochemical sensing devices. 
Lab Chip 20, 1358–1389 (2020).
15. Noviana, E., McCord, C. P., Clark, K. M., Jang, I. & Henry, C. S. Electrochemical  
paper-based devices: sensing approaches and progress toward practical applications. 
Lab Chip 20, 9–34 (2020).
16. Lei, J. P. & Ju, H. X. Signal amplification using functional nanomaterials for biosensing. 
Chem. Soc. Rev. 41, 2122–2134 (2012).  
This review introduces nanomaterial-based signal amplification strategies, 
including functionalization methods for nanoprobes and surfaces, the functions of 
nanomaterials and their applications for ultrasensitive biosensing of biomolecules.
17. Ju, H. X. Biosensors: signal amplification for highly sensitive bioanalysis based on 
biosensors or biochips. J. Biochips Tissue Chips 2, e114 (2012).
18. Heikenfeld, J. et al. Accessing analytes in biofluids for peripheral biochemical 
monitoring. Nat. Biotech. 37, 407–419 (2019).
19. Yu, Y., Nyein, H. Y. Y., Gao, W. & Javey, A. Flexible electrochemical bioelectronics: the rise 
of in situ bioanalysis. Adv. Mater. 32, 1902083 (2020).
20. Xu, C. H., Yang, Y. R. & Gao, W. Skin-interfaced sensors in digital medicine: from materials 
to applications. Matter 2, 1414–1445 (2020).
21. Song, Y., Min, J. H. & Gao, W. Wearable and implantable electronics: moving toward 
precision therapy. ACS Nano 13, 12280–12286 (2019).
22. Hussein, H. A. et al. SARS-CoV-2-impedimetric biosensor: virus-imprinted chips for early 
and rapid diagnosis. ACS Sens. 6, 4098–4107 (2021).
23. Zeng, J. et al. An impedimetric biosensor for COVID-19 serology test and modification 
of sensor performance via dielectrophoresis force. Biosen. Bioelectron. 213, 114476 
(2022).
24. Karyakin, A. A., Gitelmacher, O. V. & Karyakina, E. E. Prussian blue-based first-generation 
biosensor: a sensitive amperometric electrode for glucose. Anal. Chem. 67, 2419–2423 
(1995).
25. Ju, H. X., Zhang, X. J. & Wang, J. NanoBiosensing: Principles, Development and 
Application 85–102 (Springer, 2011).
26. Kim, S. K. et al. Bimetallic nanocatalysts immobilized in nanoporous hydrogels for 
long-term robust continuous glucose monitoring of smart contact lens. Adv. Mater. 34, 
2110536 (2022).
27. Huang, Y. Z., Han, Y. K., Sun, J. Y., Zhang, Y. & Han, L. Dual nanocatalysts co-decorated 
three-dimensional, laser-induced graphene hybrid nanomaterials integrated with a 
smartphone portable electrochemical system for point-of-care non-enzymatic glucose 
diagnosis. Mater. Today Chem. 24, 100895 (2022).
28. Wu, J. et al. A disposable electrochemical immunosensor for flow injection immunoassay 
of carcinoembryonic antigen. Biosens. Bioelectron. 22, 102–108 (2006).
29. Wu, J., Yan, F., Tang, J. H., Zhai, C. & Ju, H. X. A disposable multianalyte electrochemical 
immunosensor array for automated simultaneous determination of tumor markers. 
Clin. Chem. 53, 1495–1502 (2007).
30. Wu, J. et al. Disposable reagentless electrochemical immunosensor array based on a 
biopolymer/sol-gel membrane for simultaneous measurement of several tumor markers. 
Clin. Chem. 54, 1481–1488 (2008).
31. Fernandez-la-Villa, A., Pozo-Ayuso, D. F. & Castano-Alvarez, M. Microfluidics and 
electrochemistry: an emerging tandem for next-generation analytical microsystems. 
Curr. Opin. Electrochem. 15, 175–185 (2019).
32. Kikkeri, K., Wu, D. & Voldman, J. A sample-to-answer electrochemical biosensor system 
for biomarker detection. Lab Chip 22, 100–107 (2022).
33. Koklu, A. et al. Microfluidic integrated organic electrochemical transistor with a 
nanoporous membrane for amyloid-beta detection. ACS Nano 15, 8130–8141 (2021).
34. Sun, S. et al. Multifunctional self-driven origami paper-based integrated microfluidic 
chip to detect CRP and PAB in whole blood. Biosens. Bioelectron. 208, 114225 (2022).
35. Feng, D. Z. et al. DNA tetrahedron-mediated immune-sandwich assay for rapid and 
sensitive detection of PSA through a microfluidic electrochemical detection system. 
Microsyst. Nanoeng. 7, 33 (2021).
36. Lee, G. H. et al. Single microfluidic electrochemical sensor system for simultaneous 
multi-pulmonary hypertension biomarker analyses. Sci. Rep. 7, 7545 (2017).
37. Pursey, J. P., Chen, Y., Stulz, E., Park, M. K. & Kongsuphol, P. Microfluidic electrochemical 
multiplex detection of bladder cancer DNA markers. Sens. Actuators B Chem. 251, 34–39 
(2017).
38. Fragoso, A. et al. Integrated microfluidic platform for the electrochemical detection 
of breast cancer markers in patient serum samples. Lab Chip 11, 625–631 (2011).
39. Zhao, Y. X., Chen, F., Li, Q., Wang, L. H. & Fan, C. H. Isothermal amplification of nucleic 
acids. Chem. Rev. 115, 12491–12545 (2015).
40. Simmel, F. C., Yurke, B. & Singh, H. R. Principles and applications of nucleic acid strand 
displacement reactions. Chem. Rev. 119, 6326–6369 (2019).
41. Dai, Y. F. et al. Exploring the trans-cleavage activity of CRISPR-Cas12a (cpf1) for the 
development of a universal electrochemical biosensor. Angew. Chem. Int. Ed. 58, 
17399–17405 (2019).
42. Zhang, D. C. et al. CRISPR/Cas12a-mediated interfacial cleaving of hairpin DNA reporter 
for electrochemical nucleic acid sensing. ACS Sens. 5, 557–562 (2020).

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 358
Review article
43. Hu, J. M., Wang, T. Y., Kim, J., Shannon, C. & Easley, C. J. Quantitation of femtomolar 
protein levels via direct readout with the electrochemical proximity assay. J. Am. Chem. 
Soc. 134, 7066–7072 (2012).
44. Hu, J. M. et al. A reusable electrochemical proximity assay for highly selective, real-time 
protein quantitation in biological matrices. J. Am. Chem. Soc. 136, 8467–8474 (2014).
45. Ren, K. W., Wu, J., Yan, F. & Ju, H. X. Ratiometric electrochemical proximity assay for 
sensitive one-step protein detection. Sci. Rep. 4, 4360 (2014).
46. Ren, K. W., Wu, J., Yan, F., Zhang, Y. & Ju, H. X. Immunoreaction-triggered DNA assembly 
for one-step sensitive ratiometric electrochemical biosensing of protein biomarker. 
Biosens. Bioelectron. 66, 345–349 (2015).
47. Ren, K. W., Wu, J., Zhang, Y., Yan, F. & Ju, H. X. Proximity hybridization regulated DNA 
biogate for sensitive electrochemical immunoassay. Anal. Chem. 86, 7494–7499 (2014).
48. Ren, K. W., Wu, J., Ju, H. X. & Yan, F. Target-driven triple-binder assembly of MNAzyme 
for amplified electrochemical immunosensing of protein biomarker. Anal. Chem. 87, 
1694–1700 (2015).
49. Zhu, J., Gan, H. Y., Wu, J. & Ju, H. X. Molecular machine powered surface programmatic 
chain reaction for highly sensitive electrochemical detection of protein. Anal. Chem. 90, 
5503–5508 (2018).
50. Man, Y. et al. An anchored monopodial DNA walker triggered by proximity hybridization 
for amplified amperometric biosensing of nucleic acid and protein. Anal. Chim. Acta 
1107, 48–54 (2020).
51. Karimi-Maleh, H. et al. A critical review on the use of potentiometric based biosensors for 
biomarkers detection. Biosens. Bioelectron. 184, 113252 (2021).
52. Ding, J. W., Chen, Y., Wang, X. W. & Qin, W. Label-free and substrate-free potentiometric 
aptasensing using polycation-sensitive membrane electrodes. Anal. Chem. 84, 
2055–2061 (2012).
53. Nurlely, A. M., Heng, L. Y. & Tan, L. L. Potentiometric enzyme biosensor for rapid 
determination of formaldehyde based on succinimide-functionalized polyacrylate 
ion-selective membrane. Measurement 175, 109112 (2021).
54. Özbek, O., Berkel, C., Isildak, Ö. & Isildak, I. Potentiometric urea biosensors. Clin. Chim. 
Acta 524, 154–163 (2022).
55. Wu, J. et al. Potentiometric detection of DNA hybridization using enzyme-induced 
metallization and a silver ion selective electrode. Anal. Chem. 81, 10007–10012 (2009).
56. Ding, J. W., Li, B. W., Chen, L. X. & Qin, W. A three-dimensional origami paper-based 
device for potentiometric biosensing. Angew. Chem. Int. Ed. 55, 13033–13037 (2016).
57. Gao, W. et al. Fully integrated wearable sensor arrays for multiplexed in situ perspiration 
analysis. Nature 529, 509–514 (2016).  
This article demonstrates a mechanically flexible and fully integrated wearable 
system for sweat metabolites and electrolytes as well as for skin temperature 
monitoring.
58. Tang, H., Yan, F., Lin, P., Xu, J. B. & Chan, H. L. W. Highly sensitive glucose biosensors 
based on organic electrochemical transistors using platinum gate electrodes modified 
with enzyme and nanomaterials. Adv. Funct. Mater. 21, 2264–2272 (2011).
59. Tang, H., Lin, P., Chan, H. L. W. & Yan, F. Highly sensitive dopamine biosensors based on 
organic electrochemical transistors. Biosens. Bioelectron. 26, 4559–4563 (2011).
60. Mak, C. H. et al. Highly-sensitive epinephrine sensors based on organic electrochemical 
transistors with carbon nanomaterial modified gate electrodes. J. Mater. Chem. C. 3, 
6532–6538 (2015).
61. Parlak, O., Keene, S. T., Marais, A., Curto, V. F. & Salleo, A. Molecularly selective 
nanoporous membrane-based wearable organic electrochemical device for noninvasive 
cortisol sensing. Sci. Adv. 4, eaar2904 (2018).
62. Lin, P., Luo, X. T., Hsing, I. M. & Yan, F. Organic electrochemical transistors integrated 
in flexible microfluidic systems and used for label-free DNA sensing. Adv. Mater. 23, 
4035–4040 (2011).
63. Fu, Y. et al. Highly sensitive detection of protein biomarkers with organic electrochemical 
transistors. Adv. Mater. 29, 1703787 (2017).
64. Kim, D. J. et al. Organic electrochemical transistor based immunosensor for prostate 
specific antigen (PSA) detection using gold nanoparticles for signal amplification. 
Biosens. Bioelectron. 25, 2477–2482 (2010).
65. He, R. X. et al. Detection of bacteria with organic electrochemical transistors. J. Mater. 
Chem. 22, 22072–22076 (2012).
66. Lin, B. P., Yan, F., Yu, J. J., Chan, H. L. W. & Yang, M. The application of organic 
electrochemical transistors in cell-based biosensors. Adv. Mater. 22, 3655–3660 (2010).
67. Chen, L. Z. et al. Organic electrochemical transistors for the detection of cell surface 
glycans. ACS Appl. Mater. Interfaces 10, 18470–18477 (2018).
68. Chen, L. Z., Wang, N. X., Wu, J., Yan, F. & Ju, H. X. Organic electrochemical transistor for 
sensing of sialic acid in serum samples. Anal. Chim. Acta 1128, 231–237 (2020).
69. Chen, L. Z., Wu, J., Yan, F. & Ju, H. X. A facile strategy for quantitative sensing of glycans 
on cell surface using organic electrochemical transistors. Biosens. Bioelectron. 175, 
112878 (2021).
70. Chen, L. Z., Wu, J., Yan, F. & Ju, H. X. Monose-modified organic electrochemical transistors 
for cell surface glycan analysis via competitive recognition to enzyme-labeled lectin. 
Mikrochim. Acta 188, 1–7 (2021).
71. Wang, N., Yang, A., Fu, Y., Li, Y. & Yan, F. Functionalized organic thin film transistors for 
biosensing. Acc. Chem. Res. 52, 277–287 (2019).
72. Yang, A. N. et al. Fabric organic electrochemical transistors for biosensors. Adv. Mater. 
30, 1800051 (2018).
73. Zang, Y., Lei, J. P. & Ju, H. X. Principles and applications of photoelectrochemical sensing 
strategies based on biofunctionalized nanostructures. Biosens. Bioelectron. 96, 8–16 (2017).
74. Ruan, Y. F. et al. An integrated photoelectrochemical nanotool for intracellular drug 
delivery and evaluation of treatment effect. Angew. Chem. Int. Ed. 133, 25966–25969 
(2021).
75. Hu, F. X., Miao, J. W., Guo, C. X., Yang, H. B. & Liu, B. Real-time photoelectrochemical 
quantification of hydrogen peroxide produced by living cells. Chem. Eng. J. 407, 127203 
(2021).
76. Ye, X. X. et al. FRET modulated signaling: a versatile strategy to construct 
photoelectrochemical microsensors for in vivo analysis. Angew. Chem. Int. Ed. 60, 
11774–11778 (2021).
77. Qi, H. L. & Zhang, C. X. Electrogenerated chemiluminescence biosensing. Anal. Chem. 
92, 524–534 (2020).
78. Chen, Y. H. & Ding, Z. F. Highly sensitive analysis strategies of microRNAs based on 
electrochemiluminescence. Curr. Opin. Electrochem. 32, 100901 (2022).
79. Miao, W. J. Electrogenerated chemiluminescence and its biorelated applications. 
Chem. Rev. 108, 2506–2553 (2008).
80. Delaney, J. L., Hogan, C. F., Tian, J. & Shen, W. Electrogenerated chemiluminescence 
detection in paper-based microfluidic sensors. Anal. Chem. 83, 1300–1306 (2011).
81. Kerr, E. et al. Amplification-free electrochemiluminescence molecular beacon-based 
microRNA sensing using a mobile phone for detection. Sens. Actuators B Chem. 330, 
129261 (2021).
82. Deiss, F. et al. Multiplexed sandwich immunoassays using electrochemiluminescence 
imaging resolved at the single bead level. J. Am. Chem. Soc. 131, 6088–6089 (2009).
83. Wang, N. N., Chen, L. Z., Chen, W. W. & Ju, H. X. Potential-and color-resolved 
electrochemiluminescence of polymer dots for array imaging of multiplex microRNAs. 
Anal. Chem. 93, 5327–5333 (2021).
84. Ma, C., Cao, Y., Gou, X. D. & Zhu, J. J. Recent progress in electrochemiluminescence 
sensing and imaging. Anal. Chem. 92, 431–454 (2020).
85. Wang, N. N. et al. Dual intramolecular electron transfer for in situ coreactant‐embedded 
electrochemiluminescence microimaging of membrane protein. Angew. Chem. Int. Ed. 
60, 197–201 (2021).
86. Wang, N. N. et al. Confined electrochemiluminescence imaging microarray for high-
throughput biosensing of single cell-released dopamine. Biosens. Bioelectron. 201, 
113959 (2022).
87. Teymourian, H., Barfidokht, A. & Wang, J. Electrochemical glucose sensors in diabetes 
management: an updated review (2010-2020). Chem. Soc. Rev. 49, 7671–7709 (2020).
88. Nagata, R., Yokoyama, K., Clark, S. A. & Karube, I. A glucose sensor fabricated by the 
screen printing technique. Biosens. Bioelectron. 10, 261–267 (1995).
89. Wang, J. Electrochemical glucose biosensors. Chem. Rev. 108, 814–825 (2008).
90. Tonyushkina, K. & Nichols, J. H. Glucose meters: a review of technical challenges to 
obtaining accurate results. J. Diabetes Sci. Technol. 3, 971–980 (2009).
91. Karon, B. S., Boyd, J. C. & Klee, G. G. Glucose meter performance criteria for tight 
glycemic control estimated by simulation modeling. Clin. Chem. 56, 1091–1097 (2010).
92. Xiang, Y. & Lu, Y. Using personal glucose meters and functional DNA sensors to quantify 
a variety of analytical targets. Nat. Chem. 3, 697–703 (2011).  
This article demonstrates a method based on the target-induced release of 
invertase from a functional DNA–invertase conjugate to enable the quantification 
of non-glucose targets using a commercial personal glucose metre.
93. Zhang, J. & Lu, Y. Biocomputing for portable, resettable, and quantitative point-of-care 
diagnostics: making the glucose meter a logic-gate responsive device for measuring 
many clinically relevant targets. Angew. Chem. Int. Ed. 57, 9702–9706 (2018).
94. Amalfitano, E. et al. A glucose meter interface for point-of-care gene circuit-based 
diagnostics. Nat. Commun. 12, 724 (2021).
95. Zhang, X. et al. Electrochemical assay to detect influenza viruses and measure drug 
susceptibility. Angew. Chem. Int. Ed. 54, 5929–5932 (2015).
96. Ahn, J. K., Kim, H. Y., Park, K. S. & Park, H. G. A personal glucose meter for label-free and 
washing-free biomolecular detection. Anal. Chem. 90, 11340–11343 (2018).
97. Singh, N. K. et al. Hitting the diagnostic sweet spot: point-of-care SARS-CoV-2 salivary 
antigen testing with an off-the-shelf glucometer. Biosens. Bioelectron. 180, 113111 (2021).
98. Rackus, D. G., Shamsi, M. H. & Wheeler, A. R. Electrochemistry, biosensors and 
microfluidics: a convergence of fields. Chem. Soc. Rev. 44, 5320–5340 (2015).
99. de Campos, R. P. S. et al. “Plug-n-Play” sensing with digital microfluidics. Anal. Chem. 91, 
2506–2515 (2019).
100. Zhao, H. et al. Accessible detection of SARS-CoV-2 through molecular nanostructures 
and automated microfluidics. Biosens. Bioelectron. 194, 113629 (2021).
101. Gong, M. M. & Sinton, D. Turning the page: advancing paper-based microfluidics for 
broad diagnostic application. Chem. Rev. 117, 8447–8480 (2017).
102. Dungchai, W., Chailapakul, O. & Henry, C. S. Electrochemical detection for paper-based 
microfluidics. Anal. Chem. 81, 5821–5826 (2009).
103. Liu, H. & Crooks, R. M. Three-dimensional paper microfluidic devices assembled using 
the principles of origami. J. Am. Chem. Soc. 133, 17564–17566 (2011).
104. Liu, H., Xiang, Y., Lu, Y. & Crooks, R. M. Aptamer-based origami paper analytical device  
for electrochemical detection of adenosine. Angew. Chem. Int. Ed. 51, 6925–6928 (2012).  
This article reports a method to fabricate a self-powered origami paper analytical 
device with a simple digital multimetre for signal readout.
105. Chen, C. A. et al. An electricity- and instrument-free infectious disease sensor based on a 
3D origami paper-based analytical device. 
Lab Chip 21, 1908–1915 (2021).
106. Su, J. et al. Smartphone-based electrochemical biosensors for directly detecting  
serum-derived exosomes and monitoring their secretion. Anal. Chem. 94, 3235–3244 
(2022).

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360
 359
Review article
107. Guo, J. H. Smartphone-powered electrochemical biosensing dongle for emerging 
medical IoTs application. IEEE T. Ind. Inform. 14, 2592–2597 (2018).
108. Ainla, A. et al. Open-source potentiostat for wireless electrochemical detection with 
smartphones. Anal. Chem. 90, 6240–6246 (2018).
109. Kim, J., Campbell, A. S., de Avila, B. E. & Wang, J. Wearable biosensors for healthcare 
monitoring. Nat. Biotechnol. 37, 389–406 (2019).  
This review discusses the development of wearable biosensing systems for health-
care monitoring, including their fundamental principles, prototypes and applications 
for different biological fluids.
110. Bariya, M., Nyein, H. Y. Y. & Javey, A. Wearable sweat sensors. Nat. Electron. 1, 160–171 
(2018).
111. Park, J. et al. Soft, smart contact lenses with integrations of wireless circuits, glucose 
sensors, and displays. Sci. Adv. 4, eaap9841 (2018).
112. Moyer, J., Wilson, D., Finkelshtein, I., Wong, B. & Potts, R. Correlation between sweat 
glucose and blood glucose in subjects with diabetes. Diabetes Technol. Ther. 14, 
398–402 (2012).
113. Baker, L. B. Physiology of sweat gland function: the roles of sweating and sweat 
composition in human health. Temperature 6, 211–259 (2019).
114. Emaminejad, S. et al. Autonomous sweat extraction and analysis applied to cystic 
fibrosis and glucose monitoring using a fully integrated wearable platform. Proc. Natl 
Acad. Sci. USA 114, 4625–4630 (2017).
115. Sonner, Z. et al. The microfluidics of the eccrine sweat gland, including biomarker 
partitioning, transport, and biosensing implications. Biomicrofluidics 9, 031301 (2015).
116. Lu, Y., Jiang, K., Chen, D. & Shen, G. Z. Wearable sweat monitoring system with integrated 
micro-supercapacitors. Nano Energy 58, 624–632 (2019).
117. Arakawa, T. et al. A wearable cellulose acetate-coated mouthguard biosensor for in vivo 
salivary glucose measurement. Anal. Chem. 92, 12201–12207 (2020).
118. Khalil, O. S. Noninvasive photonic-crystal material for sensing glucose in tears. Clin. Chem. 
50, 2236–2237 (2004).
119. Gao, Y. et al. A flexible multiplexed immunosensor for point-of-care in situ wound 
monitoring. Sci. Adv. 7, eabg9614 (2021).
120. Teymourian, H. et al. Wearable electrochemical sensors for the monitoring and screening 
of drugs. ACS Sens. 5, 2679–2700 (2020).
121. Wang, M. Q. et al. A wearable electrochemical biosensor for the monitoring of 
metabolites and nutrients. Nat. Biomed. Eng. 6, 1225–1235 (2022).
122. Yu, Y. et al. All-printed soft human-machine interface for robotic physicochemical 
sensing. Sci. Robot. 7, eabn0495 (2022).
123. Quinton, P. M. Sweating and its disorders. Annu. Rev. Med. 34, 429–452 (1983).
124. Nyein, H. Y. Y. et al. A wearable patch for continuous analysis of thermoregulatory sweat 
at rest. Nat. Commun. 12, 1823 (2021).
125. Choi, J., Kang, D., Han, S., Kim, S. B. & Rogers, J. A. Thin, soft, skin-mounted microfluidic 
networks with capillary bursting valves for chrono-sampling of sweat. Adv. Healthc. Mater. 
6, 1601355 (2017).
126. Lin, H. et al. A programmable epidermal microfluidic valving system for wearable 
biofluid management and contextual biomarker analysis. Nat. Commun. 11, 4405 
(2020).
127. Manjakkal, L., Yin, L., Nathan, A., Wang, J. & Dahiya, R. Energy autonomous sweat-based 
wearable systems. Adv. Mater. 33, 2100899 (2021).
128. Chong, Y. W., Ismail, W., Ko, K. & Lee, C. Y. Energy harvesting for wearable devices: 
a review. IEEE Sens. J. 19, 9047–9062 (2019).
129. Lou, Z., Wang, L. L. & Shen, G. Z. Recent advances in smart wearable sensing systems. 
Adv. Mater. Technol. 3, 1800444 (2018).
130. Yang, P. et al. Monitoring the degree of comfort of shoes in-motion using triboelectric 
pressure sensors with an ultrawide detection range. ACS Nano 16, 4654–4665 (2022).
131. Yang, J. H. et al. Effect of garment design on piezoelectricity harvesting from joint 
movement. Smart Mater. Struct. 25, 035012 (2016).
132. Fu, K., Zhou, J., Wu, H. U. & Su, Z. Q. Fibrous self-powered sensor with high stretchability 
for physiological information monitoring. Nano Energy 88, 106258 (2021).
133. Hao, Y. et al. Self-rebound cambered triboelectric nanogenerator array for self-powered 
sensing in kinematic analytics. ACS Nano 16, 1271–1279 (2022).
134. Luo, X. X. et al. Tribovoltaic nanogenerators based on mxene-silicon heterojunctions for 
highly stable self-powered speed, displacement, tension, oscillation angle, and vibration 
sensors. Adv. Funct. Mater. 32, 2113149 (2022).
135. Song, Y. et al. Wireless battery-free wearable sweat sensor powered by human motion. 
Sci. Adv. 6, eaay9842 (2020).
136. Qin, Y. et al. Stretchable triboelectric self-powered sweat sensor fabricated from 
self-healing nanocellulose hydrogels. Adv. Funct. Mater. 32, 2201846 (2022).
137. Kim, J. et al. Wearable salivary uric acid mouthguard biosensor with integrated wireless 
electronics. Biosens. Bioelectron. 74, 1061–1068 (2015).
138. Jia, W., Valdes-Ramirez, G., Bandodkar, A. J., Windmiller, J. R. & Wang, J. Epidermal biofuel 
cells: energy harvesting from human perspiration. Angew. Chem. Int. Ed. 52, 7233–7236 
(2013).
139. Falk, M., Andoralov, V., Silow, M., Toscano, M. D. & Shleev, S. Miniature biofuel cell as a 
potential power source for glucose-sensing contact lenses. Anal. Chem. 85, 6342–6348 
(2013).
140. Huang, X. C. et al. Epidermal self-powered sweat sensors for glucose and lactate 
monitoring. Bio-Des. Manuf. 5, 201–209 (2022).
141. Yin, L. et al. A self-sustainable wearable multi-modular E-textile bioenergy microgrid 
system. Nat. Commun. 12, 1542 (2021).
142. Chen, Z., Xi, J., Huang, W. & Yuen, M. M. F. Stretchable conductive elastomer for wireless 
wearable communication applications. Sci. Rep. 7, 10958 (2017).
143. Takei, K. et al. Nanowire active-matrix circuitry for low-voltage macroscale artificial skin. 
Nat. Mater. 9, 821–826 (2010).
144. Nyein, H. Y. Y. et al. A wearable microfluidic sensing patch for dynamic sweat secretion 
analysis. ACS Sens. 3, 944–952 (2018).
145. Rose, D. P. et al. Adhesive RFID sensor patch for monitoring of sweat electrolytes. 
IEEE Trans. Biomed. Eng. 62, 1457–1465 (2015).
146. Keum, D. H. et al. Wireless smart contact lens for diabetic diagnosis and therapy. Sci. Adv. 
6, eaba3252 (2020).
147. Lukocius, R., Vaitkunas, M., Virbalis, J. A., Dosinas, A. & Vegys, A. Physiological parameters 
monitoring system for occupational safety. Elektron. Elektrotech. 20, 57–60 (2014).
148. Lee, K. et al. Mechano-acoustic sensing of physiological processes and body motions 
via a soft wireless device placed at the suprasternal notch. Nat. Biomed. Eng. 4, 148–158 
(2020).
149. Bujes-Garrido, J. & Arcos-Martínez, M. J. Development of a wearable electrochemical 
sensor for voltammetric determination of chloride ions. Sens. Actuators B Chem. 240, 
224–228 (2017).
150. Vaddiraju, S., Burgess, D. J., Tomazos, I., Jain, F. C. & Papadimitrakopoulos, F. Technologies 
for continuous glucose monitoring: current problems and future promises. J. Diabetes Sci. 
Technol. 4, 1540–1562 (2010).
151. Zhang, J. et al. Wearable glucose monitoring and implantable drug delivery systems for 
diabetes management. Adv. Healthc. Mater. 10, 2100194 (2021).
152. Rodrigues, D. et al. Skin-integrated wearable systems and implantable biosensors: 
a comprehensive review. Biosensors 10, 79 (2020).
153. Bobrowski, T. & Schuhmann, W. Long-term implantable glucose biosensors. Curr. Opin. 
Electrochem. 10, 112–119 (2018).
154. Li, P. et al. From diagnosis to treatment: recent advances in patient-friendly biosensors 
and implantable devices. ACS Nano 15, 1960–2004 (2021).
155. Dalrymple, A. N. Implanted devices: the importance of both electrochemical 
performance and biological acceptance. Neural Regen. Res. 16, 1188–1189 (2021).
156. Kotanen, C. N., Moussy, F. G., Carrara, S. & Guiseppi-Elie, A. Implantable enzyme 
amperometric biosensors. Biosens. Bioelectron. 35, 14–26 (2012).
157. Li, C. M., Dong, H., Cao, X., Luong, J. H. & Zhang, X. Implantable electrochemical sensors 
for biomedical and clinical applications: progress, problems, and future possibilities. 
Curr. Med. Chem. 14, 937–951 (2007).
158. Wagner, J., Tennen, H. & Wolpert, H. Continuous glucose monitoring: a review for 
behavioral researchers. Psychosom. Med. 74, 356–365 (2012).
159. Xu, J. et al. Implantable platinum nanotree microelectrode with a battery-free 
electrochemical patch for peritoneal carcinomatosis monitoring. Biosens. Bioelectron. 
185, 113265 (2021).
160. Singh, P. et al. Biomedical perspective of electrochemical nanobiosensor. Nanomicro Lett. 
8, 193–203 (2016).
161. McGarraugh, G. The chemistry of commercial continuous glucose monitors. Diabetes 
Technol. Ther. 11, S17–S24 (2009).
162. Gross, T. M. et al. Performance evaluation of the MiniMed continuous glucose monitoring 
system during patient home use. Diabetes Technol. Ther. 2, 49–56 (2000).
163. Lee, H., Hong, Y. J., Baik, S., Hyeon, T. & Kim, D. H. Enzyme-based glucose sensor: from 
invasive to wearable device. Adv. Healthc. Mater. 7, 1701150 (2018).
164. Clark, J. J. et al. Chronic microsensors for longitudinal, subsecond dopamine detection in 
behaving animals. Nat. Methods 7, 126–129 (2010).
165. Tavakolian-Ardakani, Z., Hosu, O., Cristea, C., Mazloum-Ardakani, M. & Marrazza, G. Latest 
trends in electrochemical sensors for neurotransmitters: a review. Sensors 19, 2037 (2019).
166. Azzouz, A. et al. Nanomaterial-based electrochemical sensors for the detection 
of neurochemicals in biological matrices. Trends Anal. Chem. 110, 15–34 (2019).
167. Lei, L. J. et al. Nonenzymatic electrochemical sensor for wearable interstitial fluid 
glucose monitoring. Electroanalysis 34, 415–422 (2022).
168. Seaton, B. T. & Heien, M. L. Biocompatible reference electrodes to enhance chronic 
electrochemical signal fidelity in vivo. Anal. Bioanal. Chem. 413, 6689–6701 (2021).
169. Zhang, D. H. et al. Dealing with the foreign-body response to implanted biomaterials: 
strategies and applications of new materials. Adv. Funct. Mater. 31, 2007226 (2021).
170. Wickramasinghe, Y., Yang, Y. & Spencer, S. A. Current problems and potential techniques 
in in vivo glucose monitoring. J. Fluoresc. 14, 513–520 (2004).
171. Nichols, S. P., Koh, A., Storm, W. L., Shin, J. H. & Schoenfisch, M. H. Biocompatible 
materials for continuous glucose monitoring devices. Chem. Rev. 113, 2528–2549 (2013).
172. Malone-Povolny, M. J., Merricks, E. P., Wimsey, L. E., Nichols, T. C. & Schoenfisch, M. H. 
Long-term accurate continuous glucose biosensors via extended nitric oxide release. 
ACS Sens. 4
, 3257–3264 (2019).
173. Hetrick, E. M. & Schoenfisch, M. H. Reducing implant-related infections: active release 
strategies. Chem. Soc. Rev. 35, 780–789 (2006).
174. Li, J. X. et al. A tissue-like neurotransmitter sensor for the brain and gut. Nature 606, 
94–101 (2022).  
This article introduces a tissue-mimicking, stretchable, neurotransmitter sensor 
fabricated by laser patterning and demonstrates its application for in vivo real-time, 
multichannel and multiplexed monoamine sensing in the mouse brain.
175. Ben Amar, A., Kouki, A. B. & Cao, H. Power approaches for implantable medical devices. 
Sensors 15, 28889–28914 (2015).
176. Rebelo, R., Barbosa, A. I., Correlo, V. M. & Reis, R. L. An outlook on implantable biosensors 
for personalized medicine. Engineering 7, 1696–1699 (2021).

Nature Reviews Bioengineering | Volume 1 | May 2023 | 346–360 360
Review article
177. Yang, Y., Wei, X. J. & Liu, J. Suitability of a thermoelectric power generator for implantable 
medical electronic devices. J. Phys. D Appl. Phys. 40, 5790–5800 (2007).
178. Hwang, G. T. et al. Self-powered cardiac pacemaker enabled by flexible single crystalline 
PMN-PT piezoelectric energy harvester. Adv. Mater. 26, 4880–4887 (2014).
179. Zheng, Q. et al. In vivo powering of pacemaker by breathing-driven implanted 
triboelectric nanogenerator. Adv. Mater. 26, 5851–5856 (2014).
180. Simons, P., Schenk, S. A., Gysel, M. A., Olbrich, L. F. & Rupp, J. L. M. A ceramic-electrolyte 
glucose fuel cell for implantable electronics. Adv. Mater. 34, 2109075 (2022).
181. Scholten, K. & Meng, E. A review of implantable biosensors for closed-loop glucose 
control and other drug delivery applications. Int. J. Pharm. 544, 319–334 (2018).
182. Green, R. A., Lovell, N. H., Wallace, G. G. & Poole-Warren, L. A. Conducting polymers for 
neural interfaces: challenges in developing an effective long-term implant. Biomaterials 
29, 3393–3399 (2008).
183. Kutner, N., Kunduru, K. R., Rizik, L. & Farah, S. Recent advances for improving 
functionality, biocompatibility, and longevity of implantable medical devices and 
deliverable drug delivery systems. Adv. Funct. Mater. 31, 2010929 (2021).
184. Tehrani, F. et al. An integrated wearable microneedle array for the continuous monitoring 
of multiple biomarkers in interstitial fluid. Nat. Biomed. Eng. 6, 1214–1224 (2022).  
This article reports the fabrication of a fully integrated prototype of a wearable sensor 
patch-based microneedle array and introduces its application for the wireless and 
continuous real-time sensing of two metabolites in the interstitial fluid.
185. Hsieh, K., Ferguson, B. S., Eisenstein, M., Plaxco, K. W. & Soh, H. T. Integrated 
electrochemical microsystems for genetic detection of pathogens at the point of care. 
Acc. Chem. Res. 48, 911–920 (2015).
186. Zhang, J., Lan, T. & Lu, Y. Translating in vitro diagnostics from centralized laboratories 
to point-of-care locations using commercially-available handheld meters. Trends Anal. 
Chem. 124, 115782 (2020).
187. Loncaric, C., Tang, Y. T., Ho, C., Parameswaran, M. A. & Yu, H. Z. A USB-based 
electrochemical biosensor prototype for point-of-care diagnosis. Sens. Actuators B 
Chem. 161, 908–913 (2012).
188. Tu, J. B., Torrente-Rodriguez, R. M., Wang, M. Q. & Gao, W. The era of digital health:  
a review of portable and wearable affinity biosensors. Adv. Funct. Mater. 30, 1906713 
(2020).
189. Bariya, M. et al. Roll-to-roll gravure printed electrochemical sensors for wearable and 
medical devices. ACS Nano 12, 6978–6987 (2018).  
This article reports batch fabrication of flexible and robust electrode arrays by  
roll-to-roll gravure printing for a range of electrochemical sensing applications.
190. Tian, L. et al. Large-area MRI-compatible epidermal electronic interfaces for prosthetic 
control and cognitive monitoring. Nat. Biomed. Eng. 3, 194–205 (2019).  
This article reports materials, device structures, handing and mounting methods, 
and manufacturing approaches for the fabrication of large-area epidermal electronic 
interfaces.
191. Gordon, W. J. & Stern, A. D. Challenges and opportunities in software-driven medical 
devices. Nat. Biomed. Eng. 3, 493–497 (2019).
192. Liu, H. & Zhao, C. Wearable electrochemical sensors for noninvasive monitoring 
of health-a perspective. Curr. Opin. Electrochem. 23, 42–46 (2020).
193. Dixon, A. M., Allstot, E. G., Gangopadhyay, D. & Allstot, D. J. Compressed sensing system 
considerations for ECG and EMG wireless biosensors. IEEE Trans. Biomed. Circuits Syst. 
6, 156–166 (2012).
194. Koh, A. et al. A soft, wearable microfluidic device for the capture, storage, and 
colorimetric sensing of sweat. Sci. Transl Med. 8, 366ra165 (2016).
195. Kamei, K. et al. 3D printing of soft lithography mold for rapid production of 
polydimethylsiloxane-based microfluidic devices for cell stimulation with concentration 
gradients. Biomed. Microdevices 17, 36 (2015).
196. Martin, A. et al. Epidermal microfluidic electrochemical detection system: enhanced 
sweat sampling and metabolite detection. ACS Sens. 2, 1860–1868 (2017).
Acknowledgements
The authors gratefully thank the National Natural Science Foundation of China (21827812, 
21890741), the Science and Technology Project of Nanjing City (202110023) and the 
Independent Research Foundation from the State Key Laboratory of Analytical Chemistry 
for Life Science (5431ZZXM2006) for start-up supply. The authors are also grateful to Y. Lu 
in Fasteur Biotechnology for market information, to Q. Yu, Y.C. Chen and L.J. Lei for helpful 
comments.
Author contributions
J.W., H.L. and H.X.J. arranged the sections of the Review. J.W., W.W.C. and H.X.J. wrote the 
introduction and the section on electrochemical biosensing of disease biomarkers, and H.L., 
B.M and H.X.J. wrote the sections on portable electrochemical biosensing devices, integration 
into wearable devices and integration into implantable devices. All authors discussed the 
outlook section and display items.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary information The online version contains supplementary material available at  
https://doi.org/10.1038/s44222-023-00032-w.
Peer review information Nature Reviews Bioengineering thanks Onur Parlak, Chung Chiun Liu, 
and Susana Campuzano for their contribution to the peer review of this work.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to  
this article under a publishing agreement with the author(s) or other rightsholder(s); author 
self-archiving of the accepted manuscript version of this article is solely governed by the 
terms of such publishing agreement and applicable law.
© Springer Nature Limited 2023