import pandas as pd
import numpy as np
import dataImport

(train,test) = dataImport.dataImportNaiveBayes()

print (train.info())
print (test.info())