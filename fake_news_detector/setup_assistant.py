#!/usr/bin/env python3
"""
🔍 FAKE NEWS DETECTION SYSTEM - STARTUP & SETUP ASSISTANT

This script guides you through setting up and running the system.
Run this first after installation!
"""

import os
import sys
import subprocess
import platform

class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}▶ {text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def check_python():
    """Check if Python version is compatible"""
    print_header("🐍 Python Version Check")
    
    version = sys.version_info
    python_version = f"{version.major}.{version.minor}.{version.micro}"
    
    print(f"Python version: {python_version}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error("Python 3.8+ required!")
        print_info("Download from: https://www.python.org/downloads/")
        return False
    
    print_success("Python version compatible!")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    print_header("📦 Checking Dependencies")
    
    packages = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'sklearn': 'Scikit-learn',
        'flask': 'Flask',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn',
        'joblib': 'Joblib',
    }
    
    missing = []
    for package, name in packages.items():
        try:
            __import__(package)
            print_success(f"{name}")
        except ImportError:
            print_error(f"{name} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print_warning(f"\nMissing {len(missing)} packages")
        print_info("Installing dependencies...")
        return install_dependencies()
    
    print_success("\nAll dependencies installed!")
    return True

def install_dependencies():
    """Install required packages"""
    print_info("Running: pip install -r requirements.txt")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print_success("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print_error("Failed to install dependencies")
        return False

def check_model():
    """Check if model exists"""
    print_header("🤖 Model Check")
    
    model_path = 'models/fake_news_model.pkl'
    
    if os.path.exists(model_path):
        print_success("Model found!")
        return True
    else:
        print_warning("Model not found - need to train first")
        return False

def train_model():
    """Train the model"""
    print_header("🚀 Training Model")
    
    print_info("This will train the ML model (~5-10 seconds)")
    print_info("Generating 2000 sample articles...")
    print_info("Training model with ~95% target accuracy...")
    print_info("Saving model to models/fake_news_model.pkl...")
    
    try:
        subprocess.check_call([sys.executable, 'train.py'])
        print_success("Model trained successfully!")
        return True
    except subprocess.CalledProcessError:
        print_error("Model training failed")
        return False

def test_setup():
    """Run setup tests"""
    print_header("🧪 Running Component Tests")
    
    try:
        subprocess.check_call([sys.executable, 'test_setup.py'])
        return True
    except subprocess.CalledProcessError:
        return False

def start_server():
    """Start the Flask server"""
    print_header("🌐 Starting Web Server")
    
    print_info("Server configuration:")
    print_info("  Host: 0.0.0.0")
    print_info("  Port: 5000")
    print_info("  Debug: True")
    print(f"\n{Colors.BOLD}Server will be available at:{Colors.END}")
    print(f"{Colors.GREEN}► http://localhost:5000{Colors.END}\n")
    print_info("Press Ctrl+C to stop the server")
    
    try:
        subprocess.call([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print_info("\nServer stopped")

def show_menu():
    """Show interactive menu"""
    print_header("🔍 Fake News Detection System - Setup Menu")
    
    print("Choose an option:")
    print(f"  {Colors.BOLD}1{Colors.END} - Run complete setup (dependencies → train → test)")
    print(f"  {Colors.BOLD}2{Colors.END} - Install dependencies only")
    print(f"  {Colors.BOLD}3{Colors.END} - Train model")
    print(f"  {Colors.BOLD}4{Colors.END} - Run component tests")
    print(f"  {Colors.BOLD}5{Colors.END} - Start web server")
    print(f"  {Colors.BOLD}6{Colors.END} - View documentation")
    print(f"  {Colors.BOLD}7{Colors.END} - Run examples")
    print(f"  {Colors.BOLD}8{Colors.END} - Exit")
    print()

def view_docs():
    """Display documentation"""
    print_header("📚 Available Documentation")
    
    docs = {
        '1': ('QUICKSTART.md', 'Quick start guide (3-step setup)'),
        '2': ('README.md', 'Complete overview & features'),
        '3': ('DOCUMENTATION.md', 'Technical reference'),
        '4': ('ARCHITECTURE.md', 'System architecture'),
        '5': ('INDEX.md', 'Quick reference'),
    }
    
    for key, (file, desc) in docs.items():
        print(f"  {Colors.BOLD}{key}{Colors.END} - {file}")
        print(f"     {Colors.BLUE}{desc}{Colors.END}")
    
    choice = input(f"\n{Colors.BOLD}Select (1-5) or press Enter to skip: {Colors.END}").strip()
    
    if choice in docs:
        file = docs[choice][0]
        if os.path.exists(file):
            print(f"\n{Colors.CYAN}Reading {file}...{Colors.END}\n")
            with open(file, 'r') as f:
                content = f.read()
            # Show first 50 lines or less
            lines = content.split('\n')[:50]
            for line in lines:
                print(line)
            print(f"\n... (truncated) Run `cat {file}` to see full content")
            input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")

def main():
    """Main setup flow"""
    os.system('clear' if platform.system() != 'Windows' else 'cls')
    
    print_header("🔍 FAKE NEWS DETECTION SYSTEM")
    print(f"{Colors.BOLD}Setup & Configuration Assistant{Colors.END}\n")
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Interactive menu
    while True:
        show_menu()
        choice = input(f"{Colors.BOLD}Select option (1-8): {Colors.END}").strip()
        
        if choice == '1':
            # Complete setup
            if check_dependencies() and train_model() and test_setup():
                print_success("\n✅ Setup complete! Ready to start server")
                if input(f"\n{Colors.BOLD}Start web server now? (y/n): {Colors.END}").lower() == 'y':
                    start_server()
        
        elif choice == '2':
            check_dependencies()
        
        elif choice == '3':
            if check_dependencies():
                train_model()
        
        elif choice == '4':
            test_setup()
        
        elif choice == '5':
            if check_model():
                start_server()
            else:
                if input("Train model first? (y/n): ").lower() == 'y':
                    if train_model():
                        start_server()
        
        elif choice == '6':
            view_docs()
        
        elif choice == '7':
            print_info("Running examples.py...")
            subprocess.call([sys.executable, 'examples.py'])
        
        elif choice == '8':
            print_info("Goodbye! 👋")
            sys.exit(0)
        
        else:
            print_error("Invalid option")
        
        if choice != '8':
            input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.END}")
            os.system('clear' if platform.system() != 'Windows' else 'cls')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrupted by user{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)
