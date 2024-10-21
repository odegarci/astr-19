import numpy as np
from astropy.table import Table

def main():
    x = np.linspace(0, 2 * np.pi, 1000)
    mytable = Table()
    mytable['x'] = x
    mytable['sin x'] = np.sin(x)
    print(mytable)

if __name__ == "__main__":
    main()