#!/usr/bin/env python3
"""
Simple programmatic interface for the legal LLM
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

class LegalTextGenerator:
    def __init__(self, model_path="."):
        """Initialize the legal text generator"""
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.device = None

    def load_model(self):
        """Load the model if not already loaded"""
        if self.model is not None:
            return

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model not found at {self.model_path}")

        print("🔧 Loading legal LLM...")
        self.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path)
        self.model.to(self.device)
        self.model.eval()

        print(f"✅ Model loaded on {self.device}")

    def generate(self, prompt, max_length=200, temperature=0.8, **kwargs):
        """Generate legal text from a prompt"""
        if self.model is None:
            self.load_model()

        # Default generation parameters
        generation_kwargs = {
            "max_length": max_length,
            "temperature": temperature,
            "do_sample": True,
            "top_p": 0.9,
            "top_k": 50,
            "pad_token_id": self.tokenizer.eos_token_id,
            "repetition_penalty": 1.2,
            **kwargs
        }

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                attention_mask=inputs.get("attention_mask"),
                **generation_kwargs
            )

        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text

# Example usage functions
def generate_case_summary(generator, case_title="Smith v. Johnson"):
    """Generate a case summary"""
    prompt = f"CASE SUMMARY: {case_title}\n\nFACTS: "
    return generator.generate(prompt, max_length=300)

def generate_contract_clause(generator, clause_type="confidentiality"):
    """Generate a contract clause"""
    prompt = f"{clause_type.upper()} CLAUSE: "
    return generator.generate(prompt, max_length=150)

def generate_legal_opinion(generator, issue="contract breach"):
    """Generate a legal opinion"""
    prompt = f"LEGAL OPINION: Regarding {issue}, "
    return generator.generate(prompt, max_length=250)

# Example usage
if __name__ == "__main__":
    # Initialize generator
    generator = LegalTextGenerator()

    print("🧪 Testing Legal Text Generator")
    print("=" * 50)

    # Generate different types of legal content
    examples = [
        ("Case Summary", lambda: generate_case_summary(generator, "Johnson v. State")),
        ("Contract Clause", lambda: generate_contract_clause(generator, "indemnification")),
        ("Legal Opinion", lambda: generate_legal_opinion(generator, "employment discrimination")),
        ("Custom Prompt", lambda: generator.generate("The plaintiff alleges that", max_length=100))
    ]

    for title, generate_func in examples:
        print(f"\n📄 {title}:")
        print("-" * 30)
        try:
            result = generate_func()
            # Show just the generated part (remove prompt if it's included)
            print(result.strip())
        except Exception as e:
            print(f"❌ Error: {e}")
        print()

    print("✅ Generation complete!")
