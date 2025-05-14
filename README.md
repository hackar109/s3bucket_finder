# 🔍 S3 Bucket Finder Tool

A simple Python tool to find publicly accessible AWS S3 buckets based on a domain or keyword.

---

## 🚀 Features

- **Keyword/Domain Based Search**: Scan for S3 buckets using a specific domain or keyword.
- **Bucket Name Pattern Generation**: Automatically generates common bucket name patterns like `keyword-bucket`, `keyword-assets`, `keyword-files`, etc.
- **Multi-region Support**: Checks common AWS regions (`us-east-1`, `us-west-1`, `ap-south-1`, etc).
- **Error Handling**: Handles HTTP status codes (200, 403, 404) to detect accessibility.
- **CLI Interface**: Simple command-line interface for ease of use.
- **Export Results** *(Coming Soon)*: Export scan results to a `.txt` or `.csv` file.

---

## 📦 Usage

```bash
python s3finder.py

# Go to your project directory
cd /path/to/s3-bucket-finder

# Initialize Git repo
git init

# Add all project files to Git
git add .

# Commit with a message
git commit -m "Initial commit: S3 Bucket Finder tool"

# Add your GitHub remote
git remote add origin https://github.com/harshalaute/s3-bucket-finder.git

# Rename default branch to main
git branch -M main

# Push the project to GitHub
git push -u origin main


---

### ✅ Ab tu is README.md ko apni repo me daal de.  
File save kar: `README.md`  
Aur commit + push kar:

```bash
git add README.md
git commit -m "Added README.md with usage and setup instructions"
git push
