#!/bin/bash

# Fake News Detection - Quick Start Script for Linux/Mac

echo ""
echo "============================================================"
echo " Fake News Detection System - Quick Start"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo "[3/4] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[4/4] Training model..."
python train.py
if [ $? -ne 0 ]; then
    echo "ERROR: Model training failed"
    exit 1
fi

echo ""
echo "============================================================"
echo " Setup Complete!"
echo "============================================================"
echo ""
echo "Starting Flask web server..."
echo ""
echo "The application will be available at:"
echo "  http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
