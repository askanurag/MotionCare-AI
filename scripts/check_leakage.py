from healthcare_ai.synthetic import generate
from healthcare_ai.splits import split
from healthcare_ai.leakage import assert_disjoint
print('Patient partitions disjoint:',assert_disjoint(*split(generate())))
