_**micromachines**_ 

## _Article_ 

## **Batch-to-Batch Variation in Laser-Inscribed Graphene (LIG) Electrodes for Electrochemical Sensing** 

**Yifan Tang[1] , Geisianny A. Moreira[2] , Diana Vanegas[3] , Shoumen P. A. Datta[4,5] and Eric S. McLamore[2,3,] *** 

- 1 Department of Plant and Environmental Sciences, Clemson University, Clemson, SC 29631, USA; ytang95@jh.edu 

- 2 Department of Agricultural Sciences, Clemson University, Clemson, SC 29631, USA; gamm.bio@gmail.com 

- 3 Department of Environmental Engineering and Earth Sciences, Clemson University, Clemson, SC 29634, USA; dvanega@clemson.edu 

- 4 Department of Mechanical Engineering, MIT Auto-ID Labs, Massachusetts Institute of Technology, Cambridge, MA 02139, USA; shoumen@mit.edu 

- 5 Biomedical Engineering Program, Medical Device (MDPnP) Interoperability and Cybersecurity Labs, Department of Anesthesiology, Massachusetts General Hospital, Harvard Medical School, Cambridge, MA 02139, USA 

- Correspondence: emclamo@clemson.edu 

**Citation:** Tang, Y.; Moreira, G.A.; Vanegas, D.; Datta, S.P.A.; McLamore, E.S. Batch-to-Batch Variation in Laser-Inscribed Graphene (LIG) Electrodes for Electrochemical Sensing. _Micromachines_ **2024** , _15_ , 874. https://doi.org/10.3390/mi15070874 

Academic Editor: Sadia Ameen 

Received: 6 May 2024 Revised: 25 June 2024 Accepted: 28 June 2024 Published: 30 June 2024 

**Abstract:** Laser-inscribed graphene (LIG) is an emerging material for micro-electronic applications and is being used to develop supercapacitors, soft actuators, triboelectric generators, and sensors. The fabrication technique is simple, yet the batch-to-batch variation of LIG quality is not well documented in the literature. In this study, we conduct experiments to characterize batch-to-batch variation in the manufacturing of LIG electrodes for applications in electrochemical sensing. Numerous batches of 36 LIG electrodes were synthesized using a CO2 laser system on polyimide film. The LIG material was characterized using goniometry, stereomicroscopy, open circuit potentiometry, and cyclic voltammetry. Hydrophobicity and electrochemical screening (cyclic voltammetry) indicate that LIG electrode batch-to-batch variation is less than 5% when using a commercial reference and counter electrode. Metallization of LIG led to a significant increase in peak current and specific capacitance (area between anodic/cathodic curve). However, batch-to-batch variation increased to approximately 30%. Two different platinum electrodeposition techniques were studied, including galvanostatic and frequency-modulated electrodeposition. The study shows that formation of metallized LIG electrodes with high specific capacitance and peak current may come at the expense of high batch variability. This design tradeoff has not been discussed in the literature and is an important consideration if scaling sensor designs for mass use is desired. This study provides important insight into the variation of LIG material properties for scalable development of LIG sensors. Additional studies are needed to understand the underlying mechanism(s) of this variability so that strategies to improve the repeatability may be developed for improving quality control. The dataset from this study is available via an open access repository. 

**Keywords:** laser-inscribed graphene; LIG; sensor; batch; variation; scalability; manufacturing 

## **1. Introduction** 

**Copyright:** © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

Laser-inscribed graphene (LIG) is an emerging material that was originally discovered by the Tour group [1]. LIG is created by irradiating a carbon source (in most cases polyimide films) with a laser to graphitize sp[3] carbon to sp[2] -hybridized carbon (see Supplemental Figure S1) [2]. Use of LIG as a technology platform in electronics has grown exponentially in the last decade [3]. Compared to other methods for conductive carbon film synthesis, laser ablation is one of the most efficient techniques used for device fabrication [4], which is rooted in the excellent intrinsic properties of LIG and the ability to customize numerous micro-device features. 

_Micromachines_ **2024** , _15_ , 874. https://doi.org/10.3390/mi15070874 

https://www.mdpi.com/journal/micromachines 

_Micromachines_ **2024** , _15_ , 874 

2 of 13 

LIG is an attractive platform for micro-device fabrication, as the one-step synthesis is relatively simple and requires a single instrument (most often a CO2 laser-writing system). Examples of LIG-based micro-devices include micro-supercapacitors [5], soft actuators [6], triboelectric generators [7], gas sensors [8], strain/motion sensors [9,10], saliva sample tubes with embedded biosensors [11–13], portable food safety sensors [14], and flexible soil sensors for column studies [15], among others. In sensing and biosensing applications, the particular properties of interest are high specific surface area, relatively high electrical conductivity, ability to micropattern custom geometries, and flexibility [16,17]. 

Microscale sensors have been developed based on LIG for targeting ions [18,19], sugars [20,21], biomolecules [22,23], bacteria [24], and viruses [12,13,25]. One of the major limitations for developing micro-sensors based on LIG is the unknown scalability of the fabrication process. Modern CO2 laser-writing systems have a wide range of control features (e.g., rastering, power density, speed). Behrent et al. [26] conducted an excellent study on the optimum laser control settings during fabrication of LIG, specifically focusing on electrochemical sensor/biosensor design (this manuscript also addresses key operational protocols such as cool-down time, etc.). This detailed study investigated numerous aspects beyond laser equipment settings, including direction of patterning, and to some extent patterning width. 

Conceptually, many devices can be micro-patterned using common computer-aided design (CAD) software and applying the optimum laser control settings [26–28]. However, polyimide films are known to undergo deformation during the graphitization process (e.g., local bending), which alters the focal plane of the laser when printing large arrays. For the fabrication of relatively small laser processing jobs (e.g., three replicate LIG electrodes to be used in sensor development), the issue of film deformation is less problematic, but electrode-to-electrode variation exists. In addition to local deformation during graphitization, analysis by electron and Raman microscopy indicate that the surface chemistry and feature size are highly variable [14,15,26,28]. For this reason, studies of the batch-to-batch variation in LIG are critical for developing quality control (QC) practices. 

Raman spectroscopy and nanoscale metrology [29,30] have been used for QC screening of graphene materials (primarily powders). However, these methods were not applied to graphene films on flat 2D surfaces. Recently, Qian et al. [25] developed a quality control screening framework and data analysis technique (hierarchical clustering) for quality control studies of LIG using cyclic voltammetry. However, batch-to-batch variation in LIG fabrication has not been characterized in detail and the source of the variation is largely unknown. Thus, it is challenging to perform detailed life cycle studies or predict scalability of LIG micro-sensor technologies at the scale of competitive devices based on classic manufacturing (e.g., the silicon semiconductor industry). 

In this manuscript, we conduct the first detailed study of the batch-to-batch variation in LIG electrodes fabricated with a CO2 laser and polyimide film. We apply some of the most common techniques employed in sensor research labs (electrochemical analysis, goniometry, and stereomicroscopy). We report LIG hydrophobicity and electrochemical behavior in batches of at least 36 electrodes. Additionally, we characterize batches of LIG metallized with platinum (Pt) to study whether electrodeposition may affect the electrochemical performance of LIG batches. 

## **2. Materials and Methods** 

## _2.1. Chemicals and Reagents_ 

Potassium ferrocyanide (K4Fe(CN)6), potassium ferricyanide (K3Fe(CN)6), potassium chloride (KCl), lead acetate (30% _w_ / _v_ ), morpholinoethanesulfonic acid hydrate (MES), tris(Hydroxymethyl)aminomethane (Tris), and 4-(2-Hydroxyethyl)-1-piperazine ethanesulfonic acid (HEPES) were purchased from Fisher Scientific (Pittsburgh, PA, USA). Isotonic bicarbonate buffer (213 mM-NaCl + 65 mM-NaHCO3) was purchased from NeilMed (Santa Rosa, CA, USA). Chloroplatinic acid (8 _w_ / _v_ ) was purchased from Sigma-Aldrich (St Louis, MO, USA). Silver/silver chloride (Ag/AgCl) reference electrode and Pt-wire counter elec- 

_Micromachines_ **2024** , _15_ , 874 

3 of 13 

trode were purchased from BASi (West Lafayette, IN, USA). Polyimide film (electrical grade polyimide film, type HN, 0.0050” thick) and chemical-resistant polyvinyl chloride sheets (1/16” thick, 12 _×_ 12 sheet) were obtained from McMaster-Carr (Elmhurst, IL, USA). Metal alloy tape was purchased from Beijing Electronics Store (Beijing, China). Lacquer for electrode passivation was purchased from a local grocer in Clemson, SC. Female USB2.0 (Type A) port socket connectors and insulated 28 AWG jumper wires were purchased from Amazon. NeilMed saline rinse powder (an isotonic bicarbonate buffer) and double-sided Scotch tape were purchased from a local pharmacy. 

## _2.2. Laser-Inscribed Graphene Electrode Fabrication_ 

Details and step-by-step methods for LIG fabrication are described in McLamore et al. [31]. Briefly, electrode patterns were first designed in CorelDraw (Corel Corporation, Ottawa, ON, Canada; see Supplemental Figure S1B,C). Patterned electrodes were graphitized on polyimide film using a Universal CO2 laser system (version VLS3.60, Scottsdale, AZ, USA). The heat map by Behrent et al. [26] was reproduced, with nearly identical results (see Supplemental Figure S2). Within a select range, additional optimization was conducted to ensure proper laser scribing in our instrument. Based on this study, the following settings were used: 5.8 cm distance from lens to polyimide surface, Z axis offset of 0.005”, image density of 7, rastering speed of 75%, power of 40%, and density of 1000 PPI. After graphitization, LIG electrodes were immediately rinsed with 70% ethanol thrice, and then rinsed with DI water. Fast drying poly-gel acrylic lacquer was used to passivate the electrode(s), and then bonding pads (0.13 mm thick conductive polyester metal tape) were pressed with forceps. Depending on the type of experiment, a single (working) LIG electrode or three-electrode LIG system was patterned and graphitized. 

A USB plug-and-play microdevice was fabricated for connecting the three-electrode LIG system (referred to as the “sensor chip”) to the potentiostat. Details are described in the protocol by Casso-Hartmann et al. [11]. Briefly, two jumper wires were soldered to the outside pins of a female USB-A plug. Next, the two inner pins were jumped using solder, and a third wire was soldered to this pin junction. These three jumper wires were the connection point for the reference, counter, and working electrodes, respectively. The USBA plastic case was attached and pressed firmly using pliers. The LIG sensor chip geometry was designed in CorelDraw such that the bonding pad of each of the three electrodes aligns with these USB-A pins. Strips (0.3 cm by 3.5 cm) of chemical-resistant 1/16” thick PVC were cut as the electrode base. After graphitization of the LIG three-electrode system, double-sided tape was applied to the back of the LIG flexible chip and then fixed to the PVC base. This micro-device (PVC backing with LIG sensor chip adhered) directly plugs to the USB-A female port socket, and jumper wires were connected to the PalmSens potentiostat. 

## _2.3. Nanoplatinum (nPt) Electrodeposition on LIG Electrodes_ 

For electrodeposition of nanoplatinum (nPt) on LIG single electrode or LIG sensor chip (working electrode), the stem was passivated and dried at room temperature as described above. The LIG working electrode and a Pt wire (99.9%) were immersed into a solution containing 0.728% chloroplatinic acid and 0.002% lead acetate. For the sensor chip, only the LIG working electrode was connected to the power supply. The LIG working electrode and the Pt wire were connected to a power supply (either DC or AC power supply). For galvanostatic deposition (GED), a DC power supply was used (Tektronix, Beaverton, OR, USA). GED was tested at 10 V for a plating time of either 90 s or 180 s based on previous work [13,32]. We also tested a frequency-modulated deposition (FMED) technique using an AC waveform generator (SDG2042X Arbitrary Waveform Function-Generators, Siglent, OH, USA). Two different FMED waveforms (0.5 Hz) were tested: (i) 5 VDC with an amplitude of 10 VAC (peak to peak), and (ii) 8 VDC with an amplitude of 4 VAC (peak to peak). Total plating times of 90 s and 180 s were tested at both FMED waveform settings. In all cases, the maximum potential was 10 V. Details of the waveforms are described by Tang et al. [33]. After electrodeposition of nPt, electrodes were rinsed with DI water gently prior to testing. 

_Micromachines_ **2024** , _15_ , 874 

4 of 13 

## _2.4. Goniometry_ 

Hydrophobicity was analyzed using a Droplet lab DROPOMETER-M (Markham, ON, Canada). After LIG fabrication and preparation, electrodes were stabilized and beveled on the testing instrument platform using the sample mounts. A 2 µL aliquot of sample was carefully pipetted on the working area of LIG electrode. The following solutions were tested: DI water, MES buffer, Tris buffer, HEPES buffer, 2 _×_ isotonic bicarbonate buffer, platinum plating solution, and ferri/ferrocyanide solution. 

Contact angle calculations were based on the polynomial method (non-axisymmetric drop). The instrument camera was used to capture a static picture in sessile droplet mode [34]. In the software, key features were identified in the images (e.g., edges as drop region profile of interest) following manufacturer recommendations [35]. In preliminary analysis, Young–Laplace fitting (axisymmetric) methods showed significant errors for the LIG surface, up to 60% for the same sample tested multiple times sequentially. Thus, non-axisymmetric drop was used throughout. 

An experiment was performed to determine the batch-to-batch variation of LIG hydrophobicity (contact angle). Four unique batches (nine electrodes each) were prepared on individual days, by the same operator. The contact angle was measured for each batch of nine electrodes using the non-axisymmetric drop method. Contact angle was calculated by Droplet lab software (version 1.4.0.10), and images of each test were archived. 

## _2.5. Electrochemical Analysis_ 

All pH measurements were conducted with a Thermo Orion A211 Benchtop pH Meter and calibration standards (Waltham, MA, USA). Electrochemical characterization of LIG, LIG-biochip, nPt-LIG, and nPt-biochip were carried out using a Multi PalmSens4 potentiostat (PalmSens BV, GA, Houten, The Netherlands). Where batches are referred to, six unique batches (six electrodes each) were prepared on individual days, by the same operator, for each electrode type. 

Open circuit potential (OCP) and cyclic voltammetry (CV) with ferri/ferroocyanide as a redox probe were analyzed. All tests were conducted in BASi electrochemical glass cells. Single LIG electrode studies used Ag/AgCl as the reference electrode and a Pt-wire as the counter electrode. Sensor chip studies used LIG as the working and counter electrodes, with metal alloy tape mounted on LIG as the reference electrode. All CV experiments were conducted at room temperature with stationary electrodes in 2.5 mM potassium ferricyanide and 2.5 mM potassium ferrocyanide, with 100 mM potassium chloride as the electrolyte. Where noted, non-Faradaic OCP testing was conducted in bicarbonate buffer (i.e., no redox probe). Bicarbonate buffer is commonly used in biological sensing (e.g., in isotonic preparations for nasal swabs) [12,13]. For OCP measurements, recording time was 120 s and data acquisition rate was 10 kHz. All testing was conducted in bicarbonate buffer as described by Moreira et al. [12,13]. 

In some experiments, conditioning experiments utilized ten successive CV sweeps at a scan rate of 200 mV/s over the range of _−_ 0.8 V to 0.8 V. Details of the experimental methods are shown in the published protocol by Tang et al. [36]. Oxidation peak (iop) and area between anodic and cathodic curve (ABC) were calculated from CV curves according to Qian et al. [25]. Peak oxidation current was defined as the maximum current within the oxidation window of ferrocyanide based on previous research. Cp was calculated using the approach by Wang et al. [37] after determination of scan rates that did not induce significant Ohmic drop. Unless otherwise noted, six batches of LIG electrodes were tested (six electrodes in each batch; n(total) = 36). 

## _2.6. Statistical Analysis_ 

Data analyses were conducted by R studio (version 1.1.463). All variables were tested for normality using the Shapiro test. Significance was tested within groups using a _t_ -test or Wilcox test as noted. To compare differences across groups, the least significant difference (LSD) test was used. All statistical tests are reported at an α level of 0.05. 

_Micromachines_ **2024** , _15_ , 874 

5 of 13 

## **3. Results and Discussion** 

Laser settings for the fabrication of LIG were optimized based on the approach by Behrent et al. [26] (Supplemental Figure S2). A heat map was created for selecting optimum laser settings using a scoring system. Results from three analyses were used to develop an equivalent weight scoring system: (i) stereomicroscopy examination (pass/fail), based on Behrent et al. [26]; (ii) peak oxidative current (higher than 150 µA), according to Qian et al. [25]; and (iii) area between anodic/cathodic sweep (more than 100 µV-A). Based on this equivalent weight scoring system, the optimum settings for LIG fabrication were determined to be 40% power, 75% speed, and 1000 lines per inch (raster mode), with a material thickness (Zaxis) of 0.005”. Additional details on the scoring system for optimizing laser settings are described in Tang [33]. Protocols with details of optimal manufacture settings are available on Protocol I/O [11,31]. 

## _3.1. Goniometry_ 

Batch-to-batch variation of LIG hydrophobicity immediately after graphitization was analyzed for four unique batches of single LIG electrodes and nPt-LIG (six electrodes each). The average contact angle for LIG in DI (58.6 _±_ 1.4 _[◦]_ ) indicates that LIG has a hydrophilic surface under these conditions, which is similar to the results reported in the detailed study by Hjort et al. [19]. Representative images of droplets are shown in Figure 1A. Isotonic bicarbonate buffer supplemented with sodium chloride is a common testing solution for LIG biosensors [12,13,25]. The mean contact angle in 2 _×_ isotonic buffer (59.3 _±_ 2.6 _[◦]_ ) was not significantly different than DI, which is expected (Figure 1B). The contact angle of non-modified LIG varied by less than 5% in DI and isotonic bicarbonate (within fabrication batches; see Figure 1D). In addition to testing the simple bicarbonate buffer, three other common biological buffers were screened, including compounds that have surfactant-like properties. Morpholinoethanesulfonic acid hydrate (MES) and 4-(2-Hydroxyethyl)-1-piperazine ethanesulfonic acid (HEPES) are organosulfonic acids with zwitterionic behavior. Tris(Hydroxymethyl)aminomethane (Tris) is a primary amino compound and an emulsifying agent. Figure 1B shows that the HEPES, MES, and Tris contact angle is significantly lower than DI, indicating that each behaves as a mild surfactant, impacting surface tension. The contact angle varied by 6% to 8% within these groups, which is higher than DI/bicarbonate solutions. 

Preliminary experiments indicated that the laser system may be limited in terms of the number of electrodes that can be fabricated in one day. When a batch of 36 electrodes was fabricated in a single day, the contact angle varied by more than 30%. Thus, we fabricated and analyzed 36 electrodes by creating four batches of nine electrodes each, with a 30 min laser downtime between each batch. Additional studies are required to identify the source of the variation during the LIG manufacturing process, but the reduced variation (from 30% to less than 5%) indicates that future manufacturing protocols should consider laser maintenance (e.g., lens cleaning), operational frequency, and batch size as important control factors. 

After metallization with nPt, the contact angle in DI and isotonic carbonate buffer (78 _±_ 4 _[◦]_ ) increased by nearly 20%, indicating that the surface is more hydrophobic (Figure 1C). The mean contact angle in 2 _×_ isotonic buffer was nearly identical in these two solutions and varied by 5% within fabrication batches (Figure 1E). The contact angle in the HEPES, MES, and Tris buffers was similar (63 _±_ 2 _[◦]_ , which is higher than all LIG experiments). These data are important for understanding the interfacial phenomena in different buffers, particularly when zwitterionic molecules are present in testing solutions [38]. 

_Micromachines_ **2024** , _15_ , 874 

6 of 13 

**Figure 1.** Hydrophobicity study of LIG and nPt-LIG. ( **A** ) Representative images from goniometry testing of four electrode batches (LIG sample with 2 µL DI). Results of non-axisymmetric method and calculated contact angle shown on each image. Violin plots show contact angle in testing liquids for: ( **B** ) non-modified LIG electrodes, and ( **C** ) nPt-LIG electrodes. White dots represent median value, black boxes show range from the lower to the upper quartile, whiskers present the variability outside upper and lower quantile, and the shape of violin indicates the data density ( _n_ = 24 for each group). Average contact angle is shown for: ( **D** ) non-modified LIG, and ( **E** ) nPt-LIG electrodes. Error bars represent standard deviation (n = 6 electrodes in each batch). Lowercase letters (a,b) indicate group subsetting based on LSD, where the same letter indicates no significant different between groups (α = 0.05). 

## _3.2. Electrochemical Characterization_ 

To further explore the behavior of LIG electrodes, single working electrode and threeelectrode non-modified LIG were tested. Open circuit potential (OCP) and cyclic voltammetry (CV) were analyzed at room temperature. For Faradaic testing, ferricyanide/ferrocyanide (2.5 mM each) was used as the redox probe couple, and potassium chloride (100 mM) as the electrolyte. 

OCP (non-Faradaic chronopotentiometry) was measured in 2 _×_ sodium bicarbonate isotonic buffer (pH = 7.6). The average OCP for single LIG electrodes (209 _±_ 11 mV) varied by less than 5% and was more than two times higher than LIG sensor chips (90.2 _±_ 8.8 mV). This experiment was repeated in an equimolar mixture of potassium ferri/ferrocyanide (2.5 mM each) to determine the half-cell constant (E0). The average E0 value for LIG electrodes was 93.5 _±_ 13.9 mV. See Supplemental Figure S3 for details on all solutions tested. 

After characterizing OCP in multiple solutions, a ferri/ferrocyanide solution was used to study current response during CV (pH 6.8). Since both LIG and the ferri/ferrocyanide redox couple have negative charge under these testing conditions, it is likely that some electrical repulsion may have occurred at the LIG surface. One common technique to alleviate this problem is use of repetitive CV sweeps (i.e., electro-conditioning). This is a 

_Micromachines_ **2024** , _15_ , 874 

7 of 13 

known mechanism for stabilizing the dielectric layer in electrochemical sensors and is often used in sensor development [39]. Thus, batches of 36 LIG electrodes were tested using ten successive CV sweeps for both single-electrode LIG and LIG sensor chips. Oxidation peak current (iop) data were extracted from CV curves as the response variable. 

Figure 2 shows representative cyclic voltammograms at 200 mV/s for LIG working electrodes using 2.5 mM potassium ferrocyanide and 2.5 mM ferricyanide as redox probes, with 100 mM potassium chloride as electrolyte. Figure 2A,C shows representative CV plots for the initial (1st scan) and final (10th scan) scan during LIG electro-conditioning. These voltammograms visualize the change in peak anodic/cathodic current during electroconditioning, and slight changes in the archetypical shape of the CV. The oxidation and reduction peaks were more defined for the single LIG electrode than the LIG sensor chip assembly. Peak separation (∆Ep) for the single LIG electrode system was 205 _±_ 50 mV, which indicates relatively slow electron transfer kinetics under these testing conditions. For the LIG sensor chip the ∆Ep was nearly double (519 _±_ 20 mV). Figure 2B,D show box plots for 36 replicates for the single LIG and LIG sensor chip, respectively, and visualize the mean, standard deviation, interquartile range, and outliers for each electrode type. The mean iop for the single LIG electrode was higher than the LIG sensor chip, which is expected since LIG was used as the counter electrode in the chip design (compared to 99.9% Pt wire used in single LIG electrode assembly). Although the LIG sensor chip has a relatively low anodic peak current under these conditions, this device represents a portable test as compared to the single LIG electrode system, which is a laboratory testing setup. 

**Figure 2.** Cyclic voltammetry at 200 mV/s for LIG working electrodes (ferro/ferricyanide redox couple). Representative CV plots for initial (1st) and final (10th) electro-conditioning scan, and box plots showing peak oxidative current; n = 36 electrodes for each experiment. In box plots, dashed lines represent data range and open circles represent outliers (values outside the range _±_ 1.5 times interquartile range). ( **A** ) Representative CV of single LIG electrode, ( **B** ) boxplot of single LIG peak current, ( **C** ) representative CV of LIG sensor chip, and ( **D** ) boxplot of LIG sensor chip peak current. 

To test for normality, CV data were further analyzed using a Shapiro–Wilk test (α = 0.05). The results indicate that single LIG assembly peak oxidative current was not normally distributed in electro-conditioning experiments. Conversely, data for the LIG sensor chip assembly were normally distributed during electro-conditioning. Thus, different methods were chosen accordingly to test for significant differences amongst conditioning 

_Micromachines_ **2024** , _15_ , 874 

8 of 13 

scans. A Wilcox test was used for the single LIG assembly (non-normal) and a two-tailed _t_ -test was used for nPt-LIG single electrodes. Supplemental Figure S4 shows a heat map of the difference testing results for each LIG electrode assembly. The dark grey shading indicates _p_ -values smaller than 0.05 (significant difference in peak oxidation current), while the light grey shading represents _p_ -values larger than 0.05 (no significant difference). The single LIG assembly requires at least four successive conditioning scans for the peak oxidative current to stabilize at 189 _±_ 20 µA. For the LIG sensor chip, only two scans were required to stabilize the dielectric layer at 155 _±_ 25 µA. 

## _3.3. Nanoplatinum Deposition on LIG Electrodes_ 

As most LIG electrodes are metallized for sensor applications [13–15,19,24], we tested the electrochemical behavior of LIG plated with nanoplatinum (nPt) in both the single LIG electrode and the LIG sensor chip format. After electro-conditioning the working electrode, LIG was immediately transferred to a chloroplatinic acid/lead acetate solution (pH 1.2) for electrodeposition of nPt. Figure 3 shows representative CV scans for LIG and nPt-LIG single-electrode and sensor chip assemblies. The iop was 150~250 µA higher after nPt deposition, and the peak was more pronounced for the single LIG electrode assembly (Figure 3A,B). The ∆Ep for both the single nPt-LIG electrodes (143 _±_ 3 mV) and nPt-LIG sensor chip (403 _±_ 43 mV) decreased significantly after metallization, which indicates an increase in electron transfer kinetics, as expected. However, the data indicate that the electron transfer properties under these conditions are relatively slow. The ABC (a proxy of specific capacitance) was seven times as high after nPt deposition, indicating a significant increase in surface charge (capacitance) for the metal–carbon hybrid material. The observed increase in capacitance (and peak current) has been shown with many other types of carbon electrodes [40,41], including LIG [12–14]. Raw CV data are presented in Supplemental Figure S5 and available in the Zenodo repository (see data availability statement). 

**Figure 3.** Representative CV plots of LIG and nPt-LIG in ferri/ferrocyanide at 200 mV/s (100 mM potassium chloride as electrolyte). ( **A** ) Single LIG electrodes (non-modified and after nPt coating). A Pt wire was used as counter electrode, and Ag/AgCl as reference electrode. ( **B** ) LIG sensor chip (nonmodified and after nPt coating). Metal alloy tape was used as reference electrode, and LIG as counter electrode. ( **C** ) Area between anodic/cathodic sweep (in µV-A) for LIG and nPt-LIG in each assembly. At least 50 electrodes were tested for each electrode type (details in Supplemental Tables S2 and S3). 

## _3.4. Batch-to-Batch Variation of Anodic Peak Current_ 

The experiment in Figure 3 was repeated in four batches of 36 electrodes as described previously. Four individual sets of each electrode type were fabricated on a different day by the same operator. Violin plots (Figure 4) indicate that the LIG sensor chip assembly had lower oxidation and reduction peaks than the LIG, with more noise (approximately 30% variation). However, when the working electrode was metallized with nPt, the effect absolves, and there is not a statistically significant difference between the single LIG and LIG sensor chip (oxidative and reductive peaks). Electron micrographs from our previous work with this material indicate that nPt coats the LIG surface. These results 

_Micromachines_ **2024** , _15_ , 874 

9 of 13 

indicate that electrodeposition of nPt on LIG homogenizes the surface charge and dielectric layer. The peak oxidation potential (Figure 4B) did significantly change for any assembly (385 _±_ 31 mV). However, the peak reduction potential for single LIG (31 _±_ 45 mV) was significantly lower than the other electrode assemblies (362 _±_ 202 mV). Further study is required to understand the variation in oxide groups on LIG before and after metal deposition, which may provide insight into the variation in Erp. Individual plots of each dataset are shown in Supplemental Figure S6. 

**Figure 4.** Average peak oxidation and reduction for LIG assemblies: ( **A** ) peak oxidation current (aqua violins) and reduction current (grey violins); ( **B** ) peak oxidation potential (teal violins) and reduction potential (purple violins); and ( **C** ) area between curve (anodic-cathodic sweep). All scans conducted at 25 _[◦]_ C in ferri/ferrocyanide solution at 200 mV/s (100 mM potassium chloride as electrolyte). White dots represent median value, black boxes range from the lower to the upper quartile, whiskers present the variability outside upper and lower quantile, and the shape of violin plot indicates the data density. 

The least significant difference (LSD) test was conducted in R studio for statistical analysis [42]. Supplemental Figure S6 shows the results of CV analysis (iop and ABC were calculated from each CV experiment). For all batches, Pt electrodeposition significantly increased iop and ABC, similar to the analysis of all merged batches in Figure 4. The specific type of Pt electrodeposition had a significant impact on the peak current and potential in all batches, which illuminates the need for additional studies focused on nanometal characterization in LIG systems. When analyzed individually, a distinct grouping of Iop for each of the batches was observed, which explains the bimodal distributions in Figure 4. For this reason, the clustering analysis tool developed by Qian et al. is critical to maximize performance (especially if CV or other DC potential techniques are used for signal transduction). 

Figure 5 shows the average batch-to-batch variation based on CV. Using oxidative peak as the response variable, the LIG single electrode had the lowest variability (less than 2% variation across batches), and the LIG sensor chip was four times higher (8% variation across batches). This was expected, as the use of a commercial counter and reference electrode is more efficient than custom designs. However, the sensor chip design is applicable for point-of-need sensing, while the single LIG electrode system is only valid for controlled lab studies. The variation within batches was approximately 10% for both LIG single-electrode and sensor chip assemblies. As shown in Figure 5B, the trend in batch variation using cathodic (reductive) peak current as the response variable was similar, but the variation within batches (12–15%) and across batches (11%) was higher than the anodic sweep. Likewise, the variation for ABC (Figure 5C) was even higher (15% across batches and 12% within batches). The peak potential varied by 5% within groups, and 2% across groups (result consistent for either anodic or cathodic sweep). The variation for the LIG sensor chip was slightly higher (5–15%), although the mean current and ABC were lower. 

_Micromachines_ **2024** , _15_ , 874 

10 of 13 

**Figure 5.** Average electrochemical parameters during batch testing. Each batch consists of six replicate electrodes. ( **A** ) Average peak oxidation (anodic) and reduction (cathodic) current; ( **B** ) peak oxidation potential (teal violins) and reduction potential (purple violins); and ( **C** ) area between curve (anodiccathodic sweep). All scans conducted at 25 _[◦]_ C in ferri/ferrocyanide solution at 200 mV/s (100 mM potassium chloride as electrolyte). Error bars represent standard deviation of the arithmetic mean (n = 6 in each batch). 

The batch variation for nPt-LIG was higher than the LIG single electrode, although the mean values were similarly significantly improved relative to the LIG electrode (without nPt). There was no significant difference between the variability of the nPt-LIG single electrode and the nPt-LIG sensor chip, which is an important design improvement compared to bare LIG electrodes. The most pronounced variability for nPt-LIG was the ABC (Figure 5C). After metallization, the batch variation was 15–20% within batches and 30–40% across batches. Supplemental Figure S6 shows that this result is likely due to the method of metal deposition. Galvanostatic electrodeposition led to a lower peak current than frequency-modulated electrodeposition (AC waveform) and had less batch variation (both within and across batches). The noted increase in capacitive behavior is critical for many sensors [12,13,43–45], but may come at the expense of high batch variation when scaling sensors (using the methods herein). While electrodeposition is a simple and reliable technique, precise control over the microscale structuring is extremely challenging. Techniques such as simultaneous sonication/plating (i.e., sono-electrodeposition) have been shown to enhance the fractality of nanometals deposited on the surface [32], but detailed studies of batch-to-batch variability using this technique have not been explored to the best of our knowledge. Further studies are required to understand the underlying mechanism(s) of this variability in system capacitance and for the development of strategies to improve the repeatability. 

The results shown here are in line with Avinash et al. [4], noting the high degree of variation for laser-ablated graphene. In accordance, we suggest that studies are needed on standardizing laser-processing equipment techniques and experimental parameters for micro-device fabrication. Additional factors of importance are the orientation of electrode scribing, which was shown to be important in the study by Behrent et al. [26]. The data from this study are available (open access) at Zenodo; see data availability statement. The data files in the repository contain all experimental metadata and equipment/instrument metadata. One of the limitations of the data are the use of a relatively high scan rate (200 mV/s), which may induce some Ohmic drop. No corrections were applied to account for uncompensated resistance, which is a consideration for follow-up studies. In addition, we have performed other analyses not represented in this body of work (e.g., Raman microscopy, electrokinetic analysis, atomic force microscopy); results and additional datasets will be appended to the Zenodo repository as they are available (in raw data format). 

## **4. Conclusions** 

Laser-inscribed graphene (LIG) is an emerging material for micro-electronic applications and is being used to develop supercapacitors, soft actuators, triboelectric generators, 

_Micromachines_ **2024** , _15_ , 874 

11 of 13 

and sensors. The fabrication technique is simple, yet the batch-to-batch variation of LIG quality is not well documented in the literature. For the first time, we conducted a study to characterize batch-to-batch variation in the manufacturing of LIG electrodes for applications in electrochemical sensing. Numerous batches of 36 LIG electrodes were synthesized using a CO2 laser system and polyimide film. The LIG material was characterized using goniometry in various solutions, stereomicroscopy, open circuit potentiometry, and cyclic voltammetry (CV). The contact angle and average OCP for LIG electrodes varied by approximately 5%, but the variability was significantly higher for LIG electrodes metallized with platinum. Contact angle did not vary across batches, but the type of liquid tested did have a significant effect on mean contact angle. Although each buffer is commonly used in sensor development/testing, a number of the compounds are zwitterionic or emulsifying agents that are known to alter wettability. Characterization of the hydrophobicity in these various buffers provides key insights into the surface charge of the graphitized/metallized materials. When LIG sensor chips were fabricated (working, counter, and reference electrode composed of LIG), the peak current at 200mV/sec decreased significantly, although the batch-to-batch variation was similar (5–10%). After metallization of LIG with nanoplatinum (nPt), anodic/cathodic current, and area between CV curve increased significantly. However, the batch variation increased to 20% within groups and up to 40% across groups. Taken together, these results indicate that metallization of LIG with nPt improves performance but comes at the expense of increased batch variability. This study provides important insight into the variation of material properties, and we note that additional studies are needed to understand the mechanisms with the aim of improving quality control in LIG micro-device scaling. The dataset is available via an open access repository for additional analysis. 

**Supplementary Materials:** The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/mi15070874/s1, Table S1. Contact angle for non-modified LIG in various solutions measured with a Droplet lab DROPOMETER-M; Table S2. Features from electrochemistry dataset for this study; Table S3. Average peak current and potential for all LIG tested; Figure S1. Process of laser induced graphitization of polyimide; Figure S2. Heat map for laser fabrication settings of LIG based on study by Behrent et al. [26]; Figure S3. Open circuit potential measured in bicarbonate buffer at room temperature; Figure S4. _p_ -value heat map of conditioning CV indicating significant testing of iop relative to the 1st scan; Figure S5. Raw cyclic voltammograms at 200 mV/s (ferri/ferrocyanide with potassium chloride as electrolyte); Figure S6. Five treatments were designed to determine the ideal nPt electrodeposition condition on both a single electrode (control) and biochip system. 

**Author Contributions:** Conceptualization: Y.T., D.V. and E.S.M.; methodology: Y.T., D.V. and E.S.M.; formal analysis: Y.T., G.A.M. and E.S.M.; investigation: Y.T., D.V., G.A.M., S.P.A.D. and E.S.M.; resources: D.V. and E.S.M.; data curation, E.S.M.; writing—original draft preparation: Y.T. and E.S.M.; writing—review and editing: Y.T., D.V., G.A.M., S.P.A.D. and E.S.M.; visualization: Y.T. and E.S.M.; supervision: E.S.M.; project administration: D.V. and E.S.M.; and funding acquisition: D.V. and E.S.M. All authors have read and agreed to the published version of the manuscript. 

**Funding:** The authors acknowledge financial support from the National Institute on Alcohol Abuse and Alcoholism of the National Institutes of Health under Award Number U01AA029328, the Science and Technologies for Phosphorus Sustainability (STEPS) Center, the National Science Foundation Science and Technology Center (CBET-2019435), and the NIFA Agriculture and Food Research Initiative Competitive Grant no. 2018-67016-27578 awarded as a Center of Excellence from the USDA National Institute of Food and Agriculture. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health, National Science Foundation, nor the National Institute of Food and Agriculture. 

**Data Availability Statement:** Cyclic voltammetry data are available in an open access repository at Zenodo: https://zenodo.org/communities/qclig/records?q=&l=list&p=1&s=10&sort=newest. 

_Micromachines_ **2024** , _15_ , 874 

12 of 13 

**Acknowledgments:** A preprint of this manuscript is posted on: https://dspace.mit.edu/handle/17 21.1/123983. The authors thank Rodenhausen from Anton Paar for discussions related to dielectrics, which greatly informed our research on this topic. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **References** 

1. Ye, R.; James, D.K.; Tour, J.M. Laser-Induced Graphene: From Discovery to Translation. _Adv. Mater._ **2019** , _31_ , 1803621. [CrossRef] 2. Lin, J.; Peng, Z.; Liu, Y.; Ruiz-Zepeda, F.; Ye, R.; Samuel, E.L.G.; Yacaman, M.J.; Yakobson, B.I.; Tour, J.M. Laser-induced porous graphene films from commercial polymers. _Nat. Commun._ **2014** , _5_ , 5714. [CrossRef] 

3. Wang, H.; Zhao, Z.; Liu, P.; Guo, X. Laser-Induced Graphene Based Flexible Electronic Devices. _Biosensors_ **2022** , _12_ , 55. [CrossRef] 

4. Avinash, K.; Patolsky, F. Laser-induced graphene structures: From synthesis and applications to future prospects. _Mater. Today_ **2023** , _70_ , 104–136. [CrossRef] 

5. Coelho, J.; Correia, R.F.; Silvestre, S.; Pinheiro, T.; Marques, A.C.; Correia, M.R.P.; Pinto, J.V.; Fortunato, E.; Martins, R. Paper-based laser-induced graphene for sustainable and flexible microsupercapacitor applications. _Microchim. Acta_ **2023** , _190_ , 40. [CrossRef] 

6. Xu, Y.; Fei, Q.; Page, M.; Zhao, G.; Ling, Y.; Chen, D.; Yan, Z. Laser-induced graphene for bioelectronics and soft actuators. _Nano Res._ **2021** , _14_ , 3033–3050. [CrossRef] 

7. Stanford, M.G.; Li, J.T.; Chyan, Y.; Wang, Z.; Wang, W.; Tour, J.M. Laser-Induced Graphene Triboelectric Nanogenerators. _ACS Nano_ **2019** , _13_ , 7166–7174. [CrossRef] [PubMed] 

8. Stanford, M.G.; Yang, K.; Chyan, Y.; Kittrell, C.; Tour, J.M. Laser-Induced Graphene for Flexible and Embeddable Gas Sensors. _ACS Nano_ **2019** , _13_ , 3474–3482. [CrossRef] [PubMed] 

9. Deng, B.; Wang, Z.; Liu, W.; Hu, B. Multifunctional Motion Sensing Enabled by Laser-Induced Graphene. _Materials_ **2023** , _16_ , 6363. [CrossRef] 

10. Menon DM, N.; Giardino, M.; Janner, D. Direct Fabrication of Ultrahydrophobic Laser-Induced Graphene for Strain Sensors. _Appl. Sci._ **2023** , _13_ , 4935. [CrossRef] 

11. Casso-Hartmann, L.; Moreira, G.A.; Tang, Y.; Vanegas, D.; McLamore, E.S. Fabrication of laser inscribed graphene (LIG) 3-electrode plug-and-play chip. _protocol.io_ **2024** , preprint. 

12. Moreira, G.; Casso-Hartmann, L.; Datta, S.P.A.; Dean, D.; McLamore, E.; Vanegas, D. Development of a Biosensor Based on Angiotensin-Converting Enzyme II for Severe Acute Respiratory Syndrome Coronavirus 2 Detection in Human Saliva. _Front. Sens._ **2022** , _3_ , 917380. [CrossRef] [PubMed] 

13. Moreira, G.; Qian, H.; Datta, S.P.; Bliznyuk, N.; Carpenter, J.; Dean, D.; McLamore, E.; Vanegas, D. A capacitive laser-induced graphene based aptasensor for SARS-CoV-2 detection in human saliva. _PLoS ONE_ **2023** , _18_ , e0290256. [CrossRef] [PubMed] 

14. Vanegas, D.; Patiño, L.; Mendez, C.; de Oliveira, D.A.; Torres, A.M.; Gomes, C.L.; McLamore, E.S. Laser Scribed Graphene Biosensor for Detection of Biogenic Amines in Food Samples Using Locally Sourced Materials. _Biosensors_ **2018** , _8_ , 42. [CrossRef] [PubMed] 

15. Garland, N.T.; McLamore, E.S.; Cavallaro, N.D.; Mendivelso-Perez, D.; Smith, E.A.; Jing, D.; Claussen, J.C. Flexible Laser-Induced Graphene for Nitrogen Sensing in Soil. _ACS Appl. Mater. Interfaces_ **2018** , _10_ , 39124–39133. [CrossRef] [PubMed] 

16. Liu, H.; Sun, Z.; Chen, Y.; Zhang, W.; Chen, X.; Wong, C.-P. Laser Processing of Flexible In-Plane Micro-supercapacitors: Progresses in Advanced Manufacturing of Nanostructured Electrodes. _ACS Nano_ **2022** , _16_ , 10088–10129. [CrossRef] [PubMed] 

17. Le, T.D.; Phan, H.P.; Kwon, S.; Park, S.; Jung, Y.; Min, J.; Chun, B.J.; Yoon, H.; Ko, S.H.; Kim, S.W.; et al. Recent Advances in Laser-Induced Graphene: Mechanism, Fabrication, Properties, and Applications in Flexible Electronics. _Adv. Funct. Mater._ **2022** , _32_ , 2205158. [CrossRef] 

18. Liu, X.; Wang, X.; Li, J.; Qu, M.; Kang, M.; Zhang, C. Nonmodified Laser-Induced Graphene Sensors for Lead-Ion Detection. _ACS Appl. Nano Mater._ **2023** , _6_ , 3599–3607. [CrossRef] 

19. Hjort, R.G.; Soares, R.R.A.; Li, J.; Jing, D.; Hartfiel, L.; Chen, B.; Van Belle, B.; Soupir, M.; Smith, E.; McLamore, E.; et al. Hydrophobic laser-induced graphene potentiometric ion-selective electrodes for nitrate sensing. _Microchim. Acta_ **2022** , _189_ , 122. [CrossRef] 

20. Zhu, J.; Liu, S.; Hu, Z.; Zhang, X.; Yi, N.; Tang, K.; Dexheimer, M.G.; Lian, X.; Wang, Q.; Yang, J.; et al. Laser-induced graphene non-enzymatic glucose sensors for on-body measurements. _Biosens. Bioelectron._ **2021** , _193_ , 113606. [CrossRef] 

21. Zhang, Y.; Zhang, C.; Chen, W.; Liu, Z. One-step laser-induced Cu-embedded graphene for non-enzymatic glucose sensing in beverages. _J. Alloys Compd._ **2024** , _992_ , 174563. [CrossRef] 

22. Rauf, S.; Lahcen, A.A.; Aljedaibi, A.; Beduk, T.; Filho, J.I.d.O.; Salama, K.N. Gold nanostructured laser-scribed graphene: A new electrochemical biosensing platform for potential point-of-care testing of disease biomarkers. _Biosens. Bioelectron._ **2021** , _180_ , 113116. [CrossRef] 

23. Wan, Z.; Umer, M.; Lobino, M.; Thiel, D.; Nguyen, N.-T.; Trinchi, A.; Shiddiky, M.J.; Gao, Y.; Li, Q. Laser induced self-N-doped porous graphene as an electrochemical biosensor for femtomolar miRNA detection. _Carbon_ **2020** , _163_ , 385–394. [CrossRef] 

24. Soares, R.R.A.; Hjort, R.G.; Pola, C.C.; Parate, K.; Reis, E.L.; Soares, N.F.F.; McLamore, E.S.; Claussen, J.C.; Gomes, C.L. LaserInduced Graphene Electrochemical Immunosensors for Rapid and Label-Free Monitoring of Salmonella enterica in Chicken Broth. _ACS Sens._ **2020** , _5_ , 1900–1911. [CrossRef] [PubMed] 

_Micromachines_ **2024** , _15_ , 874 

13 of 13 

25. Qian, H.; Moreira, G.; Vanegas, D.; Tang, Y.; Pola, C.; Gomes, C.; McLamore, E.; Bliznyuk, N. Improving high throughput manufacture of laser-inscribed graphene electrodes via hierarchical clustering. _Sci. Rep._ **2024** , _14_ , 7980. [CrossRef] 

26. Behrent, A.; Griesche, C.; Sippel, P.; Baeumner, A.J. Process-property correlations in laser-induced graphene electrodes for electrochemical sensing. _Microchim. Acta_ **2021** , _188_ , 159. [CrossRef] 

27. Puetz, P.; Behrent, A.; Baeumner, A.J.; Wegener, J. Laser-scribed graphene (LSG) as new electrode material for impedance-based cellular assays. _Sens. Actuators B Chem._ **2020** , _321_ , 128443. [CrossRef] 

28. Chen, B.; Johnson, Z.T.; Sanborn, D.; Hjort, R.G.; Garland, N.T.; Soares, R.R.A.; Van Belle, B.; Jared, N.; Li, J.; Jing, D.; et al. Tuning the Structure, Conductivity, and Wettability of Laser-Induced Graphene for Multiplexed Open Microfluidic Environmental Biosensing and Energy Storage Devices. _ACS Nano_ **2022** , _16_ , 15–28. [CrossRef] [PubMed] 

29. Goldie, S.J.; Bush, S.; Cumming, J.A.; Coleman, K.S. A Statistical Approach to Raman Analysis of Graphene-Related Materials: Implications for Quality Control. _ACS Appl. Nano Mater._ **2020** , _3_ , 11229–11239. [CrossRef] 

30. Kyle, J.R.; Ozkan, C.S.; Ozkan, M. Industrial graphene metrology. _Nanoscale_ **2012** , _4_ , 3807. [CrossRef] 

31. McLamore, E.S.; Vanegas, D.C.; Pinzon, D.B.; McCourt, K.; Tang, Y. Protocol L2.3-LIG fabrication using Universal Laser System. _Protocol_ **2020** , I/O 1–7. [CrossRef] 

32. Taguchi, M.; Schwalb, N.; Rong, Y.; Vanegas, D.C.; Garland, N.; Tan, M.; Yamaguchi, H.; Claussen, J.C.; McLamore, E.S. pulSED: Pulsed sonoelectrodeposition of fractal nanoplatinum for enhancing amperometric biosensor performance. _Analyst_ **2016** , _141_ , 3367–3378. [CrossRef] [PubMed] 

33. Tang, Y. _Laser Inscribed Graphene Aptasensor for Detection of Apple Stem Pitting Virus_ ; Clemson University: Clemson, SC, USA, 2023. 

34. Garcia-Cordero, J.L.; Fan, Z.H. Sessile droplets for chemical and biological assays. _Lab Chip_ **2017** , _17_ , 2150–2166. [CrossRef] [PubMed] 

35. Chen, H.; Muros-Cobos, J.L.; Holgado-Terriza, J.A.; Amirfazli, A. Surface tension measurement with a smartphone using a pendant drop. _Colloids Surf. A Physicochem. Eng. Asp._ **2017** , _533_ , 213–217. [CrossRef] 

36. Tang, Y.; Hartmann, L.C.; Pinzon, D.B.; Moreira, G.A.; Vanegas, D.; McLamore, E.S. Electrochemical Analysis of Laser-Inscribed Graphene Electrodes Using Cyclic Voltammetry (Ferri/Ferrocyanide Redox Couple). _protocols.io_ **2023** , working. [CrossRef] 

37. Wang, H.; Pilon, L. Physical interpretation of cyclic voltammetry for measuring electric double layer capacitances. _Electrochim. Acta_ **2012** , _64_ , 130–139. [CrossRef] 

38. Mulqueen, M.; Blankschtein, D. Prediction of Equilibrium Surface Tension and Surface Adsorption of Aqueous Surfactant Mixtures Containing Zwitterionic Surfactants. _Langmuir_ **2000** , _16_ , 7640–7654. [CrossRef] 

39. Sonmezoglu, S.; Carbas, B.; Gülen, M.; Celik, M. Hydrogen sulphate-based ionic liquid-assisted electro-polymerization of PEDOT catalyst material for high-efficiency photoelectrochemical solar cells. _Sci. Rep._ **2017** , _7_ , 11672. 

40. Paczosa-Bator, B.; Cabaj, L.; Piech, R.; Skupie´n, K. Potentiometric Sensors with Carbon Black Supporting Platinum Nanoparticles. _Anal. Chem._ **2013** , _85_ , 10255–10261. [CrossRef] 

41. Vanegas, D.C.; Taguchi, M.; Chaturvedi, P.; Burrs, S.; Tan, M.; Yamaguchi, H.; McLamore, E.S. A comparative study of carbonplatinum hybrid nanostructure architecture for amperometric biosensing. _Analyst_ **2014** , _139_ , 660–667. [CrossRef] 

42. Steel, R.; Torri, J.; Dickey, D. _Principles and Procedures of Statistics A Biometrical Approach_ ; McGraw-Hill: New York, NY, USA, 1997. 43. Qureshi, A.; Roci, I.; Gurbuz, Y.; Niazi, J.H. An aptamer based competition assay for protein detection using CNT activated gold-interdigitated capacitor arrays. _Biosens. Bioelectron._ **2012** , _34_ , 165–170. [CrossRef] 

44. Kraikaew, P.; Sailapu, S.K.; Bakker, E. Electronic control of constant potential capacitive readout of ion-selective electrodes for high precision sensing. _Sens. Actuators B Chem._ **2021** , _344_ , 130282. [CrossRef] 

45. Yagati, A.K.; Behrent, A.; Beck, S.; Rink, S.; Goepferich, A.M.; Min, J.; Lee, M.H.; Baeumner, A.J. Laser-induced graphene interdigitated electrodes for label-free or nanolabel-enhanced highly sensitive capacitive aptamer-based biosensors. _Biosens. Bioelectron._ **2020** , _164_ , 112272. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

