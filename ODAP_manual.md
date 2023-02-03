---
title: ODAP Overview
---

<!--
pandoc ODAP_manual.md --toc --filter pandoc-crossref --reference-doc ../_branding/odap-style.docx -o auto-generated/ODAP_manual.docx 
-->

# ODAP Overview

> *This is a shared description for the internal team of the core purpose, scope, operational components, and governance structure of the ODAP. It provides an introduction, plan and a reference.*

## Introduction

ODAP is long term, UK wide, 4 nations outbreak response infrastructure providing the unique and scalable capabilities of the academic sector to tackle public health challenges.  ODAP creates a UK-wide capability by curating and linking outbreak relevant data from clinical records, research studies and audit data. It brings together key initiatives and leadership across the UK including ISARIC, COG-UK, MRC CLIMB and GenOMICC. The platform combines a national Trusted Research Environment (TRE) infrastructure collocated with \>£100M of world-class computational and data science capacity including the UK National Supercomputer, with a UK-wide governance framework.

## What is the Outbreak Data Analysis Platform (ODAP)?

The ODAP is the overarching term for a range of computers supporting research within a specific scope. These include the ODAP TRE (formerly called: flexible compute space; ultra; ultra2), and various project spaces in the National Safe Haven. 

It has two components:

1.  The ODAP Core. *Getting fast answers to important public health research questions.* ODAP Core is a complicated network of overlapping, linked data from research studies and national datasets, created through a range of independent research activities, sitting in multiple computer systems. These datasets are linked through the ISARIC Clinical Characterisation Protocol (CCP). 
    - Purpose: to prepare for and support urgent public health research.
    - Access: data are openly accessible to appropriately-qualified researchers studying questions within the scope of the platform by individual agreement with the data providers. Much of the data is under embargo and publication of results requires consent from the data providers. Put simply, access is open but not easy.
    - Funding: The core ODAP is funded by the Baillie Gifford Pandemic Science Hub. 

2.  ODAP Open - *Making data access easy for approved researchers.* ODAP Open describes a robust, fully-staffed data access governance system to lower the barrier to entry by allowing FAIR data access within the 5 safes framework.
    - Funding: not in place. Funding from HDR UK infrastructure team is anticipated. 
    - Leadership: open call for a senior appointment when funding is available.
    - Access: data are openly accessible to appropriately-qualified researchers studying questions within the scope of the platform following a single, streamlined application

The foundation for the ODAP is the International Severe Acute Respiratory Infection Consortium (ISARIC) Clinical Characterisation Protocol (CCP).

# ODAP Core

## Scope of the ODAP

**The purpose of the ODAP is to facilitate biomedical research to advance understanding of severe infectious disease\* and other exposures of public health interest.\*\* Research within the ODAP is strictly limited to this purpose.**

\* Severe infectious disease - this term describes all severe infectious agents, including new, re-emerging or therapy-resistant forms of existing infectious agents.

\*\* Other exposures of public health interest: this term describes new or unexplained poisoning, or exposure to harmful energy sources such as electromagnetic radiation.

Examples of in-scope research:
- Understanding the evolution and biology of SARS-CoV-2.
- Understanding the epidemiology and transmission of SARS-CoV-2.
- Understanding COVID-19 disease risk, severity and outcomes.
- Monitoring and understanding the impact of non-pharmacological interventions against SARS-CoV-2 transmissions and COVID-19 disease.
- Monitoring, understanding, and assessing the impact of treatments, vaccines and prior infections in COVID-19 disease.
- Analysing or modelling SARS-CoV-2 and COVID-19 data for future pandemic preparedness.

Examples of out of scope activities
- Their research questions primarily focusses on a non-infectious disease area with incidental involvement of infectious disease 
(Focussed on a pathogen with no potential public health concern)

## ISARIC Clinical Characterisation Protocol (CCP)

The scope of the ODAP mirrors the objective of the CCP, an ethically-approved research study in the UK (Joint Chief Investigators: Calum Semple(Liverpool, Oxford) and Kenneth Baillie (Edinburgh, Oxford)). A broad range of scientists with relevant expertise have come together to form a UK-wide group: the ISARIC Comprehensive Clinical Characterisation Collaboration. Membership of this collaboration is by invitation and is extended to researchers performing high-quality biomedical research to advance understanding of severe infectious disease and other exposures of public health interest.

### The ISARIC Spine

Some studies, addressing aims that are within the scope of the CCP, have chosen to contribute data into the ODAP for linkage to CCP and other datasets. Because these studies are addressing questions that are directly within the scope of the CCP, where appropriate, participants in these studies are eligible to be enrolled under the CCP. 

Under our existing protocol and approvals for the ISARIC CCP, we have recruited over 300,000 Covid patients without explicit consent, into an observational study, with clear and specific aims. We are now linking this data to other studies, including consented studies such as GenOMICC and RECOVERY, and non-consented studies such as COG-UK viral sequencing.

Applying the established governance and data handling procedures for the ISARIC CCP to the additional linked data from these studies will enable cross-cutting research, all within the specific aims of the CCP. To achieve this, we have agreed to recruit all patients in the following studies into the ISARIC CCP, if they are known to meet the inclusion criteria for the CCP:

- GenOMICC
- RECOVERY
- PHOSP
- COG-UK
- HEAL-COVID

In each case, we will only recruit patients who meet the inclusion criteria for CCP. In our view, there is no ethical or information governance difference between recruiting a patient remotely from a hospital, or recruiting them remotely from within our trusted research environment. This has been agreed with the ISARIC CCP study sponsor and is explicitly stated in CAG and PBPP applications.

### Examples

The ISARIC4C consortium will incorporate participants from other studies into ISARIC4C study, creating a superset of participants in a single "spine". Doing so would allow them to match to NHS data under existing ISARIC4C data agreements.

To do this, we need to have an ID and an NHS number, or CHI number, as a minimum standard. Some participants in the other studies may already be in ISARIC4C. These need to be identified and tagged as being the same individual. This will be done by comparison of NHS or CHI numbers. The spine will contain all the joins between projects and participants. Those participants that are not already in the ISARIC4C system will have an ISARIC4C ID allocated to them.

The data from the spine will be used for several purposes:

-   it will feed into the NHS Digital data matching system. This system requires ID, NHS number, date of birth and postcode (the latter two are optional). This will allow the ongoing monthly matching of study participants to English & Welsh Health Data for the superset of ISARIC4C participants.

-   it will allow study participants to be identified against a cohort of NHS or CHI numbers for individual research studies, and as requested by Trusted Research Environments (TREs).

Currently the data for participants in these studies are held in a series of REDCap databases. These are the source of truth for the data and update on a regular basis. We will therefore need a process to update the spine from these sources.

## Computer architecture

The ODAP consists of two main compute areas. 

## Flexible Compute Space

The Flexible Compute Space (FCS) is a Trusted Research Environment with large scale compute capacity and access to a range of software tools for data analysis and machine learning. Data within the FCS can be either under embargo, or not under embargo. 

Access to the FCS is provided to researchers through *private project zones*

## PHS National Safe Haven

Some data remains within the PHS National Safe Haven but will transfer to the FCS on completion of the Systems Security Policy.

## Data ingress

Data are linked into the ISARIC Spine using the patient's NHS number by PHS before transfer to the FCS. 

## API

There will be a secure API in place from the Flexible Compute Space to External TREs and UK Public Health Agencies. This is to accelerate research by enabling data linkage across multiple data sets using unique identifiers to facilitate secure transfer of specified data fields e.g., viral sequencing data. The future purpose of the API is more in line with providing a mechanism for quick pandemic updates to national health services.

## Data Contributors

Each data contributor will explicitly consent to the lifting of any embargo on their data. A permanent record of these instructions will be held in a shared file. <!--FILE PATH TO MASTER RECORD OF EMBARGO STATUS IN SECURE LOCAION XXX -->

## Dataset map

A live [ODAP datasets mapping.xlsx](https://uoe.sharepoint.com/:x:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/ODAP/_documents/ODAP%20datasets%20mapping.xlsx?d=w1dde5dbd6a094799b1595de102fa3818&csf=1&web=1&e=coUYiB) is available for reference. \[Further details about processes and approvals to be added\]

A parallel document exists for [eDRIS](https://uoe.sharepoint.com/:x:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/Research%20Projects/ISARIC%20eDRIS%20Projects.xlsx?d=w8624bebadf7f491abc6add8587a039d8&csf=1&web=1&e=npUB8k)

Applications and approved users are found here: https://uoe.sharepoint.com/:x:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/IDAMAC/IDAMAC_Requests_Pipeline.xlsx?d=w7431f37efd1e4f53acfb2753fc03104f&csf=1&web=1&e=S0Bit5


Dataset lists and embargo status is recorded here: XXX

# OPAP Open

Once the embargo is lifted by a data contributor, data provision will be *FAIR* (Findable, Accessible, Interoperable, Reusable) and access will adhere to the *five safes* principles:

- Safe data: data is treated to protect any confidentiality concerns.
- Safe projects: research projects are approved by data owners for the public good.
- Safe people: researchers are trained and authorised to use data safely.
- Safe settings: a SecureLab environment prevents unauthorised use.
- Safe outputs: screened and approved outputs that are non-disclosive.





