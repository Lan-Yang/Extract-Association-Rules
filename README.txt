1. Team
Peng Song
Lan Yang

2. Files:
apriori.py						#python program
INTEGRATED-DATASET.csv			#integrated-dataset file
example-run.txt					#output of the interesting sample run
README.txt						#README file

3. Data Set Definition

a) which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file:

The dataset comes from "Parking Violations Issued - Fiscal Year 2014 (August 2013 – June 2014)", which is available at:
https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2014-August-/jt7v-77mi

b) what (high-level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file

We chose some of the columns from the original dataset, deleted rest of the columns, the columns remained are:

Plate Type, Violation Code, Vehicle Body Type, Vehicle Make, Issuing Agency, Violation County, Vehicle Color, Vehicle Year

We also deleted all the entries that contains an empty cell in it.

Then we take the first 5000 entry in the table and output it as INTEGRATED-DATASET.csv 

4. Description of Running:

To run out program, run the following commands
$python apriori.py <integrated-dataset file name> <min_support> <min_conf>

or

$python apriori.py <integrated-dataset file name>
$Minimum Support (between 0 and 1): <min_support>
$Minimum Confidence (between 0 and 1): <min_conf>

5. Internal Design:

First, we read input file and get original item set (item_set) and row
information (row_list).

Next, we follow a-priori algorithm to generate frequent itemsets. Suppose current
set C_k contains the frequent itemset of exactly k elements. We join each itemset
from C_k and the other itemsets from C_k to generate itemset with (k+1) elements.
Meanwhile, we record frequencies of those newly-generated itemsets. Then, we
filter those itemsets by min_support and update C_(k+1) to only contain frequent
itemsets of exactly (k+1) elements.

Then, we generate rules from (k > 1) itemsets and calculate their confidence to
get strong confidence rules.

In the end, we write results of frequent itemsets and rules of strong confidence
into "output.txt"

6. Sample run

Run the program in the command line as follows:

$ python apriori.py data/INTEGRATED-DATASET.csv 0.2 0.8

According to the example-run.txt file we produced, here are some of the interesting rules we can infer:

1. [SDN] => [PAS] (Conf: 92.7777777778%, Supp: 30.06%): SDN is Vehicle Body Type - sedan, while PAS is Plate Type - Passenger Vehicles. So that means if a vehicle is sedan, it is very likely to have a passenger vehicle plate, and that is consistent with our common believe.

2. [SUBN] => [PAS] (Conf: 90.6624102155%, Supp: 22.72%): SUBN is Vehicle Body Type, which includes Ambulance, Bus, Camper, Carryall, Coach, Hearse, Micro Bus, Station Bus, Station Wagon, Travelall Wagon. (See definition here: http://firetesttaking.com/pdfs/auc/162.pdf) And PAS is Plate Type "Passenger Vehicles". So if a vehicle is one of the above, it is also highly likely to have a passenger vehicle plate.

3. [VAN] => [COM] (Conf: 87.8892733564%, Supp: 20.32%): VAN is Vehicle Body Type, van. COM is Plate Type, which stands for Commercial Vehicles. So we can infer that if a vehicle is a van, it is highly likely to be a commercial vehicle, or posess a commercial vehicles plate.

Reference: Definition of Plate Type
http://dmv.ny.gov/registration/registration-class-codes

