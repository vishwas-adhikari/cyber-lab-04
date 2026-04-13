#!/bin/bash
echo "[*] Building Docker Image..."
docker build -t lab4-image .
echo "[*] Starting Lab Container..."
docker run -d -p 80:80 --name lab4-container lab4-image
echo "[*] Lab is running at http://localhost"
