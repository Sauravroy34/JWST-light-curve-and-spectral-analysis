import os
os.environ["CRDS_PATH"] = os.path.expanduser("~/crds_cache")
os.environ["CRDS_SERVER_URL"] = "https://jwst-crds.stsci.edu"
from jwst.pipeline import Spec2Pipeline
import shutil

os.makedirs("output_set_1", exist_ok=True)
os.makedirs("output_set_2", exist_ok=True)

spec2dict = {}

spec2dict['assign_wcs'], spec2dict['badpix_selfcal'] = {}, {}
spec2dict['nsclean'] = {}
spec2dict['extract_2d'], spec2dict['srctype'] = {}, {}
spec2dict['flat_field'], spec2dict['photom'] = {}, {}
spec2dict['pixel_replace'], spec2dict['extract_1d'] = {}, {}
spec2dict['flat_field']['skip'] = True
spec2dict['photom']['skip'] = True  

# For Brown dwarf observation uncomment the following.
#spec2dict['flat_field']['skip'] = False
#spec2dict['photom']['skip'] = False

# Run pixel replacement code to extrapolate values for otherwise bad pixels.
# This can help mitigate 5-10% negative dips in spectra of bright sources.
# Use the 'fit_profile' algorithm.
spec2dict['pixel_replace']['skip'] = False
spec2dict['pixel_replace']['n_adjacent_cols'] = 5
spec2dict['pixel_replace']['algorithm'] = 'fit_profile'

# Run nsclean for 1/f noise.
spec2dict['nsclean']['skip'] = False
spec2dict['nsclean']['n_sigma'] = 0.1
spec2dict['nsclean']['save_mask'] = False
spec2dict['nsclean']['save_results'] = False


# Build a sigma-clipped mask not based on WCS.
spec2dict['nsclean']['mask_spectral_regions'] = True
spec2dict['nsclean']['save_noise'] = False  # Save the 1/f noise removed.
spec2dict['extract_1d']['apply_apcorr'] = False
spec2dict['extract_1d']['save_results'] = False
# Turn off aperture correction.
def process_spec2(files, output_dir):
    for i in files:
       
        Spec2Pipeline.call(i,steps=spec2dict,save_results= True, output_dir=output_dir)
        
        

# File sets
files_set_1 = [
    "jw01366003001_04101_00001-seg001_nrs2_rateints.fits",
    "jw01366003001_04101_00001-seg002_nrs2_rateints.fits",
    "jw01366003001_04101_00001-seg003_nrs2_rateints.fits",
]

files_set_2 = [
    "jw01366003001_04101_00001-seg003_nrs1_rateints.fits",
    "jw01366003001_04101_00001-seg002_nrs1_rateints.fits",
    "jw01366003001_04101_00001-seg001_nrs1_rateints.fits",
]

# Run pipeline and store outputs
process_spec2(files_set_1, "output_set_1")
process_spec2(files_set_2, "output_set_2")