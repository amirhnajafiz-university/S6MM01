#!/bin/bash

function pip-install-save { 
    pip install $1 
    pip freeze | grep $1 >> requirements.txt
}

echo "[OK] Installing $1 ..."

pip-install-save
