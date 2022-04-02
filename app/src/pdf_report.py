"""
SENG2021 - Group Cupcake
File: pdf_report.py
    Description: Creates a PDF communication report
"""

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os
from datetime import datetime
from jwt import encode
from app.src.error import FormatError
from app.src.config import SECRET

def create_pdf_report(report):
    """
    Creates PDF communication report.
        Params: report
        Returns: payload
        Errors: FormatError
    """
    if not os.path.exists("app/communication_report"):
        os.makedirs("app/communication_report")

    if not all(key in report for key in ("sender", "received_time", "filename", "path")):
        raise FormatError("Communication report is not in the right format.")

    