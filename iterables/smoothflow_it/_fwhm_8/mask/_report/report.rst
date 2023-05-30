Node: mask (fsl)
================


 Hierarchy : smoothflow_it.mask
 Exec ID : mask.a1


Original Inputs
---------------


* args : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* in_file : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/smooth/001_T1_smooth.nii.gz
* internal_datatype : <undefined>
* mask_file : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/bet_node/001_T1_brain_mask.nii.gz
* nan2zeros : <undefined>
* out_file : <undefined>
* output_datatype : <undefined>
* output_type : NIFTI_GZ


Execution Inputs
----------------


* args : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* in_file : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/smooth/001_T1_smooth.nii.gz
* internal_datatype : <undefined>
* mask_file : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/bet_node/001_T1_brain_mask.nii.gz
* nan2zeros : <undefined>
* out_file : <undefined>
* output_datatype : <undefined>
* output_type : NIFTI_GZ


Execution Outputs
-----------------


* out_file : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/mask/001_T1_smooth_masked.nii.gz


Runtime info
------------


* cmdline : fslmaths /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/smooth/001_T1_smooth.nii.gz -mas /home/arkiev/git/python-tutorials/iterables/smoothflow_it/bet_node/001_T1_brain_mask.nii.gz /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/mask/001_T1_smooth_masked.nii.gz
* duration : 0.899795
* hostname : MRgFUS
* prev_wd : /home/arkiev/git/python-tutorials
* working_dir : /home/arkiev/git/python-tutorials/iterables/smoothflow_it/_fwhm_8/mask


Terminal output
~~~~~~~~~~~~~~~


 


Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~


 


Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~


 


Environment
~~~~~~~~~~~


* ANTSPATH : /home/arkiev/ANTS/install/bin/
* CHROME_DESKTOP : code-url-handler.desktop
* CLUTTER_IM_MODULE : xim
* COLORTERM : truecolor
* CONDA_DEFAULT_ENV : base
* CONDA_EXE : /home/arkiev/anaconda3/bin/conda
* CONDA_PREFIX : /home/arkiev/anaconda3
* CONDA_PROMPT_MODIFIER : (base) 
* CONDA_PYTHON_EXE : /home/arkiev/anaconda3/bin/python
* CONDA_SHLVL : 1
* DBUS_SESSION_BUS_ADDRESS : unix:path=/run/user/1001/bus
* DESKTOP_MODE : 1
* DESKTOP_SESSION : ubuntu
* DISPLAY : :1
* FIX_VERTEX_AREA : 
* FMRI_ANALYSIS_DIR : /usr/local/freesurfer/fsfast
* FREESURFER : /usr/local/freesurfer
* FREESURFER_HOME : /usr/local/freesurfer
* FSFAST_HOME : /usr/local/freesurfer/fsfast
* FSF_OUTPUT_FORMAT : nii.gz
* FSLCONVERT : /usr/bin/convert
* FSLDIR : /usr/local/fsl/
* FSLDISPLAY : /usr/bin/display
* FSLGECUDAQ : cuda.q
* FSLLOCKDIR : 
* FSLMACHINELIST : 
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLREMOTECALL : 
* FSLTCLSH : /usr/local/fsl//bin/fsltclsh
* FSLWISH : /usr/local/fsl//bin/fslwish
* FSL_BIN : /usr/local/fsl//bin
* FSL_DIR : /usr/local/fsl/
* FS_OVERRIDE : 0
* FUNCTIONALS_DIR : /usr/local/freesurfer/sessions
* GDK_BACKEND : x11
* GDMSESSION : ubuntu
* GIO_LAUNCHED_DESKTOP_FILE : /usr/share/applications/code.desktop
* GIO_LAUNCHED_DESKTOP_FILE_PID : 16900
* GIT_ASKPASS : /usr/share/code/resources/app/extensions/git/dist/askpass.sh
* GJS_DEBUG_OUTPUT : stderr
* GJS_DEBUG_TOPICS : JS ERROR;JS LOG
* GNOME_DESKTOP_SESSION_ID : this-is-deprecated
* GNOME_SHELL_SESSION_MODE : ubuntu
* GPG_AGENT_INFO : /run/user/1001/gnupg/S.gpg-agent:0:1
* GTK_IM_MODULE : ibus
* GTK_MODULES : gail:atk-bridge
* HOME : /home/arkiev
* IM_CONFIG_PHASE : 2
* KMP_DUPLICATE_LIB_OK : True
* KMP_INIT_AT_FORK : FALSE
* LANG : en_AU.UTF-8
* LESSCLOSE : /usr/bin/lesspipe %s %s
* LESSOPEN : | /usr/bin/lesspipe %s
* LOCAL_DIR : /usr/local/freesurfer/local
* LOGNAME : arkiev
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
* MINC_BIN_DIR : /usr/local/freesurfer/mni/bin
* MINC_LIB_DIR : /usr/local/freesurfer/mni/lib
* MNI_DATAPATH : /usr/local/freesurfer/mni/data
* MNI_DIR : /usr/local/freesurfer/mni
* MNI_PERL5LIB : /usr/local/freesurfer/mni/share/perl5
* OLDPWD : /home/arkiev/git/python-tutorials/dMRI_tutorial
* ORIGINAL_XDG_CURRENT_DESKTOP : ubuntu:GNOME
* OS : Linux
* PATH : /home/arkiev/ANTS/install/bin:/usr/local/freesurfer/bin:/usr/local/freesurfer/fsfast/bin:/usr/local/freesurfer/tktools:/usr/local/fsl/bin:/usr/local/freesurfer/mni/bin:/home/arkiev/mrtrix3/bin:/home/arkiev/MRtrix3Tissue/bin:/home/linuxbrew/.linuxbrew/opt/qt5/bin:/usr/local/fsl/bin:/usr/local/MATLAB/R2020b/bin:/home/arkiev/.local/bin:/home/arkiev/anaconda3/bin:/home/arkiev/anaconda3/condabin:/home/arkiev/ANTS/install/bin:/usr/local/freesurfer/bin:/usr/local/freesurfer/fsfast/bin:/usr/local/freesurfer/tktools:/usr/local/fsl/bin:/usr/local/freesurfer/mni/bin:/home/arkiev/mrtrix3/bin:/home/arkiev/MRtrix3Tissue/bin:/home/linuxbrew/.linuxbrew/opt/qt5/bin:/usr/local/fsl/bin:/usr/local/MATLAB/R2020b/bin:/home/arkiev/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/arkiev/abin:/home/arkiev/abin
* PERL5LIB : /usr/local/freesurfer/mni/share/perl5
* PWD : /home/arkiev/git/python-tutorials
* QT4_IM_MODULE : xim
* QT_ACCESSIBILITY : 1
* QT_IM_MODULE : ibus
* R_LIBS : /home/arkiev/R
* SESSION_MANAGER : local/MRgFUS:@/tmp/.ICE-unix/3233,unix/MRgFUS:/tmp/.ICE-unix/3233
* SHELL : /bin/bash
* SHLVL : 2
* SSH_AGENT_PID : 3329
* SSH_AUTH_SOCK : /run/user/1001/keyring/ssh
* SUBJECTS_DIR : /usr/local/freesurfer/subjects
* TERM : xterm-256color
* TERM_PROGRAM : vscode
* TERM_PROGRAM_VERSION : 1.78.2
* TEXTDOMAIN : im-config
* TEXTDOMAINDIR : /usr/share/locale/
* USER : arkiev
* USERNAME : arkiev
* VSCODE_GIT_ASKPASS_EXTRA_ARGS : --ms-enable-electron-run-as-node
* VSCODE_GIT_ASKPASS_MAIN : /usr/share/code/resources/app/extensions/git/dist/askpass-main.js
* VSCODE_GIT_ASKPASS_NODE : /usr/share/code/code
* VSCODE_GIT_IPC_HANDLE : /run/user/1001/vscode-git-13dd09126a.sock
* WINDOWPATH : 2
* XAUTHORITY : /run/user/1001/gdm/Xauthority
* XDG_CONFIG_DIRS : /etc/xdg/xdg-ubuntu:/etc/xdg
* XDG_CURRENT_DESKTOP : Unity
* XDG_DATA_DIRS : /usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
* XDG_MENU_PREFIX : gnome-
* XDG_RUNTIME_DIR : /run/user/1001
* XDG_SEAT : seat0
* XDG_SESSION_DESKTOP : ubuntu
* XDG_SESSION_ID : 2
* XDG_SESSION_TYPE : x11
* XDG_VTNR : 2
* XMODIFIERS : @im=ibus
* _ : /home/arkiev/anaconda3/bin/ipython
* _CE_CONDA : 
* _CE_M : 

