# Instructions

## 1.) Install Necessary Libraries
*The needed libraries are OpenCV, NumPy, RegEx, Sys, and MatPlotLib.*

### Install OpenCV:
#### Windows

```
pip install opencv-python
```
#### Mac
```
pip install opencv-python
```

### Install NumPy:
#### Windows
```
python -mpip install --user numpy
```

#### Mac
```
python3 -mpip install --user numpy
```

### Install RegEx:
#### Windows
```
python -mpip install --user regex
```

#### Mac
```
python3 -mpip install --user regex
```

### Install Sys Library:
No need, it is automatically imported due to:
```
import sys
```

### Install MatPlotLib:
#### Windows
```
python -mpip install --user matplotlib
```

#### Mac
```
python3 -mpip install --user matplotlib
```

---

## 2.) Setting Up
1. Make sure you have a video file in the folder _"Movie"_
    
    (__MUST BE A .MP4 FILE__)

2. CD Into folder _"Code"_
    ```
    cd Code
    ```
3. Run the file _"generator_plotter.py"_
    
    *On Windows:*
    ```
    python generator_plotter.py
    ```

    *On Mac:*
    ```
    python3 generator_plotter.py
    ```

## 3.) Troubleshooting
* To test generation of Dominant Color Text File (in _"Code"_ folder):

    *On Windows:*
    ```
    python generator.py
    ```

    *On Mac:*
    ```
    python3 generator.py
    ```

    **This will generate a text file in the _"Dominant_Color_Files"_ folder.**

* To test plotting of dominant colors file as an image:
    
    *On Windows:*
    ```
    python plotter.py
    ```

    *On Mac:*
    ```
    python3 plotter.py
    ```

    **This will generate an image file in the _"Image_Output"_ folder**
    
    **MUST already have a dominant colors text file to use**

## 4.) Output of Code
After running _generator_plotter.py_, two new files will be produced:
    
*  **A txt file -** This will contain all the dominant 
    colors of each frame (one frame per line on the file),
    used to generate png file. ***Color contained as RGB code.***
    
*  **A png file -** This will be a plotted image of the dominant
    color of each frame. ***May need to be cropped after generation.***

**NOTE: _generator.py_ generates JUST the txt file, and _plotter.py_ generates JUST the png file.**