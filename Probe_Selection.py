"""Probe_Selection.py will pull all variants from the CIViC Knowledgebase and subdivide them into different folders.  These folders will include:
Not_Evaluated: Probes that will not be evaluated in the Biomarker Capture Panel
NanoString_Probes_Needed: Probes that will need to be evaluated using NanoString Technology
Capture_Sequence_Probes_Needed: Probes that will need to be evaluated using Capture-Sequencing Technology
Biomarker_Probe_Already_Created: Probe that have already been designed and validated

Usage: Probe_Selection.py



"""

#Pull in Data from JSON
#!/usr/bin/env python3
import json, requests

variant_dict = {}

variant_list = requests.get('https://civic.genome.wustl.edu/api/variants?count=1000000000').json()['records']

Nanostring = []

for current_variant in range(0, len(variant_list)):
    if variant_list[current_variant]['coordinates']['chromosome2'] is not None:
        print(variant_list[current_variant]['coordinates']['chromosome2'])
        #bob
        Nanostring.append([variant_list[current_variant]['coordinates']['chromosome2'],variant_list[current_variant]['coordinates']['chromosome']])
#    variant_dict[variant_list[current_variant]["name"]] = gene_list[current_variant]

print(Nanostring)


"""

#Create Buckets Variants for Evaluation
Not_Evaluated = []
NanoString_Probes_Needed = []
Capture_Sequence_Probes_Needed = []
Biomarker_Probe_Already_Created = []

#Pull Information from CIVIC
all_genes = []
genes = []
variants = []
chromosomes_1 = []
starts_1 = []
stops_1 = []
chromosomes_2 = []
starts_2 = []
stops_2 = []
probe = []
evidence_rating = []
trust_rating = []

#Filter out variants into Not_Evaluated
	#Criteria: 1. At least 1 B rating evidence items
	#Criteria: 2. At least 1 Trust Rating of 3 Stars
	#Criteria 3. At least 2 Accepted Evidence Items per Variant



#Bucket Variants that Already Have Probe Designs
#Bucket Fusion Proteins and RNA dysregulation into NanoString_Probes_Needed
#Bucket other variants into Capture_Sequence_Probes_Needed

for i in range len(genes):
	gene = gene(i)
	variant = variant(i)	
	chromosome_1 = chromosomes_1(i)	
	start_1 = starts_1(i)	
	stop_1 = stops_1(i)	
	chromosome_2 = chromosomes_2(i)	
	start_2 = starts_2(i)	
	stop_2 = stops_2(i)
	probe = probes(i)
	if probe == “YES”
		Biomarker_Probe_Already_Created.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	elif chromosome_2 > 0:
		NanoString_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	elif variant == “*FUSION*”:
		NanoString_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	elif variant == “AMPLIFICATION”:
		NanoString_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	elif variant == “*EXPRESSION”:
		NanoString_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	elif variant == “LOSS”
		NanoString_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)
	else:
		Capture_Sequence_Probes_Needed.append(gene, variant, chromosome_1, start_1, stop_1, chromosome_2, start_2, stop_2)


#Create Output for Probe Design

First, create a variable that opens a writeable file:
`bucket_1 = open('actual_file_name', "w")`
Second, write whatever you want to the file:
`print('my_string_of_info_here', file = bucket_1)`
OR
`bucket_1.write('my_string_of_info_here')`
LAST (at end of entire code), close your file:
`bucket_1.close()`


"""






