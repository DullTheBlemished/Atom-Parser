ORBIT_ORDER = {
        "1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2,
        "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2,
        "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 14, "6d": 10,
        "7p": 6
        }

SUBSHELL_ORDER = {'s': 1, 'p': 2, 'd': 3, 'f': 4}

EXCEPTIONS = {
    # --- d-Block Transition Metal Exceptions ---
    24: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 1, "3d": 5},                   # Chromium (Cr)
    29: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 1, "3d": 10},                  # Copper (Cu)
    41: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 1, "4d": 4},  # Niobium (Nb)
    42: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 1, "4d": 5},  # Molybdenum (Mo)
    44: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 1, "4d": 7},  # Ruthenium (Ru)
    45: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 1, "4d": 8},  # Rhodium (Rh)
    46: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 0, "4d": 10}, # Palladium (Pd)
    47: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 1, "4d": 10}, # Silver (Ag)
    78: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 1, "4f": 14, "5d": 9},  # Platinum (Pt)
    79: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 1, "4f": 14, "5d": 10}, # Gold (Au)

    # --- f-Block Lanthanides & Actinides Exceptions ---
    57: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "5d": 1},            # Lanthanum (La)
    58: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 1, "5d": 1},  # Cerium (Ce)
    64: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 7, "5d": 1},  # Gadolinium (Gd)
    89: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "6d": 1}, # Actinium (Ac)
    90: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "6d": 2}, # Thorium (Th)
    91: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 2, "6d": 1}, # Protactinium (Pa)
    92: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 3, "6d": 1}, # Uranium (U)
    93: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 4, "6d": 1}, # Neptunium (Np)
    96: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 7, "6d": 1}, # Curium (Cm)
    103: {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 14, "6d": 1} # Lawrencium (Lr)
}

SUPERSCRIPTS = {
        '0': "⁰", '1': "¹", '2': "²", '3': "³", '4': "⁴",
        '5': "⁵", '6': "⁶", '7': "⁷", '8': "⁸", '9': "⁹",
        }

NOBELGASNOTATION = {
    "1s": ("He", 2),
    "2p": ("Ne", 10),
    "3p": ("Ar", 18),
    "4p": ("Kr", 36),
    "5p": ("Xe", 54),
    "6p": ("Rn", 86),
    "7p": ("Og", 118)
}

class InvalidDataTypingError(Exception):
    pass

def parse(atomic_num: int, atomic_weight: int, real: bool = False) -> tuple[int, int, int, dict[str, int]]:
    """
    Calculates basic atomic properties and the electron configuration for a neutral atom.

    This function determines the number of protons, neutrons, and electrons based on 
    the provided atomic number and weight. It also calculates the electron configuration 
    using the standard Aufbau principle, with an option to account for known 
    configuration exceptions (e.g., Transition metals, Lanthanides, Actinides).

    Args:
        atomic_num (int): The atomic number of the element (number of protons).
        atomic_weight (int): The mass number of the element (protons + neutrons).
        real (bool, optional): If True, returns the observed (anomalous) electron 
            configuration for known exception elements. If False, follows the standard 
            Madelung (Aufbau) rule strictly. Defaults to False.

    Returns:
        tuple: A 4-tuple containing:
            - proton (int): The number of protons.
            - neutron (int): The number of neutrons.
            - electron (int): The number of electrons (assuming a neutral atom).
            - electron_config (dict): A dictionary where keys are subshells 
              (e.g., '1s', '2p') and values are the number of electrons in that subshell.
    """
    # The docstring is ai-generated

    if not isinstance(real, bool):
        real = False

    # Get proton, neutron, and electron count
    neutron, proton, electron = atomic_weight - atomic_num, atomic_num, atomic_num
    electron_config = {}  # inits the dictionary for the config

    # Get electron config (real = False)
    if not real or atomic_num not in EXCEPTIONS:
        for orbit in ORBIT_ORDER:
            if ORBIT_ORDER[orbit] <= atomic_num:
                electron_config[orbit] = ORBIT_ORDER[orbit]
                atomic_num -= ORBIT_ORDER[orbit]

            elif ORBIT_ORDER[orbit] > atomic_num and atomic_num != 0:
                electron_config[orbit] = atomic_num
                atomic_num = 0

    # Get electron config (real = True)
    elif real and atomic_num in EXCEPTIONS:
        electron_config = EXCEPTIONS[atomic_num]

    return(proton, neutron, electron, electron_config)

def read(electron_config: dict) -> str | None:
    """
    Converts an electron configuration dictionary into a formatted string.
    
    Args:
        electron_config (dict): A dictionary of orbitals and their electron counts.
        
    Returns:
        str: The formatted electron configuration string (e.g., '1s²2s²2p⁶').
    """
    # the docstring is ai-generated
    new = []  # inits the thingy

    if not isinstance(electron_config, dict):
        return None

    for orbit, count in electron_config.items():
        num = "".join(SUPERSCRIPTS[digit] for digit in str(count))
        new.append(f"{orbit}{num}")

    return "".join(new)

def valenceElectron(electron_config: dict) -> int:
    """
    Calculates the total number of valence electrons for a given electron configuration.

    This function identifies the outermost electron shell (the highest principal 
    quantum number) and sums the electrons present in all subshells of that specific shell.

    Args:
        electron_config (dict): A dictionary representing the electron configuration, 
            where keys are orbital strings (e.g., '1s', '3d') and values are the 
            corresponding electron counts.

    Returns:
        int: The total number of valence electrons in the outermost shell.
    """
    outermost = 1
    valance_electron = 0
    for orbit in electron_config:
        if int(orbit[0]) > outermost:
            outermost = int(orbit[0])

    for orbit in electron_config:
        if str(outermost) in orbit:
            valance_electron += electron_config[orbit]

    return valance_electron

def standardFormat(electron_config: dict) -> dict[str, int]:
    """
    Sorts an electron configuration dictionary into standard notation order.

    The configuration is sorted first by the principal quantum number (the shell number), 
    and then by the subshell type (s, p, d, f) using the predefined SUBSHELL_ORDER mapping.

    Args:
        electron_config (dict): An unsorted or abnormally sorted dictionary of orbitals 
            and their electron counts.

    Returns:
        dict: A new dictionary containing the sorted electron configuration.
    """
    new = dict(sorted(electron_config.items(), key=lambda d: (int(d[0][:-1]), SUBSHELL_ORDER[d[0][-1]])))
    return new

def nobleGasNotation(electron_config: dict) -> tuple[str, dict[str, int]]:
    electron_config = standardFormat(electron_config)
    # WIP, no finish date, should be soon, however

if __name__ == "__main__":  # allows to act as a libary and a standalone thingy majiggy
    print("input exactly as so: 'atomic_num(int) atomic_weight(int) real(bool)'")
    print("if the program detects 'break' in the input, it will kill itself")
    print("")
    while True:
        user_input = input(">>>:").split()

        if "break" in user_input:
            break

        if len(user_input) < 1 or len(user_input) > 3:
            input("Invalid input")
            print("")
            continue

        if len(user_input) != 3:
            user_input.append(False)
        elif user_input[2].lower() == "true":
            user_input[2] = True
        else:
            user_input[2] = False

        if not isinstance(user_input[0], int) or not isinstance(user_input[1], int):
            input("Invalid input")
            print("")
            continue

        try:
            info = parse(int(user_input[0]), int(user_input[1]), user_input[2])

        except IndexError:
            info = parse(int(user_input[0]), int(user_input[1]))

        except (IndexError, ValueError):
            input("Invalid Input")
            print("")
            continue

        input(f"""Proton: {info[0]}
Neutron: {info[1]}
Electron: {info[2]}
Configuration: {read(standardFormat(info[3]))}""")
        print("")
        
