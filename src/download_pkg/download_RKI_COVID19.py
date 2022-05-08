#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import DownloadFile
import os
import json

def download_RKI_COVID19():
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
    filename = "RKI_COVID19.csv"
    meta_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Fallzahlen')
    filename_meta = "RKI_COVID19_meta.json" 
    url = "https://www.arcgis.com/sharing/rest/content/items/f10774f1c63e40168479a1feb6c7ca74/data"

    url_meta = "https://www.arcgis.com/sharing/rest/content/items/f10774f1c63e40168479a1feb6c7ca74?f=pjson"

    meta = DownloadFile(url=url_meta, filename=filename_meta, download_path=meta_path, compress=False, add_date=False, add_latest=False)
    meta.write_file()
    with open(meta_path + "/" + filename_meta,'r') as file:
        metaobj = json.load(file)
    metaobj['description'] = ""
    metaobj['licenseInfo'] = "Die Daten sind die Fallzahlen in Deutschland des Robert Koch-Institut (RKI) und stehen unter der Open Data Datenlizenz Deutschland – Namensnennung – Version 2.0 zur Verfügung."
    json.dump(metaobj,open(meta_path + "/" + filename_meta,'w'))

    a = DownloadFile(url=url, filename=filename, download_path=data_path, compress=True, add_date=True, add_latest=False)
    a.write_file()
