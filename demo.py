#!/usr/bin/env python3
"""
🚀 Legatus LM Demo - The Legal Don

Quick demonstration of Legatus LM's legal text generation capabilities.
"""

import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from legal_generator import LegalTextGenerator

def main():
    print("🤖 LEGATUS LM - THE LEGAL DON")
    print("=" * 50)
    print()
    print('"You are Legatus LM, the legal don - master of law, contracts, and judicial wisdom."')
    print()

    try:
        # Initialize Legatus LM
        print("🔧 Initializing Legatus LM...")
        generator = LegalTextGenerator()
        print("✅ Model loaded successfully!")
        print()

        # Demo prompts
        demo_prompts = [
            ("Contract Law", "CONTRACT CLAUSE: The parties agree that"),
            ("Tort Law", "The plaintiff alleges that"),
            ("Constitutional Law", "Pursuant to the First Amendment"),
            ("Case Summary", "CASE SUMMARY: Smith v. Johnson"),
            ("Legal Opinion", "LEGAL OPINION: The court holds that")
        ]

        print("📄 Generating Legal Content:")
        print("-" * 30)

        for category, prompt in demo_prompts:
            print(f"\n🔹 {category}:")
            print(f"Prompt: '{prompt}'")

            try:
                # Generate text
                result = generator.generate(prompt, max_length=100, temperature=0.8)
                # Show only the generated part
                generated_part = result[len(prompt):].strip()
                if len(generated_part) > 150:
                    generated_part = generated_part[:150] + "..."
                print(f"Result: {generated_part}")
            except Exception as e:
                print(f"❌ Error: {e}")

        print("\n" + "=" * 50)
        print("🎉 Demo Complete!")
        print()
        print("To use Legatus LM:")
        print("1. python3 legal_api.py          # Start API server")
        print("2. open simple_frontend.html     # Open web interface")
        print("3. python3 demo.py              # Run this demo")
        print("4. Visit http://localhost:9090/docs  # API documentation")

    except Exception as e:
        print(f"❌ Error initializing Legatus LM: {e}")
        print("\nMake sure you have:")
        print("- Python 3.8+ installed")
        print("- Required packages: pip install -r requirements.txt")
        print("- Model files in the current directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
