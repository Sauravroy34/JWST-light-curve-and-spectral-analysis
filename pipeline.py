
from jwst.pipeline import Spec2Pipeline

def process_spec2(files):
    import os
    os.environ["CRDS_PATH"] = os.path.expanduser("~/crds_cache")
    os.environ["CRDS_SERVER_URL"] = "https://jwst-crds.stsci.edu"
    for i in files:
        Spec2Pipeline.call(i)