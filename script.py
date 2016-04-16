import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

from location import Location
from transaction import Transaction
from fare import Fare

all_transactions = []
with open('dataset_50.csv') as data_f:
	for line in data_f:
		line_list = line.split(',')
		# Intialize pickup location
		pickup_location = Location(line_list[1], line_list[0], 0, 'P')
		# Initialize drop-ff location
		dropoff_location = Location(line_list[3], line_list[2], 0, 'D')
		# Intialize fare 
		fare = Fare(line_list[6], line_list[9], line_list[10], line_list[13], line_list[14])
		# Finally, the transaction itself
		transaction = Transaction(pickup_location, dropoff_location, fare, line_list[4], line_list[5])
		all_transactions.append(transaction)

print(all_transactions)

# coordinates= np.array([[40.68075562,-73.95561981],
# [40.69169617,-73.99147034],
# [40.759552,-73.83067322],
# [40.68760681,-73.94764709],
# [40.8085289,-73.94487762],
# [40.81087875,-73.95250702],
# [40.82391357,-73.91757202],
# [40.82083511,-73.95436859],
# [40.71453857,-73.94947815],
# [40.74377441,-73.92160034],
# [40.71666336,-73.95684052],
# [40.7181778,-73.95733643],
# [40.710186,-73.96353912],
# [40.8598938,-73.92694855],
# [40.7897377,-73.95245361],
# [40.81296158,-73.95606232],
# [40.8118782,-73.95149994],
# [40.8055687,-73.96198273],
# [40.79628372,-73.94761658],
# [40.82255936,-73.94954681],
# [40.8101387,-73.95313263],
# [40.67615128,-73.98065186],
# [40.74684143,-73.89089203],
# [40.67601013,-73.9499588],
# [40.74530029,-73.90348816],
# [40.74648285,-73.89083099],
# [40.7052269,-73.94450378],
# [40.72105789,-73.84414673],
# [40.71607208,-73.95188141],
# [40.70385742,-73.91835785],
# [40.71659851,-73.95690918],
# [40.77521515,-73.91178131],
# [40.77513123,-73.91189575],
# [40.84978867,-73.90602112],
# [40.63173294,-73.94686127],
# [40.67970276,-73.98217773],
# [40.71690369,-73.95880127],
# [40.67470169,-73.97053528],
# [40.75816727,-73.93750763],
# [40.82504654,-73.94039154],
# [40.68954086,-73.99227142],
# [40.73368073,-73.9548645],
# [40.81512833,-73.92433929],
# [40.80470657,-73.93812561],
# [40.72822189,-73.87099457],
# [40.76861572,-73.91121674],
# [40.6859169,-73.97332001],
# [40.7141571,-73.95600128],
# [40.71670914,-73.96107483],
#            ])
# x = kmeans2(whiten(coordinates), 3, iter = 20)  
# print(x)
# plt.scatter(coordinates[:,0], coordinates[:,1], c=y);plt.show()