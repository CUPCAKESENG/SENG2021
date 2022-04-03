'''
SENG2021 - Group Cupcake
File: pdf_report.py
    Description: Creates a PDF communication report
'''

import cairosvg
import os
from datetime import datetime
from jwt import encode
from app.src.error import FormatError
from app.src.config import SECRET

def create_pdf_report(report):
    '''
    Creates PDF communication report.
        Params: report
        Returns: payload
        Errors: FormatError
    '''

    if not all(key in report for key in ('sender', 'received_time', 'filename', 'path')):
        raise FormatError('Communication report is not in the right format.')

    payload = {
        'sender': report['sender'],
        'received_time': report['received_time'],
        'save_time': report['save_time'],
        'file_size': report['file_size'],
        'file_name': report['filename'][:-4],
        'file_type': 'xml'
    }

    token = encode(payload, SECRET)
    payload['token'] = token[-10:]

    vector_path = 'app/communication_report/' + payload['token'] + '.svg'
    pdf_path = 'app/communication_report/' + payload['token'] + '.pdf'
    
    info = []

    with open('app/saves/template.svg', 'r') as template:
        info = template.readlines()

        for index, line in enumerate(info):
            if '%Recipient%' in line:
                info[index] = line.replace('%Recipient%', 'Cupcake E-Invoicing Inc.')

            if '%Filename%' in line:
                line = line.replace('%Filename%', payload['file_name'])
                info[index] = line.replace('%FileType%', payload['file_type'])

            if '%Filesize%' in line:
                info[index] = line.replace('%Filesize%', payload['file_size'])

            if '%Sender%' in line:
                info[index] = line.replace('%Sender%', payload['sender'])
  
            if '%TimeRec%' in line:
                info[index] = line.replace('%TimeRec%', payload['received_time'])

            if '%TimeSaved%' in line:
                info[index] = line.replace('%TimeSaved%', payload['save_time'])

    with open(vector_path, 'w') as vector:
        vector.writelines(info)

    cairosvg.svg2pdf(url=vector_path, write_to=pdf_path)

    return payload['token'] + '.pdf'