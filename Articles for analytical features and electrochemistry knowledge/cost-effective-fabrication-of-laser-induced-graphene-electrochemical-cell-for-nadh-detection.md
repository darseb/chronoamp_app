> This article is licensed under ~~___~~ CC-BY 4.0 ©® ~~TO~~ http://pubs.acs.org/journal/acsodf Article 

## **Cost-Effective Fabrication of Laser-Induced Graphene Electrochemical Cell for NADH Detection** 

_Published as part of ACS Omega special issue “Chemistry in Brazil: Advancing through Open Science”._ 

Ketley Caroline Rocha Pereira, Elsa Maria Materón, Matheus Santos Dias, Tatiana Parra Vello, Deissy Feria Garnica, Gustavo Miguel Sousa, Camila Marchetti Maroneze, and Cecilia de Carvalho Castro Silva* 

**Cite This:** https://doi.org/10.1021/acsomega.5c04282 **Read Online** ~~e~~ s ~~i~~ © 

ACCESS Metrics & More Article Recommendations 

* **sı** Supporting Information 

ABSTRACT: The unique properties and versatile applications of laser-induced graphene (LIG) have garnered significant interest for electrochemical sensing technologies. In this study, we report the fabrication and application of an in-house produced LIG/polyimide (PI) composite, generated via 450 nm laser irradiation, for the amperometric detection of Nicotinamide Adenine Dinucleotide (NADH), a critical biomarker associated with several neurodegenerative human diseases. The LIG structure was confirmed by Raman spectroscopy, X-ray photoelectron spectroscopy (XPS), and sheet resistance measurements, with an average sheet resistance ( _R_ s) of 24.38 ± 2.19 Ω/□, indicating excellent electrical conductivity. XPS analysis revealed the presence of C O bonds (288.9 eV), formed under oxidizing conditions during LIG fabrication, which may contribute to enhanced electrocatalytic activity by facilitating NADH oxidation Graphene through redox mediation. Using a printed Ag/AgCl pseudoreference electrode and an applied potential of only 50 mV vs Ag/AgCl, NADH was detected within a concentration range of 5 _μ_ mol L[−][1] to 10 mmol L[−][1] . The sensor exhibited a limit of detection (LOD) of 2.72 _μ_ mol L[−][1] and a limit of quantification (LOQ) of 9.07 _μ_ mol L[−][1] , with a linear response up to 1 mmol L[−][1] . The repeatability of the electrochemical oxidation of NADH resulted in a relative standard deviation (RSD) of 2.76%, while the reproducibility, evaluated as intra- and interbatch variability, yielded RSD values of 5.78 and 8.22%, respectively. Furthermore, the total material cost for each electrochemical cell was estimated at only U$ 0.10, highlighting the method’s potential for low-cost and environmentally friendly biosensor development. The fabricated LIG platform offers a promising route for sensitive, scalable, and sustainable detection of NADH and potentially other clinically relevant analytes. 

## **1. INTRODUCTION** 

Current diagnostic techniques often require specialized personnel, intricate laboratory setups, and expensive reagents and solvents.[1][,][2] Undoubtedly, the imperative for point-of-care solutions cannot be overstated, owing to their remarkable attributes of swift response and high sensitivity. In light of this demand, wearable and flexible disposable electrochemical sensors and biosensors have emerged as promising alternatives, offering affordability, potential for miniaturization, low cost, and compatibility with eco-friendly methodologies.[3][−][5] 

Graphene derivative materials are often used as an ideal electrode material for the development of electrochemical sensors[6] due to their excellent electrical (carrier mobility ∼250,000 cm[2] V[−][1] s[−][1] ) and mechanical (Young’s modulus: 1 × 10[12] Pa) properties, large surface area (2630 m[2] g[−][1] ), chemical stability and biocompatibility.7−10 Conventionally, graphene derivative materials with some degree of structural defects, such as dangling bonds, vacancies, exposed edges, or even a limited presence of oxygen functional groups, demonstrate enhanced electrochemical activity (fast heteroge- 

neous electron transfer (HET)) in electrochemical sensors and biosensors.[10][−][13] In this context, reduced graphene oxide (rGO) has been deeply explored in the development of electrochemical sensors[14][−][16] and biosensors.[17][−][19] Despite notable progress in the large-scale solution process of graphene oxide (GO), the utilization of rGO often involves the complex synthesis of GO. This process traditionally requires strong chemical reagents for oxidizing graphite to GO, as the Hummers’ method,[20] leading to the generation of a substantial volume of acidic residues that demand considerable energy and operational costs for recovery and treatment.[21] Moreover, releasing toxic fumes such as N2O4 and NO2 into the atmosphere, along with ion leaching into water (Na[+] and 

Received: May 8, 2025 Revised: August 8, 2025 Accepted: October 6, 2025 

© XXXX The Authors. Published by American Chemical Society 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**A** 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

Scheme 1. Schematic Representation of the Laser-Induced Graphene Sensors Fabrication Process 

NO3−), raises environmental concerns.22 Besides the manufacturing process of GO dispersion, it is imperative to fabricate a film with precise control over the thickness and orientation of the flakes on the target substrate before the reduction process.[21] Various surface-based coating techniques, such as − dip coating, spin coating, drop-casting, Langmuir Blodgett method, and electrophoretic deposition, have been investigated for this purpose.[23][,][24] However, scaling up these methods remains challenging. Finally, to obtain rGO, it is necessary to undergo the reduction process of GO, which can be achieved through various approaches, but conventionally through thermal treatment at high temperatures and/or through the use of hazardous chemical reduction agents (e.g., hydrazine, hydroiodic acid, and sodium borohydride),[23] representing high energy consumption and environmental impact. 

Despite intensive research efforts, achieving chemical-free, low-temperature, and cost-effective processing of high-quality graphene derivative materials remains a significant challenge. In this way, researchers investigate alternative synthesis methods for graphene-based conductive materials. These methods aim to minimize ecological impact and waste generation and facilitate mass production while enhancing technological accessibility. In this scenario, laser-assisted processing methods have emerged as a powerful technique across diverse applications, spanning from materials processing to device fabrication. Particularly, laser-direct writing (LDW) distinguishes itself as a mask-less, catalyst-free, harmless, and noncontact approach, facilitating adaptable, swift, direct, and effective fabrication of intricate structures at macro-, micro-, and nanoscales utilizing laser technology.[25] Significantly, LDW has been used in numerous investigations to transform GO into graphene derivative[26] aiming at the development of different electrochemical and electrical devices, from sensing to energy storage.[17][−][19][,][26][,][27] For instance, in 2014, James Tour’s research team at Rice University introduced a technique for producing three-dimensional (3D) porous graphene, denominated laser-induced graphene (LIG), by directly converting polymeric substrates into graphene through LDW.[28] LIG production stands out as a one-step process that eliminates the need for high-temperature conditions, solvents, or subsequent treatments.[29][,][30] It offers high precision, reproducibility, scalability (from nanomicro to macro dimensions), industrial feasibility, affordability, rapidity, large surface areas, eco- 

friendliness, ease of pattern creation, and excellent thermal and electrical conductivity.[30] Furthermore, this methodology allows for the incorporation of metallic precursors to facilitate the simultaneous formation of nanoparticles and graphenebased materials, reducing the number of modification steps in the devices and enabling fast production.[31] 

Laser-scribed polyimide materials have been widely explored, but it has been demonstrated that most of other polymer source materials undergo ablation when irradiated with a laser at room temperature.[32][,][33] This opens up the possibility of utilizing nonpolymers, paper, metal/plastic composites, biodegradable materials, naturally occurring substances, and even foods as platforms for generating LIG.[34][,][35] The laser transforms a suitable polymeric substrate into LIG through a photothermal pyrolysis process. Various laser types, including excimer (248 nm), CO2 (10.6 _μ_ m), a low-energy laser diode (780 nm), near-IR (NIR) lasers (1070 nm), and neodymium-doped yttrium aluminum garnet laser (1064 nm), have been employed in LIG methodology.[30] However, the high intrinsic cost of some lasers severely restricts their widespread use in mass manufacturing LIGbased applications, limiting them primarily to laboratory settings. Numerous studies documented in the literature have employed LIG for detecting a range of analytes, including uric acid,[36] _Salmonella enterica_ in chicken broth,[37] sulfanilamide,[38] nitrogen,[39] paraquat,[40] and atrazine pesticides,[41] among others. 

In this study, we present a cost-effective, straightforward, one-step fabrication method for producing flexible electrochemical sensors utilizing a simple, low-cost laser engraver machine (450 nm), exploring a low power consumption of energy (295 mW) and polyimide (PI) as a polymer source, in a complete integrated electrochemical cell. As a proof of concept, we employed the versatile electrochemical sensor based on LIG to detect Nicotinamide Adenine Dinucleotide (NADH), a crucial biomarker involved in metabolic redox reactions within living cells.[42] Ultimately, this methodology enables the fabrication of conductive materials for many applications. 

## **2. EXPERIMENTAL SECTION** 

**2.1. Laser-Induced Graphene-Based Sensor Fabrication.** First, the LIG was obtained on PI with 125 _μ_ m-thick substrates (FlexFilm, Brazil), using a pulsed laser (laser 

**B** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**==> picture [498 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
ACS Omega http://pubs.acs.org/journal/acsodf Article<br>**----- End of picture text -----**<br>


Figure 1. (a) Schematic representation of LIG sensor, working electrode (WE) and counter electrode (CE) obtained on Polyimide substrate by laser irradiation. (b) SEM images of LIG surface morphology in different magnifications (i and ii). (c) Representation of the obtained Raman spectra of LIG in different sample areas in multiple samples. (d) Representative XPS analysis of LIG samples: survey spectrum with elemental composition analysis (i) and high-resolution spectrum for C 1s (ii). 

wavelength of 450 nm, frequency of 20 kHz), under conditions of 295 mW laser power, engraving speed of 8 mm/s, and one processing step, in an air atmosphere. A control experiment was conducted to prepare the surface of LIG electrodes under varying laser conditions, specifically using a laser power of 82.5 mW, an engraving speed of 17 mm/s, and two processing passes, all performed in ambient air. The laser power was measured using a Newport 1935-C power meter (minimum resolution: 1 pW), coupled to a Thorlabs 1W optical fiber (Model 5401C, S/N 00114 WARL, spectral range: 0.2−10.6 _μ_ m). 

The electrochemical LIG-based sensors were manufactured following the procedure illustrated in Scheme 1. The electrochemical cell was composed of three electrodes. The working (geometric area = 0.096 cm[2] ) and counter electrodes were made by LIG. The metal contact lines and silver reference electrode were obtained using silver ink (SPI-ink), deposited using a regular brush over the polyimide, and a shadow mask delimited the LIG area. A curing process was performed in a hot plate (Tecnal) at 120 °C for 20 min to remove the excess solvent from the silver ink. To delimit the active area of the electrodes and avoid interference response from exposed silver contact lines, a layer of nail polish was applied between the electric contacts and electrodes (the work, counter, and pseudo reference, respectively), followed by passivation with Kapton tape. Finally, the Ag/AgCl pseudo reference electrode was manufactured based on the work reported by Silva et al.[43] A commercial bleach solution (2.5% (v/v) sodium hypochlorite) was dripped over the reference silver electrode area for 10 min, followed by Milli-Q water rinsing and dried by a Nitrogen stream. 

**2.2. Laser-Induced Graphene Characterization.** LIG’s structure was characterized through Raman spectroscopy coupled to a confocal optical microscope, Witec _α_ 300R. The measurement was performed using a 532 nm laser source with a power of 1.5 mW and a microscope objective of 50× magnification. The spectra were acquired with 10 s of integration time and an accumulation of 10 spectra. 

X-ray photoelectron spectroscopy (XPS) experiments (survey and high-resolution C 1s spectra), were performed with a Thermo Scientific K-Alpha spectrometer. Two different areas of the LIG’s sample were analyzed, and all spectra were taken using an Al K _α_ microfocused monochromatized source with a resolution of 0.100 eV, pass energy of 50 eV, and a spot size of 300 _μ_ m. The peak fitting was performed using the Avantage software (version 6.6). 

For the electrical characterization, circular samples (1 cm of diameter) were obtained, and the values of LIG sheet resistance (Ω/□) were analyzed by the Osilla Four-Point probe system, with a maximum current range applied of 100 _μ_ A. Six different samples of LIG were analyzed in two to four different areas of each sample. The morphology of the LIG was characterized by field-emission scanning electron microscopy (SEM) (Jeol, model JSM-7800). 

The fabricated LIG sensors and Ag/AgCl pseudoreference electrodes were electrochemically characterized. First, the quality of the pseudoreference electrode was evaluated by chrono potentiometric analysis, using a potentiostat from Autolab (PGSTAT204) in a solution of KCl 3 mol L[−][1] and a standard external reference Ag/AgCl (3 mol L[−][1] KCl) electrode. The long-term stability of the Ag/AgCl pseudoreference electrodes was evaluated over a one-year period by analyzing 12 electrodes, with measurements performed on 

**C** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

three different electrodes at each time point using the same experimental procedure. To preserve their integrity, the electrodes were stored in a desiccator under vacuum conditions (−400 mmHg) between measurements. 

In addition, the electrochemical behavior of the LIG sensors was characterized by cyclic voltammetry employing Fe(CN)6 2−/3− at 10 mmol L−1 in KCl 3 mol L−1 as a redox probe. 

**2.3. Electrochemical Detection of NADH.** The fabricated laser-induced graphene-based sensors were tested for NADH detection as proof of concept. For this, cyclic voltammetry was performed on a blank sample, and a 1 mmol L[−][1] NADH solution was prepared in a 100 mmol L[−][1] sodium phosphate buffer (pH 7.4) at a scan rate of 10 mV/s. Chronoamperometry was employed to quantify NADH in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4) and measured at 50.0 mV vs a printed Ag/AgCl pseudo reference electrode. The current signal for each concentration was recorded at 150 s. Additionally, results from cyclic voltammetry were compared with those obtained from a commercial screen-printed carbon electrode (SPCE), under the same experimental conditions described previously. 

Selectivity studies were conducted by evaluating potential interfering compounds commonly present in whole blood, specifically glucose and urea, at fixed concentrations of 5 mM and 7 mM, respectively, values that correspond to their normal physiological levels.[44] Chronoamperometric measurements were carried out in triplicate ( _n_ = 3) using a 0.1 M phosphate-buffered saline (PBS) solution at pH 7.4. A potential of +50 mV vs Ag/AgCl was applied to LIG-based electrodes for the electrochemical detection of 1 mM NADH under different conditions: in the presence of 5 mM glucose, 7 mM urea, and both interferents simultaneously. 

## **3. RESULTS AND DISCUSSION** 

Figure 1(a) presents a schematic representation of LIG nanomaterials synthesis on PI polymer substrate. The laser scribing process promotes the fabrication of porous carbon nanostructures by simultaneously breaking the carbon bonds in PI, thereby embedding and patterning them into LIG shaped electrode.[31] The porous structure of LIG is confirmed by the SEM images in Figure 1(b i-ii), which reveal the material’s surface. The high-magnification image (Figure 1b-ii) illustrates the microporosity of the LIG material, exhibiting a random aspect due to the high local heating and thermal expansion induced by laser irradiation during the conversion of PI to LIG.[45] 

Figure 1(c) exemplifies the characteristic Raman spectra of the LIG obtained from different prepared samples. The graphene-derived materials exhibit three characteristic bands. The D band, around 1350 cm[−][1] , suggests a structural disorder in the basal plane of the sample, indicating possible defects in the sheet plane or edge defects (dangling bonds) and residual oxygen functional groups. The G band, at 1580 cm[−][1] , has its position and intensity directly related to the degree of graphitization in sp[2] carbon atom structures, attributed to the stretching mode of C�C. Lastly, the two-dimensional (2D) band, near 2700 cm[−][1] , suggests the level of organization in the bidimensional plane of the structure.[46] 

The observed high intensity of the D band relative to the G band in the Raman spectra was confirmed by the high mean value of the intensity ratio of D and G bands ( _I_ D/ _I_ G) of 1.13 ± 0.15 ( _n_ = 10), indicating a high defect density in the formed graphitic structure, possibly due to the low power of the laser 

used in the air atmosphere, which may contribute to a lower level of graphitization degree and the presence of some oxygen functional groups.[35][,][47] The low intensity of the 2D band is related to the structural disorder of the bidimensional plane of LIG due to the porous structure of this material.[31] Despite these characteristics, slight deviations in the band intensities were observed in the Raman features, which may be related to the laser path. In some areas, there may exist an overlap between the LIG layers when the second laser scanner interacts with the borders of the LIG formed in the previous scan, altering some structural aspects of the LIG in these specific areas.[48] 

XPS measurements were performed to evaluate the atomic composition of LIG electrodes. Figure 1(d - (i)) shows the survey XPS spectrum of the representative LIG sample confirming the dominant presence of carbon atoms (C 1s) at 285.07 eV and 85.21%, followed by oxygen (O 1s) at 532,78 eV and 10.26%, and nitrogen (N 1s) at 400.08 eV and 4.54%. Nitrogen atoms are related to some residues of C−N bonds from polyimide that were not fully converted during the laser irradiation to LIG.[49][,][50] The C 1s high-resolution XPS spectra presented in Figure 1(d - (ii)) shown the four bonding modes and their approximate binding energies: C�C/C−C (284.5 eV), C�O (288.9 eV) and _π_ − _π_ shakeup satellite peaks characteristic of sp[2] -hybridized carbon (291.2 and 293.8 eV), which reveal the crystalline nature of carbon atoms on the LIG structure.[51][−][53] The band observed at 288.9 eV confirms the presence of C�O bonds within the LIG structure, formed during the laser-induced graphene fabrication process in an air environment (an oxidizing atmosphere).[54] This feature is particularly valuable for the electrochemical performance of LIG-based sensors, as carbonyl oxygen groups can act as redox mediators in the electrocatalytic oxidation of specific biomolecules, such as NADH. Carlson and Miller were among the first to demonstrate the mechanism of NADH oxidation mediated by quinones,[55] and later, de Camargo et al. further explored the role of these functional groups in enhancing the electrocatalytic oxidation of NADH on electrochemically reduced graphene oxide-based electrodes.[56] 

The electric aspects of formed LIG were investigated by a four-point probe system, which indicates an extremely important parameter for attesting the electric quality of materials applied to the development of electrochemical sensors. Regarding this, six different samples of LIG in PI substrates were evaluated, and different areas of the samples were measured, totalizing 20 sheet resistance measurements, enabling the sheet resistance ( _R_ s) mean value of 24.38 ± 2.19 Ω/□. This low value obtained characterizes the material as having excellent electrical conductivity in comparasion with other works reported in the literature that obtained LIG from PI.[57][−][62] Despite the high density of structural defects revealed by Raman spectroscopy (indicated by the strong intensity of the D band), the LIG produced under these conditions exhibits good electrical percolation and excellent electrical conductivity. This is attributed to the use of a low-wavelength (450 nm), low-power (295 mW) laser, which enables the formation of C sp[2] domains without reaching excessively high local temperatures. As a result, the surface roughness of the LIG is reduced, further enhancing electrical percolation.[63] 

The fabricated LIG-based sensors were electrochemically characterized. Primarily, the quality of the pseudoreference electrode was evaluated through chronopotentiometric analysis, comparing the manufactured electrode with a commercial 

**D** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega http://pubs.acs.org/journal/acsodf** 

Article 

Figure 2. (a) Chronopotentiometric analysis of fabricated reference electrode vs commercial Ag/AgCl (3 mol L[−][1] KCl) reference electrode recorded in KCl (3 mol L[−][1] ). (b) Cyclic voltammetry of LIG sensor fabricated reference electrode vs commercial Ag/AgCl (3 mol L[−][1] KCl) reference electrode in 10 mmol L[−][1] Fe[(CN)6][3][−][/4][−] 3 mol L[−][1] KCl solution. Scan rate: 30 mV/s. (c) Cyclic voltammetry of LIG sensor in 10 mmol L[−][1] Fe[(CN)6][3][−][/4][−] 3 mol L[−][1] KCl solution (Scan rate: 10 to 200 mV/s). (d) Linear relationship of the anodic (Ipa) and cathodic (Ipc) peak currents as a function of the square root of the potential scan rate. 

Ag/AgCl (3 mol L[−][1] KCl), as shown in Figure 2(a). The potential variation between the commercial electrode and the manufactured electrode obtained was under 1.5 (±0.5) mV in 800 s, demonstrating excellent stability and the effectiveness of the method in producing a pseudoreference electrode with performance comparable to that of a commercial one. The long-term stability of the fabricated Ag/AgCl pseudoreference electrodes was evaluated over a period of one year by analyzing 12 samples, as shown in Figure S1. After one year, the opencircuit potential (OCP) exhibited a slight variation, changing from 1.5 ± 0.5 to 2.2 ± 1.9 mV, indicating good stability and reproducibility of the pseudoreference electrodes under the tested storage conditions. 

To better understand the electrochemical behavior of manufactured pseudoreference electrode, cyclic voltammetry experiments were performed in Ferri/Ferro redox couple (Fe[(CN)6][3][−][/4][−] ) 10 mmol L[−][1] in KCl (3 mol L[−][1] ) electrolyte (which is sensitive to electrode surface) compared to a commercial Ag/AgCl reference electrode. Figure 2(b) exhibits the voltammetric profile of the LIG sensor with a manufactured pseudoreference electrode (in red) in comparison to the commercial reference electrode (in black). 

As presented, the voltammetric profile overlap demonstrates that the manufactured pseudoreference electrode of the sensor has a very similar behavior compared to a commercial sensor. 

For a deeper evaluation of the electrochemical behavior of the electrode surface, experiments using the Ferri/Ferro redox couple with different scan rates were done with values between 10 and 200 mV/s, as demonstrated in Figure 2(c). The scan profile indicates an increase of the oxidation and reduction peak currents along with the increase of the scan rate. 

The obtained values of oxidation (Ipa) and reduction (Ipc) peak current were plotted as a function of the scan rate square root (v[1/2] ), aiming to evaluate the diffusion-controlled nature of the electrochemical process, as illustrated in Figure 2(d). 

Analyzing the graph, and throw linear equations: Ipa = −2.28 × 10[−][5] ± (1.14 × 10[−][6] ) + 1.57 × 10[−][3] ± (5.04 × 10[−][6] ) v[1/2] ( _r_[2] = 0.999) and Ipc = 2.86 × 10[−][5] ± (9.84 × 10[−][7] ) − 1.61 × 10[−][3] ± (6.59 × 10[−][6] ) v[1/2] ( _r_[2] = 0.999) it is possible to observe that Ipa and Ipc values rise linearly as the scan rate square root increases, proving that the Fe[3+] /Fe[2+] redox couple is commanded by a diffusion process, with mass transport as a determinant factor of the reaction, not electron transference.[64] 

Cyclic voltammetry measurements were carried out at a scan rate of 10 mV s[−][1] in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4), using both a blank sample (black curve, Figure 3a) and a sample containing 1 mmol L[−][1] NADH (red curve). Experiments were conducted on the LIG sensor and a commercial SPCE for comparison. On the LIG sensor, the NADH oxidation peak appears at approximately −22 mV vs 

**E** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega http://pubs.acs.org/journal/acsodf** 

Article 

Figure 3. (a) Cyclic voltammetry of LIG-based sensor vs SPCE in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4) comparing oxidation potential of 1 mmol L[−][1] NADH. Scan rate: 10 mV/s. (b) Schematic representation of NADH oxidation on the surface of the LIG electrode. (c) Amperometry of LIG-based sensor in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4). The potential applied: 50 mV vs. printed Ag/AgCl. (d) Calibration curve of LIG-based sensor for NADH detection in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4). _n_ = 3. (e) The linear range of the LIG-based sensor’s calibration curve for NADH detection in 100 mmol L[−][1] sodium phosphate buffer (pH 7.4). _n_ = 3. 

Ag/AgCl. Under identical conditions, the commercial SPCE requires a substantially higher overpotential to oxidize the NADH. As shown in Figure 3(a), the potential difference between the oxidation peaks recorded on the LIG sensor and the SPCE is approximately 330 mV vs Ag/AgCl. The peak potential observed with the fabricated sensors enables the application of amperometric detection for NADH by applying a fixed potential corresponding to the NADH oxidation peak and monitoring the resulting current aiover time. Notably, while NADH typically oxidizes at potentials above 1 V on bare electrodes,[65] in this case, oxidation was achieved at a much lower potential, around 50 mV (end of the oxidation process on the LIG electrode). This behavior suggests that the oxygen functional groups present on the LIG surface, C O, determined by C 1s high resolution XPS (Figure 1(d-ii)), interact with NADH as a redox mediator, promoting electrocatalytic activity toward NADH oxidation, a typical behavior, proton-dependent, previously observed for quinone groups,[56] as can be seen in the schematic representation of Figure 3(b). The role of carbonyl oxygen groups (quinones) in enabling the electrooxidation of NADH at lower overpotentials was confirmed by fabricating LIG-based electrodes under modified laser conditions, using a lower laser fluence (303.5 mJ/cm[2] ) compared to that employed in the preparation of the standard LIG electrodes used in this study (1086.8 mJ/cm[2] , as calculated in the Supporting Information). The reduced laser fluence limited the formation of carbonyl functionalities and decreased the overall content of C−O groups, due to a lower local temperature that inhibits the extensive oxidation of carbon atoms in the ambient atmosphere.[51][,][66][,][67] This variation in chemical composition was confirmed by XPS analysis, including both survey and high-resolution C 1s spectra, as shown in Figure S2(a−b). The electrodes fabricated under 

low-laser fluence conditions exhibited a reduced oxygen content (5.74%) compared to the standard LIG electrodes (10.26%), and showed the absence of C O (carbonyl) groups, with only a small contribution from less oxidized carbon species, such as C−O groups. This limited surface oxidation led to a significantly higher electrooxidation potential for NADH, approximately ∼600 mV vs Ag/AgCl, as shown in the cyclic voltammogram of Figure S3. These findings clearly demonstrate that the presence of quinone groups is essential to promote efficient electrooxidation of NADH at low overpotentials. 

Figure 3(c) shows the amperometric response of NADH at different concentrations, recorded at an applied potential of 50 mV vs Ag/AgCl for 200 s. On the LIG sensor, the current increases proportionally with NADH concentration, indicating effective oxidation. These results were used to construct the calibration curve for NADH detection, shown in Figure 3(d). The current values at 150 s of amperometry were used for the calibration. The linear regression equation obtained from Figure 3(e) was: LIG sensor Δ _I_ (A) = 1.49 × 10[−][8] (±7.09 × 10[−][9] ) + 0.00219 (±7.97 × 10[−][5] ) [NADH] (mol L[−][1] ) ( _r_[2] = 0.995). Based on these results, the sensor exhibited a linear response over the concentration range of 5 _μ_ M to 1 mM. The limit of detection (LOD), calculated as 3 × Sd blank/Slope for the LIG-based sensor was determined to be 2.72 _μ_ mol L[−][1] , while the limit of quantification (LOQ), calculated as (10 × Sd blank[/Slope)][was][9.07] _[μ]_[mol][L][−][1][.] 

One of the main challenges in developing electrode materials for the electrochemical detection of NADH is their instability due to surface fouling caused by the oxidation of NADH to NAD[+] .[44] Another critical issue is selectivity, as the electrochemical signal for NADH oxidation can be influenced by the oxidation of other species commonly present in whole blood 

**F** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

samples, such as glucose and urea, typically found at concentrations of 5 and 7 mM, respectively.[44] To evaluate the selectivity of the sensor, chronoamperometric measurements were performed at +50 mV vs Ag/AgCl using LIGbased electrodes for the electrochemical detection of 1 mM NADH, 5 mM glucose, 7 mM urea, and 1 mM NADH in the presence of 5 mM glucose, 7 mM urea, and both interferents simultaneously. The corresponding chronoamperograms are presented in Figure S4(a−f). From these measurements, the variation in oxidation current (Δ _I_ = _I_ a − _I_ blank) for the different analyzed species is presented in Figure 4. The results 

Figure 5. Evaluation of the repeatability and reproducibility (intraand interbatch) of the LIG-based sensor for the detection of 100 _μ_ M NADH in 100 mM PBS (pH 7.4). Applied potential: 50 mV vs Ag/ AgCl; total measurement time: 200 s. 

Figure 4. Selectivity test for the LIG-based sensor for 1 mM of NADH, 5 mM of glucose and 7 mM of urea. 

demonstrate that the LIG-based sensor developed in this study exhibits high selectivity for NADH, even in the presence of potential interferents such as glucose and urea. This enhanced selectivity is attributed to the low applied potential (+50 mV vs Ag/AgCl) and the presence of carbonyl functional groups on the LIG surface, which act as quinone-like redox mediators, as previously discussed. These characteristics facilitate the selective electrooxidation of NADH while effectively suppressing the contribution of other electroactive species. 

Figure 5 presents the repeatability of NADH measurements and the intra- and interbatch reproducibility of the LIG-based sensor fabrication process. Repeatability was assessed by performing 10 successive chronoamperometric measurements using the same sensor for the detection of 100 _μ_ M NADH in 100 mM PBS (pH 7.4), resulting in a relative standard deviation (RSD) of 2.76%, which indicates excellent measurement consistency. Intrabatch reproducibility was evaluated by analyzing five independently fabricated electrodes ( _n_ = 5) produced on the same day under identical conditions, yielding an RSD of 5.78%. To assess interbatch reproducibility, three electrodes fabricated on three different days were used to detect 100 _μ_ M NADH under the same experimental conditions, resulting in an RSD of 8.22%. These results demonstrate that the LIG-based electrodes exhibit good repeatability and reproducibility, both among electrodes produced in the same batch and between different fabrication batches, highlighting their potential as a reliable platform for the development of electrochemical sensors. 

The stability and lifetime of the electrochemical sensor are critical parameters for practical applications and were therefore thoroughly investigated. The long-term stability of the LIGbased sensors was evaluated over a one-year period by analyzing a total of 12 electrodes. At each time point, measurements were performed using three different electrodes ( _n_ = 3) fabricated in separate batches, following the same experimental protocol for the detection of 100 _μ_ M NADH under identical conditions. To maintain their integrity, all electrodes were stored in a desiccator under vacuum conditions (−400 mmHg) between measurements. As shown in Figure 6(a,b), a slight decrease in the current variation during the electrooxidation of 100 _μ_ M NADH was observed, with a reduction of approximately 26.24%. In addition, after one year of storage under vacuum, the relative standard deviation (RSD) for the detection of 100 _μ_ M NADH increased from 2.04 to 10.36%, indicating low loss of reproducibility over time. 

Several studies from the literature were evaluated for comparison with our results, focusing on cases where carbon electrodes were modified for NADH detection, as summarized in Table 1. Although some of these electrochemical sensors operate at relatively low potentials, they generally require additional surface modifications. In contrast, the fabricated LIG-based sensor achieved a significantly lower oxidation potential without any modification or post-treatment. In addition to the results obtained in this work, the fabrication of the LIG sensor can be considered low-cost. The unit cost for sensor fabrication is presented in Table 2. 

The cost per sensor for the polyimide was calculated based on the area used to fabricate each sensor, while the costs of the other materials were estimated considering their use in the fabrication of approximately 200 sensors. The total cost for the fabrication of each electrochemical cell was U$ 0.10. 

## **4. CONCLUSIONS** 

In this work, we successfully demonstrated the fabrication of a low-cost, in-house laser-induced graphene (LIG) sensor for the amperometric detection of NADH. The LIG/polyimide (PI) composite, produced via 450 nm laser irradiation, exhibited 

**G** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

Figure 6. (a) Long-term stability analysis of LIG-based sensors over a one-year storage period, showing the variation in current response for 100 _μ_ M NADH. (b) Representative chronoamperometry curves for the electrooxidation of 100 _μ_ M NADH in 0.01 M PBS (pH 7.4), obtained using LIG-based sensors after different storage durations (1 day and 1 year). Applied potential: 50 mV vs Ag/AgCl; total measurement time: 200 s. 

Table 1. Comparison of other Carbon-Based Sensors for NADH Determination _[a]_ 

|electrode|potential|linear range (_μ_mol L−1)|LoD (_μ_mol L−1)|refs|
|---|---|---|---|---|
|graphene/tungstate/GCE|−1.04 V vs Ag/AgCl|10−270|49.80|68|
|CRGO/GCE|0.45 V vs Ag/AgCl|50−650|21.85|69|
|AuNR@RGO/GCE|0.54 V vs SCE|1−31|0.22|70|
|TOA+ /PGE|0.55 V vs Ag/AgCl|1.0−15|0.077|71|
|MWCNT/3,5-DNBPh/GCE|0 V vs Ag/AgCl|100−600|22.30|72|
|PTZ/AgSNPs/SPE|0.4 V vs Ag/AgCl|1.9−89|0.76|73|
|PTZ/AgPNPs/SPE|0.4 V vs Ag/AgCl|1.9−89|0.61|73|
|PTZ/AgRNPs/SPE|0.4 V vs Ag/AgCl|1.9−89|0.52|73|
|NPG/Os(bpy)2PVI/DIA|0.35 V vs Ag/AgCl|5−100|0.80|74|
|Co-NC/Pd/CPE|0.22 V vs Ag/AgCl|5−1250|2.00|75|
|LIG|0.05 V vs Ag/AgCl|5−1000|2.72|this work|



> _a_ CRGO- chemically reduced graphene oxide, AuNR-Gold nanorods, SCE- saturated calomel electrode, RGO-reduced graphene oxide, MWCNT -Multiwall carbon nanotube, TOA+- tetraoctylammonium ions, PGE-pencyl graphite electrode, 3,5 DNBPh −4-phenylbutyl-3,5-dinitrobenzoate, SPE-screen-printing electrode, GCE-glassy carbon electrode, AgPNPS-Silver nanoprism, AgRNPs-Silver nanorods, AgSNPs-Silver nanospheres. GCE-glassy carbon electrode, SPE-Screen-printing electrode, NPG-Gold nanoporous Os(bpy)2(PVI)-osmium-based polymer, DIA-Diaphorase, Co-NC/Pd-Cobalt-N-doped carbon and palladium, CPE-carbon paste electrode. 

Table 2. Estimated Material Costs for LIG Sensor Fabrication _[a]_ 

|material<br>value in USD ($)<br>polyimide<br>249.96<br>Kapton tape<br>4.45<br>conductive silver paint<br>78.00<br>bleach<br>2.18<br>nail polish<br>1.31<br>total value per sensor<br>_a_*Laser Engraver (3W, 450 nm) cost: $253.41.|value per sensor <br>0.013<br>0.002<br>0.07<br>0.00002<br>0.01<br>0.10|($)|
|---|---|---|



resulted in a relative standard deviation (RSD) of 2.76%, while the reproducibility, evaluated as intra- and interbatch variability, yielded RSD values of 5.78 and 8.22%, respectively. In addition to its strong analytical performance, the low fabrication cost of approximately U$ 0.10 per device highlights its potential for scalable, sustainable, and eco-friendly electrochemical sensing. These results position the LIG-based platform as a promising candidate for detecting NADH and, by extension, for broader applications in biomedical diagnostics and environmental monitoring. 

## ■ **[ASSOCIATED][CONTENT]** 

excellent electrical conductivity, as confirmed by Raman spectroscopy, XPS, and sheet resistance measurements. The presence of C O functional groups on the LIG surface likely enhanced the electrocatalytic oxidation of NADH, enabling detection at a remarkably low applied potential of 50 mV vs Ag/AgCl. The sensor showed high sensitivity, with a limit of detection of 2.72 _μ_ mol L[−][1] , a limit of quantification of 9.07 _μ_ mol L[−][1] , and a wide linear range up to 1 mmol L[−][1] . The repeatability of the electrochemical oxidation of NADH 

## **Data Availability Statement** 

The authors declare that the data supporting the findings of this study are available within the paper. Should any raw data files be needed in another format, they are available from the corresponding author upon request. 

* **sı Supporting Information** 

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsomega.5c04282. 

**H** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

- Equation for laser fluence calculation; stability of Ag/ AgCl pseudoreference electrodes; XPS spectra (survey and C 1s) of LIG (82.5 mW, 17 mm/s, two passes, air); cyclic voltammetry of 5 mM NADH (PBS, pH 7.4) on LIG (82.5 mW, 17 mm/s, two passes, air) sensor; chronoamperograms for interferent studies (PDF) 

## ■ **[AUTHOR][INFORMATION]** 

## **Corresponding Author** 

- Cecilia de Carvalho Castro Silva − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil;_ orcid.org/0000-0003-3933-1838; Email: cecilia.silva@mackenzie.br 

## **Authors** 

- Ketley Caroline Rocha Pereira − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil_ 

- Elsa Maria Materón − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil;_ orcid.org/0000-0002-3382-1193 

- Matheus Santos Dias − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil_ 

- Tatiana Parra Vello − _MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil_ 

- Deissy Feria Garnica − _MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil_ 

- Gustavo Miguel Sousa − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil;_ orcid.org/0009-0000-0475-4713 

- Camila Marchetti Maroneze − _School of Engineering, Mackenzie Presbyterian University, Sao Paulo, 01302-907 Sao Paulo, Brazil; MackGraphe_ − _Mackenzie Institute for Research in Graphene and Nanotechnologies, Mackenzie Presbyterian Institute, Sao Paulo, 01302-907 Sao Paulo, Brazil;_ orcid.org/0000-0002-6835-4476 

Complete contact information is available at: https://pubs.acs.org/10.1021/acsomega.5c04282 

## **Author Contributions** 

Conceptualization: C.C.C.S and K.C.R.P. Methodology: C.C.C.S., C.M.M., K.C.R.P., E.M.M., M.S.D., D.F.G., G.M.S. and T.P.V. Validation: C.C.C.S and K.C.R.P. Formal analysis: 

K.C.R.P. and E.M.M. Investigation: K.C.R.P., E.M.M., M.S.D., D.F.G., G.M.S. and T.P.V. Resources: C.C.C.S and C.M.M. Data curation: C.C.C.S., K.C.R.P. and E.M.M. Writing� original draft preparation: K.C.R.P, E.M.M and C.C.C.S. Writing�review and editing: K.C.R.P, E.M.M, C.C.C.S. and C.M.M. Visualization: K.C.R.P., E.M.M., M.S.D., D.F.G., G.M.S and T.P.V. Resources: C.C.C.S and C.M.M. Supervision: C.C.C.S. Project administration: C.C.C.S. Funding acquisition: C.C.C.S. and C.M.M. All authors have read and agreed to the published version of the manuscript. 

## **Funding** 

The Article Processing Charge for the publication of this research was funded by the Coordenacao de Aperfeicoamento de Pessoal de Nivel Superior (CAPES), Brazil (ROR identifier: 00x0ma614). 

## **Notes** 

The authors declare no competing financial interest. 

## ■ **[ACKNOWLEDGMENTS]** 

The authors acknowledge financial support from Coordination for the Improvement of Higher Education Personnel (CAPES), Mackenzie Research Fund (MackPesquisa), National Council for Scientific and Technological Development (CNPq) (grant Nos. 408248/2023-8, 313091/2022-6 and 408798/2022-0), INCT NanoVida (grant No. 406079/20226) and Financiadora de Estudos e Projetos (Finep) (Grant No. 1151/22 and Grant No. 1755/22). This research used the facilities of the MackGraphe-Mackenzie Institute for Research in Graphene and Nanotechnologies. 

## ■ **[REFERENCES]** 

(1) Nemceková, K.; Labuda, J. Advanced Materials-Integrated Electrochemical Sensors as Promising Medical Diagnostics Tools: A Review. _Mater. Sci. Eng., C_ 2021, _120_ , No. 111751, DOI: 10.1016/ j.msec.2020.111751. 

(2) Beaver, K.; Dantanarayana, A.; Minteer, S. D. Materials Approaches for Improving Electrochemical Sensor Performance. _J. Phys. Chem. B_ 2021, _125_ (43), 11820−11834. 

(3) He, W.; Liu, L.; Cao, Z.; Lin, Y.; Tian, Y.; Zhang, Q.; Zhou, C.; Ye, X.; Cui, T. Shrink Polymer Based Electrochemical Sensor for Point-of-Care Detection of Prostate-Specific Antigen. _Biosens. Bioelectron._ 2023, _228_ , No. 115193. 

(4) Kulyk, B.; Pereira, S. O.; Fernandes, A. J. S.; Fortunato, E.; Costa, F. M.; Santos, N. F. Laser-induced Graphene from Paper for Non-Enzymatic Uric Acid Electrochemical Sensing in Urine. _Carbon_ 2022, _197_ (March), 253−263. 

(5) Baldo, T. A.; De Lima, L. F.; Mendes, L. F.; De Araujo, W. R.; Paixao, T. R. L. C.; Coltro, W. K. T. Wearable and Biodegradable Sensors for Clinical and Environmental Applications. _ACS Appl. Electron Mater._ 2021, _3_ (1), 68−100. 

(6) Coros, M.; Pruneanu, S.; Staden, R.-I. S.-v. Review�Recent Progress in the Graphene-Based Electrochemical Sensors and Biosensors. _J. Electrochem. Soc._ 2020, _167_ (3), No. 037528. 

(7) Vivaldi, F. M.; Dallinger, A.; Bonini, A.; Poma, N.; Sembranti, L.; Biagini, D.; Salvo, P.; Greco, F.; Di Francesco, F. Three-Dimensional (3D) Laser-Induced Graphene: Structure, Properties, and Application to Chemical Sensing. _ACS Appl. Mater. Interfaces_ 2021, 30245− 30260, DOI: 10.1021/acsami.1c05614. 

(8) Immanuel, S.; Sivasubramanian, R. Electrochemical studies of NADH Oxidation on Chemically Reduced Graphene Oxide Nanosheets Modified Glassy Carbon Electrode. _Mater. Chem. Phys._ 2020, _249_ (2), No. 123015. 

(9) Liu, J.; Bao, S.; Wang, X. Applications of Graphene-Based Materials in Sensors: A Review. _Micromachines_ 2022, _13_ (2), No. 184. 

**I** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

(10) Ambrosi, A.; Chua, C. K.; Bonanni, A.; Pumera, M. Electrochemistry of Graphene and Related Materials. _Chem. Rev._ 2014, _114_ (14), 7150−7188. 

(11) Brownson, D. A. C.; Banks, C. E. CVD Graphene Electrochemistry: The Role of Graphitic Islands. _Phys. Chem. Chem. Phys._ 2011, _13_ (35), 15825−15828. 

(12) Brownson, D. A. C.; Banks, C. E. Limitations of CVD Graphene When Utilised towards the Sensing of Heavy Metals. _RSC Adv._ 2012, _2_ (12), 5385. 

(13) Guell, A. G.; Ebejer, N.; Snowden, M. E.; Macpherson, J. V.; Unwin, P. R. Structural Correlations in Heterogeneous Electron Transfer at Monolayer and Multilayer Graphene Electrodes. _J. Am. Chem. Soc._ 2012, _134_ (17), 7258−7261. 

(14) Ahmed, A.; Singh, A.; Young, S.-J.; Gupta, V.; Singh, M.; Arya, S. Synthesis Techniques and Advances in Sensing Applications of Reduced Graphene Oxide (RGO) Composites: A Review. _Composites, Part A_ 2023, _165_ , No. 107373. 

(15) Wei, J.; Qiu, J.; Li, L.; Ren, L.; Zhang, X.; Chaudhuri, J.; Wang, S. A Reduced Graphene Oxide Based Electrochemical Biosensor for Tyrosine Detection. _Nanotechnology_ 2012, _23_ (33), No. 335707. 

(16) Scroccarello, A.; Alvarez-Diduk, R.; Della Pelle, F.; de Carvalho Castro e Silva, C.; Idili, A.; Parolo, C.; Compagnone, D.; Merkoci, A. One-Step Laser Nanostructuration of Reduced Graphene Oxide Films Embedding Metal Nanoparticles for Sensing Applications. _ACS Sens._ 2023, _8_ (2), 598−609. 

(17) Zhao, L.; Rosati, G.; Piper, A.; de Carvalho Castro e Silva, C.; Hu, L.; Yang, Q.; Della Pelle, F.; Alvarez-Diduk, R. R.; Merkoci, A. Laser Reduced Graphene Oxide Electrode for Pathogenic _Escherichia Coli_ Detection. _ACS Appl. Mater. Interfaces_ 2023, _15_ (7), 9024−9033. 

(18) Calucho, E.; Alvarez-Diduk, R.; Piper, A.; Rossetti, M.; Nevanen, T. K.; Merkoci, A. Reduced Graphene Oxide Electrodes Meet Lateral Flow Assays: A Promising Path to Advanced Point-ofCare Diagnostics. _Biosens. Bioelectron._ 2024, _258_ , No. 116315. 

(19) Echeverri, D.; Calucho, E.; Marrugo-Ramírez, J.; AlvarezDiduk, R.; Orozco, J.; Merkoci, A. Capacitive Immunosensing at Gold Nanoparticle-Decorated Reduced Graphene Oxide Electrodes Fabricated by One-Step Laser Nanostructuration. _Biosens. Bioelectron._ 2024, _252_ , No. 116142. 

(20) Hummers, W. S.; Offeman, R. E. Preparation of Graphitic Oxide. _J. Am. Chem. Soc._ 1958, _80_ (6), 1339. 

(21) Dixit, N.; Singh, S. P. Laser-Induced Graphene (LIG) as a Smart and Sustainable Material to Restrain Pandemics and Endemics: A Perspective. _ACS Omega_ 2022, _7_ (6), 5112−5130. 

(22) Barbhuiya, N. H.; Kumar, A.; Singh, S. P. A Journey of LaserInduced Graphene in Water Treatment. _Trans. Indian Natl. Acad. Eng._ 2021, _6_ (2), 159−171. 

(23) Singh, R. K.; Kumar, R.; Singh, D. P. Graphene Oxide: Strategies for Synthesis, Reduction and Frontier Applications. _RSC Adv._ 2016, _6_ (69), 64993−65011. 

(24) Henriques, P. C.; Borges, I.; Pinto, A. M.; Magalhaes, F. D.; Goncalves, I. C. Fabrication and Antimicrobial Performance of Surfaces Integrating Graphene-Based Materials. _Carbon_ 2018, _132_ , 709−732. 

(25) Pinheiro, T.; Morais, M.; Silvestre, S.; Carlos, E.; Coelho, J.; Almeida, H. V.; Barquinha, P.; Fortunato, E.; Martins, R. Direct Laser Writing: From Materials Synthesis and Conversion to Electronic Device Processing. _Adv. Mater._ 2024, _36_ (26), No. 2402014. 

(26) El-Kady, M. F.; Strong, V.; Dubin, S.; Kaner, R. B. Laser Scribing of High-Performance and Flexible Graphene-Based Electrochemical Capacitors. _Science_ 2012, _335_ (6074), 1326−1330. 

(27) Yang, Q.; Nguyen, E. P.; Panácek, D.; Sedajová, V.; Hruby, V.; Rosati, G.; de Carvalho Castro Silva, C.; Bakandritsos, A.; Otyepka, M.; Merkoci, A. Metal-Free Cysteamine-Functionalized Graphene Alleviates Mutual Interferences in Heavy Metal Electrochemical Detection. _Green Chem._ 2023, _25_ (4), 1647−1657. 

(28) Lin, J.; Peng, Z.; Liu, Y.; Ruiz-Zepeda, F.; Ye, R.; Samuel, E. L. G.; Yacaman, M. J.; Yakobson, B. I.; Tour, J. M. Laser-induced Porous Graphene Films from Commercial Polymers. _Nat. Commun._ 2014, _5_ (1), No. 5714. 

(29) Ye, R.; James, D. K.; Tour, J. M. Laser-induced Graphene. _Acc. Chem. Res._ 2018, _51_ (7), 1609−1620. 

(30) Avinash, K.; Patolsky, F. Laser-Induced Graphene Structures: From Synthesis and Applications to Future Prospects. _Mater. Today_ 2023, _70_ , 104−136. 

(31) Vivaldi, F. M.; Dallinger, A.; Bonini, A.; Poma, N.; Sembranti, L.; Biagini, D.; Salvo, P.; Greco, F.; Di Francesco, F. ThreeDimensional (3D) Laser-Induced Graphene: Structure, Properties, and Application to Chemical Sensing. _ACS Appl. Mater. Interfaces_ 2021, _13_ (26), 30245−30260. 

(32) Mendes, L. F.; Pradela-Filho, L. A.; Paixao, T. R. L. C. Polyimide Adhesive Tapes as a Versatile and Disposable Substrate to Produce CO2 Laser-Induced Carbon Sensors for Batch and Microfluidic Analysis. _Microchem. J._ 2022, _182_ , No. 107893. 

(33) Mendes, L. F.; de Siervo, A.; de Araujo, W. R.; Paixao, T. R. L. C. Reagentless Fabrication of a Porous Graphene-like Electrochemical Device from Phenolic Paper Using Laser-Scribing. _Carbon_ 2020, _159_ , 110−118. 

(34) de Araujo, W. R.; Frasson, C. M. R.; Ameku, W. A.; Silva, J. R.; Angnes, L.; Paixao, T. R. L. C. Single-Step Reagentless Laser Scribing Fabrication of Electrochemical Paper-Based Analytical Devices. _Angew. Chem._ 2017, _129_ (47), 15309−15313. 

(35) Kaidarova, A.; Kosel, J. Physical Sensors Based on Laserinduced Graphene: A Review. _IEEE Sens. J._ 2021, _21_ (11), 12426− 12443. 

(36) Kulyk, B.; Pereira, S. O.; Fernandes, A. J. S.; Fortunato, E.; Costa, F. M.; Santos, N. F. Laser-Induced Graphene from Paper for Non-Enzymatic Uric Acid Electrochemical Sensing in Urine. _Carbon_ 2022, _197_ , 253−263. 

(37) Soares, R. R. A.; Hjort, R. G.; Pola, C. C.; Parate, K.; Reis, E. L.; Soares, N. F. F.; Mclamore, E. S.; Claussen, J. C.; Gomes, C. L. LaserInduced Graphene Electrochemical Immunosensors for Rapid and Label-Free Monitoring of Salmonella Enterica in Chicken Broth. _ACS Sens._ 2020, _5_ (7), 1900−1911. 

(38) de Farias, D. M.; Pradela-Filho, L. A.; Arantes, I. V. S.; Gongoni, J. L. M.; Veloso, W. B.; Meloni, G. N.; Paixao, T. R. L. C. Sulfanilamide Electrochemical Sensor Using Phenolic Substrates and CO2 Laser Pyrolysis. _ACS Appl. Mater. Interfaces_ 2023, _15_ (48), 56424−56432. 

(39) Garland, N. T.; McLamore, E. S.; Cavallaro, N. D.; MendivelsoPerez, D.; Smith, E. A.; Jing, D.; Claussen, J. C. Flexible LaserInduced Graphene for Nitrogen Sensing in Soil. _ACS Appl. Mater. Interfaces_ 2018, _10_ (45), 39124−39133. 

(40) Sain, S.; Roy, S.; Mathur, A.; Rajesh, V. M.; Banerjee, D.; Sarkar, B.; Roy, S. S. Electrochemical Sensors Based on Flexible LaserInduced Graphene for the Detection of Paraquat in Water. _ACS Appl. Nano Mater._ 2022, _5_ (12), 17516−17525. 

(41) Kucherenko, I. S.; Chen, B.; Johnson, Z.; Wilkins, A.; Sanborn, D.; Figueroa-Felix, N.; Mendivelso-Perez, D.; Smith, E. A.; Gomes, C.; Claussen, J. C. Laser-Induced Graphene Electrodes for Electrochemical Ion Sensing, Pesticide Monitoring, and Water Splitting. _Anal. Bioanal. Chem._ 2021, _413_ (25), 6201−6212. 

(42) Lee, J. K.; Suh, H. N.; Yoon, S. H.; Lee, K. H.; Ahn, S. Y.; Kim, H. J.; Kim, S. H. Non-Destructive Monitoring via Electrochemical NADH Detection in Murine Cells. _Biosensors_ 2022, _12_ (2), No. 107. 

(43) Da Silva, E. T. S. G.; Miserere, S.; Kubota, L. T.; Merkoci, A. Simple On-Plastic/Paper Inkjet-Printed Solid-State Ag/AgCl Pseudoreference Electrode. _Anal. Chem._ 2014, _86_ (21), 10531−10534. 

(44) Lee, J.; Suh, H. N.; Ahn, S.; Park, H. B.; Lee, J. Y.; Kim, H. J.; Kim, S. H. Disposable Electrocatalytic Sensor for Whole Blood NADH Monitoring. _Sci. Rep._ 2022, _12_ (1), No. 16716. 

(45) Pedro, P. I.; Pinheiro, T.; Silvestre, S. L.; Marques, A. C.; Coelho, J.; Marconcini, J. M.; Fortunato, E.; Luiz, L. H.; Martins, R. Sustainable Carbon Sources for Green Laser-Induced Graphene: A Perspective on Fundamental Principles, Applications, and Challenges. _Appl. Phys. Rev._ 2022, _9_ (4), No. 041305, DOI: 10.1063/5.0100785. (46) Dresselhaus, M. S.; Jorio, A.; Hofmann, M.; Dresselhaus, G.; Saito, R. Perspectives on Carbon Nanotubes and Graphene Raman Spectroscopy. _Nano Lett._ 2010, _10_ (3), 751−758. 

**J** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

**ACS Omega** 

**http://pubs.acs.org/journal/acsodf** 

Article 

(47) Cai, J.; Lv, C.; Watanabe, A. Laser Direct Writing of HighPerformance Flexible All-Solid-State Carbon Micro-Supercapacitors for an on-Chip Self-Powered Photodetection System. _Nano Energy_ 2016, _30_ , 790−800. 

(48) de la Roche, J.; López-Cifuentes, I.; Jaramillo-Botero, A. Influence of Lasing Parameters on the Morphology and Electrical Resistance of Polyimide-Based Laser-Induced Graphene (LIG). _Carbon Lett._ 2023, _33_ (2), 587−595. 

(49) Lin, J.; Peng, Z.; Liu, Y.; Ruiz-Zepeda, F.; Ye, R.; Samuel, E. L. G.; Yacaman, M. J.; Yakobson, B. I.; Tour, J. M. Laser-Induced Porous Graphene Films from Commercial Polymers. _Nat. Commun._ 2014, _5_ (1), No. 5714. 

(50) Ye, R.; James, D. K.; Tour, J. M. Laser-Induced Graphene. _Acc. Chem. Res._ 2018, _51_ (7), 1609−1620. 

(51) Pinheiro, T.; Rosa, A.; Ornelas, C.; Coelho, J.; Fortunato, E.; Marques, A. C.; Martins, R. Influence of CO2 Laser Beam Modelling on Electronic and Electrochemical Properties of Paper-Based LaserInduced Graphene for Disposable PH Electrochemical Sensors. _Carbon Trends_ 2023, _11_ , No. 100271. 

(52) Kaidarova, A.; Kosel, J. Physical Sensors Based on LaserInduced Graphene: A Review. _IEEE Sens J._ 2021, _21_ (11), 12426− 12443. 

(53) Crapnell, R. D.; Bernalte, E.; Munoz, R. A. A.; Banks, C. E. Electroanalytical Overview: The Use of Laser-Induced Graphene Sensors. _Anal. Methods_ 2025, _17_ (4), 635−651. 

(54) Materón, E. M.; de Azevedo, L. M. L.; Dias, J. M.; Pereira, K. C. R.; Sousa, G. M.; Dias, M. S.; Maroneze, C. M.; Dias, D.; de Carvalho Castro Silva, C. Advancing Biomedical Analysis: Harnessing LaserInduced Graphene for Next-Gen of Low-Cost Sensor Technology. _J. Pharm. Biomed. Anal. Open_ 2025, _5_ , No. 100077. 

(55) Carlson, B. W.; Miller, L. L. Mechanism of the Oxidation of NADH by Quinones. Energetics of One-Electron and Hydride Routes. _J. Am. Chem. Soc._ 1985, _107_ (2), 479−485. 

(56) de Camargo, M. N. L.; Santhiago, M.; Maroneze, C. M.; Silva, C. C. C.; Timm, R. A.; Kubota, L. T. Tuning the Electrochemical Reduction of Graphene Oxide: Structural Correlations towards the Electrooxidation of Nicotinamide Adenine Dinucleotide Hydride. _Electrochim. Acta_ 2016, _197_ , 194−199. 

(57) Stanford, M. G.; Li, J. T.; Chyan, Y.; Wang, Z.; Wang, W.; Tour, J. M. Laser-Induced Graphene Triboelectric Nanogenerators. _ACS Nano_ 2019, _13_ (6), 7166−7174. 

(58) Rahimi, R.; Ochoa, M.; Yu, W.; Ziaie, B. Highly Stretchable and Sensitive Unidirectional Strain Sensor via Laser Carbonization. _ACS Appl. Mater. Interfaces_ 2015, _7_ (8), 4463−4470. 

(65) Sahin, M.; Ayranci, E. Electrooxidation of NADH on Modified Screen-Printed Electrodes: Effects of Conducting Polymer and Nanomaterials. _Electrochim. Acta_ 2015, _166_ , 261−270. 

(66) Bai, S.; Tang, Y.; Lin, L.; Ruan, L.; Song, R.; Chen, H.; Du, Y.; Lin, H.; Shan, Y.; Tang, Y. Investigation of Micro/Nano Formation Mechanism of Porous Graphene Induced by CO2 Laser Processing on Polyimide Film. _J. Manuf. Process_ 2022, _84_ , 555−564. 

(67) Pedro, P. I.; Pinheiro, T.; Silvestre, S. L.; Marques, A. C.; Coelho, J.; Marconcini, J. M.; Fortunato, E.; Luiz, L. H.; Martins, R. Sustainable Carbon Sources for Green Laser-Induced Graphene: A Perspective on Fundamental Principles, Applications, and Challenges. _Appl. Phys. Rev._ 2022, No. 041305, DOI: 10.1063/5.0100785. 

(68) Nagarajan, R. D.; Murugan, P.; Sundramoorthy, A. K. Selective Electrochemical Sensing of NADH and NAD+ Using Graphene/ Tungstate Nanocomposite Modified Electrode. _ChemistrySelect_ 2020, _5_ (46), 14643−14651. 

(69) Immanuel, S.; Sivasubramanian, R. Electrochemical Studies of NADH Oxidation on Chemically Reduced Graphene Oxide Nanosheets Modified Glassy Carbon Electrode. _Mater. Chem. Phys._ 2020, _249_ (2), No. 123015. 

(70) Marlinda, A. R.; Sagadevan, S.; Yusoff, N.; Pandikumar, A.; Huang, N. M.; Akbarzadeh, O.; Johan, M. R. Gold Nanorods-Coated Reduced Graphene Oxide as a Modified Electrode for the Electrochemical Sensory Detection of NADH. _J. Alloys Compd._ 2020, _847_ , No. 156552. 

(71) Dokur, E.; Uruc, S.; Gorduk, O.; Sahin, Y. A Novel Approach for Ultrasensitive Amperometric Determination of NADH via Graphene-Based Electrode Obtained by Electrochemical Intercalation of Tetraalkylammonium Ions. _Ionics_ 2023, _29_ (5), 2005−2019. 

(72) Contreras, G.; Barrientos, C.; Moscoso, R.; Alvarez-Lueje, A.; Squella, J. A. Electrocatalytic Determination of NADH by Means of Electrodes Modified with MWCNTs and Nitroaromatic Compounds. _Microchem. J._ 2020, _159_ , No. 105422. 

(73) Manusha, P.; Yadav, S.; Satija, J.; Senthilkumar, S. Designing Electrochemical NADH Sensor Using Silver Nanoparticles/Phenothiazine Nanohybrid and Investigation on the Shape Dependent Sensing Behavior. _Sens. Actuators, B_ 2021, _347_ , No. 130649. 

(74) Otero, F.; Mandal, T.; Leech, D.; Magner, E. An Electrochemical NADH Biosensor Based on a Nanoporous Gold Electrode Modified with Diaphorase and an Osmium Polymer. _Sens. Actuators, Rep._ 2022, _4_ , No. 100117. 

(75) Singh, K.; Singh, C.; Maurya, K. K.; Malviya, M. Redox Electrochemistry of Electrodes Tuned with Dimethyl Ferrocene Based on Co−NC−Pd Nanogeometry: An Impedimetric Sensor for NADH Sensing. _J. Mater. Sci.:Mater. Electron._ 2023, _34_ (27), No. 1898. 

(59) Cardoso, A. R.; Marques, A. C.; Santos, L.; Carvalho, A. F.; Costa, F. M.; Martins, R.; Sales, M. G. F.; Fortunato, E. MolecularlyImprinted Chloramphenicol Sensor with Laser-Induced Graphene Electrodes. _Biosens. Bioelectron._ 2019, _124_ − _125_ , 167−175. 

(60) Wan, Z.; Umer, M.; Lobino, M.; Thiel, D.; Nguyen, N.-T.; Trinchi, A.; Shiddiky, M. J. A.; Gao, Y.; Li, Q. Laser Induced Self-NDoped Porous Graphene as an Electrochemical Biosensor for Femtomolar MiRNA Detection. _Carbon_ 2020, _163_ , 385−394. 

(61) Kaur, S.; Mager, D.; Korvink, J. G.; Islam, M. Unraveling the Dependency on Multiple Passes in Laser-Induced Graphene Electrodes for Supercapacitor and H2O2 Sensing. _Mater. Sci. Energy Technol._ 2021, _4_ , 407−412. 

(62) Beduk, T.; Lahcen, A. A.; Tashkandi, N.; Salama, K. N. OneStep Electrosynthesized Molecularly Imprinted Polymer on Laser Scribed Graphene Bisphenol a Sensor. _Sens. Actuators, B_ 2020, _314_ , No. 128026. 

(63) Franco, F. F.; Malik, M. H.; Manjakkal, L.; Roshanghias, A.; Smith, C. J.; Gauchotte-Lindsay, C. Optimizing Carbon Structures in Laser-Induced Graphene Electrodes Using Design of Experiments for Enhanced Electrochemical Sensing Characteristics. _ACS Appl. Mater. Interfaces_ 2024, _16_ (47), 65489−65502. 

(64) Bard, A. J.; Faulkner, L. R. _Electrochemical Methods: Fundamentals and Applications_ , 2nd ed.; John Wiley & Sons, 2000. 

**K** 

https://doi.org/10.1021/acsomega.5c04282 _ACS Omega_ XXXX, XXX, XXX−XXX 

