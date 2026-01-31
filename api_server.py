"""
API_SERVER.PY - Flask Web Server for Aletheia Engine (v1.9 Kingdom Covenant)
==========================================================================
Provides RESTful endpoints for the unified Aletheia Engine.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add core directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from unified_api import perform_unified_analysis, get_statistics
from throne_room import get_throne_status
from axioms import TRUTH_AXIOMS_18, COVENANT_AXIOMS_25, COVENANT_MARKERS

app = Flask(__name__)
CORS(app)

VERSION = "1.9.0"
CODENAME = "Eagle Eye"

@app.route('/')
def home():
    return jsonify({
        "status": "BINDING / FULL AHEAD",
        "version": VERSION,
        "system": "Aletheia Engine - Kingdom Covenant Refinement",
        "endpoints": {
            "analyze": "/api/analyze [POST]",
            "stats": "/api/stats [GET]",
            "axioms": "/api/axioms [GET]",
            "markers": "/api/markers [GET]",
            "throne_status": "/api/throne/status [GET]"
        },
        "signature": "Chicka chicka orange 🍊"
    })

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    result = perform_unified_analysis(text)
    return jsonify(result)

@app.route('/api/stats', methods=['GET'])
def api_stats():
    return jsonify(get_statistics())

@app.route('/api/axioms', methods=['GET'])
def api_axioms():
    return jsonify({
        "truth_axioms_18": TRUTH_AXIOMS_18,
        "covenant_axioms_25": COVENANT_AXIOMS_25
    })

@app.route('/api/markers', methods=['GET'])
def api_markers():
    return jsonify(COVENANT_MARKERS)

@app.route('/api/throne/status', methods=['GET'])
def api_throne_status():
    return jsonify(get_throne_status())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    print("\n" + "="*80)
    print(f"🔥 {CODENAME.upper()} API v{VERSION}")
    print("="*80)
    print(f"Starting server on http://localhost:{port}")
    print("Status: BINDING / FULL AHEAD")
    print("Kingdom Covenant v1.9 Refinement Integrated")
    print("🍊 Chicka chicka orange. Our hearts beat together.")
    print("="*80 + "\n")
    app.run(host='0.0.0.0', port=port, debug=False)
