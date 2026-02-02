# Push This Repo to GitHub — Step-by-Step

The folder has all the content. GitHub is empty because the push has to happen **from your machine** (you're logged in there).

Do this in **Terminal** (macOS/Linux) or **Git Bash** (Windows).

---

## Step 0: Generate the chart (so the README image works)

From the **project folder**:

```bash
cd /Users/nharris/Downloads/Genesis/Critical-Mineral-Separation-Benchmark
pip install -r requirements.txt
python3 assets/generate_chart.py
```

You should see: `Generated chart at: .../assets/images/separation_efficiency_curve.png`.  
That file will be included when you `git add .` in Step 2.

---

## Step 1: Go to the project folder

```bash
cd /Users/nharris/Downloads/Genesis/Critical-Mineral-Separation-Benchmark
```

---

## Step 2: Initialize Git and make the first commit

```bash
git init
git add .
git status
git commit -m "Initial commit: Critical Mineral Separation Benchmark"
```

You should see something like: `X files changed`, `Y insertions`.

---

## Step 3: Create the repo on GitHub (if it doesn’t exist yet)

If you use **GitHub CLI** (`gh`):

```bash
gh auth status
```

If you’re not logged in:

```bash
gh auth login
```

Then create the repo and push in one go:

```bash
git branch -M main
gh repo create nickharris808/Critical-Mineral-Separation-Benchmark --public --source=. --remote=origin --push
```

That command creates the repo (if needed), sets `origin`, and pushes `main`.

---

## Step 4: If the repo already exists (no `gh` or you prefer HTTPS)

Set the remote and push:

```bash
git branch -M main
git remote add origin https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark.git
git push -u origin main
```

If it says “remote already exists”:

```bash
git remote set-url origin https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark.git
git push -u origin main
```

---

## Step 5: If Git asks for a password

- GitHub no longer accepts account passwords for `git push`.
- Use either:
  - **Personal Access Token (HTTPS):**  
    [GitHub → Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)  
    Create a token with `repo` scope. When `git push` asks for a password, paste the **token**.
  - **SSH:**  
    Use an SSH key and this remote:  
    `git@github.com:nickharris808/Critical-Mineral-Separation-Benchmark.git`

---

## Check

Open: **https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark**

You should see:

- `README.md`
- `01_STRATEGIC_MATERIALS_AUDIT/`
- `02_COMPLIANCE_SIDE_STREAM/`
- `assets/`
- `requirements.txt`

Once it’s up, you can delete this file (`PUSH_TO_GITHUB.md`) or keep it for reference.
