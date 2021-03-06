# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# [![Notebook Tutorial](__code/__all/notebook_tutorial.png)](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/extract_evenly_spaced_files)
#
# <img src='__docs/__all/notebook_rules.png' />

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Your IPTS 

# + run_control={"frozen": false, "read_only": false}
from __code.extract_evenly_spaced_files import ExtractEvenlySpacedFiles as EESF
from __code import system
system.System.select_working_dir()
from __code.__all import custom_style
custom_style.style()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Folder with Images to Extract 

# + run_control={"frozen": false, "read_only": false}
o_extract = EESF(working_dir=system.System.get_working_dir())
o_extract.select_folder()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Extraction Method to Use

# + run_control={"frozen": false, "read_only": false}
o_extract.how_to_extract()
# -

# # Renamed files ?

# This will replace the last part of the name (file counter digit)
#
# for example:
#     
#     original first file:  20191030_object1_0070_004_594_0003.tiff
#     new first file name:  20191030_object1_0070_004_594_0000.tiff

o_extract.renamed_files()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Output Folder 

# + run_control={"frozen": false, "read_only": false}
o_extract.select_output_folder()
# -


