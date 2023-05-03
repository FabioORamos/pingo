# !/usr/bin/python
%load_ext dotenv
%dotenv

import os
import requests
from requests_ntlm import HttpNtlmAuth

# SSRS server details
report_server_url = 'https://macq-poc.ctrfy31kg8iq.ap-southeast-2.rds.amazonaws.com:8443/ReportServer/Pages/ReportViewer.aspx?'
report_path = 'Sales+Orders'

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
domain = 'MACQ.POC'
cert_path = "/Users/fr/cevo/macq/rds-ca-2019-root.pem"
report_name = "report"
export_format = 'mhtml'

def get_report(domain, username, password, cert_path, export_format, report_server_url, report_path, report_name):
# Create a session with NTLM authentication
    session = requests.Session()
    session.auth = HttpNtlmAuth(f'{domain}\\{username}', password)
    session.verify = cert_path

    export_format = f'{export_format}'
    request_url = (f'{report_server_url}'
                f'%2f{report_path}'
                f'&rs:Format={export_format}'
                f'&rs:ParameterLanguage=en-US'
                f'&rs:Command=Render')

    response = session.get(request_url, stream=True)
    with open(f'{report_name}.{export_format}', 'wb') as f:
        f.write(response.content)
        print(response)