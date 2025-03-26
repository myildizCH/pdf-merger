import os
from pypdf import PdfReader, PdfWriter

folder_path = "pdfs_to_merge"
pdf_files = sorted([
    f for f in os.listdir(folder_path)
    if f.endswith(".pdf")
])

writer = PdfWriter()

for pdf in pdf_files:
    full_path = os.path.join(folder_path, pdf)
    reader = PdfReader(full_path)

    for page in reader.pages:
        writer.add_page(page)

    print(f"Added: {pdf}")

output_file = "merged_output.pdf"
with open(output_file, "wb") as out:
    writer.write(out)

print(f"\n✅ Merged {len(pdf_files)} PDFs into '{output_file}'")
