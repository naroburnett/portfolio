def make_periodic_table():
    periodic_table_dict = {
        # [symbol, name, atomic_mass]
    "Ac":	["Actinium",	227],
    "Ag":	["Silver",	107.8682],
    "Al":	["Aluminum",	26.9815386],
    "Am":	["Americium",	243],
    "Ar":	["Argon",	39.948],
    "As":	["Arsenic",	74.9216],
    "At":	["Astatine",	210],
    "Au":	["Gold",	196.966569],
    "B":	["Boron",	10.811],
    "Ba":	["Barium",	137.327],
    "Be":	["Beryllium",	9.012182],
    "Bh":	["Bohrium",	272],
    "Bi":	["Bismuth",	208.9804],
    "Bk":	["Berkelium",	247],
    "Br":	["Bromine",	79.904],
    "C":	["Carbon",	12.0107],
    "Ca":	["Calcium",	40.078],
    "Cd":	["Cadmium",	112.411],
    "Ce":	["Cerium",	140.116],
    "Cf":	["Californium",	251],
    "Cl":	["Chlorine",	35.453],
    "Cm":	["Curium",	247],
    "Cn":	["Copernicium",	285],
    "Co":	["Cobalt",	58.933195],
    "Cr":	["Chromium",	51.9961],
    "Cs":	["Cesium",	132.9054519],
    "Cu":	["Copper",	63.546],
    "Db":	["Dubnium",	268],
    "Ds":	["Darmstadtium",	281],
    "Dy":	["Dysprosium",	162.5],
    "Er":	["Erbium",	167.259],
    "Es":	["Einsteinium",	252],
    "Eu":	["Europium",	151.964],
    "F":	["Fluorine",	18.9984032],
    "Fe":	["Iron",	55.845],
    "Fl":	["Flerovium",	289],
    "Fm":	["Fermium",	257],
    "Fr":	["Francium",	223],
    "Ga":	["Gallium",	69.723],
    "Gd":	["Gadolinium",	157.25],
    "Ge":	["Germanium",	72.64],
    "H":	["Hydrogen",	1.00794],
    "He":	["Helium",	4.002602],
    "Hf":	["Hafnium",	178.49],
    "Hg":	["Mercury",	200.59],
    "Ho":	["Holmium",	164.93032],
    "Hs":	["Hassium",	270],
    "I":	["Iodine",	126.90447],
    "In":	["Indium",	114.818],
    "Ir":	["Iridium",	192.217],
    "K":	["Potassium",	39.0983],
    "Kr":	["Krypton",	83.798],
    "La":	["Lanthanum",	138.90547],
    "Li":	["Lithium",	6.941],
    "Lr":	["Lawrencium",	262],
    "Lu":	["Lutetium",	174.9668],
    "Lv":	["Livermorium",	293],
    "Mc":	["Moscovium",	288],
    "Md":	["Mendelevium",	258],
    "Mg":	["Magnesium",	24.305],
    "Mn":	["Manganese",	54.938045],
    "Mo":	["Molybdenum",	95.96],
    "Mt":	["Meitnerium",	276],
    "N":	["Nitrogen",	14.0067],
    "Na":	["Sodium",	22.98976928],
    "Nb":	["Niobium",	92.90638],
    "Nd":	["Neodymium",	144.242],
    "Ne":	["Neon",	20.1797],
    "Nh":	["Nihonium",	284],
    "Ni":	["Nickel",	58.6934],
    "No":	["Nobelium",	259],
    "Np":	["Neptunium",	237],
    "O":	["Oxygen",	15.9994],
    "Og":	["Oganesson",	294],
    "Os":	["Osmium",	190.23],
    "P":	["Phosphorus",	30.973762],
    "Pa":	["Protactinium",	231.03588],
    "Pb":	["Lead",	207.2],
    "Pd":	["Palladium",	106.42],
    "Pm":	["Promethium",	145],
    "Po":	["Polonium",	209],
    "Pr":	["Praseodymium",	140.90765],
    "Pt":	["Platinum",	195.084],
    "Pu":	["Plutonium",	244],
    "Ra":	["Radium",	226],
    "Rb":	["Rubidium",	85.4678],
    "Re":	["Rhenium",	186.207],
    "Rf":	["Rutherfordium",	267],
    "Rg":	["Roentgenium",	280],
    "Rh":	["Rhodium",	102.9055],
    "Rn":	["Radon",	222],
    "Ru":	["Ruthenium",	101.07],
    "S":	["Sulfur",	32.065],
    "Sb":	["Antimony",	121.76],
    "Sc":	["Scandium",	44.955912],
    "Se":	["Selenium",	78.96],
    "Sg":	["Seaborgium",	271],
    "Si":	["Silicon",	28.0855],
    "Sm":	["Samarium",	150.36],
    "Sn":	["Tin",	118.71],
    "Sr":	["Strontium",	87.62],
    "Ta":	["Tantalum",	180.94788],
    "Tb":	["Terbium",	158.92535],
    "Tc":	["Technetium",	98],
    "Te":	["Tellurium",	127.6],
    "Th":	["Thorium",	232.03806],
    "Ti":	["Titanium",	47.867],
    "Tl":	["Thallium",	204.3833],
    "Tm":	["Thulium",	168.93421],
    "Ts":	["Tennessine",	294],
    "U":	["Uranium",	238.02891],
    "V":	["Vanadium",	50.9415],
    "W":	["Tungsten",	183.84],
    "Xe":	["Xenon",	131.293],
    "Y":	["Yttrium",	88.90585],
    "Yb":	["Ytterbium",	173.054],
    "Zn":	["Zinc",	65.38],
    "Zr":	["Zirconium",	91.224]
    }

    return periodic_table_dict

def make_known_molecules_table():
    known_molecules_dict = {
        "Al2O3": ["aluminum oxide"],
        "CH3OH": ["methanol"],
        "C2H6O": ["ethanol"],
        "C2H5OH": ["ethanol"],
        "C3H8O": ["isopropyl alcohol"],
        "C3H8": ["propane"],
        "C4H10": ["butane"],
        "C6H6": ["benzene"],
        "C6H14": ["hexane"],
        "C8H18": ["octane"],
        "CH3(CH2)6CH3": ["octane"],
        "C13H18O2": ["ibuprofen"],
        "C13H16N2O2": ["melatonin"],
        "Fe2O3": ["iron oxide"],
        "FeS2": ["iron pyrite"],
        }
    return known_molecules_dict

class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """
    pass

def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]
    """
    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    elem_dict[symbol] = prev + group_dict[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError(
                            "invalid formula, unknown element symbol:",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError(
                        "invalid formula, unmatched close parenthesis:",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula:"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character:"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError(
                "invalid formula, unmatched open parenthesis:",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())

# These are the indexes of the
# elements in the periodic table.
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list. Each element in
    symbol_quantity_list is a list in the form: ["symbol", quantity].

    As an example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_mass = 0
    # For each element in the symbol_quantity_list:
    #   Split the element into symbol and quantity.
    for element in symbol_quantity_list:
        symbol = element[0]
        quantity = element[1]
    #   Get the atomic mass for the symbol.
        element_list = periodic_table_dict[symbol]
        atomic_mass = element_list[ATOMIC_MASS_INDEX]
    #   Multiply the atomic mass by the quantity.
        mass = atomic_mass * quantity
    #   Add the product into the total mass.
        total_mass += mass
    return total_mass
        
def num_moles(mass, total_mass):
    number_moles = mass / total_mass
    return number_moles
        
def user_input_formula():
    formula = input('Enter the molecular formula of the sample: ')
    return  formula

def user_input_mass():
    mass = float(input('Enter the mass in grams of the sample: '))
    return mass

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    """
    if formula in known_molecules_dict:
        compund_list = known_molecules_dict[formula]
        compound_name = compund_list[0]
        known = 1
    else:
        compound_name = 'unknown compound'
        known = 0
    
    return compound_name , known

def known_mol_update(formula, known, known_molecules_dict):
    def updating_name_input():
        compound_name = input('What is the name of the compound?(Please be carfule with spelling and capitlization): ')
        return compound_name

    if known == 1:
        return known_molecules_dict

    elif known == 0:
        print(f"Our system could not find the inputed compound {formula} in our list of known compounds.")
        recognized_name = input("Do you know its name?(Yes or No): ").lower()
        if recognized_name == "yes":
            willingness = input('would you like to help us with updating our known compound catalog?(Yes or No):' ).lower()
            if willingness == 'yes':
                while True:
                    compound_name = updating_name_input()
                    name_verified  = input(f'You inputed ---> {compound_name} <--- is this correct?(Yes or No):') .lower()
                    if name_verified != 'yes':
                        print("Please try tryping it again")
                    else:
                        break
                known_molecules_dict[formula] = [compound_name]
                print('Thank you for your contribution! Your input has been added to the catalog.')
                return known_molecules_dict
                 
                    
            else:
                print('No worries. Thank you for using our program.')
                return known_molecules_dict
        else: 
            print('No worries. Thank you for using our program.') 
            return known_molecules_dict


def main():
    # Get a chemical formula for a molecule from the user.
    formula = user_input_formula()

    # Get a mass in grams from the user.
    mass = user_input_mass()

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()

    #Call the make_known_molecules_table and
    #store the known molecules table in a variable
    known_mol_table_dict = make_known_molecules_table()

     #call get_formula_name function
    #determin if user inputed chemical formula exists
    #in known known_mol_table_dict
    compund_name, known = get_formula_name(formula, known_mol_table_dict)


    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    total_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

    # Compute the number of moles of the sample.
    number_moles = num_moles(mass, total_mass)

    known_mol_table_dict = known_mol_update(formula ,known, known_mol_table_dict)

    compund_name, known = get_formula_name(formula, known_mol_table_dict)

    #to add space
    print()

    #print name of compound
    print(compund_name)

    # Print the molar mass.
    print(f'{total_mass:.5f} grams/mole')

    # Print the number of moles.
    print(f'{number_moles:.5f} moles')

if __name__ == "__main__":
    main()