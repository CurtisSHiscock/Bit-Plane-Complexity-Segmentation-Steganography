# BPCS Steganoraphy Application

A Bit-Plane Complexity Segmentation program based on an undergraduate research project at the University of Florida
The program conceals data within the hard to distinguish 'noise-like regions' of the bit planes of images.

More Info: http://datahide.org/BPCSe/principle-e.html

### Prerequisites

Python

### Installing

Simply clone the repository to your desired directory 

```
git clone https://github.com/CurtisSHiscock/Bit-Plane-Complexity-Segmentation-Steganography.git
```

## Deployment

```
./BPCS.py encode -i [infile] -v [vessel]
```

```
./BPCS.py decode -v [vessel]
```

## Built With

* [Python](https://www.python.org/downloads/)

## Acknowledgments

* Jesse Dubbs
* Based on 'Principle of BPCS-Steganography by Eiji Kawguchi and Richard Eason'
