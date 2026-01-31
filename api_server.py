"""
API_SERVER.PY - Flask REST API for Aletheia Engine (v1.1.0 Integration)
======================================================================

Provides HTTP endpoints for:
- Text analysis (Lambda + DreamSpeak + Human Meter + Throne Room)
- History retrieval
- Statistics
- Health checks
- Throne Room status

Designed for integration with Human Meter UI and other clients.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add core directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from unified_api import AletheiaEngine

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Initialize engine
engine = AletheiaEngine()


@app.route('/')
def home():
    """Root endpoint - API information."""
    return jsonify({
        "name": "Aletheia Engine API",
        "version": engine.VERSION,
        "codename": engine.CODENAME,
        "status": "BINDING / FULL AHEAD",
        "endpoints": {
            "analyze": "/api/analyze [POST]",
            "history": "/api/history [GET]",
            "statistics": "/api/statistics [GET]",
            "health": "/api/health [GET]",
            "reset": "/api/reset [POST]",
            "throne_status": "/api/throne/status [GET]",
        },
        "signature": "Chicka chicka orange 🍊"
    })


@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "version": engine.VERSION,
        "analyses_count": len(engine.analysis_history),
    })


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyze text input.
    
    Request body:
    {
        "text": "input text to analyze",
        "truth_score": 0.5,  // optional
        "covenant_alignment": 0.5,  // optional
        "apply_filter": true  // optional
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                "error": "Missing 'text' field in request body"
            }), 400
        
        text = data['text']
        truth_score = data.get('truth_score')
        covenant_alignment = data.get('covenant_alignment')
        apply_filter = data.get('apply_filter', True)
        
        # Validate scores if provided
        if truth_score is not None and not (0.0 <= truth_score <= 1.0):
            return jsonify({
                "error": "truth_score must be between 0.0 and 1.0"
            }), 400
        
        if covenant_alignment is not None and not (0.0 <= covenant_alignment <= 1.0):
            return jsonify({
                "error": "covenant_alignment must be between 0.0 and 1.0"
            }), 400
        
        # Perform analysis
        result = engine.analyze(
            text=text,
            truth_score=truth_score,
            covenant_alignment=covenant_alignment,
            apply_filter=apply_filter,
        )
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/history')
def get_history():
    """Get analysis history."""
    try:
        limit = request.args.get('limit', type=int)
        offset = request.args.get('offset', default=0, type=int)
        
        history = engine.get_history()
        
        # Apply pagination
        if limit:
            history = history[offset:offset+limit]
        else:
            history = history[offset:]
        
        return jsonify({
            "total": len(engine.analysis_history),
            "offset": offset,
            "limit": limit,
            "results": history,
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/statistics')
def get_statistics():
    """Get aggregate statistics."""
    try:
        stats = engine.get_statistics()
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/throne/status')
def throne_status():
    """Get Throne Room status."""
    try:
        status = engine.throne_room.get_sanctuary_status()
        return jsonify(status)
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset all engines and history."""
    try:
        engine.reset()
        return jsonify({
            "status": "success",
            "message": "All engines and history reset"
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/dreamspeak/archive')
def dreamspeak_archive():
    """Get DreamSpeak resonance archive."""
    try:
        archive = engine.dreamspeak_engine.get_resonance_archive()
        return jsonify({
            "total": len(archive),
            "archive": archive,
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/dreamspeak/signals')
def dreamspeak_signals():
    """Get active DreamSpeak signals."""
    try:
        signals = engine.dreamspeak_engine.get_active_signals()
        stats = engine.dreamspeak_engine.get_recurrence_stats()
        
        return jsonify({
            "active_signals": signals,
            "recurrence_stats": stats,
            "eternal_status": engine.dreamspeak_engine.calculate_eternal_solution_status(),
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/lambda/history')
def lambda_history():
    """Get Lambda calculation history."""
    try:
        history = engine.lambda_engine.get_history()
        average = engine.lambda_engine.get_average_lambda()
        
        return jsonify({
            "total": len(history),
            "average_lambda": average,
            "history": history,
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/api/human-meter/history')
def human_meter_history():
    """Get Human Meter distortion history."""
    try:
        history = engine.human_meter.get_distortion_history()
        average = engine.human_meter.get_average_distortion()
        
        return jsonify({
            "total": len(history),
            "average_distortion": average,
            "history": history,
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Endpoint not found",
        "available_endpoints": {
            "root": "/",
            "analyze": "/api/analyze [POST]",
            "history": "/api/history [GET]",
            "statistics": "/api/statistics [GET]",
            "health": "/api/health [GET]",
        }
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal server error",
        "message": str(error)
    }), 500


if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 8888))
    
    print("\n" + "="*80)
    print(f"🔥 {engine.CODENAME.upper()} API v{engine.VERSION}")
    print("="*80)
    print(f"Starting server on http://localhost:{port}")
    print("Status: BINDING / FULL AHEAD")
    print("Kingdom Covenant v1.8 Refinement Integrated")
    print("🍊 Chicka chicka orange. Our hearts beat together.")
    print("="*80 + "\n")
    
    # Run server
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
    )
