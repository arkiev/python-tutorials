import os
from os.path import abspath

from nipype import Workflow, Node, MapNode, Function
from nipype.interfaces.fsl import BET, IsotropicSmooth, ApplyMask

#from nilearn.plotting import plot_anat
%matplotlib inline
import matplotlib.pyplot as plt


# define input image
input_file =  abspath("/home/arkiev/git/python-tutorials/dMRI_tutorial/Data/001/001_T1.nii.gz")

#BET
bet = BET()
bet.inputs.in_file = input_file
bet.inputs.out_file = "T1w_nipype_bet.nii.gz"
res = bet.run()

#smoothing
smooth=IsotropicSmooth()
smooth.inputs.in_file = input_file
smooth.inputs.out_file = "T1w_nipype_bet_smoothed.nii.gz"
smooth.inputs.sigma = 4

res_smooth= smooth.run()

# Nodes and Workflows¶
# Create Node
bet_node = Node(BET(), name='bet')
# Specify node inputs
bet_node.inputs.in_file = input_file
bet_node.inputs.mask = True

# here are some other nodes
smooth_node = Node(IsotropicSmooth(in_file=input_file, fwhm=4), name="smooth")
mask_node = Node(ApplyMask(), name="mask")

# create work flow
d=abspath("/home/arkiev/git/python-tutorials")
wf = Workflow(name="smoothflow", base_dir=d)

# Connect nodes in workflow
wf.connect(smooth_node, "out_file", mask_node, "in_file")

# Let's see a graph describing our workflow:
wf.write_graph("workflow_graph.dot")
from IPython.display import Image, display
display(Image(filename="/home/arkiev/git/python-tutorials/smoothflow/workflow_graph.png"))

# detailed image
wf.write_graph(graph2use='flat')
from IPython.display import Image
Image(filename="/output/working_dir/smoothflow/graph_detailed.png")

#run workflow
res = wf.run()

# we can check the output of specific nodes from workflow
list(res.nodes)[0].result.outputs

# visualise outputs
! tree -L 3 smoothflow/

################
# plot results #
################

import numpy as np
import nibabel as nb
#import matplotlib.pyplot as plt

# Let's create a short helper function to plot 3D NIfTI images
def plot_slice(fname):

    # Load the image
    img = nb.load(fname)
    data = img.get_data()

    # Cut in the middle of the brain
    cut = int(data.shape[-1]/2) + 10

    # Plot the data
    plt.imshow(np.rot90(data[..., cut]), cmap="gray")
    plt.gca().set_axis_off()

f = plt.figure(figsize=(12, 4))
for i, img in enumerate(["/home/arkiev/git/python-tutorials/dMRI_tutorial/Data/001/001_T1.nii.gz",
                         "/home/arkiev/git/python-tutorials/smoothflow/smooth/001_T1_smooth.nii.gz",
                         "/home/arkiev/git/python-tutorials/smoothflow/bet/001_T1_brain_mask.nii.gz'",
                         "/home/arkiev/git/python-tutorials/smoothflow/mask/001_T1_smooth_masked.nii.gz"]):
    f.add_subplot(1, 4, i + 1)
    plot_slice(img)


# Iterables
smooth_node_it = Node(IsotropicSmooth(in_file=input_file), name="smooth")
smooth_node_it.iterables = ("fwhm", [4, 8, 16])

# new smoothing and masking nodes
bet_node_it = Node(BET(in_file=input_file, mask=True), name='bet_node')
mask_node_it = Node(ApplyMask(), name="mask")

# Initiation of iterables workflow
wf_it = Workflow(name="smoothflow_it", base_dir="/home/arkiev/git/python-tutorials/iterables/")
wf_it.connect(bet_node_it, "mask_file", mask_node_it, "mask_file")
wf_it.connect(smooth_node_it, "out_file", mask_node_it, "in_file")

# run the workflow and check the output
res_it = wf_it.run()

# view the graph
list(res_it.nodes)

# visualise outputs
! tree -L 3 iterables/


