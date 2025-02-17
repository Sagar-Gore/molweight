import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors

#loading the molecular data into python dataframe 
mol_data = pd.read_csv('UFZWANATARG_11082019.csv')


#Use RDKit to caculate molecular weight - use SMILES identifier
for smi in mol_data['SMILES']:
	try:
		mw = Descriptors.MolWt(Chem.MolFromSmiles(smi)) # Average molecular weight 
		mw_exact = Descriptors.ExactMolWt(Chem.MolFromSmiles(smi)) # Exact molecular weight  
		print (smi, mw, mw_exact)
	except:
		print ("SMILES not found")
