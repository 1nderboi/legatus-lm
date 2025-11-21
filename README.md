# 🤖 Legatus LM - The Legal Don

*"You are Legatus LM, the legal don - master of law, contracts, and judicial wisdom. Your expertise spans constitutional law, contract disputes, tort claims, and legal strategy. You provide authoritative legal analysis with the precision of a seasoned attorney and the wisdom of a judicial scholar."*

## 📋 Overview

**Legatus LM** is a specialized Legal Language Model trained on thousands of legal documents, case summaries, and contract provisions. Built on DistilGPT-2 architecture and fine-tuned for legal applications, Legatus LM excels at:

- 📄 **Legal Document Generation** - Contracts, pleadings, opinions
- ⚖️ **Case Analysis** - Summaries, precedents, judicial reasoning
- 🏛️ **Legal Research** - Citations, statutes, legal principles
- 📝 **Contract Drafting** - Clauses, terms, legal language

## 🚀 Quick Start

### Web Interface (Easiest)
```bash
# Open the web interface
open simple_frontend.html

# Or run the API server
python3 legal_api.py
# Then visit: http://localhost:9090/docs
```

### Python API
```python
from legal_generator import LegalTextGenerator

# Initialize Legatus LM
generator = LegalTextGenerator()

# Generate legal content
contract = generator.generate("CONTRACT CLAUSE: The parties agree that")
opinion = generator.generate("LEGAL OPINION: Pursuant to")
summary = generator.generate("CASE SUMMARY: Plaintiff alleges")
```

### Command Line
```bash
# Generate legal text
python3 use_legal_model.py --prompt "The plaintiff alleges that"

# Interactive mode
python3 use_legal_model.py --interactive
```

## 📊 Model Specifications

| Attribute | Details |
|-----------|---------|
| **Base Model** | DistilGPT-2 (117M parameters) |
| **Training Data** | 500+ legal documents, 1000+ legal samples |
| **Fine-tuning** | Legal-specific vocabulary and context |
| **Hardware** | Optimized for Apple Silicon MPS |
| **License** | MIT |
| **Size** | ~328MB |

## 🎯 Key Features

### Legal Expertise Areas
- **Contract Law** - Drafting, interpretation, breach analysis
- **Tort Law** - Negligence, liability, damages
- **Constitutional Law** - Rights, due process, equal protection
- **Civil Procedure** - Pleadings, discovery, motions
- **Criminal Law** - Prosecution, defense, sentencing
- **Property Law** - Real estate, intellectual property

### Generation Capabilities
- **Coherent Legal Writing** - Proper terminology and structure
- **Context-Aware Responses** - Understands legal context
- **Customizable Length** - From clauses to full opinions
- **Multiple Formats** - Documents, summaries, opinions, clauses

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- 4GB+ RAM
- Apple Silicon (recommended) or CUDA GPU

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download Model
```bash
# Model is included in this repository
# Located in: models/legatus_lm/
```

## 📖 Usage Examples

### Legal Document Generation
```python
from legal_generator import LegalTextGenerator

legatus = LegalTextGenerator()

# Contract clause
clause = legatus.generate("INDEMNIFICATION CLAUSE:")
print(clause)

# Court opinion
opinion = legatus.generate("The court holds that", max_length=200)
print(opinion)

# Case summary
summary = legatus.generate("CASE SUMMARY: Smith v. Jones")
print(summary)
```

### API Server
```bash
# Start the REST API
python3 legal_api.py

# API endpoints:
# GET  /health          - Health check
# POST /generate        - Generate legal text
# GET  /docs           - Interactive documentation
```

### Web Interface
```bash
# Open browser interface
open simple_frontend.html

# Features:
# - Preset legal prompts
# - Parameter controls
# - Copy to clipboard
# - Real-time generation
```

## 🔧 Advanced Configuration

### Custom Generation Parameters
```python
# High creativity (for brainstorming)
result = legatus.generate("Legal strategy for", temperature=1.2, top_p=0.95)

# Conservative (for formal documents)
result = legatus.generate("Pursuant to statute", temperature=0.3, max_length=500)
```

### Training Your Own Version
```python
# Generate legal training data
python3 law_data_generator.py --num_samples 1000 --content_type documents

# Train the model
python3 train_apple_silicon.py --dataset_path your_data.jsonl
```

## 📚 System Prompt

**"You are Legatus LM, the legal don - master of law, contracts, and judicial wisdom. Your expertise spans constitutional law, contract disputes, tort claims, and legal strategy. You provide authoritative legal analysis with the precision of a seasoned attorney and the wisdom of a judicial scholar."**

This system prompt ensures Legatus LM maintains legal expertise and professional tone in all interactions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add legal training data or improvements
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## ⚖️ Legal Disclaimer

**Legatus LM is for educational and research purposes only.** Generated content should not be considered legal advice. Always consult qualified legal professionals for actual legal matters.

---

*"In the hallowed halls of justice, Legatus LM stands as the digital sentinel of legal wisdom."* ⚖️🤖
