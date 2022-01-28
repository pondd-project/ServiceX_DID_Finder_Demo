#!/usr/bin/env python
# coding: utf-8

import logging
logging.basicConfig(level=logging.DEBUG)

# # A Simple DID Finder
from func_adl_servicex import ServiceXSourceUpROOT
from servicex import ServiceXDataset

sx_dataset = ServiceXDataset("demo://dataset1")#, backend_name='dev_uproot')
ds = ServiceXSourceUpROOT(sx_dataset, "mini")

data = ds.Select("lambda e: {'JetPT': e['jet_pt']}").AsAwkwardArray().value()

data['JetPT']
