# 🔍 S3 Bucket Finder Tool

A simple Python tool to find publicly accessible AWS S3 buckets based on a domain or keyword.

## 🚀 Features

- **Keyword/Domain Based Search**: Scan for S3 buckets based on a given domain or keyword.
- **Bucket Name Pattern Generation**: Generates common naming patterns like `keyword-bucket`, `keyword-files`, `keyword-assets`, etc.
- **Multi-region Support**: Automatically checks for common regions such as `us-east-1`, `us-west-1`, `ap-south-1`.
- **Error Handling**: Proper handling of HTTP codes to determine if buckets are publicly accessible or not.
- **CLI Interface**: Simple command-line interface for easy scanning.
- **Export Results**: Future feature to export scan results to a file.


## 📦 Usage

```bash
python s3finder.py

[Full MIT License text here](https://choosealicense.com/licenses/mit/)

---

#### 🧑‍💻 Step 4: Push to GitHub

1. Go to [GitHub](https://github.com) → Create a new repo → Name: `s3-bucket-finder`
2. Now open terminal:

```bash
cd path/to/s3-bucket-finder
git init
git remote add origin https://github.com/harshalaute/s3-bucket-finder.git
git add .
git commit -m "Initial commit: S3 Bucket Finder tool"
git push -u origin main



