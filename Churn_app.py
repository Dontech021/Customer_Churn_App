import os
import sys
import subprocess
import streamlit as st
p=subprocess.call(['pwd'])
name = 'main'

subprocess.call(['pip', 'install', '-r', 'requirement.txt', '--target=/home/appuser/venv/lib/python3.9/site-packages'])
