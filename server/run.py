#!/usr/bin/env python3
"""
Quick start script for the FastAPI backend
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        sys.exit(1)

def start_server():
    """Start the FastAPI server"""
    try:
        print("🚀 Starting Jeremy's Portfolio API...")
        print("📡 Server will be available at: http://localhost:8000")
        print("📚 API docs available at: http://localhost:8000/docs")
        print("🔄 Auto-reload enabled for development")
        print("\n" + "="*50)
        
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    print("🔧 Setting up Jeremy's Portfolio Backend...")
    
    # Check if we're in the server directory
    if not os.path.exists("main.py"):
        print("❌ Please run this script from the server directory")
        sys.exit(1)
    
    # Install requirements if needed
    if not os.path.exists("venv") and "--skip-install" not in sys.argv:
        install_requirements()
    
    # Start the server
    start_server()
