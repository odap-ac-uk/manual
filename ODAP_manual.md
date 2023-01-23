---
title: ODAP Manual
---

<!--
pandoc ODAP_manual.md --toc --filter pandoc-crossref --reference-doc ../_branding/odap-style.docx -o auto-generated/ODAP_manual.docx 
-->

**This PROJECT INITIATION DOCUMENT is a shared description for the internal team of the core purpose, scope, operational components, and governance structure of the ODAP. It provides an introduction and a reference.**

# What is the Outbreak Data Analysis Platform (ODAP)?

The ODAP is the overarching term for a range of computers supporting research within a specific scope. These include the ODAP TRE (formerly called: flexible compute space; ultra; ultra2), and various project spaces in the National Safe Haven.

It is divided into two sections:

1.  The "UNDER EMBARGO" section -- in which data are wholly controlled by contributors
2.  The "NO EMBARGO" section -- in which data are accessible to appropriately-qualified researchers studying questions within the scope of the platform

The foundation for the ODAP is the International Severe Acute Respiratory Infection Consortium (ISARIC) Clinical Characterisation Protocol (CCP).

## Core principles of the ODAP

ODAP is long term, UK wide, 4 nations outbreak response infrastructure providing the unique and scalable capabilities of the academic sector to tackle public health challenges. 

Ultimately, once the embargo is lifted by a data contributor, data provision will be *FAIR* (Findable, Accessible, Interoperable, Reusable) and access will adhere to the *five safes* principles:

- Safe data: data is treated to protect any confidentiality concerns.
- Safe projects: research projects are approved by data owners for the public good.
- Safe people: researchers are trained and authorised to use data safely.
- Safe settings: a SecureLab environment prevents unauthorised use.
- Safe outputs: screened and approved outputs that are non-disclosive.


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

# ISARIC Clinical Characterisation Protocol (CCP)

The scope of the ODAP mirrors the objective of the CCP, an ethically-approved research study in the UK (Joint Chief Investigators: Calum Semple(Liverpool, Oxford) and Kenneth Baillie (Edinburgh, Oxford)). A broad range of scientists with relevant expertise have come together to form a UK-wide group: the ISARIC Comprehensive Clinical Characterisation Collaboration. Membership of this collaboration is by invitation and is extended to researchers performing high-quality biomedical research to advance understanding of severe infectious disease and other exposures of public health interest.

## The ISARIC Spine

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

<!--

Source: AL, updates from JH, MC

>     Kenny, clarification: Everyone in the study will be added to the spine, those without infectious diseases are still relevant as controls.
>
> Does the API transfer need to be a separate section? How will be it relevant to this manual?
>
> ODAP query API;\
> Moni, question: Is the ODAP API a dependency for the Spine?\
> Rob: No, they're related but separate concerns.

-->


# Computer architecture

The ODAP consists of two main compute areas. 

## Flexible Compute Space

The Flexible Compute Space (FCS) is a Trusted Research Environment with large scale compute capacity and access to a range of software tools for data analysis and machine learning. Data within the FCS can be either under embargo, or not under embargo. 

Access to the FCS is provided to researchers through *private project zones*

## PHS National Safe Haven

Data within the National Safe Haven can be either under embargo, or not under embargo. 

Embargo area is data not yet published or available for use, non-embargoed is data that can be accessed by bona fide researchers with no DSA required.


## API

There will be a secure API in place from the Flexible Compute Space to External TREs and UK Public Health Agencies. This is to accelerate research by enabling data linkage across multiple data sets using unique identifiers to facilitate secure transfer of specified data fields e.g., viral sequencing data. The future purpose of the API is more in line with providing a mechanism for quick pandemic updates to national health services.


## Data tranfers

The preferred way to move data between another TRE and ODAP are the already established methods for that TRE.

# Governance

## Summary

- ODAP Partnership steering group to provide strategic direction, support, and challenge to ODAP delivery team, data contributors, and other agencies, to ensure deliverables are on track and University of Edinburgh accountable.
- The University of Edinburgh is the lead institution for ODAP and is responsible to each individual funder for delivering on agreed milestones (including HDR UK, the Data and Connectivity National Core Studies, and UKRI)
- ODAP Delivery Group (University of Edinburgh team) is responsible for operational delivery, and secreterial support to ODAP Steering group, ODAP Data Access Governance Committee, and ODAP Project Review Panel.
- ODAP Data Access Governance Committee to approve the ODAP information governance processes for non-embargo data proposed by the Lead Institute
- ODAP Project Review Panel to ensure compliance with the 5 safes, for non-embargo data particularly safe projects - providing scientific review for applications for data use and approve/refer/reject data access requests for the Outbreak Data Analysis Platform.

## Background

ODAP creates a UK-wide capability by curating and linking outbreak relevant data from clinical records, research studies and audit data. It brings together key initiatives and leadership across the UK including ISARIC, COG-UK, MRC CLIMB and GenOMICC.

The platform combines a national Trusted Research Environment (TRE) infrastructure collocated with \>£100M of world-class computational and data science capacity including the UK National Supercomputer, with a UK-wide governance framework.


## The ODAP Partnership Steering Group

The ODAP Partnership is a UK-wide body which decides on strategic matters to facilitate vital research, supporting additional data linkages, and democratising access to research datasets with full agreement from the contributing studies.

The Partnership aims to strengthen the UK-wide NHS/academic partnership between the CLIMB COVID viral sequence analysis system, the Outbreak Data Analysis Platform, ISARIC-4C, COG-UK, the four UK Public Health Agencies, ICNARC, ONS and HDR UK.

The ODAP Partnership steering group exists to provide advice, support and challenge to ODAP delivery team and will have voting rights on decisions not made by consensus.

## The ODAP Delivery Team

ODAP Delivery team to report progress to Data and Connectivity Delivery Group

## Specific Roles

University of Edinburgh (as the lead institution for ODAP) is accountable to Health Data Research UK for the delivery of ODAP. 

HDRUK is accountable to UKRI for delivery of the Data and Connectivity National Core Study

<!--Source: HDR UK slides (various)-->

## Data management

1.  The Lead Institute will become a Data Controller to facilitate the onboarding of key data sets to the ODAP and to facilitate external access to ODAP only.

2.  All Data Contributors (those who hold the key data sets) will sign a Data Contributor Agreement (DCA) with the Lead Institution for the following purposes:

    -   To allow the Lead Institute to onboard, curate and link the data using ODAP.

        -   The Lead Institution will manage process to enable access to data however Data Contributor must give permission.

    -   This Data Contributor Agreement will require a due diligence process to ensure any data can be accessed by researchers for the agreed purposes. These agreed purposes will clearly articulated and decided with public/patient input.

3.  This access facilitated through the Gateway using the 5 safes data access form.

    -   This governance structure sets out appropriate safeguards for privacy and effective use of sensitive data when it is embedded throughout each stage of a project

4.  The Lead Institution + Data Contributor can together approve researchers access to data on ODAP if:

    -   Research is for already agreed purpose. There will be specific research purposes detailed in the DCA which will all relate to patient outcomes.

    -   Any linkage has been detailed in the methodology and is in an approved format. This may include only exporting certain agreed data points such as a co-morbidity score, vaccination status, covid-19 severity score, and/or outcomes.

    -   All aspects of the project satisfies the 5 safes.

5.  If a request is outside of the agreed purposes the Lead Institution will go back to Data Contributor and request permission.

    -   This should be done either through a Data Access Committee formed between the Data Contributors or by the relevant Data Contributor only. The DAC should include public/patient representatives.

    -   New project approvals will always be subject to the Data Contributors approval and a DAC should be convened of Data Contributors whose data is involves.

6.  The Lead Institution will sign a Data Access Agreement with any Institutions accessing the data).

7.  All aspects of any projects will be subject to clear, transparent and detailed processes.

8.  The Data Contributor will remain a Data Controller of their data sets. Lead Institution becomes independent controller for facilitating access and onboarding to ODAP only.


<!-- below section is probably out of scope for the manual and should be moved/integrated elsewhere [JKB] -->

# Information for data contributors

## How do I add my dataset (within scope) into ODAP?

Check the scope

Within scope, arrange a discussion by emailing: <ODAP@ed.ac.uk>

Speak with the ODAP team

Agree what data and where it needs to be hosted: clinical consented data SNSH TRE and/or analysis data ODAP TRE

Does the dataset need to be linked with other datasets? Scottish health data; English health data

Can the dataset be added to the ISARIC Spine?

ODAP team will advise on most appropriate agreement: joint data controller; data processor

Agreements executed/signed off

Data to be transferred into ODAP and added to spine and/or

Refer to the the ICODA due diligence: [https://icoda-research.org/hdr-uk-as-data-controller-for-icoda, for incoming: 1](https://icoda-research.org/hdr-uk-as-data-controller-for-icoda,%20for%20incoming:%201). Datasets 2. Legal basis for use 3. Ethical review 4. Public and patient review

# Access for data analysts

## What are the datasets are available for research analyses? What process(es) must I follow? What approvals must I obtain?

A live [ODAP datasets mapping.xlsx](https://uoe.sharepoint.com/:x:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/ODAP/_documents/ODAP%20datasets%20mapping.xlsx?d=w1dde5dbd6a094799b1595de102fa3818&csf=1&web=1&e=coUYiB) is available for reference. \[Further details about processes and approvals to be added\]

A parallel document exists for [eDRIS](https://uoe.sharepoint.com/:x:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/Research%20Projects/ISARIC%20eDRIS%20Projects.xlsx?d=w8624bebadf7f491abc6add8587a039d8&csf=1&web=1&e=npUB8k)


<!--
So can you include another side for the embargo area? Most data will enter via it. 
Access to any data in embargo section is filtered by secretariat (to remove out of scope) and then approved by the data contributor. That\'s the entire process. 
-->
<!--
For ISARIC4C that\'s Kenny and Calum as joint CIs. For the other studies it is different people.
Under consortium arrangements (ISARIC4C; PHOSP; COG-UK; GenOMINCC)
The process in the embargo area is simple: 

1.  Request for collaborative analysis approved by data contributor. 

2.  Access provided.


Write it out: [ISARIC4C Data Access Process.pdf](https://uoe.sharepoint.com/:b:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/IDAMAC/ISARIC4C%20Access/ISARIC4C%20Data%20Access%20Process.pdf?csf=1&web=1&e=32JQ6o)
-->

<!--Source: EM-->

# Process for Application for data access for non-embargoed data

1.  Details of the dataset will be published on the ODAP website; HDR UK Innovation Gateway and/or the data controller's website. HDR-UK will ensure that appropriately trained researchers (and not just COG-UK or ISARIC4C) can easily access data.

2.  Researchers will submit initial data request via the HDR UK Innovation Gateway.

3.  Applications will be discussed informally with (i) the data processor (ODAP Data Management and Monitoring Team), and (ii) with the data controller (i.e. UKHSA).

4.  Applications will complete the full 'Five Safes' form and submits it via the HDR UK Innovation Gateway.

**TRIAGE/APPROVAL**:

5.  The ODAP Internal Triage Secretariat (i.e. the ODAP Data Management and Monitoring Team) will review and triage applications based on the 'Five Safes' form. If required, data requests will be discussed with requestors.

6.  Data access approval is required from two sources:

    a.  The ODAP Internal Triage Secretariat or the ODAP Data Access Committee

    b.  The data controller (i.e. UKHSA)

7.  The ODAP Internal Triage Secretariat or the full OPAP Data Access Committee, when deemed necessary for complex requests, shall approve or decline requests on behalf of ODAP. The OPAP Data Access Committee should always have sight of data access requests even if only for information.

    -   The data controller (i.e. UKHSA) will be sent details of all ODAP approved requests. Where UKHSA is joint controller, requests will be sent to a central UKHSA coordinator generic in-box; [Covid19genomics@phe.gov.uk](mailto:Covid19genomics@phe.gov.uk).

    -   Where UKHSA is a joint controller, UKHSA coordinator arranges the UKHSA response on whether approval is granted for specific projects to access genomic data. 

        -   The response will be made within 7-days

        -   The UKHSA decision will be based on joint opinion of:

            -   Ian Harrison (Genomics data product owner)

            -   Sam Organ (Joint Chief Data Officer)

            -   Saheer Gharbia (Genomics Board)

**GOVERNANCE & LOGISTICS:**

8.  The ODAP Data Management and Monitoring Team initiate process for data access with eDRIS National Safe Haven) and/or Edinburgh (FCE)

9.  The ODAP Data Management and Monitoring Team

    a.  Prepares data sharing agreement between the requestor and data processor/controller and relevant contracts team

    b.  Ensures appropriate sign-off.

**DATA RELEASE FROM RELEVANT TRE:**

10. The ODAP Data Management and Monitoring Team will review figures and outputs of data analysis performed in the TRE before they are removed from the TRE .

11. For figures and outputs created using genomic data, the data controller (i.e. UKHSA) will also need to review and authorise removal of data.

3.  DATA CREATION PROCESS

**LINKAGE IDENTIFIER USED IN TRE (NATIONAL SAFE HAVEN AND FCE)**

-   ISARIC4C-ID will be used as the unique identifier. ALL COG participants will be enrolled into ISARIC4C.  This means that the ISARIC4C-ID can be used and we can link to NHSD health records

-   Data compartmentalised within EPCC prevents data being linked to other datasets held by EPCC without approval. EPCC environment prevents copying or removal of data from the relevant TRE.


# How can I transfer my data files...? (not outputs but for further analyses)

Refer to: [ISARIC4C Data Transfer Processv1.docx](https://uoe.sharepoint.com/:w:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/IDAMAC/Documentation/ISARIC4C%20Data%20Transfer%20Processv1.docx?d=wd5006b07d2da43d4a511a8528fb052a0&csf=1&web=1&e=TPoXoG)

# How can I get outputs from ODAP?

Refer to:

[NA National Safe Haven Statistical Disclosure v5.docx](https://uoe.sharepoint.com/:w:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/IDAMAC/Documentation/NA%20National%20Safe%20Haven%20Statistical%20Disclosure%20v5.docx?d=w8e62494d77674ec99dd25a5b3eed5844&csf=1&web=1&e=NMtbB8)

[FCS Output Request Form - 20220608.docx](https://uoe.sharepoint.com/:w:/r/sites/ISARIC4C/DataInfrastructureAndGovernance/IDAMAC/Documentation/FCS%20Output%20Request%20Form%20-%2020220608.docx?d=w4c6e0d65713742ff92f4464c98053a99&csf=1&web=1&e=5OgOQQ)

# How is ODAP communicated? Where can I refer people to about ODAP?

Discoverability:

HDR UK Innovation Gateway

-   CO-CONNECT:  

    -   CO-CONNECT is HDR UK programme: limited number of cohorts from ISARIC4C
