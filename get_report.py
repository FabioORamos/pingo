# !/usr/bin/python
from dotenv import load_dotenv
load_dotenv()

import os
import requests
from requests_ntlm import HttpNtlmAuth

# SSRS server details
report_server_url = os.environ.get("REPORT_SERVER_URL")
report_path = os.environ.get("REPORT_PATH")
cert_path = os.environ.get("CERT_PATH")
report_name = os.environ.get("REPORT_NAME")
export_format = os.environ.get("EXPORT_FORMAT")

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
domain = os.environ.get("DOMAIN")

def make_session(domain, username, password, cert_path, export_format, report_server_url, report_path, report_name):
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
        