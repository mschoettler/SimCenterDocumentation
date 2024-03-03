.. _lbl-capabilities_eeuq:
.. role:: blue

************
Capabilities
************

**Version 3.4** of |app| was released on **September 29**. This version introduces new functionalities and enhancements, as detailed below. New features and fixes are highlighted in :blue:`blue`.

Structural Information Model
============================

Facilitates the specification or selection of structural models for analysis.

#. MDOF: Idealized multi-degree-of-freedom model creation
#. OpenSees: Custom OpenSees model definition
#. Steel Building Model: Automated steel frame design and modeling
#. Concrete Building Model: Automated concrete moment frame design and modeling
#. MDOF-LU: MDOF shear building model
#. SurrogateGP: Surrogate model training in EE-UQ
#. Multiple models: Ability to select multiple structural models :blue:`[<- renamed from Multimodel]`

Earthquake Motion Event
=======================

Tools for specifying or selecting ground motions for analysis.

#. Stochastic Ground Motion: Stochastic ground motion simulation
#. PEER NGA Records: Selection and scaling of PEER NGA West2 ground motions
#. Site Response: Surface propagation of rock motions
#. Multiple PEER: Utilization of multiple PEER recordings
#. Multiple SimCenter: Utilization of multiple SimCenter-format recordings
#. User Specified Database: Selection and scaling of ground motions from a user-defined flatfile

Engineering Demand Parameter Generator
======================================

Tools for identifying output parameters of interest based on the ground motion and structural model.

#. Standard Earthquake: Maximum story drift ratio, lateral story displacement, peak floor acceleration
#. User Defined: Custom EDP specification
#. None: Reserved for surrogate model-based predictions

Finite Element Application
==========================

Tools for determining response output parameters based on the ground motion and structural model.

#. OpenSees: Open System for Earthquake Engineering Simulation
#. CustomPy-Simulation: Custom Python script
#. None: Reserved for surrogate model-based predictions
#. Multiple models: Ability to select multiple finite element applications :blue:`[<- renamed from Multimodel]`

Uncertainty Quantification
==========================

Tools for performing uncertainty quantification of response parameters given the inputs and random variables.

#. Forward Uncertainty Propagation

     A. Dakota Options

        #. Monte Carlo Sampling (MCS)
        #. Latin Hypercube Sampling (LHS)
        #. Gaussian Process Regression
        #. Polynomial Chaos Expansion

     B. SimCenterUQ Options

        #. Monte Carlo Sampling (MCS)

           a. Resampling from an existing correlated dataset

        #. :blue:`Multi-fidelity Monte Carlo (MFMC)`

#. Global Sensitivity Analysis

     A. Dakota Sensitivity Options

        #. MCS
        #. LHS

     B. SimCenterUQ Sensitivity Options

        #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

           a. Importing input/output samples from data files

#. Surrogate Modeling

     A. SimCenterUQ Engine Surrogate Options:

        #. Probabilistic Learning on Manifolds (PLoM)
        #. Gaussian Process Modeling