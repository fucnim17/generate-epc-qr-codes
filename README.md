# EPC QR Code Generator

A minimal script that reads an **Export.xlsx** file and generates EPC-compliant QR codes, including recipient name, IBAN, BIC, amount, and remittance info.

## Usage

1. Clone this repository: `git clone https://github.com/fucnim17/generate-epc-qr-codes.git`
2. Install dependencies: `pip install pandas qrcode[pil] openpyxl`
3. Create or generate your Export.xlsx file. You can also find a sample template in the repository.
4. Update the script if needed (e.g., path to your Excel file).
5. Run the script: `python generate-epc-qr-codes.py`
6. Check for generated QR codes (qr_code_<index>.png).
 
## License

This script is licensed under the GNU General Public License Version 3. See the `LICENSE` file for details.

