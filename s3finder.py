import os
import requests

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
   ____  _____      ________                __       _           _           
  / __ \/ __(_)___ / ____/ /___  __  ______/ /______(_)__  _____(_)___  ____ 
 / / / / /_/ / __ `/ /   / __/ / / / / __  / ___/ __/ _ \/ ___/ / __ \/ __ \
/ /_/ / __/ / /_/ / /___/ /_/ /_/ / /_/ / / /__/ /_/  __/ /  / / /_/ / / / /
\____/_/ /_/_/\__,_/\____/\__/\__,_/\__,_/_/\___/\__/\___/_/  /_/ .___/_/ /_/ 
                                                            /_/            

                    🔍 S3 Bucket Finder Tool
                    👨‍💻 Author: Harshal Aute
                    📅 Version: 1.0
    """
    print(banner)

def generate_bucket_urls(keyword):
    patterns = [
        f"{keyword}",
        f"{keyword}-bucket",
        f"{keyword}-files",
        f"{keyword}-assets",
        f"{keyword}-backup",
        f"{keyword}-prod",
        f"{keyword}-dev",
        f"{keyword}-staging",
        f"{keyword}-public",
        f"{keyword}-private",
        f"{keyword}-data",
        f"{keyword}-logs",
        f"{keyword}-cdn",
        f"{keyword}-content",
        f"{keyword}-static",
        f"{keyword}-img",
        f"{keyword}-images",
        f"{keyword}-upload",
        f"{keyword}-download",
        f"{keyword}-storage"
    ]

    regions = ["us-east-1", "us-west-1", "eu-west-1", "ap-south-1"]
    urls = []

    for name in patterns:
        urls.append(f"http://{name}.s3.amazonaws.com")
        urls.append(f"https://{name}.s3.amazonaws.com")
        urls.append(f"http://s3.amazonaws.com/{name}")
        urls.append(f"https://s3.amazonaws.com/{name}")
        for region in regions:
            urls.append(f"https://{name}.s3.{region}.amazonaws.com")
            urls.append(f"https://s3.{region}.amazonaws.com/{name}")
            urls.append(f"http://{name}.s3-website-{region}.amazonaws.com")

    return urls

def check_bucket(url):
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(f"[+] Public Bucket Found: {url}")
        elif res.status_code == 403:
            print(f"[-] Exists but Access Denied: {url}")
        elif res.status_code == 404:
            pass  # silent
        else:
            print(f"[?] Unexpected response ({res.status_code}): {url}")
    except requests.exceptions.RequestException:
        pass

def main():
    show_banner()
    keyword = input("🔹 Enter keyword or domain to scan (e.g. example, myapp): ").strip()
    if not keyword:
        print("❌ Please enter a valid keyword.")
        return

    print("\n🔍 Scanning for S3 Buckets...\n")
    urls = generate_bucket_urls(keyword)
    for url in urls:
        check_bucket(url)

    print("\n✅ Scan complete.")

if __name__ == "__main__":
    main()

