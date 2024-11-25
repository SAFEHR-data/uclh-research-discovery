---
layout: project
title: MS-PINPOINT
status: ongoing
authors:
  - Benjamin Ford
  - Arman Eshaghi
  - Johnathan Stutters
tabs:
- {
  name: descriptive_data,
  source: data.html,
  label: Dataset Overview
  }
---

MS-PINPOINT is a multi-centre project developing healthcare tools to aid in the treatment of patients with Multiple Sclerosis. Based at UCL, we develop tools for segmenting MS-typical lesions in brain and spinal cord MRI, as well as tools that use electronic health record data to model how individual patients will respond to the range of treatment options available.

To support these endeavours we use MRI and EHR data obtained as part of routine care. In this datacard we provide an overview of the structured data that we store, as free-text data is highly identifiable and cannot be shared in a way that guarantees patient privacy while retaining semblance of the original data.

More info about MS-PINPOINT can be found at: https://www.ms-pinpoint.com/
## Data Format

We present 3 types of data in this datacard. Data Description describes the categories of patient data we store in parquet files exported directly from Epic EHR service. Ranges as well as means and standard deviations are supplied for the fields in which this applies. We also report the frequencies of entries for certain fields in Distribution of Values. This datasheet shows the frequency with which different OMOP concepts are observed, and can also inform about the demographics of our dataset. In line with privacy guidelines, entries which occur 5 times or less have been removed. We also supply purely representative examples of the parquet files we export, in csv form. These are only representative as cannot release certain fields such as measurement values, or model the interrelationships between different fields due to the risk of patient data exposure.

## Purpose of this Datacard

We hope that this datacard aids us in keeping our research transparent to both patients and members of the research community. This datacard gives a brief insight into the scope of our dataset and we hope provides an avenue for collaboration with researchers whose questions can be addressed by our dataset