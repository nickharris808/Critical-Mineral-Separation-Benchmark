# How to Push This Repository to GitHub

This document provides step-by-step instructions to publish the Critical Mineral Separation Benchmark to GitHub.

---

## Prerequisites

1. **GitHub Account:** You need a GitHub account (https://github.com)

2. **Git Installed:** Check with `git --version`

3. **GitHub CLI (optional but recommended):** Check with `gh --version`
   - Install: https://cli.github.com/

4. **Python + Dependencies:** For generating charts before pushing
   ```bash
   python3 --version
   pip install -r requirements.txt
   ```

---

## Step 0: Generate Charts (IMPORTANT)

The README embeds images that must be generated locally before pushing:

```bash
# Navigate to the repository
cd /Users/nharris/Downloads/Genesis/Critical-Mineral-Separation-Benchmark

# Install dependencies
pip install -r requirements.txt

# Generate all charts
python3 assets/generate_all_charts.py
```

You should see:
```
================================================================
CHART GENERATION SUITE
Critical Mineral Separation Benchmark
================================================================

Output directory: /Users/nharris/Downloads/Genesis/Critical-Mineral-Separation-Benchmark/assets/images
Generating Figure 1: Separation Efficiency Curve...
  ✓ Saved: .../separation_efficiency_curve.png
Generating Figure 2: PFAS Binding Energy Comparison...
  ✓ Saved: .../binding_energy_comparison.png
Generating Figure 3: Economic Impact Analysis...
  ✓ Saved: .../economic_impact.png
Generating Figure 4: Supply Chain Risk Map...
  ✓ Saved: .../supply_chain_risk.png

================================================================
SUCCESS: Generated 4 figures
================================================================
```

---

## Step 1: Initialize Git Repository

If not already initialized:

```bash
cd /Users/nharris/Downloads/Genesis/Critical-Mineral-Separation-Benchmark

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Critical Mineral Separation Benchmark

Technical white paper on thermodynamic selectivity in REE recovery.
Includes:
- Janus Ligand vs P507 separation factor comparison
- PFAS remediation secondary application
- DFT methodology documentation
- Reproducible audit scripts
- Publication-quality visualizations

Patent Status: Provisional filed January 2026"
```

---

## Step 2: Create GitHub Repository

### Option A: Using GitHub CLI (Recommended)

```bash
# Authenticate if needed
gh auth login

# Create the repo (public)
gh repo create nickharris808/Critical-Mineral-Separation-Benchmark \
  --public \
  --description "Technical benchmark: REE separation efficiency. Janus Ligand vs P507." \
  --source=. \
  --remote=origin \
  --push
```

### Option B: Using GitHub Web Interface

1. Go to https://github.com/new

2. Fill in:
   - **Repository name:** `Critical-Mineral-Separation-Benchmark`
   - **Description:** `Technical benchmark: REE separation efficiency. Janus Ligand vs P507.`
   - **Visibility:** Public
   - **DO NOT** initialize with README, .gitignore, or license

3. Click **Create repository**

4. Then run:
   ```bash
   # Add remote
   git remote add origin https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark.git

   # Push
   git branch -M main
   git push -u origin main
   ```

---

## Step 3: Verify Publication

Visit: https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark

You should see:
- README.md rendered with embedded images
- Directory structure (01_STRATEGIC_MATERIALS_AUDIT, etc.)
- License badge, patent badge, DFT badge

---

## Troubleshooting

### Authentication Errors

If `git push` fails with authentication errors:

1. **GitHub CLI:** Run `gh auth login` and follow prompts

2. **Personal Access Token:**
   - Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
   - Generate new token with `repo` scope
   - Use token as password when prompted

3. **SSH Keys:**
   ```bash
   # Generate key if needed
   ssh-keygen -t ed25519 -C "your_email@example.com"
   
   # Add to SSH agent
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   
   # Copy public key
   cat ~/.ssh/id_ed25519.pub
   
   # Add to GitHub: Settings → SSH and GPG keys → New SSH key
   
   # Change remote to SSH
   git remote set-url origin git@github.com:nickharris808/Critical-Mineral-Separation-Benchmark.git
   ```

### Images Not Showing

1. Verify images exist locally:
   ```bash
   ls -la assets/images/
   ```

2. Regenerate if needed:
   ```bash
   python3 assets/generate_all_charts.py
   ```

3. Make sure images are committed:
   ```bash
   git add assets/images/*.png
   git commit -m "Add generated charts"
   git push
   ```

### Large Files Warning

Git may warn about large files. Our images should be <1MB each, which is fine. If you see warnings about files >50MB, check for accidental inclusion of data files.

---

## Post-Publication Checklist

After pushing:

- [ ] README renders correctly with embedded images
- [ ] Audit scripts work when cloned fresh
- [ ] Chart generation works in clean environment
- [ ] FAQ and methodology docs are accessible
- [ ] License is correctly displayed

---

## Sharing the Repository

Use this link:
**https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark**

For Hacker News / HackerNoon, consider a title like:
> "We reduced rare earth Nd/Fe separation from ~10 stages to 1. Here's the thermodynamics."

Or:
> "DFT-validated ligand design achieves 4,400x selectivity improvement for Nd/Fe separation"

Or (for full REE refinery context):
> "Janus Ligands: From 50-150 stages to single-stage rare earth separation"

---

*Last updated: February 2026*
