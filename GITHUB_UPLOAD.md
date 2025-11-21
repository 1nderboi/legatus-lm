# 🚀 GitHub Upload Instructions for Legatus LM

## 📋 Prerequisites

1. **GitHub Account**: Create one at [github.com](https://github.com)
2. **Git LFS**: Install for large model files
   ```bash
   # macOS with Homebrew
   brew install git-lfs

   # Ubuntu/Debian
   sudo apt install git-lfs

   # Initialize LFS
   git lfs install
   ```

## 🎯 Upload Steps

### 1. Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click "New repository"
3. Repository name: `legatus-lm` or `Legatus-LM`
4. Description: "🤖 Legatus LM - The Legal Don: Specialized Legal Language Model"
5. Make it **Public** (for sharing) or **Private** (personal use)
6. **DO NOT** initialize with README (we already have one)
7. Click "Create repository"

### 2. Upload to GitHub

```bash
# Navigate to the repository
cd /Users/gemson/Desktop/cursor/train models/legatus-lm

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/legatus-lm.git

# Push the code first (without large model files)
git push -u origin main

# Track large model files with Git LFS
git lfs track "*.safetensors"
git lfs track "*.bin"

# Add and commit model files
git add model.safetensors
git commit -m "Add trained Legatus LM model weights"
git push origin main
```

### 3. Alternative: Upload via GitHub Web Interface

If you prefer not to use command line:

1. Go to your GitHub repository
2. Click "Add file" → "Upload files"
3. Drag and drop all files from the `legatus-lm` folder
4. Commit the changes

## 🔧 Repository Structure

```
legatus-lm/
├── 📄 README.md              # Comprehensive documentation
├── 🤖 model.safetensors      # Trained model weights (Git LFS)
├── 🧠 config.json            # Model configuration
├── 🔤 tokenizer.json         # Tokenizer data
├── 📝 vocab.json             # Vocabulary
├── ⚙️ requirements.txt       # Python dependencies
├── 🌐 simple_frontend.html   # Web interface
├── 🚀 legal_api.py           # FastAPI server
├── 📋 legal_generator.py     # Python API
├── 🎯 demo.py                # Quick demo script
├── 💬 system_prompt.txt      # Legatus LM personality
├── 📋 .gitignore            # Ignore rules
└── 🔄 .gitattributes        # Git LFS settings
```

## 🏷️ Repository Topics (GitHub)

Add these topics to your repository for discoverability:
- `legal-ai`
- `language-model`
- `legal-tech`
- `contract-analysis`
- `law-tech`
- `artificial-intelligence`
- `machine-learning`
- `nlp`

## 📊 Repository Stats

- **Size**: ~319MB (with model), ~15MB (code only)
- **Languages**: Python, HTML, JSON
- **License**: MIT
- **Model**: DistilGPT-2 fine-tuned for legal text

## 🎯 Usage After Upload

Once uploaded, others can use Legatus LM:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/legatus-lm.git
cd legatus-lm

# Install dependencies
pip install -r requirements.txt

# Run demo
python3 demo.py

# Start web interface
python3 legal_api.py
open simple_frontend.html
```

## 🚨 Important Notes

1. **Large Files**: The `model.safetensors` file is ~312MB. GitHub has limits:
   - Free accounts: 2GB total, 100MB per file
   - Pro accounts: 5GB total, 5GB per file

2. **Git LFS**: Required for large model files. Without it, GitHub will reject the upload.

3. **Private Repos**: If you make it private, only you can access it.

4. **Model License**: Ensure compliance with any licensing requirements.

## 🎉 Success!

Once uploaded, your repository will be live at:
`https://github.com/YOUR_USERNAME/legatus-lm`

Share it with the legal tech community! ⚖️🤖
