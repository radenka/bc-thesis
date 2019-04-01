from attyc.classifier import Classifier


class HybridClassifier(Classifier):
    def __init__(self, input_sdf, SMARTS_and_atom_types):
        super().__init__(input_sdf, SMARTS_and_atom_types)

    def get_hybridization(self, atom):
        return f'{atom.GetSymbol()}#{str(atom.GetHybridization())}'

    def classify_atoms(self):
        for mol in self.supplier:
            atom_types = []
            for i in range(mol.GetNumAtoms()):
                atom_types.append(self.get_hybridization(mol.GetAtomWithIdx(i)))
            self.all_atom_types.append(atom_types)
