Review 

pubs.acs.org/acssensors 

## **Strategy, Design, and Fabrication of Electrochemical Biosensors: A Tutorial** 

Karthika Sankar, Uros Kuzmanovic, Scott E. Schaus,* James E. Galagan,* and Mark W. Grinstaff* 

**Cite This:** https://doi.org/10.1021/acssensors.4c00043 **Read Online** 

ACCESS | al Metrics & More | Article Recommendations 

ABSTRACT: Advanced healthcare requires novel technologies Electrochemicaltechniques biorecognitionBiomarkerselementsand —_ of biosensorDesign Electrodechoices & capable of real-time sensing to monitor acute and long-term health. , to detect them , : : Data The challenge relies on converting a real-time quantitative = Time | | - | lon | 3 biological and chemical signal into a desired measurable output. S|5 weAN || SZ I| sd| fe) ) I1°3 JS, Given the success in detecting glucose and the commercialization nedTimeII I1 jen || || GY of glucometers, electrochemical biosensors continue to be a | -ae I | ae | mainstay of academic and industrial research activities. Despite the £ m4 4 ‘| ( } , 'e2o0100 ©).e || “| 4 I1 ieeeDOR lg8 wealth of literature on electrochemical biosensors, reports are often Ze | KL ~ | ' 3 o | I I 1 By Ue specific to a particular application (e.g., pathogens, cancer markers, z \ 1 Ble glucose, etc.), and most fail to convey the underlying strategy and E \ AUC ; “| Oo | | Fo False ©} slopes \ ,—— || | design, and if it is transferable to detection of a different analyte. Time || Here we present a tutorial review for those entering this research '! ' 1 area that summarizes the basic electrochemical techniques utilized as well as discusses the designs and optimization strategies employed to improve sensitivity and maximize signal output. KEYWORDS: _optimization of biosensors, biorecognition elements, sensor design, biosensor components, electrochemical techniques, enzymatic, immunosensor, DNA sensors_ 

B iosensors are devices that convert a chemical or biological change into a quantifiable signal and thereby measure the concentration of an analyte(s). Biosensors differ from conventional sensors as they consist of a biological recognition element that selectively binds to the analyte of interest, offering analyte specificity, a transducer that produces the signal, and a signal processor that collects, amplifies, and displays the signal output. Biosensors play a pivotal role in medicine as they are used to monitor disease progression and health biomarkers as well as in drug discovery.[1][,][2] Electrochemical (E-chem) biosensors are a subclass of biosensors that comprises enzymes/proteins/nucleic acids as biorecognition elements, electrodes as transducers, and a current/impedance signal output correlated to the analyte concentration. For example, glucometers, the blood glucose monitoring device around since the 1980s, is a prime example of a success story with a >$15 B market worldwide.[3] Although glucometers detect millimolar concentrations of glucose in the blood, E-chem biosensors have the potential to attain low limits of quantitative detection combined with high sensitivity. 

Electrochemical detection offers the advantages of low cost, ease of use, miniaturization, and portability over laboratorybased sensing methods like immunoassays, molecular diagnostics, etc.[4][,][5] E-chem detection also requires very small sample volumes and is not influenced by the presence of sample components that typically interfere with spectrophotometric detection (such as chromophores, fluorophores− 

hemoglobin, and red blood cells). However, the applied potential must be carefully selected so as to not reduce or oxidize other molecules/biomacromolecules present in the sample. The two general designs of E-chem biosensors include biocatalytic- and affinity-based sensors.[6] Biocatalytic sensors incorporate enzymes or whole cells that recognize the target analyte and produce electroactive species. Affinity sensors, in contrast, operate by selective binding between the analyte and biorecognition element (antibody or nucleic acid). Biosensors are in development today that perform point-of-care single measurements as well as noninvasive continuous monitoring[7][,][8] of protein, metabolite, or hormone biomarkers from cancer to metabolic diseases. The increased accuracy, effectiveness, and reliability enhance the potential commercial impact of these biosensing platforms. 

In order to further develop these technologies, it is critical to understand the basic concepts of these sensing methodologies to create far-reaching impacts in this field. We provide a guidebook for beginning graduate students and professionals 

Received: January 8, 2024 Revised: March 31, 2024 Accepted: April 10, 2024 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

© XXXX American Chemical Society 

**A** 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

not specialized in diagnostics into the basics of electrochemical techniques for analyte detection as well as the different parts and techniques used to build electrochemical biosensors. We then describe various data analysis methods and optimization strategies for improving the signal-to-noise ratio in the context of achieving rapid, quantitative, and specific analyte detection using E-chem biosensors. 

## ■ **[ELECTROCHEMICAL][BIOSENSOR] FUNDAMENTALS** 

The fundamental basis of electrochemical biosensors is redox reactions in which one chemical species gains electrons and another gives up electrons. In redox terminology, the species that gains electrons is reduced, the species that loses electrons is oxidized, and a pair of species participating in electron transfer is called a redox couple. The ratio between the reduced and oxidized species is described using the Nernst equation: 

**==> picture [229 x 24] intentionally omitted <==**

where _R_ is the universal gas constant, _F_ is the Faraday constant, _T_ is the temperature, _z_ is the number of electrons transferred, _E_[0] is the standard reduction potential, _E_ cell is the external voltage across the reaction, and [red] and [ox] are the concentrations of the reduced and oxidized species, respectively. 

In the absence of an external potential, the ratio of oxidized to reduced species at a given temperature is determined by _E_[0] . Importantly, the application of an external potential, _E_ cell, modifies the ratio of oxidized to reduced species according to the Nernst equation. The application of an external voltage thus biases the electron flow between the redox couples. Electrochemical biosensors take advantage of this capability with externally applied voltages. 

Electrochemical biosensors tap into the flow of electrons of redox reactions by linking several processes in a reaction cell (Figure 1): 

- A complementary transfer of charge across the solution/ electrode interface to balance charge in the solution. 

- An application of an external potential across the cell to modulate electron flow and diffusion. 

The combination of these processes defines a complex impedance between an externally applied voltage and electron flow that is modulated by the concentration of the analyte (Figure 1). Figure 1 shows an example of a linear range of a biosensor. However, at higher concentrations of the analyte, the output signal plateaus due to saturation effects and is explained in the later section. 

Biosensing consists of applying different patterns of external voltages and measuring the current flow to probe the impedance of the overall reaction cell. This measurement infers the presence or concentration of the target analyte. While many different patterns of applied external voltages can be applied, we discuss three of the most common electrochemical techniques: 

- Amperometry: voltage is applied as a step function to a constant level, and current as a function of time is analyzed. 

- Voltammetry: voltage is scanned back and forth between two different voltage levels, and current as a function of voltage is analyzed. 

- Impedance spectroscopy: a frequency-varying sinusoidal voltage is applied, and complex impedance as a function of frequency is analyzed. 

Each of these approaches has been analyzed in detail, and corresponding mathematical descriptions defined.[9] We describe the fundamentals of each in the next section. 

## ■ **[ELECTROCHEMICAL][TECHNIQUES][FOR] BIOSENSING APPLICATIONS** 

**Amperometry.** Amperometry measures the current after the application of a constant applied potential value. The application of a constant potential initiates several processes. First, a capacitive current (Figure 2a) is generated as charge shifts across the electrode−solution boundary. The capacitive current does not involve any chemical reaction but is merely due to the accumulation or removal of ions on the electrode surface or in the electrolyte solution adjacent to the electrode surface. This current ( _I_[0] ) is significant immediately after the change in potential (<0.1 s), but decays exponentially as 

Figure 1. Processes in a biosensing system. Example of the linear range of a biosensing system. 

- Diffusion of analyte to the site of a redox reaction in which the analyte participates as one species of a redox couple and transfers electrons. Use of a redox enzyme to catalyze this transfer and confer specificity to this reaction. 

- Possible additional coupled redox reactions within the solution matrix that continue the transfer of electrons. 

- A transfer of electrons at a solution/electrode interface (often called a Faradaic current). 

Figure 2. Amperometry technique: (a) Capacitive current and (b) Faradaic current. 

**B** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

determined by the capacitance of the boundary layer resistance, as described by the following equation (eq 2). The change in potential and the resistance of the circuit dictate the initial current _I_[0] : ( _I_ = final current, _I_ ° = Δ _V_ / _R_ = initial current, _R_ = resistance of circuit, _C_ = capacitance, _t_ = time) 

**==> picture [229 x 11] intentionally omitted <==**

Second, electrochemically active species undergo oxidation (or reduction) on the working electrode, as governed by the Nernst equation, and produce faradaic current (Figure 2 b). This results in a depletion layer of reduced (or oxidized) species at the electrode surface. As oxidation (or reduction) at the electrode continues, the width of this depletion layer increases. Third, depleted species at the electrode surface are continuously replenished by mass transport to the surface (and through any coupled redox reactions occurring near the surface). This mass transport of electroactive species to the electrode becomes the rate-limiting step in the generation of continuous current at the electrode. Under conditions where transport is dominated by diffusion, the rate of replenishment is determined by the concentration gradient between bulk solution and the electrode surface (d _C_ /d _x_ ) and the diffusion coefficient of the species ( _D_ ) as predicted by Fick’s first law of diffusion (eq 3): 

**==> picture [228 x 22] intentionally omitted <==**

where _J_ is the rate of diffusion. Assuming that the concentration at the surface is zero, the gradient is given by _C_ /Δ _x_ , where _C_ is the bulk concentration. And since the depletion layer (Δ _x_ ) grows over time, this leads to a decreasing gradient and a current that also decreases over time. 

This system has been extensively analyzed.[10] Assuming that replenishment of the depletion layer depends entirely on the transport and oxidation (or reduction) of an analyte of interest to the surface, and that the concentration of analyte is zero at the electrode surface, the resulting predicted time-varying current is given by Cottrell equation (eq 4): 

**==> picture [230 x 28] intentionally omitted <==**

where _n_ = number of electrons transferred in the oxidation (or reduction) of the analyte, _F_ = Faraday constant, _A_ = active electrode area, _D_ = diffusion coefficient of the analyte, _C_ * = bulk concentration of analyte, _t_ = time. 

Under the assumptions of the Cottrell equation, the impedance ( _V_ / _I_ ) of the electrochemical cell, after any capacitive currents have diminished, appears as a pure resistance that decreases over time. Note that this faradaic current decay ( _I_ ∝ _t_[−][1/2] ) is much slower than the exponential decay of capacitive current if sufficient analyte is present. The current measurement is thus proportional to the concentration of the analyte in the bulk solution at any given time point after application of the potential. 

**Voltammetry.** Voltammetry measures the current after the application of a time-varying potential. The most common form of voltammetry is cyclic voltammetry (CV) in which the potential is repeatedly varied between two different voltage levels. As with amperometry, at any given potential level, certain redox species will undergo depletion near the electrode and replenishment by diffusion from the bulk solution. But since the applied voltage is time-varying, the resulting 

processes have more complex behaviors. Moreover, rather than analyzing current as a function of time, voltammetry typically considers current as a function of the voltage applied. Current versus potential is plotted over the range of voltages scanned, producing a set of overlapping cyclic traces, one for each repeated scan. This plot of current versus potential is called a voltammogram (Figure 1 and Figure 3c). 

Figure 3. Cyclic voltammetry. (a) Repeated scans of cyclic voltammetry, (b) contribution of Nernst equation and Cottrell equation, and (c) forward and reverse scan showing oxidation and reduction of species A 

Through the time-varying interplay between redox reactions, the formation of depletion layers, and diffusion, a “duck”shaped voltammogram is typically formed. In the case of a single freely diffusing electroactive analyte A, as one scans the potential toward a positive potential driving the oxidation of analyte (A → A[+] ) the concentration of A steadily depletes near the electrode surface. This depletion is governed by the Nernst equation (eq 1), leading initially to increasing current as the voltage increases until a peak oxidative current is reached. But as a depletion layer is formed, the diffusion of A to the electrode becomes the rate-limiting step, and as the voltage continues to increase, the current decreases from its peak to that predicted by the Cottrell equation (eq 4).[11] The shape of the voltammogram thus reflects a transition from an electrochemical current (Nernst) to a diffusion current (Cottrell; Figure 3b). On reversing the scan direction, we observe the reverse process leading to a peak reductive current. 

A crucial parameter that determines the shape of a voltammogram is the scan rate or the speed at which the potential is varied (in mV/s). The concentration of analyte species (oxidized and reduced) relative to the distance from the electrode depends on the potential applied and how the species migrates between the electrode surface and bulk solution. Faster scan rates result in decreased diffusion layer thickness and therefore higher currents. 

The shape of the voltammogram provides significant information about the electrochemical cell. For example, in the case of a single freely diffusing electroactive analyte, a symmetric curve indicates a reversible electrochemical reaction. Moreover, the two voltages at which the peak oxidative and reductive currents are observed will be symmetric to the standard reduction potential of the analyte (Figure 3a). In addition, the shape of the voltammogram reflects the magnitude of the capacitance and background resistance of the cell. Given a constant change in voltage, the 

**C** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

capacitance will contribute a constant positive current (oxidative scan) or constant negative current (reductive scan) shifting the baseline up or down, respectively.[11] The background resistance of the cell will result in a current dictated by Ohm’s law ( _V_ = _IR_ ), appearing as a line with a positive slope, and thus rotating the voltammogram counterclockwise by an amount depending on the resistance (Figure 3a). 

Of particular interest is the magnitude of the peak currents of the voltammogram. For a constant linear voltage sweep, with a single reversible electroactive species, the peak current (in either sweep direction) is described by the Randles−Sevcik equation: 

**==> picture [230 x 28] intentionally omitted <==**

where _ip_ (A) is the peak current (positive or negative depending on the sweep direction), _n_ is the number of electrons transferred in the redox event, _A_ (cm[2] ) is the electrode area, _D_ 0 (cm[2] s) is the diffusion coefficient of the oxidized analyte, _C_[0] (mol/cm[3] ) is the bulk concentration of the analyte, _v_ (V/s) is the scan rate. 

Peak currents are thus determined by three key parameters of the electrochemical cell: the surface area, the diffusion coefficient of the electroactive species, and the bulk analyte concentration. By fixing or varying two of these parameters, the third parameter can be determined. In the context of biosensors, the Randles−Sevcik equation predicts that for a given surface area, diffusion coefficient, and voltage scan rate, the peak current will be proportional to the bulk concentration of the analyte. Thus, either through calibration or determination of _A_ and _D_ 0, the concentration of the analyte is quantified.[11][,][12] 

Even though one uses cyclic voltammetry to study the nature of a redox reaction and the mechanism, determination of formal potentials, and electron transfer kinetics, the literature also describes the use of pulsed voltammetry techniques like differential pulsed voltammetry and square wave voltammetry-based biosensors. In CV, the waveform is linear, or in other words, there is continuous change in potential as a linear function of time, whereas in pulsed techniques, the potential is pulsed from one potential to another. In these techniques, we sample current twice per cycle, at the end of the forward and the reverse pulse. The principle of pulsed techniques relies on the difference in the decay rates of the charging and faradaic currents. Capacitive currents decay at an exponential rate and more rapidly than the faradaic current. The faradaic current is inversely proportional to the square root of time. As one samples the current at the end of the pulse, capacitive current is negligible and the current is solely due to the faradaic reaction, and this increased ratio to faradaic to nonfaradaic current improves the detection limit and higher sensitivity.[13][−][15] 

One of the approaches to increase current output signal is to vary the different parameters of square wave voltammetry such as amplitude, frequency and step size.[16][,][17] The peak current signal increases with an increase in frequency and amplitude of the square wave input. Changing the square wave frequency determines the time scale of the measurement and electrontransfer rate and, in turn, influences the peak current.[18][,][19] Changing the square wave amplitude alters the driving force underlying electron transfer, changing the forward and 

backward electron-transfer reaction rates, and in turn influences peak splitting and peak current. However, there is negligible effect on the step size of square wave as the increase in step size increases the variability in peak currents and causes shift in peak potentials. There is maximum binding-induced signal change (signal gain) at intermediate frequency and amplitude values.[20] At higher frequencies, the signal-to-noise ratio decreases as the instrument noise increases. These parameters should be studied in detail to choose the optimum frequency and amplitude for biosensing applications. 

**Electrochemical Impedance Spectroscopy (EIS).** EIS is a technique for analyzing the impedance of an electrochemical system in the frequency domain. Alternating sinusoidal voltages over a range of frequencies are applied, and the resulting sinusoidal currents enable calculation of a complex impendence as a function of frequency. The characteristics of this complex impedance infer properties of the system, typically through both visualization and fitting the impedance to an equivalent electric circuit model. 

Impedance, _Z_ ( _ω_ ) = _V_ ( _ω_ )/ _I_ ( _ω_ ), is the relationship between voltage and current expressed as a complex function of frequency ( _ω_ = 2 _πf_ where _ω_ and _f_ are frequencies in radians/s and hertz, respectively). Assuming a linear time-invariant system, a sinusoidal input voltage results in a sinusoidal output current. For a pure resistor R, the impedance is the same for all frequencies: 

**==> picture [41 x 24] intentionally omitted <==**

Thus, an output current will be in phase with the input voltage and have a magnitude scaled by the resistance (Figure 4a). For pure capacitance, the impedance is a purely complex function of _ω_ : 

**==> picture [42 x 24] intentionally omitted <==**

Figure 4. Impedance spectroscopy. (a) Output current in phase with the voltage, (b) output current with a phase shift of 90°, (c) semicircular Nyquist plot, and (d) Randles circuit. 

The output current proceeds with the input voltage with a phase shift of 90°, and the magnitude of the current is proportional to the frequency (zero at _w_ = 0 and approach an infinite value as _w_ →∞) (Figure 4b). Combinations of resistors and capacitors result in impedances that are additive (elements in series) or reciprocally additive (elements in parallel). 

**D** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

Properties of the impedance of an electrochemical system are typically visualized using either a Bode plot or a Nyquist plot. A Bode plot visualizes the phase and magnitude of _Z_ ( _ω_ ) as a function of frequency in two separate subplots and is less commonly used for electrochemical analysis. The Nyquist plot is a scatter plot of the imaginary component versus the real component of _Z_ ( _ω_ ) for a range of values of _ω_ . This plot is more common in electrochemical analysis, and the shape of the plot also implies general properties of the system. For example, a parallel RC circuit (Figure 4d) gives rise to the classic semicircular Nyquist plot (Figure 4c). 

Insight into the underlying system is also gained by fitting the impedance to an equivalent electric circuit model consisting of resistances, capacitors, and constant phase elements. For biosensing applications, the most widely used equivalent circuit model is the Randles circuit shown in Figure 4d. This model consists of a solution resistance ( _R_ s) in series with a parallel combination of a double-layer capacitance ( _C_ dl), a charge transfer resistance ( _R_ ct), and a Warburg impedance ( _W_ ). 

with higher resistances, higher surface area electrodes are preferred due to a lower resulting current density. Electrodes with higher resistance require a higher applied potential due to an ohmic drop, which may result in a temperature increase and damage to the biorecognition element. Common electrode materials include carbon, graphite, glassy carbon, gold, and platinum. Glassy carbon, a fullerene allotrope of carbon, is the most commonly used carbon-based electrode and has a high thermal stability, high conductivity, and low electrical resistance. Graphite is more conductive, less chemically inert, and less expensive as an alternative. Gold electrodes are highly conductivity- and corrosion-resistant and are readily functionalized using thiolated molecules. Finally, platinum electrodes are highly inert and highly corrosion-resistant and are known for their catalytic activity. An electrode is either heavily or minimally involved in electron transfer (Figure 5).[28] In the 

The conversion of an electroactive analyte to an output current is modeled through the combination of the chargetransfer resistance and Warburg impedance. The chargetransfer resistance describes the resistance to electron transfer through the relevant redox reactions. The Warburg impedance, in turn, models the diffusion process through a complex function whose magnitude is dominant in the low-frequency region:[21] 

**==> picture [42 x 24] intentionally omitted <==**

EIS biosensors are categorized into faradaic and nonfaradaic sensors.[22] Faradaic sensors use redox-active analytes in solution. Impedance changes correlate to differences in the concentration of analyte present, reflected in the fitted values of the charge-transfer resistance and Warburg elements.[23] In addition, the surface binding of nonconductive molecules blocks electron transfer, increasing _R_ ct, whereas conductive molecules lead to a decrease in _R_ ct. On the contrary, nonfaradaic sensors require no redox molecules, but instead rely on the charging and discharging of the dielectric layer on the electrode surface. The _C_ dl is a parameter that characterizes the reaction occurring at the electrode/electrolyte interface. The binding of molecules usually leads to a decrease in the level of _C_ dl. Electrochemical impedance spectroscopy has been widely used to detect enzymatic activity,[24] DNA hybridization,[25] antibody−antigen recognition,[26] and binding affinity.[27] 

## ■ **[COMPONENTS][OF][ELECTROCHEMICAL] BIOSENSORS** 

**Electrodes.** The electrode choice dramatically affects the performance of the electrochemical biosensor. The kinetics, thermodynamics, mechanism of electron transfer, electrode separation distance, shape, and size, which determine the surface area in contact with bulk solution, field homogeneity, and resulting current density all influence performance. When choosing an electrode, it should ideally be inexpensive, recyclable/degradable, and temperature-, pressure-, and solvent-stable, as well as corrosion-resistant. Depending on the use case, short- or long-term biocompatibility is also a key design requirements. In the case of organic solvent systems 

Figure 5. Electrode involvement in electrochemical reactions. (a) Double layer effects. (b) Electrode material heavily involved in innersphere electron transfer. (c) Electrode material minimally involved in outer-sphere electron transfer. 

presence of an electrical potential across an electrode in an electrolyte solution, a double layer forms (Figure 5a). The double layer consists of two regions, the inner Helmholtz plane (IHP) and the outer Helmholtz plane (OHP). The IHP consists of a compact layer of electrolyte solvent molecules in the orientation of the electric field. The OHP passes through the center of the solvated ions of the electrolyte solution outside the IHP. A diffusion layer is formed as solvated ions are concentrated at the surface of the electrode in comparison to the bulk solution. Electrodes are heavily involved in innersphere electron transfer, as in the case of electron exchange with a chloride ion on the surface of an electrode and an iron metal ion (Figure 5b). 

When electrodes are intimately involved in electron transfer, the material choice substantially dictates biosensor signal. Electron transfer in inner spheres is connected by a chemical bridge with strong electronic coupling. Alternatively, the electrode remains inert and acts as a source or electron sink for the substrate some distance from its surface participating in outer-sphere electron transfer (Figure 5c). In this instance, electron transfer occurs between species which do not bond with one another and remain separate throughout the whole process.[29] A practical example is the electron transfer between the electrode and ferri/ferrocyanide. 

Potential, in electrochemistry, refers to the electrical potential difference (voltage) or energy required to bring charge from one point to another. Potential also determines how likely a species will gain or lose an electron and the 

**E** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

direction and rate of electron transfer. With respect to the Nernst equation, it determines the concentrations of electroactive species on the surfaces of electrodes. Standard electrode potentials are defined as standard conditions (1 M concentration of species, 1 atm pressure, and 25 °C temperature) and the relative tendency of a half-reaction to occur at an electrode. The standard electrode potential tables are useful to reference for predicting the flow of electrons in an electrochemical system. 

The potential above which a reaction is favored thermodynamically is the overpotential ( _η_ ). The observed overpotential is the sum of overpotentials for each step of a reaction, including adsorption, charge-transfer, desorption, and the three modes of mass-transport. A low overpotential ensures that a reaction proceeds more efficiently and with better selectivity against undesired side reactions. The mechanism of electrode transfer and thus choice of electrode material is the largest contributor to the overpotential, providing one more reason for careful selection. 

Manufacturing advances led to the introduction of ultramicro and nanoelectrodes which have drastically improved biosensor sensitivity.[30] As the name implies, these electrodes are fabricated at extremely small dimensions on the order of micro- or nanometers. Ultramicroelectrodes (UMEs) are defined as having one dimension smaller than the thickness of the analyte diffusion layer (typically 20−25 _μ_ m).[31] Fabrication techniques allow for numerous geometric designs, such as rectangular or circular shapes or interdigitated electrodes. The advantage is a high surface area to volume ratio, allowing for enhanced sensitivity. Due to the small distance between electrodes, there is a small voltage drop and thus distortion at the electrode−solution interface, allowing for the use of two-electrode configurations instead of conventional three-electrode systems. Furthermore, these small features demonstrate a greatly reduced capacitance and thus a decreased RC time constant, allowing for faster measurements. 

Finally, even though there are numerous examples of electrode choices in the literature, electrode processes are highly complex with different manufacturing steps and slight compositional changes affecting performance. Often testing different electrodes as well as the same type of electrode produced by different companies is critical to identifying the optimal electrode as manufacturing methods influence final performance.[32] 

**Biorecognition Elements and How to Choose Them.** 

A biorecognition element is a critical part of a biosensor as it uniquely (ideally) identifies and selectively binds a target analyte and then relays that binding event to a transducer to produce a measurable signal. Biorecognition elements broadly fall into the categories of natural (e.g., antibodies, enzymes), synthetic (e.g., molecularly imprinted polymer (MIP)), and pseudo natural (e.g., aptamers).[33][,][34] Naturally occurring biorecognition elements consist of biologically derived constructs that rely on naturally evolved physiological interactions to achieve analyte specificity, whereas synthetic biorecognition elements include artificially engineered elements that mimic naturally evolved interactions. 

Researchers choose biorecognition elements based on the intended application and the nature of the analyte. Characteristics to consider when building a biosensor include sensitivity, selectivity, specificity, reproducibility, and reusability. _Sensitivity_ determines how the biosensor responds to small changes in the analyte concentration, whereas _selectivity_ defines the ability of 

the biosensor to differentiate different analytes in a mixture from each other. _Specificity_ refers to the identification of one particular target analyte without recognition of any other analytes. _Reproducibility_ indicates the ease of fabrication of identical multiple sensors to provide consistent sensor responses, and _reusability_ describes the ability to reuse a single sensor multiple times. See the data analysis and interpretation section for further details, including significance and equations to calculate them. The most commonly used biorecognition elements include antibodies, enzymes, nucleic acids, aptamers, transcription factors, and molecularly imprinted polymers. 

_Antibodies_ are 3D protein structures with an approximate molecular weight of ≈150 kDa and comprise light and heavy chain regions linked by disulfide bonds. They bind bioanalytes tightly (typically with binding constants in the low micromolar to nanomolar range) with high specificity and with binding domains located on the arms of its Y-shaped conformation (or the variable domain) of the light and heavy chains. Often antibodies are immobilized on a surface via covalent linkage and undergo a binding event with an analyte or the analyte and a second antibody to form an antibody−analyte or antibody− analyte−antibody immunocomplex, respectively. The limitations of antibody-based biosensors include antibody production which involves costly isolation and purification steps, identifying multiple antibodies for the same target with different epitope binding sites, and requiring controlled orientation of antibodies to facilitate binding.[35][,][36] 

_Enzymes_ possess binding cavities within or on the surface of their 3D structure and capture their respective bioanalytes with high specificity using hydrogen bonds, electrostatics, and other noncovalent interactions. Enzymes catalytically convert the analytes into a measurable product, and one uses chronoamperometry techniques, for example, to detect the products as described in the section above. This high specificity of enzymes stems from the biologically evolved role they play in physiological processes. However, there are certain limitations for amperometric enzymatic sensors that include signal reduction from fouling agents present in the sample matrix, rapid loss of enzyme activity from electrode/sample interactions that shorten shelf life, and challenges with enzyme immobilization.[37] 

_Nucleic acids_ take advantage of complementary binding motifs to achieve bioanalyte specificity. On identifying a target DNA sequence, it is reasonably straightforward to artificially design a complementary capture DNA strand and immobilize it on the sensor surface acting as a biorecognition element. Recent advances include the use of locked nucleic acids and peptide nucleic acids to solve the poor selectivity issues of nucleic acids as the inherent negative charge may result in nonspecific electrostatic interactions.[38] The other limitations of DNA based sensors include incorporating biochemical labeling methods for signal transduction, applicable only to nucleic acids or transcription factor targets, and potential need for amplification strategies (like PCR)/sample processing before detection.[39] 

_Aptamers_[40] are single-stranded oligonucleotides that undergo conformational change on target binding. Aptamers respond to a wide range of targets including small molecules, metal ions, proteins, whole cells, etc. Systematic evolution of ligands by exponential enrichment (SELEX) is a process to select aptamers that entails screening a library of oligonucleotides to choose an aptamer sequence that responds to the analyte of interest. Chemical synthesis of aptamers involves a 

**F** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

Figure 6. Different groups of analytes and biorecognition elements are used to detect them. 

well-defined, highly reproducible process, and is amenable to post-translational modifications thus simplifies the manufacturing process.[40] The limitations of aptamer-based sensors are the tedious SELEX discovery process, misfolding due to possible secondary structures, and the binding affinity dependence on pH and composition of the media.[40] 

_Transcription factors_ (TFs) are a new class of biorecognition elements whereby a differential binding affinity between the TF and the DNA exhibits a dose-dependent response to analyte addition. Typical analytes are small molecules, where, for example, the binding of the analyte results in a separation of the TF and DNA, leading to a readout in the form of an electrochemical output. Some of the limitations include response to structurally similar ligands, and hence, directed evolution and other microbiology techniques are applied to fine-tune the affinity of the TF.[41] 

_Molecularly imprinted polymers_ (MIPs) are synthetic biorecognition elements prepared from a template polymer matrix that achieves analyte specificity using noncovalent bonding, electrostatic, or size inclusion/exclusion. MIPs respond to a particular target analyte alone as it effectively forms synthetic recognition patterns between an analyte and polymer matrix.[42][,][43] Fabrication and design of MIPs in situ around the analyte can avoid the need for any biochemical identification process. The fundamental aspect of MIP fabrication involves the creation of a pore for an analyte in a polymer matrix. For example, polymerization of a monomer in the presence of the target analyte and after fabrication, the analyte is removed via elution to create a custom binding site for the target analyte. The analyte binding to MIP is either covalent or noncovalent. Advanced fabrication methods also involve techniques such as seeding, precipitation, and emulsion polymerization.[44] There is comprehensive literature available on MIP synthesis.[45][−][47] Along with the synthesis method, efficient removal of the template after fabrication is required to create a sensitive and specific biosensor as the number of cavities dictates binding sites for improved sensitivity and shape of the cavity for specificity. Chemical and electrochemical strategies are commonly employed for template removal.[48] The disadvantages of this system include a time- 

consuming, complicated manufacturing process,[49] poor selectivity of the binding sites as interferents may enter the binding sites and provide false readings,[48][,][50] and lower “binding” affinities in comparison to antibodies and aptamers. 

Biosensor sensitivity is critical for monitoring small variations in analyte concentrations, especially for early disease diagnosis and treatment intervention. A critical factor that affects the sensitivity is the number of binding sites available per surface area. High loading density is possible with aptamers (∼1−2 nm in size) and nucleic acids, as they are smaller in size compared to larger antibodies (∼10−15 nm). Apart from surface loading, steric hindrances from adjacent molecules especially in antibodies may result in a conformational change alteration of the binding pocket, lowering the binding affinity. Recently, nanobodies[51][,][52] (a single chain format of an antibody) and locked nucleic acids[53] (LNA) are being investigated to mitigate the above challenges. But it is also important to note that antibodies can achieve picomolar binding affinities, whereas aptamer biorecognition elements typically exhibit nanomolar affinities. Thus, it is a compromise between surface loading and binding affinities that determines the sensitivity of the biosensor. In contrast to aptamers and antibodies which are covalently linked to a surface for analyte capture, enzymes are embedded in a matrix, and MIPs are a matrix, adding variables such as thickness/depth and density into the equation of biosensor output. 

The _regeneration and reusability_ process of a biosensor involves unraveling the analyte-biorecognition element complex while keeping the biorecognition element intact. For reusability of biosensors, enzymatic biosensors are often used as they undergo minimal consumption or alteration during the catalytic reactions. Enzymatic biosensors when used at an optimum pH and temperature produce highly _stable_ and _reproducible_ sensors. Lower binding affinities (nanomolar levels) of TFs to the analyte reagents also enable regeneration of biosensors in comparison to antibody-based (picomolar) biosensors. The schematic in Figure 6 shows the different target analytes of interest and the biorecognition elements to choose from based on your specifications. 

**G** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

a **ACS Sensors pubs.acs.org/acssensors** ~~e~~ Review 8§8§=6|—l| 

Figure 7. Designs were used to build a nucleic acid sensor. Examples of nucleic acid sensors are shown: (a) stem-loop configuration, (b) linear probe configuration, (c) Cas-based sensor, (d) two-piece DNA architecture, (e) DNA tetrahedron nanostructure, and (f) unlabeled system. 

## ■ **[ELECTRODE]**[−] **[MEDIATOR][INTERACTIONS][AND] SIGNAL TRANSDUCTION** 

The following section details the role of the various biosensor components in generating an electrochemical response and thereby an output signal. Before we discuss the different reactions that result in an electrochemical response, it is pertinent to understand the role of the mediators. Mediators are intermediary compounds that aid in shuttling electrons between the biorecognition element and the transducer. Mediators are either organic-based (methylene blue, Prussian blue, quinones, etc.) or metal-ion based (ferrocene, ferrocyanide, ruthenium, etc.).[54][,][55] The organic-based mediators suffer from solubility and pH-dependence of redox potentials, and metal-based suffer from redox potential tunability issues. There are several attributes that one must be aware of when choosing the appropriate mediator for their application. Typically, mediators are stable and do not participate in side reactions during electron transfer, are unaffected by sample pH, exhibit fast and reversible heterogeneous kinetics, possess a lower redox potential(s) than active interferents, and provide an appropriate potential gradient for efficient transfer of electrons.[56] The mediators, the biorecognition element, and the electrode in turn participate in signal transduction to produce an electrochemical response. The signal transduction broadly falls into three categories: direct oxidation/reduction, indirect oxidation/reduction, and amplification reactions. 

_Direct oxidation/reduction_ . The goal of electrochemical biosensors is to determine the concentration, activity, or presence of an analyte of interest. If the analyte of interest is redox-active, or, in other words, exchanges electrons with the electrode surface on application of a potential, that is sufficient to cause oxidation or reduction of the molecule, a current output is recorded. This approach possesses the drawback that other redox-active substances in the sample may interfere with the current output. Hence this method may not be selective. 

_Indirect oxidation/reduction of redox mediators_ . Electrochemical biosensors capture interaction/binding events between analytes in a sample and biomolecules on electrode surfaces. These interactions involve binding, hybridization, etc. Since these events are not themselves redox-active, common practice is to add redox-active moieties in solution, to immobilize redox-active moieties on the electrode surface, or to conjugate them to the biorecognition element. Some of the scenarios include: 1) a binding or hybridization event changes the path or rate of electron transfer, 2) conformational changes upon binding bring tethered redox moieties closer or father away from the electrode, and 3) a binding event contributes to changes in resistance to electron flow in the case of redox molecules in solution. 

_Enzymatic reaction/amplification_ . Enzymes as biorecognition elements or amplification units attached to a biorecognition element amplify a redox reaction, during which they consume their substrate to produce a redox-active species that is shuttled to the electrode surface. Commonly used enzymes for amplification are highly active enzymes with high turnover rates such as HRP (horseradish peroxidase) and GOx (glucose oxidase), to name a few. 

## ■ **[ELECTROCHEMICAL][SENSOR][DESIGNS][FOR] DIFFERENT TYPES OF ANALYTES** 

**Nucleic Acid Detection.** There has been substantial interest in the rapid and sensitive detection of nucleic acids since the development of the first microarrays. Electrochemical biosensors avoid the tedious route of time-consuming sequencing and amplification steps. The central theme of nucleic acid detection is a hybridization event that occurs when a target DNA recognizes a captured DNA strand and produces a change in the electrochemical output. One variant of this technique is very sensitive and detects a single mismatch of bases in the DNA strands as a result of changes in charge transfer through the DNA strands.[57] Several different DNA 

**H** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

a **ACS Sensors pubs.acs.org/acssensors** ~~e~~ Review = 8§|— ~~|~~ 

Figure 8. Designs to build a protein biosensor. Design of protein sensors include: (a) aptamer sensors, (b) protein scaffold sensors, (c) DNAdirected sensors, and (d) immunosensors. 

biosensor architectures are described in the literature, and this review summarizes the most common ones. 

_Design of Nucleic Acid-Based Sensors._ Nucleic acid detection is broadly used to assess a spectrum of disease states from viral diseases to cancers and genetic disorders.[58] High sensitivity is critical for nucleic acid detection, and affinities ranging from picomolar down to femtomolar levels are highly desirable. Advances in the field of electrochemical biosensors are close to achieving such low femtomolar levels of detection while maintaining selectivity and specificity.[59] Below, we highlight some of the common designs of biosensors based on nucleic acids (Figure 7a−e). The sensors broadly fall into two categories: Signal-OFF Sensors and Signal-ON sensors. In the case of Signal-OFF sensors, the electrochemical output signal decreases on identification of a target analyte. When the concentration of the analyte is higher, the signal decreases more dramatically, and this change in output signal correlates to the analyte concentration. Such Signal-OFF sensors are prone to false-positive results. On the other hand, Signal-ON sensors increase the electrochemical output signal in the presence of target analyte. The ON sensors, especially with structure-switching sensors (for example, aptamers tagged with redox moieties) produce a higher background signal (as the redox moieties are always present near the electrode surface and the output signal depends on target induced structural changes of the aptamer) and reduce the overall sensitivity of the biosensors, but avoid any false-positive results.[60] 

Figure 7a−e shows the detection of nucleic acids by redoxactive probes attached to the capture strand or attached to a reporter strand. In these labeled systems, the presence of target analyte causes binding-induced structural changes, bringing the redox-active molecule closer (or farther away) from the electrode surface, and generates a change in electrochemical output. One of the commonly used redox probes for labeling is methylene blue due to its exceptional stability with repeated electrochemical scans.[61] Figure 7a−b show the stem loop and linear probe configuration of nucleic acid based sensors, respectively. In the stem-loop configuration (Figure 7a), the absence of a target enables the attached redox tag to be in close proximity to the electrode surface. Upon target hybridization of the perfectly matched DNA strand, the resulting doublestranded DNA configuration forces the redox tag away from 

the electrode surface, impedes electron transfer, and leads to reduction in redox current. Whereas in the linear probe configuration, (Figure 7b) the signaling arises from the redox labeled probe and as the flexibility of the redox probe decreases upon target duplex formation, there is significant decrease in output current.[62] 

Figure 7c shows a design of a Cas-based sensor these gene editing systems offer high specificity and sensitivity without any need for nucleic acid amplification strategies.[63][,][64] The redox probe leaves the surface after Cas cleavage of the reporter strand in the presence of target DNA. In recent years, DNA nanostructures have attracted significant attention due to their programmability. Figure 7d describes a “two-piece” DNA architecture where two DNA strands are connected via a polyethylene glycol (PEG) spacer and the probe strand tethered to a redox molecule. This specific architecture exploits a conformational change that occurs on target binding and acts as an ON-Sensor that brings the redox molecule closer to the electrode surface.[65] A DNA tetrahedron nanostructure (Figure 7e), composed of six double stranded edges and four vertexes, where a strand on the vertex captures the target and reporter nucleic acid with a redox probe generating a current signal increase.[66][−][68] In an unlabeled system (Figure 7f), redox probes in solution capture resistance changes (by impedance spectroscopy) or intercalate between nucleic acid strands to generate an output signal. Researchers frequently use a mixture of ferrocyanide/ferricyanide molecules in solution to capture impedance changes in a system, but one should be aware of the potential buffer and etching effects on electrode surfaces.[69][−][71] In order to monitor DNA hybridization processes, intercalators such as hexamine ruthenium chloride intercalate between DNA strands and alter the electron transfer through DNA.[72][,][73] In the case of labeled systems, there are several reports of enzyme-labeled probes (HRP, GOx) that provide signal amplification and better sensitivity, but require additional reagents for detection (substrate for the enzyme).[74][−][76] 

**Protein Detection.** There is an ever-increasing demand for protein-based biosensors for monitoring protein concentrations, especially the proteins associated with early detection of cancer, myocardial regulation, and infectious disease antigens, to name a few. The existing clinical-based approaches (enzyme-linked immunosorbent assay (ELISA), blots, immu- 

**I** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

(ee **ACS Sensors pubs.acs.org/acssensors** ~~e~~ Review 

Figure 9. Designs to build a small molecule biosensor. Design of small biosensors include (a) labeled aptamers, (b) enzymatic sensors, (c) transcription factor-based sensors, and (d) direct electrochemical detection. 

nohistochemical stains, etc.) suffer from one or more of the following disadvantages: time-consuming, requires experienced personnel, and extensive reagents.[77] In fact, one positive consequence of the COVID-19 pandemic is the greater public acceptance of personal testing, resulting in a shift in focus to technologies that are portable, facile, and easily scalable. There are many protein biomarkers of importance for detection including cancer biomarkers (osteopontin, troponin, her-2, and prostate specific antigen, to name a few),[78][,][79] transcription factors, antigens, and antibodies associated with infectious disease detection (Flu, COVID, common cold). Typically, for protein detection, one uses antibodies or aptamers on electrode surfaces as biorecognition elements and tracks changes in electron-transfer rates due to the binding event or an enzymatic amplification reaction. For detection of transcription factors, one utilizes their innate binding affinity to DNA strands when the latter acts as a capture reagent. 

Here we list four different protein detection designs used for the development of electrochemical biosensors, and these designs include both Signal-OFF and Signal-ON systems (Figure 8). Aptamers, labeled with a redox molecule, switch their structure (DNA scaffold) upon protein binding, bringing the redox molecule closer to the electrode surface and increasing the efficiency of electron transfer (Figure 8 a).[80][,][81] For the detection of transcription factors, the DNA molecule acts as a capture strand. TF binding changes the charge transfer rate through redox-probe labeled DNA and a bulky TF, increasing the resistance to electron flow.[82][,][83] There are also reports of protein scaffold sensors (Figure 8b) where a smallermolecular-weight protein (typically a peptide) labeled with a redox reporter binds the target protein, reducing the electrontransfer efficiency from the reporter molecule to the electrode.[84] Note, in the case of protein scaffold sensors, peptides act as capture molecules, and typically no larger-sized antibodies or proteins are used as they dramatically increase steric hindrance and decrease the baseline current to a level where target binding currents cannot be discerned. DNAdirected immobilization of protein/aptamers for detection of protein biomarkers rely on charge transfer through DNA (Figure 8c).[85][−][87] Alternatively, to improve sensitivity, researchers use signal amplification strategies such as an antibody with an enzyme reporter label (Figure 8 d). For 

example, antibodies with their picomolar binding affinities to their corresponding antigen are conjugated to enzymes for signal amplification, yielding a sandwich style electrochemical ELISA. This approach improves the limit of detection for the analyte detection. 

**Small Molecule Detection.** The small molecule analytes detected by electrochemical biosensors broadly fall into the categories of metabolites, drugs, hormones, and neurotransmitters. The first true origin of the biosensor is the Clark electrode for oxygen detection,[88] followed by Clark’s detection of glucose by an amperometric enzyme. The commercialization of biosensors started with the development of glucometers a device for the measurement of blood glucose, a metabolite of energy production in our body. Since then, technology advancements progressed from single-point blood measurement to continuous noninvasive measurement of glucose from various bodily analytes (sweat, tears, interstitial fluid, etc.) as well as sensing other metabolites such as lactate, uric acid, etc. 

Small molecules are detected either enzymatically or nonenzymatically. The enzymatic method is highly commercialized (e.g., glucometer) and utilizes enzymes that react with the analyte of interest to produce products or byproducts that are electrochemically measured. For example, in glucometers, the analyte glucose reacts with a highly active enzyme, glucose oxidase, to produce hydrogen peroxide, which is electrochemically detected. The detection of lactate is performed in a similar manner. Whereas a nonenzymatic method, for example, relies on the analyte itself being electrochemically active for example, cholesterol, dopamine, and uric acid. However, one runs the risk of interference from other electrochemically active substances present in solution. Several groups report the use of nanomaterial-based electrode surfaces to alleviate this issue.[89][−][91] For example, platinum nanoparticles electrocatalyze hydrogen peroxide without the need of a mediator,[92] and gold nanosurfaces oxidize glucose.[93] Additional nonenzymatic designs include aptamer- or other protein-based strategies where a conformational change occurs upon analyte binding, which is transmitted to an electrochemical signal.[94][,][95] 

As mentioned above, small molecule targets include simple inorganic ions to small organic compounds such as antibiotics, neurotransmitters, drugs, vitamins, etc. The common sensing 

**J** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

designs are shown in Figure 9. Aptamers or enzymatic routes for small molecule detection are highly specific, in comparison to the direct redox reaction of an analyte on the electrode surfaces. In one configuration, aptamers are labeled with redox probes for the detection of small molecules, and the proximity of the probe to the electrode surface change as the aptamer configuration changes as a result of binding of the small molecule (Figure 9a). Whereas enzymatic sensing (Figure 9b) relies on products or byproducts of an enzyme reaction (e.g., H2O2) for subsequent electrochemical detection. Recently, we reported the potential of transcription factors as a transduction methodology for small molecule sensing utilizing the impedance changes that occur as a result of protein unbinding from its cognate DNA sequence as a result of analyte (progesterone) binding (Figure 9c).[83] Alternatively, for analyte binding, direct detection (Figure 9d) on modified electrodes is also a convenient and easy-to-develop method, but one should be aware of the potential effect of interferents on the output signal based on the applied potential.[89] 

## ■ **[OPTIMIZATION][STRATEGIES][FOR] ELECTROCHEMICAL BIOSENSORS** 

**Optimization of Nucleic Acid-Based Sensors.** To improve the performance of nucleic acid−based sensors, one must consider optimization methods such as immobilization strategies, electrode surface modifications, detection strategies, and overall design (Figure 10). Immobilization of capture 

nucleic acids with no directionality. One can use a positively charged polymeric film composed of chitosan, polypyrrole, polyaniline, etc., to serve as DNA anchors and improve the stability by application of a positive electrochemical potential.[96][−][98] But in this mode of immobilization, the DNA layer is prone to desorption under the influence of pH, buffer ionic strength, and temperature as well as result in nonspecific attachment of DNA probe. Another strategy for noncovalent interaction relies on the _biotin_ − _streptavidin_ interaction, wherein biotin, a small molecule interacts with tetrameric protein (streptavidin) with four binding pockets with a very high binding affinity ( _K_ d = 10[−][14] M). This binding is quite stable and resistant to temperature, pH, and solvent effects typically found in diagnostic assays.[99] Whereas covalent bonding of the DNA probe to a metal surface electrode increases stability and prevents desorption of the DNA monolayer. In the _covalent bonding_ technique, for example, the DNA probe with a thiol or amine at its 3′ or 5′ end covalently attaches to the electrode surface. Thiolated DNA probes self-assemble onto gold electrodes to form a self-assembled monolayer due to a strong affinity between the thiol group and gold surface. This particular method finds application in the construction of various sensors due to its strong binding strength, easy preparation, and highly stable monolayer formation. However, the thiol−gold bond is not stable over extended periods in an aqueous solution. The amine-terminated probes covalently react with several functional groups such as carboxyl, aldehyde, epoxy, and isothiocyanate present on a postfunctionalized electrode surface. 

After selection of a desirable immobilization strategy, one must consider the properties of the layer on the electrode surface such as probe density/surface coverage and blocking to minimize nonspecific adsorption of molecules/biomacromolecules in the analyte solution. The intrinsic sensitivity of the sensor depends strongly on the surface architecture along with probe density, target length of the capture strand, and electrochemical surface area of the biosensor. A simplified Cottrell equation gives the _probe density_ on the electrode surface or the number of molecules immobilized per cm[2] : 

Figure 10. Optimization to consider while building a DNA-based biosensor. 

moieties on the working electrode is a crucial step in the construction of a biosensor (Figure 11). A good immobilization technique promotes high reactivity and correct orientation toward the analyte molecules (complementary DNA strand, proteins, small molecule, etc.). _Adsorption_ is a simple technique that relies on the electrostatic adsorption of negatively charged 

Figure 11. DNA immobilization strategies. 

**==> picture [66 x 48] intentionally omitted <==**

ΓRu: surface coverage of redox molecule, _Q_ : Integrated current, _A_ : Area of electrode (cm[2] ), _F_ : Faraday constant (C/ mol), _n_ : number of electrons in the redox reaction, _z_ : charge of redox molecule, _N_ A: Avogadro’s number; _m_ : number of nucleotides on the DNA strand. 

It is pertinent to study the effects of surface coverage on the signal output value, and choose an optimum probe density.[100] Binding efficiency of the target decreases with increasing coverage/probe density on the electrode surface due to steric crowding/hindrance and prevention of target binding. Whereas very low surface coverage enables binding but leads to DNA folding, nonspecific adsorption on the electrode surface, and alternate electron transfer events, which reduces the performance of the sensor.[101] Blocking agents or _anti-fouling agents_ serve to prevent nonspecific adsorption of sample constituents and ionic diffusion through receptor layer defects. The most commonly used blocking agent is mercaptohexanol (MCH) that facilitates a 90° orientation of DNA strands and thereby 

**K** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

Figure 12. Optimizations to consider while building an immunosensor. 

favors a configuration for subsequent hybridization. There are also reports of other blocking agents in the literature such as mercaptoethanol, cysteamine hydrochloride, and benzenedithiol, to name a few.[102] In fact, blocking agents are usually underappreciated in an academic setting, but industry experts are aware that reducing unwanted adsorption is key to a low background signal and device performance. 

The next critical step involves the design of detection, whether _label-free_ or _labeling_ with redox mediators/enzymes/ nanoparticles. Most of the label-free systems involve monitoring the changes in the redox reaction of DNA bases adenine and guanine upon hybridization. Whereas the labeled systems involve redox mediators[94] or enzymes in the configuration given in Figure 7a−e. There are also reports of DNA strands labeled with nanoparticles and ones monitoring their redox properties.[102] 

**Optimization of Immunosensors.** An electrochemical immunosensor is a type of sensor that employs the binding event of an antibody and a target molecule that results in an electrical signal change. A sandwich type of immunoassay is a common format in which the target of interest forms a sandwich between a capture reagent and a detection reagent. Typically, a detection reagent with a redox or enzyme label is responsible for an electrochemical output. To improve the performance of an immunosensor, one relies on several strategies starting from the working electrode of the biosensor (Figure 12). The _working electrode_ is the area where a capture event and the reaction that follows take place, and the final output of the sensor is directly proportional to the working electrode area. Therefore, choosing an appropriate electrode and the corresponding surface modifications directly impacts the sensitivity of the sensor. There are several reports of nanomaterials as an alternative to conventional screen-printed electrodes to enhance electric signals. Nanomaterials possess a large _surface area_ , which supports enhanced loading capacity of the capture reagent as well as mass transport of reaction molecules, leading to signal amplification. Some of the widely used nanomaterials for working electrodes include graphene,[99] carbon nanotubes,[99] nanowires,[103][,][104] and nanoparticles.[105][−][107] 

It is also critical to account for the effect of _surface coverage_ of the capture reagent on the working electrode surface, similar to nucleic acid-based sensors. In the case of antibody sensors, it is important to note that overcrowding of bigger antibody molecules results in steric hindrance and prevents the binding of target molecules. Similar to nucleic acid immobilization on a working electrode, immobilization strategies must be adapted for efficient immobilization. Reports suggest that stable conjugation methods prevent hydrophobic interaction-induced 

denaturation of antibodies and provide a higher active number of antibody molecules available for binding improving sensitivity, as well as proper antibody orientation, increasing the dynamic range of assays.[108] 

The _concentration_ of the capture and detection reagents significantly affects the biosensor sensitivity. Careful consideration must be given when choosing the concentration of these reagents, and one must account for the binding affinities of the target analytes to the capture (and/or detection) reagents. Binding constants dictate the binding affinities of the analyte to the capture reagent for example, a lower binding constant indicates strong affinity, and a higher constant indicates weaker affinity. Upon lowering the concentration of these capture reagents in the assay to that approaching or below binding constants, complex formation diminishes and detection is challenging. Similarly, very high concentrations result in the target molecule individually binding to capture and detection molecules instead of forming a sandwich complex thus limiting performance. To highlight this balance, a 5-fold improvement to the limits of detection and cross-reactivity of immunoassays for antibiotic detection occurs by decreasing the concentrations of reagents, without an overall substantial decrease in detected signal.[109] Also, _binding affinities_ of these reagents before and after labeling with electroactive species, especially excessive labeling, will significantly alter the target binding affinity. When building a sensor, it is informative to study the kinetics of binding and optimize the incubation time required for binding and for reaching equilibrium. In the case of antibodies with enzyme labels, it is critical to study the enzyme activity and to study the exact composition of substrate reagents plus the cofactor needed to attain maximum enzyme activity as the limit of detection of the sensor ultimately relies on enzyme amplification properties. One may notice that increasing substrate concentrations increases the rate of a reaction, until it reaches a substrate concentration where you observe the maximum rate of reaction ( _V_ max), and no further increase. Thus, it is important to perform the immunoassays at these high substrate concentrations. It is also critical to optimize wash steps as any remaining detection reagents not part of the analyte complex increase the signal and give rise to false positives. Wash buffers include detergents,[110] which can introduce electrode fouling, hence one must optimize detergent/wash buffer concentrations so they do not significantly change the working electrode surface and alter the electrochemical output therein. 

There are reports of using multiple electroactive species or enzymes per antibody molecule to boost the output signal. One can link several enzyme molecules together on a polymer 

**L** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

Figure 13. Optimizations to consider while building an enzyme-based sensor. 

skeleton, namely, dextran, and further link the dextran to the detection antibody. This allowed an increase in the _degree of labeling_ or many enzyme molecules per binding event to participate in signal enhancement, thus improving the limit of detection of the analyte present in low concentrations.[111][,][112] Although _enzyme_ -based approaches offer signal amplification, incubation time of the enzyme reagent with substrate also significantly impacts the level of detectable signals and therefore the limit of detection (LOD) of the sensor. Nanomaterials with very high surface areas act as a _nanocarrier_ to increase the loading capacity of the electroactive tracer molecules (enzymes or redox molecules). Some of the widely used nanomaterials include gold nanoparticles, magnetic beads, graphene oxide,[113] and carbon nanotubes, to name a few.[114][,][115] Alternatively, some nanomaterials, specifically metal nanoparticles, act as electroactive _nanotracers_ in construction of electrochemical immunosensors. For example, nanoparticles linked to the detection antibody produce an electrochemical signal based on the redox state of particles.[116] 

**Optimization of Enzymatic Sensors.** To successfully engineer an enzyme-based biosensor, both the performance of the enzyme and electron transfer at the electrode surface are critical.[117] As the number of enzymes sourced from nature grows, methods for their optimization are becoming increasingly important. Enzymatic biosensors are classified into 3 classes or generations. The first generation are those where the product of enzymatic reaction diffuses to an electrode surface and generates an electrochemical response. Second-generation biosensors utilize mediators as electron carriers to transport electrons from the enzyme to the electrode surface to generate a response. The most advanced third-generation biosensors directly capture electron transfer between the enzyme and the electrode. We refer the reader to several reviews that discuss the generations of these biosensors in further detail.[5][,][118][−][120] 

Newly discovered enzymes can be broad-spectrum to several analytes, kinetically slow, able to perform more than one type 

of reaction (e.g., oxidase and dehydrogenase), insoluble when mixed with immobilization polymers, and incompatible with abiotic electrodes or toxic electron mediators. Furthermore, the catalytic core, which is essential to substrate turnover in enzymes and electron transfer, may be buried deep within the enzyme in an insulated polypeptide shell, difficult to access by either mediators for building second-generation biosensors or electrodes themselves for building third-generation biosensors.[121][,][122] In order to build enhanced biosensors, wellestablished protein engineering techniques such as rational design, directed evolution, and a combination of the two are employed to optimize electron transfer to the electrode (Figure 13).[123][,][124] Rational design of enzymes improves enzyme activity, stability, and selectivity, alters redox potential, improves electron transfer, and allows for oriented immobilization on electrodes. 

For example, to optimize third-generation biosensors, one can employ a _protein fusion_ strategy. Electron transfer in this generation of biosensors usually moves from a FAD (flavin adenine dinucleotide) or PQQ (pyrroloquinoline quinone) cofactor in a dehydrogenase to an internal mediator such as a heme or a Fe−S cluster and ultimately to the electrode.[122][−][126] For example, Algov et al. describe the fusion of the catalytic domain of the _Burkholderia cepacia_ FAD−glucose dehydrogenase (GDH) with a c-type cytochrome domain MCR-2 from a MamP protein which increases catalytic activity 5-fold.[127] An alternate approach involves covalently conjugating electrochemical mediators to electron transfer enzymes ( _mediator fusion_ ). Suzuki et al. report the covalent linking of an aminereactive phenazine ethosulfate at a mutated lysine residue of _Aspergillus niger_ GOx. This mutant exhibits direct electron transfer as a result and lowered interference.[128] A final fusion strategy involves the addition of an _allosteric domain_ that imparts ligand-specific catalysis. In pioneering work by Alexandrov et al, they report a calcium-specific biosensor based on the fusion of a calmodulin binding domain to a PQQGDH.[129] Further expansion on the idea includes using a two- 

**M** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

Figure 14. Analytical parameters. (a) Defining limit of detection (LoD) and limit of quantitation (LoQ). (b) Calibration curve showing linear dynamic range and LoD. (c) Diagnostic test parameters. (d) Receiver operating characteristic (ROC) curve. 

component sensing platform that works by intramolecular recombination in the presence of an analyte, proven by detection of immunosuppressant drugs. Other approaches include the _truncation_ of enzymes to reduce the distance between active sites and electrodes in third-generation biosensors. Kaido et al. report that _truncation_ of _Gluconobacter japonicus_ fructose dehydrogenase by 199 amino acids significantly improves direct electron transfer and minimizes electrode overpotential.[130][−][132] Similar to truncation, the removal of nonconductive sugar moieties from enzymes reduces the electron transfer distance. For example, _deglycosylation_ of GOx derived from fungus changes its hydrodynamic diameter from 89 to 76 Å, affording a doubling of the electrontransfer rate. 

Enzymes covalently bound to an electrode allow for improved electrochemical performance, especially with direct electron transfer over simple _immobilization_ techniques to deposit enzymes. Specifically, there are reports of enzymes covalently linked to electrodes in an oriented manner. For example, oriented attachment of bilirubin oxidase, glucose oxidase, and cellobiose dehydrogenase to gold electrodes by their surface-exposed cysteines improves direct electron transfer between the enzyme and electrode, as well as the intramolecular electron transfer between the substrate and cofactors.[128][,][133][−][135] The introduction of artificial amino acids to enzymes enables site-specific covalent linking to electrodes with their catalytic cores oriented to decrease the electrontransfer distance between the core and the electrode. For example, coupling of an azide-pyrene to a propargyl-L-lysine modified recombinant GDH fused to a cytochrome c-domain improves the current response 10-fold.[136] Another approach involves adding a peptide to either the N- or C-terminus of a protein for attachment to the electrode. Lee et al. fused a sitespecific gold binding peptide to GDH for attachment to a gold 

electrode. They observe a 10-fold enhancement in catalytic current over the native variant.[137] Similarly, a recombinant sarcosine oxidase with a 6-histidine and silaffine peptide tags allows for self-immobilization onto the electrode surface instead of glutaraldehyde immobilization.[138] 

## ■ **[DATA][ANALYSIS][AND][INTERPRETATION]** 

We briefly referred to sensitivity in the context of the biorecognition element selection; however, researchers use more defined terms to describe sensitivity such as analytical sensitivity, functional sensitivity, limit of detection (LoD), limit of blank (LoB), and limit of quantitation (LoQ). All of these terms describe the smallest concentration of an analyte that an analytical procedure reliably measures.[139] 

_Limit of Blank (LoB)_ or highest apparent analyte concentration found when one measure replicates of a blank sample with no analyte. In this analysis, one assumes a Gaussian distribution for the signals from the blank sample. Or in other words, LoB represents 95% of the observed values. The remaining 5% may even represent signals produced by very low concentrations of analyte, represented by _α_ (or false positivity or Type I error). (Figure 14a). 

**==> picture [136 x 12] intentionally omitted <==**

_Limit of Detection (LoD)_ or the lowest analyte concentration likely to be distinguished from the blank sample and where detection is feasible. As shown in Figure 14a, it again assumes a Gaussian distribution for low-concentration samples: 95% of the samples produce a signal higher than the previously described LoB, and only 5% of the samples will produce a signal lower than LoB, or in other words falsely show there is no analyte present, represented by _β_ (or false negativity or Type II error). 

**N** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

a **ACS Sensors pubs.acs.org/acssensors** ~~e~~ Review 8§€=6—| 

## LoD = LoB + 1.645(SDlow conc.analyte) 

There are several reports, even in IUPAC, that describe LoD as the mean blank value plus 3 times standard deviation of blank (ignoring the standard deviation (SD) of the lowest analyte concentration). Whereas, some reports describe LoD (or analytical sensitivity) as the slope of a calibration curve. However, this is erroneous as LoD might lie outside the linear range of the assay, where the calibration curve is no longer valid. 

_Limit of Quantitation (LoQ)_ is the lowest concentration that one reliably measures and meets goals for bias and imprecision. Or in other words, points above which two different concentrations of analyte are reliably distinguishable. 

**==> picture [106 x 11] intentionally omitted <==**

_Linear dynamic range_ or the portion of the curve where the biosensor response changes linearly with analyte concentration.[140][,][141] The boundaries of linear range include upper and lower limit of quantitation as shown in Figure 14b. One may encounter different shapes of biosensor plots in the literature. Figure 15 shows the dose response curves of a 

Figure 15. Optimizations to consider while building an immunosensor. (a) Linear plot of analyte concentration versus signal. (b) Log plot of analyte concentration versus signal. 

biosensor that correlate the analyte concentration to signal output. There are linear and semilog approaches to plot this relationship. For example, in case of an enzymatic metabolite biosensor, when the dose response curve is plotted on a linear scale, the output signal is hyperbolic and described by a Langmuir binding isotherm. At higher concentrations of analyte, the response reaches a plateau as all the binding receptors of the enzyme are saturated by the analyte. Whereas a semilog plot is a preferred method for displaying results as the response becomes sigmoid and shows a linear section in the transition from low to high response. 

**Parameters for Diagnostic Tests.** Diagnostic _tests_ determine if an individual or a patient has a particular condition or not. These diagnostic tests must perform with a degree of reliability and validity. _Reliability_ refers to the consistency and repeatability of outcomes of a diagnostic test. This includes if the test provides the same result irrespective of who performs the test, or when performed at a different time. Whereas, _validity_ refers to how the test compares in performance to a gold standard. Since this comparison is not possible for every single test, one looks at either a positive or a negative result which is indicative of presence or absence of a particular condition. Sensitivity, specificity, predictive values, and likelihood ratios are parameters that contribute toward and characterize the validity of diagnostic tests. 

The _sensitivity_ of the test refers to the proportion of samples with the condition correctly identified as a positive test result. Thus, if the sensitivity is high, a negative test result will effectively rule out the condition. 

The _specificity_ of the test refers to the proportion of samples with no condition correctly identified as a negative test result. Thus, if specificity is high, a positive result will effectively rule in the condition. 

The _positive predictive value_ refers to the proportion of samples correctly identified to be a positive test result. Whereas _negative predictive value_ is the proportion of samples correctly identified as a negative test result. The prevalence of the condition in the population influences predictive values. Higher prevalence results in higher positive predictive value, and lower prevalence results in higher negative predictive value. Whereas prevalence does not affect sensitivity and specificity values. 

Likelihoods of positive and negative tests are better indicators of the usefulness of a diagnostic clinical test. Higher (a value of 10 or higher) _the likelihood of a positive test result_ , higher the certainty that a positive test result will rule in the condition. Lower (a value of 0.1 or lower) _the likelihood of a negative test_ , the higher the certainty that a negative test result will rule out the condition. A likelihood of close to 1 means the test is not good (i.e., accurate) and should not be used to rule in or rule out the condition.[142][,][143] 

ROC (Receiver Operating Characteristic Curve, Figure 14c), widely used in medical diagnostics, is an effective measure of accuracy of diagnostic tests. Some of the benefits of this curve include−ability to discriminate the true state of subjects, finding the optimal cutoff values, and comparing two alternate diagnostic tests. This curve is a plot of Sensitivity vs (1 − Specificity) or true positivity rate (TPR) vs false positivity rate (FPR). Area under the ROC curve (AUC) is an effective way to summarize the diagnostic accuracy of the test. An AUC of 0 indicates a perfectly inaccurate test, and 1 indicates a perfectly accurate test. 

ROC curves assume overlapping distributions of two sample states in the diagnostic test case, “diseased and “nondiseased”. No overlap between distributions implies a perfectly discriminating test, and a complete overlap means no discrimination. An AUC of 0.5 (45° line) indicates that the test has no discrimination ability, whereas an AUC above this line suggests reasonable ability to discriminate between diseased and nondiseased state. While assessing a diagnostic test, an acceptable value falls in the range 0.7−0.8, excellent values in the range 0.8−0.9, and outstanding above 0.9. To sum up, an ROC curve shows a trade-off between TPR and FPR as you change the criterion for positivity.[142][,][143] 

## ■ **[FUTURE][PROSPECTS][FOR][ELECTROCHEMICAL] BIOSENSORS AND THEIR APPLICATIONS IN POC TECHNOLOGIES** 

The COVID-19 pandemic reiterated the urgent need for pointof-care (POC) technologies. Apart from disease diagnoses, POC devices find use in food quality control and environmental and general health monitoring. POC devices are easy to use and deliver real-time results directly to patients or individuals without the need of any special training. Use of these technologies reduces the cost of analysis, saves time and healthcare costs, and avoids the need for specific facilities and trained professionals. Often these tests employ microfluidic platforms to carry liquid samples to the testing site without the 

**O** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

need for any extra steps from the operator and hence, coupled with POC devices, ensure complete automation of conducting tests as well as analysis under the same integrated platform. _Paper-based microfluidic devices_[142][,][143] are attractive due to their cost effectiveness, biocompatibility, and driving of the liquid solution passively without need of external pumps and valves. Another aspect of development includes miniaturization of transducers and readout instruments. Among the transducers developed thus far, electrochemical biosensors are advantageous in terms of quantitative assessment, high sensitivity, portability, low cost, miniaturization of instrumentation, and simple operation. 

Most notable miniaturized platforms include _screen-printed electrode (SPE)_[144][−][146] coupled to portable reading platforms. The advantages of SPEs include reduced sample volume and easy modification of electrode surfaces, facile disposal, and possibility of coupling to portable systems. When using the different human fluids, nonspecific adsorption of proteins and other biomolecules in the sample will affect the performance of the system. Use of nanoengineered surfaces (such as graphene oxide and carbon nanotube), antifouling layers (PEG, zwitterionic polymers), and hydrogels reduce the effect of this problem. There is a recent surge in the development of _microelectrode arrays (MEA)_[133] for multitarget and highthroughput detection. MEAs are small microlevel (about tens to thousands) ordered or disordered electrodes on silicon or glass substrates that detect multiple targets simultaneously through the biospecificity of biorecognition elements. The _signal amplification technologies_[107][,][147][,][148] (enzymes and nanotechnology) previously described are a key aspect for the development of POC technologies. 

Continuous glucose monitors (CGM), which track glucose levels in diabetics over time, are at the forefront of modern biosensors and a growing industry sector. These monitors are worn on the skin with microneedles delivering glucose to the transducer, and a response (e.g., glucose concentration) is read by the user on their smartphone.[149] Some of the more recent developments in the CGM space include noninvasive glucose detection by utilizing glucose measurement in sweat,[150] implantable glucose meters that do not require the monitor to be worn on the outside of the body,[151] and automated insulin delivery system integrated with a CGM.[152] This research space is constantly growing and holds promise for easier access to healthcare. 

As we enter the world of artificial intelligence, there are already reports of the integration of machine learning models to improve the sensitivity of electrochemical biosensors. Electrochemical biosensors are plagued by interference and background noise in samples. The implementation of machine learning into devices enhances the reliability to discriminate responses. Machine learning also paves the way for intelligent biosensors wherein these models automatically predict the analyte concentration based on a decision system.[153][−][155] Therefore, coupling machine learning with POC devices will have a tremendous positive impact in the healthcare space. 

The improvements in electrodes, sample retrieval, signal processing, etc., in biosensors need to coincide with advancement in the diversity of biorecognition elements available for use. We must not fall into the supply chain trap of only working on those elements (e.g., antibodies, enzymes) we can buy or, worse yet, designing experiments based on the enzymes we can buy and not the application need. Screening technologies are critical, and capitalizing on existing RNA, 

antibody, and enzyme methodologies will provide new sensors, and collaborating with those experts in the field to further our biosensor components and designs will lead to improved selectivity, specificity, and sensitivity. 

Within medicine, electrochemical (i.e., E-chem) biosensors will continue to play key roles in prevention, treatment, and surveillance. The clinical impact target areas are diverse and include, for example, chronic disease management and monitoring of cardiovascular and pulmonary diseases, rehabilitation medicine and therapy to monitor patient progress and administer the next best steps, prenatal monitoring to reduce maternal mortality rates, and preventative medicine by routine monitoring of key health indicators. Additionally, Bluetoothenabled electrochemical biosensors will ensure automatic transfer of test results to healthcare facilities and practitioners as well as the individual. Thus, in our opinion, electrochemical POC devices are the future for bringing healthcare resources to our fingertips. The success of glucometer technologies illustrates the potential of electrochemical biosensors to revolutionize patient care and positively affect society. We encourage all to engage in this research area to design, build, and evaluate new electrochemical POC devices that are highly specific, sensitive, and quantitative, as well as easy to use by the healthcare professional or consumer. 

## ■ **[AUTHOR][INFORMATION]** 

## **Corresponding Authors** 

- Scott E. Schaus − _Department of Chemistry, Boston University, Boston, Massachusetts 02215, United States;_ orcid.org/0000-0002-5877-6587; Email: seschaus@ 

- bu.edu 

- James E. Galagan − _Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States_ ; Email: jgalag@bu.edu 

- Mark W. Grinstaff − _Division of Materials Science and Engineering, Department of Biomedical Engineering, and Department of Chemistry, Boston University, Boston, Massachusetts 02215, United States;_ orcid.org/00000002-5453-3668; Email: mgrin@bu.edu 

## **Authors** 

- Karthika Sankar − _Division of Materials Science and Engineering, Boston University, Boston, Massachusetts 02215, United States_ 

- Uros Kuzmanovic − _Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States_ 

Complete contact information is available at: https://pubs.acs.org/10.1021/acssensors.4c00043 

## **Author Contributions** 

The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript. No AI was used in the writing of this manuscript, just revision after revision between the authors. 

## **Notes** 

The authors declare the following competing financial interest(s): KS, UK, JEG, and MWG are inventors on a patent describing transcription factor and enzyme based electrochemical biosensors filed by Boston University, which is available for license. UK and JEG are co-founders of BioSens8 and MWG is an advisor, and SES, JEG, and MWG were cofounders of Virex Health (acquired by Sorrento Therapeutics). 

**P** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

## ■ **[ACKNOWLEDGMENTS]** 

This work was supported in part by the DARPA (W911NF-16C-0044; JEG, MWG), the Motorola Foundation sponsored Society of Women Engineer’s scholarship (KS), and the NIH (R01EB029795; JEG, MWG). 

## ■ **[VOCABULARY][SECTION]** 

1) Faradaic current, current that results from redox reactions occurring at the solution−electrode interface; 2) Transducer, in a biosensor, the element (for example, electrode) that converts a biorecognition event into a measurable electrical output; 3) Biorecognition element, a component of biosensor that uniquely (ideally) identifies and selectively binds a target analyte and then relays that binding event to a transducer to produce a measurable signal; 4) Mediator, small electroactive molecules that shuttle electrons between a biorecognition element and a transducer; 5) Binding affinity, the strength of binding interaction between one biomolecule and its binding partner (for example, antigen−antibody); 6) Limit of detection, the lowest analyte concentration to be distinguished from the blank sample 

## ■ **[ABBREVIATIONS]** 

POC, point-of-care; LOD, limit of detection; LOB, limit of blank; LoQ, limit of quantitation; SWV, square wave voltammetry; ELISA, enzyme linked immunosorbent assay; CV, cyclic voltammetry; EIS, electrochemical impedance spectroscopy; PAD, Pulsed Amperometry; MIP, molecularly imprinted polymers; DNA, deoxyribonucleic acid; SELEX, systematic evolution of ligands by exponential enrichment; PCR, polymerase chain reaction; GOx, glucose oxidase; GDH, glucose dehydrogenase; COVID-19, coronavirus disease-19; TFs, Transcription factors; NAD, Nicotinamide adenine dinucleotide; FAD, flavin adenine dinucleotide; PQQ, pyrroloquinoline quinone; ALP, alkaline phosphatase; HRP, horseradish peroxidase; MCH, 6-mercaptohexanol; MEA, microelectrode arrays; PEG, polyethylene glycol; SPE, screen-printed electrode; FPR, false positivity rate; TPR, true positivity rate; ROC, receiver operating characteristic curve 

## ■ **[REFERENCES]** 

(1) Patel, S.; Nanda, R.; Sahoo, S.; Mohapatra, E. Biosensors in Health Care: The Milestones Achieved in Their Development towards Lab-on-Chip-Analysis. _Biochem Res. Int._ 2016, _2016_ , 3130469. 

(2) Hasan, A.; Nurunnabi, M.; Morshed, M.; Paul, A.; Polini, A.; Kuila, T.; Al Hariri, M.; Lee, Y. K.; Jaffa, A. A. Recent advances in application of biosensors in tissue engineering. _Biomed Res. Int._ 2014, _2014_ , 307519. 

(3) Hirsch, I. B. Introduction: history of glucose monitoring. _Compendia_ 2018, _2018_ (1), 1. 

(4) Grieshaber, D.; MacKenzie, R.; Voros, J.; Reimhult, E. Electrochemical Biosensors - Sensor Principles and Architectures. _Sensors (Basel)_ 2008, _8_ (3), 1400−1458. 

(5) Mehrvar, M.; Abdi, M. Recent developments, characteristics, and potential applications of electrochemical biosensors. _Anal. Sci._ 2004, _20_ (8), 1113−1126. 

(6) Shanbhag, M. M.; Manasa, G.; Mascarenhas, R. J.; Mondal, K.; Shetti, N. P. Fundamentals of bio-electrochemical sensing. _Chemical Engineering Journal Advances_ 2023, _16_ , 100516. 

(7) Kim, J.; Campbell, A. S.; de Avila, B. E.; Wang, J. Wearable biosensors for healthcare monitoring. _Nat. Biotechnol._ 2019, _37_ (4), 389−406. 

(8) Liu, D.; Wang, J.; Wu, L.; Huang, Y.; Zhang, Y.; Zhu, M.; Wang, Y.; Zhu, Z.; Yang, C. Trends in miniaturized biosensors for point-ofcare testing. _TrAC Trends in Analytical Chemistry_ 2020, _122_ , 115701. (9) Bard, A. J.; Faulkner, L. R.; White, H. S. _Electrochemical methods: fundamentals and applications_ ; John Wiley & Sons, 2022. 

(10) Rackus, D. G.; Shamsi, M. H.; Wheeler, A. R. Electrochemistry, biosensors and microfluidics: a convergence of fields. _Chem. Soc. Rev._ 2015, _44_ (15), 5320−5340. 

(11) Elgrishi, N.; Rountree, K. J.; McCarthy, B. D.; Rountree, E. S.; Eisenhart, T. T.; Dempsey, J. L. A Practical Beginner’s Guide to Cyclic Voltammetry. _J. Chem. Educ._ 2018, _95_ (2), 197−206. 

(12) Simoska, O.; Minteer, S. D. _Techniques in electroanalytical chemistry_ ; American Chemical Society, 2022. 

(13) Gupta, V. K.; Jain, R.; Radhapyari, K.; Jadon, N.; Agarwal, S. Voltammetric techniques for the assay of pharmaceuticals-a review. _Anal. Biochem._ 2011, _408_ (2), 179−196. 

(14) Chen, A.; Shah, B. Electrochemical sensing and biosensing based on square wave voltammetry. _Analytical Methods_ 2013, _5_ (9), 2158−2173. 

(15) Uslu, B.; Ozkan, S. A. Electroanalytical methods for the determination of pharmaceuticals: a review of recent trends and developments. _Analytical letters_ 2011, _44_ (16), 2644−2702. 

(16) Song, P.; Fisher, A. C.; Wadhawan, J. D.; Cooper, J. J.; Ward, H. J.; Lawrence, N. S. A mechanistic study of the EC′ mechanism-the split wave in cyclic voltammetry and square wave voltammetry. _RSC Adv._ 2016, _6_ (74), 70237−70242. 

(17) Codognoto, L.; Machado, S. A. S.; Avaca, L. A. Square wave voltammetry on boron-doped diamond electrodes for analytical determinations. _Diamond Relat. Mater._ 2002, _11_ (9), 1670−1675. 

(18) Dauphin-Ducharme, P.; Arroyo-Curras, N.; Kurnik, M.; Ortega, G.; Li, H.; Plaxco, K. W. Simulation-Based Approach to Determining Electron Transfer Rates Using Square-Wave Voltammetry. _Langmuir_ 2017, _33_ (18), 4407−4413. 

(19) Mirceski, V.; Laborda, E.; Guziejewski, D.; Compton, R. G. New approach to electrode kinetic measurements in square-wave voltammetry: amplitude-based quasireversible maximum. _Anal. Chem._ 2013, _85_ (11), 5586−5594. 

(20) Dauphin-Ducharme, P.; Plaxco, K. W. Maximizing the Signal Gain of Electrochemical-DNA Sensors. _Anal. Chem._ 2016, _88_ (23), 11654−11662. 

(21) Magar, H. S.; Hassan, R. Y. A.; Mulchandani, A. Electrochemical Impedance Spectroscopy (EIS): Principles, Construction, and Biosensing Applications. _Sensors (Basel)_ 2021, _21_ (19), 6578. 

(22) Zamfir, L. G.; Puiu, M.; Bala, C. Advances in Electrochemical Impedance Spectroscopy Detection of Endocrine Disruptors. _Sensors (Basel)_ 2020, _20_ (22), 6443. 

(23) Lisdat, F.; Schafer, D. The use of electrochemical impedance spectroscopy for biosensing. _Anal Bioanal Chem._ 2008, _391_ (5), 1555−1567. 

(24) Vidakovic-Koch, T.; Mittal, V. K.; Do, T.; Varnicic, M.; Sundmacher, K. Application of electrochemical impedance spectroscopy for studying of enzyme kinetics. _Electrochim. Acta_ 2013, _110_ , 94−104. 

(25) Park, J.-Y.; Park, S.-M. DNA hybridization sensors based on electrochemical impedance spectroscopy as a detection tool. _Sensors_ 2009, _9_ (12), 9513−9532. 

(26) Yu, X.; Lv, R.; Ma, Z.; Liu, Z.; Hao, Y.; Li, Q.; Xu, D. An impedance array biosensor for detection of multiple antibody-antigen interactions. _Analyst_ 2006, _131_ (6), 745−750. 

(27) Santos, A.; Carvalho, F. C.; Roque-Barreira, M. C.; Bueno, P. R. Impedance-derived electrochemical capacitance spectroscopy for the evaluation of lectin-glycoprotein binding affinity. _Biosens Bioelectron_ 2014, _62_ , 102−105. 

(28) Heard, D. M.; Lennox, A. J. J. Electrode Materials in Modern Organic Electrochemistry. _Angew. Chem., Int. Ed. Engl._ 2020, _59_ (43), 18866−18884. 

(29) McNaught, A. D.; Wilkinson, A. _Compendium of chemical terminology_ ; Blackwell Science Oxford, 1997. 

**Q** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

(30) Wightman, R. M. Microvoltammetric electrodes. _Anal. Chem._ 1981, _53_ (9), 1125A−1134A. 

(31) Heinze, J. Ultramicroelectrodes in electrochemistry. _Angewandte Chemie International Edition in English_ 1993, _32_ (9), 1268− 1288. 

(32) Couper, A. M.; Pletcher, D.; Walsh, F. C. Electrode materials for electrosynthesis. _Chem. Rev._ 1990, _90_ (5), 837−865. 

(33) Morales, M. A.; Halpern, J. M. Guide to Selecting a Biorecognition Element for Biosensors. _Bioconjug Chem._ 2018, _29_ (10), 3231−3239. 

(34) Chambers, J. P.; Arulanandam, B. P.; Matta, L. L.; Weis, A.; Valdes, J. J. Biosensor recognition elements. _Curr. Issues Mol. Biol._ 2008, _10_ (1−2), 1−12. 

(35) Byrne, B.; Stack, E.; Gilmartin, N.; O’Kennedy, R. Antibodybased sensors: principles, problems and potential for detection of pathogens and associated toxins. _Sensors (Basel)_ 2009, _9_ (6), 4407− 4445. 

(36) Sharma, S.; Byrne, H.; O’Kennedy, R. J. Antibodies and antibody-derived analytical biosensors. _Essays Biochem_ 2016, _60_ (1), 9−18. 

(37) Rocchitta, G.; Spanu, A.; Babudieri, S.; Latte, G.; Madeddu, G.; Galleri, G.; Nuvoli, S.; Bagella, P.; Demartis, M. I.; Fiore, V. Enzyme Biosensors for Biomedical Applications: Strategies for Safeguarding Analytical Performances in Biological Fluids. _Sensors (Basel)_ 2016, _16_ (6), 780. 

(38) Singh, K. R.; Sridevi, P.; Singh, R. P. Potential applications of peptide nucleic acid in biomedical domain. _Eng. Rep_ 2020, _2_ (9), No. e12238. 

(39) Teles, F.; Fonseca, L. Trends in DNA biosensors. _Talanta_ 2008, _77_ (2), 606−623. 

(40) Yang, L. F.; Ling, M.; Kacherovsky, N.; Pun, S. H. Aptamers 101: aptamer discovery and in vitro applications in biosensors and separations. _Chem. Sci._ 2023, _14_ (19), 4961−4978. 

(41) Tellechea-Luzardo, J.; Stiebritz, M. T.; Carbonell, P. Transcription factor-based biosensors for screening and dynamic regulation. _Front Bioeng Biotechnol_ 2023, _11_ , 1118702. 

(42) Crapnell, R. D.; Dempsey-Hibbert, N. C.; Peeters, M.; Tridente, A.; Banks, C. E. Molecularly imprinted polymer based electrochemical biosensors: Overcoming the challenges of detecting vital biomarkers and speeding up diagnosis. _Talanta Open_ 2020, _2_ , 100018. 

(43) Gui, R.; Jin, H.; Guo, H.; Wang, Z. Recent advances and future prospects in molecularly imprinted polymers-based electrochemical biosensors. _Biosens Bioelectron_ 2018, _100_ , 56−70. 

(44) Denmark, D. J.; Mohapatra, S.; Mohapatra, S. S. Point-of-care diagnostics: molecularly imprinted polymers and nanomaterials for enhanced biosensor selectivity and transduction. _EuroBiotech Journal_ 2020, _4_ (4), 184−206. 

(45) BelBruno, J. J. Molecularly Imprinted Polymers. _Chem. Rev._ 2019, _119_ (1), 94−119. 

(46) Chen, L.; Wang, X.; Lu, W.; Wu, X.; Li, J. Molecular imprinting: perspectives and applications. _Chem. Soc. Rev._ 2016, _45_ (8), 2137−2211. 

(47) Erturk, G.; Mattiasson, B. Molecular Imprinting Techniques Used for the Preparation of Biosensors. _Sensors (Basel)_ 2017, _17_ (2), 288. 

(48) Garg, M.; Pamme, N. Strategies to remove templates from molecularly imprinted polymer (MIP) for biosensors. _TrAC Trends in Analytical Chemistry_ 2024, _170_ , 117437. 

(49) Vasapollo, G.; Sole, R. D.; Mergola, L.; Lazzoi, M. R.; Scardino, A.; Scorrano, S.; Mele, G. Molecularly imprinted polymers: present and future prospective. _Int. J. Mol. Sci._ 2011, _12_ (9), 5908−5945. 

(50) Sullivan, M. V.; Dennison, S. R.; Archontis, G.; Reddy, S. M.; Hayes, J. M. Toward Rational Design of Selective Molecularly Imprinted Polymers (MIPs) for Proteins: Computational and Experimental Studies of Acrylamide Based Polymers for Myoglobin. _J. Phys. Chem. B_ 2019, _123_ (26), 5432−5443. 

(51) Fan, R.; Li, Y.; Park, K. W.; Du, J.; Chang, L. H.; Strieter, E. R.; Andrew, T. L. A Strategy for Accessing Nanobody-Based Electro- 

chemical Sensors for Analyte Detection in Complex Media. _ECS Sens Plus_ 2022, _1_ (1), 010601. 

(52) Goode, J.; Dillon, G.; Millner, P. A. The development and optimization of nanobody based electrochemical immunosensors for IgG. _Sens. Actuators, B_ 2016, _234_ , 478−484. 

(53) Briones, C.; Moreno, M. Applications of peptide nucleic acids (PNAs) and locked nucleic acids (LNAs) in biosensor development. _Anal Bioanal Chem._ 2012, _402_ (10), 3071−3089. 

(54) Saleem, M.; Yu, H.; Wang, L.; Zain-ul-Abdin; Khalid, H.; Akram, M.; Abbasi, N. M.; Huang, J. Review on synthesis of ferrocene-based redox polymers and derivatives and their application in glucose sensing. _Analytica chimica acta_ 2015, _876_ , 9−25. 

(55) Tichy, V.; Sebest, P.; Orsag, P.; Havran, L.; Pivonkova, H.; Fojta, M. Protein p53 Binding to Cisplatin-modified DNA Targets Evaluated by Modification-specific Electrochemical Immunoprecipitation Assay. _Electroanalysis_ 2017, _29_ (2), 319−323. 

(56) Chaubey, A.; Malhotra, B. D. Mediated biosensors. _Biosens Bioelectron_ 2002, _17_ (6−7), 441−456. 

(57) Kelley, S. O.; Boon, E. M.; Barton, J. K.; Jackson, N. M.; Hill, M. G. Single-base mismatch detection based on charge transduction through DNA. _Nucleic Acids Res._ 1999, _27_ (24), 4830−4837. 

(58) Yang, S.; Rothman, R. E. PCR-based diagnostics for infectious diseases: uses, limitations, and future applications in acute-care settings. _Lancet Infect Dis_ 2004, _4_ (6), 337−348. 

(59) Hu, Q.; Wan, J.; Luo, Y.; Li, S.; Cao, X.; Feng, W.; Liang, Y.; Wang, W.; Niu, L. Electrochemical Detection of Femtomolar DNA via Boronate Affinity-Mediated Decoration of Polysaccharides with Electroactive Tags. _Anal. Chem._ 2022, _94_ (37), 12860−12865. 

(60) Dong, X.; Yan, X.; Li, M.; Liu, H.; Li, J.; Wang, L.; Wang, K.; Lu, X.; Wang, S.; He, B. Ultrasensitive detection of chloramphenicol using electrochemical aptamer sensor: A mini review. _Electrochem. Commun._ 2020, _120_ , 106835. 

(61) Kang, D.; Ricci, F.; White, R. J.; Plaxco, K. W. Survey of RedoxActive Moieties for Application in Multiplexed Electrochemical Biosensors. _Anal. Chem._ 2016, _88_ (21), 10452−10458. 

(62) Yang, W.; Lai, R. Y. Comparison of the stem-loop and linear probe-based electrochemical DNA sensors by alternating current voltammetry and cyclic voltammetry. _Langmuir_ 2011, _27_ (23), 14669−14677. 

(63) Swetha, P. D. P.; Sonia, J.; Sapna, K.; Prasad, K. S. Towards CRISPR powered electrochemical sensing for smart diagnostics. _Current opinion in electrochemistry_ 2021, _30_ , 100829. 

(64) Zhuang, X.; Yang, X.; Cao, B.; Sun, H.; Lv, X.; Zeng, C.; Li, F.; Qu, B.; Zhou, H. S.; Cui, F.; et al. CRISPR/Cas Systems: Endless Possibilities for Electrochemical Nucleic Acid Sensors. _J. Electrochem. Soc._ 2022, _169_ (3), 037522. 

(65) Immoos, C. E.; Lee, S. J.; Grinstaff, M. W. DNA-PEG-DNA triblock macromolecules for reagentless DNA detection. _J. Am. Chem. Soc._ 2004, _126_ (35), 10814−10815. 

(66) Hua, Y.; Ma, J.; Li, D.; Wang, R. DNA-Based Biosensors for the Biochemical Analysis: A Review. _Biosensors (Basel)_ 2022, _12_ (3), 183. (67) Li, N.; Wang, M.; Gao, X.; Yu, Z.; Pan, W.; Wang, H.; Tang, B. A DNA Tetrahedron Nanoprobe with Controlled Distance of Dyes for Multiple Detection in Living Cells and in Vivo. _Anal. Chem._ 2017, _89_ (12), 6670−6677. 

(68) Huang, R.; He, N.; Li, Z. Recent progresses in DNA nanostructure-based biosensors for detection of tumor markers. _Biosens Bioelectron_ 2018, _109_ , 27−34. 

(69) Krishnaveni, P.; Ganesh, V. Electron transfer studies of a conventional redox probe in human sweat and saliva bio-mimicking conditions. _Sci. Rep_ 2021, _11_ (1), 7663. 

(70) Sawhney, M. A.; Azzopardi, E. A.; Teixeira, S. R.; Francis, L. W.; Conlan, R. S.; Gazze, S. Measuring the impact on impedance spectroscopy of pseudo-reference electrode accumulations. _Electrochem. Commun._ 2019, _105_ , 106508. 

(71) Vogt, S.; Su, Q.; Gutiérrez-Sánchez, C.; Nöll, G. Critical view on electrochemical impedance spectroscopy using the ferri/ ferrocyanide redox couple at gold electrodes. _Analytical chemistry_ 2016, _88_ (8), 4383−4390. 

**R** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

(72) Steichen, M.; Decrem, Y.; Godfroid, E.; Buess-Herman, C. Electrochemical DNA hybridization detection using peptide nucleic acids and [Ru(NH3)6]3+ on gold electrodes. _Biosens Bioelectron_ 2007, _22_ (9−10), 2237−2243. 

(73) Steel, A. B.; Herne, T. M.; Tarlov, M. J. Electrochemical quantitation of DNA immobilized on gold. _Anal. Chem._ 1998, _70_ (22), 4670−4677. 

(74) Xu, L.; Liang, W.; Wen, Y.; Wang, L.; Yang, X.; Ren, S.; Jia, N.; Zuo, X.; Liu, G. An ultrasensitive electrochemical biosensor for the detection of mecA gene in methicillin-resistant Staphylococcus aureus. _Biosens Bioelectron_ 2018, _99_ , 424−430. 

(75) Li, L.; Wang, L.; Xu, Q.; Xu, L.; Liang, W.; Li, Y.; Ding, M.; Aldalbahi, A.; Ge, Z.; Wang, L.; et al. Bacterial Analysis Using an Electrochemical DNA Biosensor with Poly-Adenine-Mediated DNA Self-Assembly. _ACS Appl. Mater. Interfaces_ 2018, _10_ (8), 6895−6903. (76) Wang, Q.; Wen, Y.; Li, Y.; Liang, W.; Li, W.; Li, Y.; Wu, J.; Zhu, H.; Zhao, K.; Zhang, J.; et al. Ultrasensitive Electrochemical Biosensor of Bacterial 16S rRNA Gene Based on polyA DNA Probes. _Anal. Chem._ 2019, _91_ (14), 9277−9283. 

(77) Shah, K.; Maghsoudlou, P. Enzyme-linked immunosorbent assay (ELISA): the basics. _Br J. Hosp Med. (Lond)_ 2016, _77_ (7), C98−101. 

(78) Polanski, M.; Anderson, N. L. A list of candidate cancer biomarkers for targeted proteomics. _Biomarker insights_ 2006, _1_ , 117727190600100. 

(79) Liang, S.-L.; Chan, D. W. Enzymes and related proteins as cancer biomarkers: a proteomic approach. _Clinica chimica acta_ 2007, _381_ (1), 93−97. 

(80) Kang, D.; Parolo, C.; Sun, S.; Ogden, N. E.; Dahlquist, F. W.; Plaxco, K. W. Expanding the Scope of Protein-Detecting Electrochemical DNA ″Scaffold″ Sensors. _ACS Sens_ 2018, _3_ (7), 1271−1275. 

(81) Lubin, A. A.; Plaxco, K. W. Folding-based electrochemical biosensors: the case for responsive nucleic acid architectures. _Acc. Chem. Res._ 2010, _43_ (4), 496−505. 

(82) Bonham, A. J.; Hsieh, K.; Ferguson, B. S.; Vallee-Belisle, A.; Ricci, F.; Soh, H. T.; Plaxco, K. W. Quantification of transcription factor binding in cell extracts using an electrochemical, structureswitching biosensor. _J. Am. Chem. Soc._ 2012, _134_ (7), 3346−3348. 

(83) Sankar, K.; Baer, R.; Grazon, C.; Sabatelle, R. C.; Lecommandoux, S.; Klapperich, C. M.; Galagan, J. E.; Grinstaff, M. W. An Allosteric Transcription Factor DNA-Binding Electrochemical Biosensor for Progesterone. _ACS Sens_ 2022, _7_ (4), 1132−1137. 

(84) Jhaveri, S. D.; Mauro, J. M.; Goldston, H. M.; Schauer, C. L.; Tender, L. M.; Trammell, S. A. A reagentless electrochemical biosensor based on a protein scaffold. _Chem. Commun. (Camb)_ 2003, No. 3, 338−339. 

(85) Furst, A. L.; Muren, N. B.; Hill, M. G.; Barton, J. K. Label-free electrochemical detection of human methyltransferase from tumors. _Proc. Natl. Acad. Sci. U. S. A._ 2014, _111_ (42), 14985−14989. 

(86) Pheeney, C. G.; Barton, J. K. DNA electrochemistry with tethered methylene blue. _Langmuir_ 2012, _28_ (17), 7063−7070. 

(87) Song, Z.; Li, R.; Yang, X.; Zhang, Z.; Luo, X. Functional DNApeptide conjugates with enhanced antifouling capabilities for electrochemical detection of proteins in complex human serum. _Sens. Actuators, B_ 2022, _367_ , 132110. 

(88) Severinghaus, J. W.; Astrup, P. B. History of blood gas analysis. IV. Leland Clark’s oxygen electrode. _J. Clin Monit_ 1986, _2_ (2), 125− 139. 

(89) Panahi, Z.; Custer, L.; Halpern, J. M. Recent advances in nonenzymatic electrochemical detection of hydrophobic metabolites in biofluids. _Sensors and Actuators Reports_ 2021, _3_ , 100051. 

(90) Si, Y.; Lee, H. J. Carbon nanomaterials and metallic nanoparticles-incorporated electrochemical sensors for small metabolites: Detection methodologies and applications. _Current Opinion in Electrochemistry_ 2020, _22_ , 234−243. 

(91) Xiao, F.; Wang, L.; Duan, H. Nanomaterial based electrochemical sensors for in vitro detection of small molecule metabolites. _Biotechnol Adv._ 2016, _34_ (3), 234−249. 

(92) Yu, H.; Yu, J.; Li, L.; Zhang, Y.; Xin, S.; Ni, X.; Sun, Y.; Song, K. Recent Progress of the Practical Applications of the Platinum Nanoparticle-Based Electrochemistry Biosensors. _Front Chem._ 2021, _9_ , 677876. 

(93) Viet, N. X.; Chikae, M.; Ukita, Y.; Takamura, Y. Enzyme-free glucose sensor based on micro-nano Dualporous gold-modified screen-printed carbon electrode. _Int. J. Electrochem. Sci._ 2018, _13_ (9), 8633−8644. 

(94) Cheng, A. K.; Sen, D.; Yu, H. Z. Design and testing of aptamerbased electrochemical biosensors for proteins and small molecules. _Bioelectrochemistry_ 2009, _77_ (1), 1−12. 

(95) White, R. J.; Rowe, A. A.; Plaxco, K. W. Re-engineering aptamers to support reagentless, self-reporting electrochemical sensors. _Analyst_ 2010, _135_ (3), 589−594. 

(96) Xu, C.; Cai, H.; Xu, Q.; He, P.; Fang, Y. Characterization of single-stranded DNA on chitosan-modified electrode and its application to the sequence-specific DNA detection. _Fresenius J. Anal Chem._ 2001, _369_ (5), 428−432. 

(97) Kulikova, T.; Porfireva, A.; Evtugyn, G.; Hianik, T. Electrochemical DNA Sensors with Layered Polyaniline-DNA Coating for Detection of Specific DNA Interactions. _Sensors (Basel)_ 2019, _19_ (3), 469. 

(98) Zhang, W.; Yang, T.; Huang, D. M.; Jiao, K. Electrochemical sensing of DNA immobilization and hybridization based on carbon nanotubes/nano zinc oxide/chitosan composite film. _Chin. Chem. Lett._ 2008, _19_ (5), 589−591. 

(99) Rashid, J. I. A.; Yusof, N. A. The strategies of DNA immobilization and hybridization detection mechanism in the construction of electrochemical DNA sensor: A review. _Sensing and bio-sensing research_ 2017, _16_ , 19−31. 

(100) White, R. J.; Phares, N.; Lubin, A. A.; Xiao, Y.; Plaxco, K. W. Optimization of electrochemical aptamer-based sensors via optimization of probe packing density and surface chemistry. _Langmuir_ 2008, _24_ (18), 10513−10518. 

(101) Ricci, F.; Lai, R. Y.; Heeger, A. J.; Plaxco, K. W.; Sumner, J. J. Effect of molecular crowding on the response of an electrochemical DNA sensor. _Langmuir_ 2007, _23_ (12), 6827−6834. 

(102) Szymczyk, A.; Soliwodzka, K.; Moskal, M.; Rózanowski, K.; Ziółkowski, R. Further insight into the possible influence of electrode blocking agents on the stem-loop based electrochemical DNA sensor parameters. _Sens. Actuators, B_ 2022, _354_ , 131086. 

(103) He, B.; Morrow, T. J.; Keating, C. D. Nanowire sensors for multiplexed detection of biomolecules. _Curr. Opin Chem. Biol._ 2008, _12_ (5), 522−528. 

(104) Cao, X.; Liu, S.; Feng, Q.; Wang, N. Silver nanowire-based electrochemical immunoassay for sensing immunoglobulin G with signal amplification using strawberry-like ZnO nanostructures as labels. _Biosens. Bioelectron._ 2013, _49_ , 256−262. 

(105) Li, M.; Wang, P.; Li, F.; Chu, Q.; Li, Y.; Dong, Y. An ultrasensitive sandwich-type electrochemical immunosensor based on the signal amplification strategy of mesoporous core-shell Pd@Pt nanoparticles/amino group functionalized graphene nanocomposite. _Biosens Bioelectron_ 2017, _87_ , 752−759. 

(106) Liu, X.; Li, W.-J.; Li, L.; Yang, Y.; Mao, L.-G.; Peng, Z. A labelfree electrochemical immunosensor based on gold nanoparticles for direct detection of atrazine. _Sens. Actuators, B_ 2014, _191_ , 408−414. 

(107) Lim, S. A.; Ahmed, M. U. Electrochemical immunosensors and their recent nanomaterial-based signal amplification strategies: A review. _RSC Adv._ 2016, _6_ (30), 24995−25014. 

(108) Sharafeldin, M.; McCaffrey, K.; Rusling, J. F. Influence of antibody immobilization strategy on carbon electrode immunoarrays. _Analyst_ 2019, _144_ (17), 5108−5116. 

(109) Sotnikov, D. V.; Zherdev, A. V.; Zvereva, E. A.; Eremin, S. A.; Dzantiev, B. B. Changing cross-reactivity for different immunoassays using the same antibodies: Theoretical description and experimental confirmation. _Applied Sciences_ 2021, _11_ (14), 6581. 

(110) Chikkaveeraiah, B. V.; Bhirde, A. A.; Morgan, N. Y.; Eden, H. S.; Chen, X. Electrochemical immunosensors for detection of cancer protein biomarkers. _ACS Nano_ 2012, _6_ (8), 6546−6561. 

**S** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

(111) Siddiqui, M. F.; Khan, Z. A.; Park, S. Detection of C-Reactive Protein Using Histag-HRP Functionalized Nanoconjugate with Signal Amplified Immunoassay. _Nanomaterials (Basel)_ 2020, _10_ (6), 1240. 

(112) Gan, N.; Du, X.; Cao, Y.; Hu, F.; Li, T.; Jiang, Q. An ultrasensitive electrochemical immunosensor for HIV p24 based on Fe3O4@ SiO2 nanomagnetic probes and nanogold colloid-labeled enzyme-antibody copolymer as signal tag. _Materials_ 2013, _6_ (4), 1255−1269. 

(113) Xiong, P.; Gan, N.; Cao, Y.; Hu, F.; Li, T.; Zheng, L. An ultrasensitive electrochemical immunosensor for alpha-fetoprotein using an envision complex-antibody copolymer as a sensitive label. _Materials_ 2012, _5_ (12), 2757−2772. 

(114) Akter, R.; Rhee, C. K.; Rahman, M. A. Sensitivity enhancement of an electrochemical immunosensor through the electrocatalysis of magnetic bead-supported non-enzymatic labels. _Biosens. Bioelectron._ 2014, _54_ , 351−357. 

(115) Wu, L.; Xiong, E.; Zhang, X.; Zhang, X.; Chen, J. Nanomaterials as signal amplification elements in DNA-based electrochemical sensing. _Nano Today_ 2014, _9_ (2), 197−211. 

(116) Valera, E.; Hernández-Albors, A.; Marco, M.-P. Electrochemical coding strategies using metallic nanoprobes for biosensing applications. _TrAC Trends in Analytical Chemistry_ 2016, _79_ , 9−22. 

(117) Ito, Y.; Okuda-Shimazaki, J.; Tsugawa, W.; Loew, N.; Shitanda, I.; Lin, C. E.; La Belle, J.; Sode, K. Third generation impedimetric sensor employing direct electron transfer type glucose dehydrogenase. _Biosens Bioelectron_ 2019, _129_ , 189−197. 

(118) Ronkainen, N. J.; Halsall, H. B.; Heineman, W. R. Electrochemical biosensors. _Chem. Soc. Rev._ 2010, _39_ (5), 1747− 1763. 

(119) Hammond, J. L.; Formisano, N.; Estrela, P.; Carrara, S.; Tkac, J. Electrochemical biosensors and nanobiosensors. _Essays Biochem_ 2016, _60_ (1), 69−80. 

(120) Grieshaber, D.; MacKenzie, R.; Vörös, J.; Reimhult, E. Electrochemical biosensors-sensor principles and architectures. _Sensors_ 2008, _8_ (3), 1400−1458. 

(121) Adachi, T.; Kitazumi, Y.; Shirai, O.; Kano, K. Direct electron transfer-type bioelectrocatalysis of redox enzymes at nanostructured electrodes. _Catalysts_ 2020, _10_ (2), 236. 

(122) Takeda, K.; Nakamura, N. Direct electron transfer process of pyrroloquinoline quinone-dependent and flavin adenine dinucleotidedependent dehydrogenases: Fundamentals and applications. _Current Opinion in Electrochemistry_ 2021, _29_ , 100747. 

(123) Kano, K.; Shirai, O.; Kitazumi, Y.; Sakai, K.; Xia, H.-Q. Protein-Engineering Approach for Improvement of DET-Type Bioelectrocatalytic Performance. _Enzymatic Bioelectrocatalysis_ 2021, 93−104. 

(124) Adamson, H.; Jeuken, L. J. C. Engineering Protein Switches for Rapid Diagnostic Tests. _ACS Sens_ 2020, _5_ (10), 3001−3012. 

(125) Yu, S.; Myung, N. V. Recent Advances in the Direct Electron Transfer-Enabled Enzymatic Fuel Cells. _Front Chem._ 2021, _8_ , 620153. 

(126) Adachi, T.; Fujii, T.; Honda, M.; Kitazumi, Y.; Shirai, O.; Kano, K. Direct electron transfer-type bioelectrocatalysis of FADdependent glucose dehydrogenase using porous gold electrodes and enzymatically implanted platinum nanoclusters. _Bioelectrochemistry_ 2020, _133_ , 107457. 

(127) Algov, I.; Grushka, J.; Zarivach, R.; Alfonta, L. Highly Efficient Flavin-Adenine Dinucleotide Glucose Dehydrogenase Fused to a Minimal Cytochrome C Domain. _J. Am. Chem. Soc._ 2017, _139_ (48), 17217−17220. 

(128) Suzuki, N.; Lee, J.; Loew, N.; Takahashi-Inose, Y.; OkudaShimazaki, J.; Kojima, K.; Mori, K.; Tsugawa, W.; Sode, K. Engineered Glucose Oxidase Capable of Quasi-Direct Electron Transfer after a Quick-and-Easy Modification with a Mediator. _Int. J. Mol. Sci._ 2020, _21_ (3), 1137. 

(129) Guo, Z.; Johnston, W. A.; Stein, V.; Kalimuthu, P.; PerezAlcala, S.; Bernhardt, P. V.; Alexandrov, K. Engineering PQQ-glucose dehydrogenase into an allosteric electrochemical Ca 2+ sensor. _Chem. Commun._ 2016, _52_ (3), 485−488. 

(130) Kaida, Y.; Hibino, Y.; Kitazumi, Y.; Shirai, O.; Kano, K. Ultimate downsizing of D-fructose dehydrogenase for improving the performance of direct electron transfer-type bioelectrocatalysis. _Electrochem. Commun._ 2019, _98_ , 101−105. 

(131) Kaida, Y.; Hibino, Y.; Kitazumi, Y.; Shirai, O.; Kano, K. Discussion on direct electron transfer-type bioelectrocatalysis of downsized and axial-ligand exchanged variants of D-fructose dehydrogenase. _Electrochemistry_ 2020, _88_ (3), 195−199. 

(132) Hibino, Y.; Kawai, S.; Kitazumi, Y.; Shirai, O.; Kano, K. Construction of a protein-engineered variant of D-fructose dehydrogenase for direct electron transfer-type bioelectrocatalysis. _Electrochem. Commun._ 2017, _77_ , 112−115. 

(133) Yanez-Sedeno, P.; Campuzano, S.; Pingarron, J. M. Multiplexed Electrochemical Immunosensors for Clinical Biomarkers. _Sensors (Basel)_ 2017, _17_ (5), 965. 

(134) Ma, S.; Laurent, C. V.; Meneghello, M.; Tuoriniemi, J.; Oostenbrink, C.; Gorton, L.; Bartlett, P. N.; Ludwig, R. Direct electron-transfer anisotropy of a site-specifically immobilized cellobiose dehydrogenase. _ACS catalysis_ 2019, _9_ (8), 7607−7615. 

(135) Meneghello, M.; Al-Lolage, F. A.; Ma, S.; Ludwig, R.; Bartlett, P. N. Studying direct electron transfer by site-directed immobilization of cellobiose dehydrogenase. _ChemElectroChem._ 2019, _6_ (3), 700− 713. 

(136) Algov, I.; Feiertag, A.; Alfonta, L. Site-specifically wired and oriented glucose dehydrogenase fused to a minimal cytochrome with high glucose sensing sensitivity. _Biosens Bioelectron_ 2021, _180_ , 113117. 

(137) Lee, H.; Lee, Y. S.; Reginald, S. S.; Baek, S.; Lee, E. M.; Choi, I. G.; Chang, I. S. Biosensing and electrochemical properties of flavin adenine dinucleotide (FAD)-Dependent glucose dehydrogenase (GDH) fused to a gold binding peptide. _Biosens Bioelectron_ 2020, _165_ , 112427. 

(138) Chen, S.; Hall, E. A. A biosilification fusion protein for a ‘selfimmobilising’sarcosine oxidase amperometric enzyme biosensor. _Electroanalysis_ 2020, _32_ (4), 874−884. 

(139) Armbruster, D. A.; Pry, T. Limit of blank, limit of detection and limit of quantitation. _Clin Biochem Rev._ 2008, _29_ (Suppl 1), S49− 52. 

(140) Bhalla, P.; Singh, N. Generalized Drude scattering rate from the memory function formalism: an independent verification of the Sharapov-Carbotte result. _European Physical Journal B_ 2016, _89_ , 1−8. 

(141) Kristjansdottir, K.; Takahashi, S.; Volchenboum, S. L.; Kron, S. J. Strategies and Challenges in Measuring Protein Abundance Using Stable Isotope Labeling and Tandem Mass Spectrometry. _Tandem Mass Spectrometry - Applications and Principles_ 2012, 253. 

(142) Bruno, P. The importance of diagnostic test parameters in the interpretation of clinical test findings: The Prone Hip Extension Test as an example. _Journal of the Canadian Chiropractic Association_ 2011, _55_ (2), 69. 

(143) Parikh, R.; Mathai, A.; Parikh, S.; Chandra Sekhar, G.; Thomas, R. Understanding and using sensitivity, specificity and predictive values. _Indian J. Ophthalmol_ 2008, _56_ (1), 45−50. 

(144) Wang, X.; Zhang, Z.; Wu, G.; Xu, C.; Wu, J.; Zhang, X.; Liu, J. Applications of electrochemical biosensors based on functional antibody-modified screen-printed electrodes: a review. _Analytical Methods_ 2021, _14_ (1), 7−16. 

(145) Ahmed, M. U.; Hossain, M. M.; Safavieh, M.; Wong, Y. L.; Abd Rahman, I.; Zourob, M.; Tamiya, E. Toward the development of smart and low cost point-of-care biosensors based on screen printed electrodes. _Crit Rev. Biotechnol_ 2016, _36_ (3), 495−505. 

(146) Yamanaka, K.; Vestergaard, M. d. C.; Tamiya, E. Printable electrochemical biosensors: A focus on screen-printed electrodes and their application. _Sensors_ 2016, _16_ (10), 1761. 

(147) Liu, Y.; Liu, Y.; Qiao, L.; Liu, Y.; Liu, B. Advances in signal amplification strategies for electrochemical biosensing. _Current Opinion in Electrochemistry_ 2018, _12_ , 5−12. 

(148) Thapa, K.; Liu, W.; Wang, R. Nucleic acid-based electrochemical biosensor: Recent advances in probe immobilization and signal amplification strategies. _Wiley Interdiscip Rev. Nanomed Nanobiotechnol_ 2022, _14_ (1), No. e1765. 

**T** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

**ACS Sensors** 

**pubs.acs.org/acssensors** 

Review 

(149) Chien, M. N.; Chen, Y. J.; Bai, C. H.; Huang, J. T. Continuous Glucose Monitoring System Based on Percutaneous Microneedle Array. _Micromachines (Basel)_ 2022, _13_ (3), 478. 

(150) Wu, J.; Liu, Y.; Yin, H.; Guo, M. A new generation of sensors for non-invasive blood glucose monitoring. _Am. J. Transl Res._ 2023, _15_ (6), 3825−3837. 

(151) Boscari, F.; Vettoretti, M.; Cavallin, F.; Amato, A. M. L.; Uliana, A.; Vallone, V.; Avogaro, A.; Facchinetti, A.; Bruttomesso, D. Implantable and transcutaneous continuous glucose monitoring system: a randomized cross over trial comparing accuracy, efficacy and acceptance. _J. Endocrinol Invest_ 2022, _45_ (1), 115−124. 

(152) Garg, S. K.; McVean, J. J. Development and Future of Automated Insulin Delivery (AID) Systems. _Diabetes Technol. Ther_ 2024, _26_ (S3), 1−6. 

(153) Cui, F.; Yue, Y.; Zhang, Y.; Zhang, Z.; Zhou, H. S. Advancing Biosensors with Machine Learning. _ACS Sens_ 2020, _5_ (11), 3346− 3364. 

(154) de Oliveira Filho, J. I.; Faleiros, M. C.; Ferreira, D. C.; Mani, V.; Salama, K. N. Empowering Electrochemical Biosensors with AI: Overcoming Interference for Precise Dopamine Detection in Complex Samples. _Advanced Intelligent Systems_ 2023, _5_ (10), 2300227. 

(155) Puthongkham, P.; Wirojsaengthong, S.; Suea-Ngam, A. Machine learning and chemometrics for electrochemical sensors: moving forward to the future of analytical chemistry. _Analyst_ 2021, _146_ (21), 6351−6364. 

**U** 

https://doi.org/10.1021/acssensors.4c00043 _ACS Sens._ XXXX, XXX, XXX−XXX 

