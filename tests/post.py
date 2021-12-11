import requests
import json
import sys

servicex_port = 5000
payload = \
{
	"did": "demo://dataset1",
    "selection": "(Select (Where (call EventDataset 'mini') (lambda (list e) (or (attr e 'trigE') (attr e 'trigM')))) (lambda (list e) (dict (list 'lep_pt' 'lep_eta' 'lep_phi' 'lep_energy' 'lep_charge' 'lep_ptcone30' 'lep_etcone20' 'lep_type' 'lep_trackd0pvunbiased' 'lep_tracksigd0pvunbiased' 'lep_z0') (list (attr e 'lep_pt') (attr e 'lep_eta') (attr e 'lep_phi') (attr e 'lep_E') (attr e 'lep_charge') (attr e 'lep_ptcone30') (attr e 'lep_etcone20') (attr e 'lep_type') (attr e 'lep_trackd0pvunbiased') (attr e 'lep_tracksigd0pvunbiased') (attr e 'lep_z0')))))",
	"result-destination": "object-store",
	"result-format": "root-file",
	"chunk-size": 7000,
	"workers": 1
}

r = requests.post('http://localhost:{port}/servicex/transformation'.format(port=servicex_port), data = payload)

print(r.json())