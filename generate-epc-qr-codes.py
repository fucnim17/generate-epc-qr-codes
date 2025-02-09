# -----------------------------------------------------------------------------
# Copyright (C) 2025 Niklas Fuchshofer
#
# This script is licensed under the GNU General Public License Version 3 or
# any later version.
# See the LICENSE file for more details.
# -----------------------------------------------------------------------------
# Script to create EPC QR codes from an Excel file.
# -----------------------------------------------------------------------------

import pandas as pd
import qrcode
import os

# Path to the folder (adjust if necessary)
downloads_folder = os.path.expanduser('~/Downloads')
excel_file_path = os.path.join(downloads_folder, 'Export.xlsx')

# Read the Excel file
try:
    df = pd.read_excel(excel_file_path)
    print("Excel file read successfully")
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit()

# Function to create the EPC QR code content
def create_epc_qr_content(row):
    try:
        name = row['Name']
        iban = row['IBAN']
        bic = row.get('BIC', '')  # BIC is optional if not present
        amount = row['Amount']
        currency = row.get('Currency', 'EUR')  # Default currency is EUR
        remittance_info = row['Remittance Info']

        # Debug output
        print(f"Processing: Name={name}, IBAN={iban}, BIC={bic}, Amount={amount}, Currency={currency}, Remittance Info={remittance_info}")

        # If BIC is missing, use an empty string
        if pd.isna(bic):
            bic = ''

        epc_qr_content = (
            f"BCD\n001\n1\nSCT\n{name}\n"
            f"{bic}\n{iban}\n"
            f"{amount}\n{currency}\n\n"
            f"{remittance_info}"
        )
        return epc_qr_content
    except KeyError as e:
        print(f"Missing column: {e}")
        return None

# Generate and save QR codes
for index, row in df.iterrows():
    content = create_epc_qr_content(row)
    if content:
        qr = qrcode.make(content)
        qr_filename = f"qr_code_{index}.png"
        qr.save(qr_filename)
        print(f"QR code saved: {qr_filename}")
    else:
        print(f"QR code could not be created for row {index}")

print("QR code creation completed.")
