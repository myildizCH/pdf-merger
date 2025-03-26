# PDF Merger Tool 🧩📄

A lightweight Python script to merge multiple PDF files into a single document using `pypdf`.


## 🚀 How It Works

1. Drop the PDF files you want to merge into the `pdfs_to_merge/` folder.
2. Run the script.
3. The merged file will be saved as `merged_output.pdf` in the project root.

## 🛠️ Setup Instructions

#### 1. **Clone this repo or create the folder manually**

#### 2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

#### 3. Install Dependencies

`pip install pypdf`

#### 4. Create the folder for your PDFs:

`mkdir pdfs_to_merge`

#### 5. Run the script:

`python merge_pdfs.py`

## 📄 Example Output
After running the script, you'll see something like:
```
Added: file1.pdf
Added: file2.pdf

✅ Merged 2 PDFs into 'merged_output.pdf'
```

## 📌 Notes

* Make sure your PDF files are named in the order you want them merged (e.g., 01_intro.pdf, 02_chapter.pdf).
* The script merges all .pdf files in the pdfs_to_merge/ folder in alphabetical order.

## 📦 Requirements

- Python 3.7+
- pypdf



## 📁 Project Structure
```
pdf-merger/ 
    ├── merge_pdfs.py # Main script 
    ├── venv/ # Python virtual environment 
    └── pdfs_to_merge/ # Folder to drop PDF files for merging
```
