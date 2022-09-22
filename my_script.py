import sys
import math

# cast the system argument as a numeric value
number = int(sys.argv[1])
number_processed = (math.pow(number,2) * math.pi)
print("\nResult: {}\n".format(str(number_processed)))