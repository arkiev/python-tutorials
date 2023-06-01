# https://nipype.readthedocs.io/en/latest/users/examples/dmri_mrtrix_dti.html
# tutorial using mrtrix3 and FSL in nipype

import nipype.interfaces.io as nio  # Data i/o
import nipype.interfaces.utility as util  # utility
import nipype.pipeline.engine as pe  # pypeline engine
import nipype.interfaces.mrtrix as mrtrix  # <---- The important new part!
import nipype.interfaces.fsl as fsl
import nipype.algorithms.misc as misc
import os
import os.path as op  # system functions

fsl.FSLCommand.set_default_output_type('NIFTI')

data_dir =  op.abspath(op.join(op.curdir, 'Data/'))
# os.listdir(data_dir)
# subject_list = ['001','002','003']

# infosource = pe.Node(
#     interface=util.IdentityInterface(fields=['subject_id']), name="infosource")
# infosource.iterables = ('subject_id', subject_list)

subject_id = '001'

info = dict(
    dwi=[['subject_id', 'data']],
    bvecs=[['subject_id', 'bvecs']],
    bvals=[['subject_id', 'bvals']])

datasource = pe.Node(
    interface=nio.DataGrabber(
        infields=['subject_id'], outfields=list(info.keys())),
    name='datasource')

datasource.inputs.template = "%s/%s"
datasource.inputs.base_directory = data_dir
datasource.inputs.field_template = dict(dwi='%s/%s.nii.gz')
datasource.inputs.template_args = info
datasource.inputs.sort_filelist = True

inputnode = pe.Node(
    interface=util.IdentityInterface(fields=["dwi", "bvecs", "bvals"]),
    name="inputnode")

fsl2mrtrix = pe.Node(interface=mrtrix.FSL2MRTrix(), name='fsl2mrtrix')

gunzip = pe.Node(interface=misc.Gunzip(), name='gunzip')
dwi2tensor = pe.Node(interface=mrtrix.DWI2Tensor(), name='dwi2tensor')
tensor2vector = pe.Node(interface=mrtrix.Tensor2Vector(), name='tensor2vector')
tensor2adc = pe.Node(
    interface=mrtrix.Tensor2ApparentDiffusion(), name='tensor2adc')
tensor2fa = pe.Node(
    interface=mrtrix.Tensor2FractionalAnisotropy(), name='tensor2fa')

MRconvert = pe.Node(interface=mrtrix.MRConvert(), name='MRconvert')
MRconvert.inputs.extract_at_axis = 3
MRconvert.inputs.extract_at_coordinate = [0]
threshold_b0 = pe.Node(interface=mrtrix.Threshold(), name='threshold_b0')
median3d = pe.Node(interface=mrtrix.MedianFilter3D(), name='median3d')

erode_mask_firstpass = pe.Node(
    interface=mrtrix.Erode(), name='erode_mask_firstpass')
erode_mask_secondpass = pe.Node(
    interface=mrtrix.Erode(), name='erode_mask_secondpass')
MRmultiply = pe.Node(interface=mrtrix.MRMultiply(), name='MRmultiply')
MRmult_merge = pe.Node(interface=util.Merge(2), name="MRmultiply_merge")
threshold_FA = pe.Node(interface=mrtrix.Threshold(), name='threshold_FA')
threshold_FA.inputs.absolute_threshold_value = 0.7

bet = pe.Node(interface=fsl.BET(mask=True), name='bet_b0')
gen_WM_mask = pe.Node(
    interface=mrtrix.GenerateWhiteMatterMask(), name='gen_WM_mask')
threshold_wmmask = pe.Node(
    interface=mrtrix.Threshold(), name='threshold_wmmask')
threshold_wmmask.inputs.absolute_threshold_value = 0.4

estimateresponse = pe.Node(
    interface=mrtrix.EstimateResponseForSH(), name='estimateresponse')
estimateresponse.inputs.maximum_harmonic_order = 6
csdeconv = pe.Node(
    interface=mrtrix.ConstrainedSphericalDeconvolution(), name='csdeconv')
csdeconv.inputs.maximum_harmonic_order = 6


probCSDstreamtrack = pe.Node(
    interface=mrtrix.ProbabilisticSphericallyDeconvolutedStreamlineTrack(),
    name='probCSDstreamtrack')
probCSDstreamtrack.inputs.inputmodel = 'SD_PROB'
probCSDstreamtrack.inputs.maximum_number_of_tracks = 150000
tracks2prob = pe.Node(interface=mrtrix.Tracks2Prob(), name='tracks2prob')
tracks2prob.inputs.colour = True
tck2trk = pe.Node(interface=mrtrix.MRTrix2TrackVis(), name='tck2trk')


tractography = pe.Workflow(name='tractography')

tractography.connect([(inputnode, fsl2mrtrix, [("bvecs", "bvec_file"),
                                               ("bvals", "bval_file")])])
tractography.connect([(inputnode, gunzip, [("dwi", "in_file")])])
tractography.connect([(gunzip, dwi2tensor, [("out_file", "in_file")])])
tractography.connect([(fsl2mrtrix, dwi2tensor, [("encoding_file",
                                                 "encoding_file")])])

tractography.connect([
    (dwi2tensor, tensor2vector, [['tensor', 'in_file']]),
    (dwi2tensor, tensor2adc, [['tensor', 'in_file']]),
    (dwi2tensor, tensor2fa, [['tensor', 'in_file']]),
])
tractography.connect([(tensor2fa, MRmult_merge, [("FA", "in1")])])

tractography.connect([(gunzip, MRconvert, [("out_file", "in_file")])])
tractography.connect([(MRconvert, threshold_b0, [("converted", "in_file")])])
tractography.connect([(threshold_b0, median3d, [("out_file", "in_file")])])
tractography.connect([(median3d, erode_mask_firstpass, [("out_file",
                                                         "in_file")])])
tractography.connect([(erode_mask_firstpass, erode_mask_secondpass,
                       [("out_file", "in_file")])])
tractography.connect([(erode_mask_secondpass, MRmult_merge, [("out_file",
                                                              "in2")])])
tractography.connect([(MRmult_merge, MRmultiply, [("out", "in_files")])])
tractography.connect([(MRmultiply, threshold_FA, [("out_file", "in_file")])])

tractography.connect([(gunzip, bet, [("out_file", "in_file")])])
tractography.connect([(gunzip, gen_WM_mask, [("out_file", "in_file")])])
tractography.connect([(bet, gen_WM_mask, [("mask_file", "binary_mask")])])
tractography.connect([(fsl2mrtrix, gen_WM_mask, [("encoding_file",
                                                  "encoding_file")])])
tractography.connect([(gen_WM_mask, threshold_wmmask, [("WMprobabilitymap",
                                                        "in_file")])])

tractography.connect([(gunzip, estimateresponse, [("out_file", "in_file")])])
tractography.connect([(fsl2mrtrix, estimateresponse, [("encoding_file",
                                                       "encoding_file")])])
tractography.connect([(threshold_FA, estimateresponse, [("out_file",
                                                         "mask_image")])])

tractography.connect([(gunzip, csdeconv, [("out_file", "in_file")])])
tractography.connect([(gen_WM_mask, csdeconv, [("WMprobabilitymap",
                                                "mask_image")])])
tractography.connect([(estimateresponse, csdeconv, [("response",
                                                     "response_file")])])
tractography.connect([(fsl2mrtrix, csdeconv, [("encoding_file",
                                               "encoding_file")])])

tractography.connect([(threshold_wmmask, probCSDstreamtrack, [("out_file",
                                                               "seed_file")])])
tractography.connect([(csdeconv, probCSDstreamtrack,
                       [("spherical_harmonics_image", "in_file")])])
tractography.connect([(probCSDstreamtrack, tracks2prob, [("tracked",
                                                          "in_file")])])
tractography.connect([(gunzip, tracks2prob, [("out_file", "template_file")])])

tractography.connect([(gunzip, tck2trk, [("out_file", "image_file")])])
tractography.connect([(probCSDstreamtrack, tck2trk, [("tracked", "in_file")])])

dwiproc = pe.Workflow(name="dwiproc")
dwiproc.base_dir = os.path.abspath('dmri_mrtrix_dti')
dwiproc.connect([(infosource, datasource, [('subject_id', 'subject_id')]),
                 (datasource, tractography,
                  [('dwi', 'inputnode.dwi'), ('bvals', 'inputnode.bvals'),
                   ('bvecs', 'inputnode.bvecs')])])

# dwiproc.connect(infosource, datasource, [('subject_id', 'subject_id')])

if __name__ == '__main__':
    dwiproc.run()
    dwiproc.write_graph()




