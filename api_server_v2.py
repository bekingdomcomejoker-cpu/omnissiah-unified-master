"""
API_SERVER_V2.PY - Enhanced Aletheia Engine API Server
======================================================
FastAPI server exposing all enhanced analysis capabilities.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
import uvicorn
from datetime import datetime
import sys
import os

# Add core directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

# Import all engine components
try:
    from core.unified_orchestrator import (
        analyze_comprehensive,
        get_orchestrator_statistics,
        export_analysis_json
    )
    from core.discernment_enhanced import (
        analyze_discernment,
        get_discernment_statistics
    )
    from core.pattern_recognition import (
        analyze_patterns,
        get_pattern_statistics
    )
    from core.temporal_coherence import (
        analyze_temporal_coherence,
        get_temporal_statistics
    )
    from core.reporting_engine import (
        generate_markdown_report,
        generate_html_report,
        generate_summary_report
    )
    ENGINES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Enhanced engines not available: {e}")
    ENGINES_AVAILABLE = False
    
# Try to import original engines as fallback
try:
    from core.unified_api import analyze as legacy_analyze
    from core.lambda_engine import calculate_lambda
    LEGACY_AVAILABLE = True
except ImportError:
    LEGACY_AVAILABLE = False

# ============================================================================
# API Models
# ============================================================================

class AnalysisRequest(BaseModel):
    """Request model for analysis"""
    text: str = Field(..., description="Text to analyze", min_length=1)
    context: Optional[Dict] = Field(None, description="Optional context information")
    include_prophecy: Optional[bool] = Field(True, description="Include prophecy generation")
    analysis_type: Optional[str] = Field("comprehensive", description="Type of analysis: comprehensive, discernment, pattern, temporal")

class AnalysisResponse(BaseModel):
    """Response model for analysis"""
    success: bool
    analysis_id: str
    timestamp: str
    data: Dict
    message: Optional[str] = None

class ReportRequest(BaseModel):
    """Request model for report generation"""
    analysis_id: str
    format: str = Field("markdown", description="Report format: markdown, html, json, summary")

class StatsResponse(BaseModel):
    """Response model for statistics"""
    success: bool
    engine: str
    statistics: Dict

# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Aletheia Engine API v2.0",
    description="Enhanced truth analysis and discernment engine with comprehensive multi-dimensional analysis",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Storage for analysis results (in-memory for now)
# ============================================================================

analysis_cache = {}

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint with API information"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Aletheia Engine API v2.0</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                   max-width: 1200px; margin: 0 auto; padding: 40px; background: #f5f7fa; }
            .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     color: white; padding: 40px; border-radius: 10px; text-align: center; }
            .content { background: white; padding: 30px; margin-top: 20px; border-radius: 10px; }
            .endpoint { background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #667eea; }
            .method { display: inline-block; padding: 4px 12px; border-radius: 4px; font-weight: bold; margin-right: 10px; }
            .get { background: #d4edda; color: #155724; }
            .post { background: #d1ecf1; color: #0c5460; }
            code { background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🦅 Aletheia Engine API v2.0</h1>
            <p>Enhanced Truth Analysis & Discernment Engine</p>
            <p><em>ἀλήθεια - The Un-concealment of Truth</em></p>
        </div>
        
        <div class="content">
            <h2>Available Endpoints</h2>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/analyze</strong>
                <p>Comprehensive multi-engine analysis</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/analyze/discernment</strong>
                <p>Enhanced discernment analysis (truth/fact/lie separation)</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/analyze/patterns</strong>
                <p>Pattern recognition and manipulation detection</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/analyze/temporal</strong>
                <p>Temporal coherence and consistency tracking</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/report/generate</strong>
                <p>Generate formatted reports (Markdown, HTML, JSON)</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/stats</strong>
                <p>Get comprehensive engine statistics</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/health</strong>
                <p>Health check endpoint</p>
            </div>
            
            <h2>Documentation</h2>
            <p>Interactive API documentation: <a href="/docs">/docs</a></p>
            <p>Alternative documentation: <a href="/redoc">/redoc</a></p>
            
            <h2>Features</h2>
            <ul>
                <li>✅ Comprehensive multi-dimensional analysis</li>
                <li>✅ Enhanced discernment engine (truth/fact/lie separation)</li>
                <li>✅ Advanced pattern recognition (30+ patterns)</li>
                <li>✅ Temporal coherence tracking</li>
                <li>✅ Manipulation detection</li>
                <li>✅ Signal/noise separation</li>
                <li>✅ Covenant axiom verification</li>
                <li>✅ Lambda & resonance measurement</li>
                <li>✅ Report generation (Markdown, HTML, JSON)</li>
            </ul>
            
            <p style="text-align: center; margin-top: 40px; color: #95a5a6;">
                <strong>Chicka chicka orange.</strong> 🍊
            </p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "2.0.0",
        "engines_available": ENGINES_AVAILABLE,
        "legacy_available": LEGACY_AVAILABLE,
        "timestamp": datetime.now().isoformat()
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Comprehensive analysis endpoint.
    
    Performs multi-engine analysis including:
    - Lambda & resonance analysis
    - Discernment (truth/fact/lie)
    - Pattern recognition
    - Temporal coherence
    - Risk assessment
    """
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    try:
        # Perform comprehensive analysis
        result = analyze_comprehensive(
            text=request.text,
            context=request.context,
            include_prophecy=request.include_prophecy
        )
        
        # Cache result
        analysis_cache[result.analysis_id] = result
        
        # Convert to dict for response
        response_data = {
            "analysis_id": result.analysis_id,
            "timestamp": result.timestamp,
            "overall_status": result.overall_status,
            "risk_level": result.risk_level,
            "confidence": result.overall_confidence,
            "unified_scores": result.unified_scores,
            "warnings": result.warnings,
            "recommendations": result.recommendations,
            "action_items": result.action_items,
            "lambda_analysis": result.lambda_analysis,
            "discernment_summary": {
                "truth_score": result.discernment_analysis.get('truth_score'),
                "fact_score": result.discernment_analysis.get('fact_score'),
                "lie_score": result.discernment_analysis.get('lie_score'),
                "coherence_score": result.discernment_analysis.get('coherence_score')
            },
            "pattern_summary": {
                "manipulation_score": result.pattern_analysis.get('manipulation_score'),
                "authenticity_score": result.pattern_analysis.get('authenticity_score'),
                "detected_patterns": result.pattern_analysis.get('detected_patterns')
            },
            "temporal_summary": {
                "consistency_score": result.temporal_analysis.get('consistency_score'),
                "drift_magnitude": result.temporal_analysis.get('drift_magnitude'),
                "stability_index": result.temporal_analysis.get('stability_index')
            }
        }
        
        return AnalysisResponse(
            success=True,
            analysis_id=result.analysis_id,
            timestamp=result.timestamp,
            data=response_data,
            message="Analysis completed successfully"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/analyze/discernment")
async def analyze_discernment_endpoint(request: AnalysisRequest):
    """Enhanced discernment analysis endpoint"""
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    try:
        result = analyze_discernment(request.text, request.context)
        
        return {
            "success": True,
            "timestamp": result.timestamp,
            "scores": {
                "truth": result.truth_score,
                "fact": result.fact_score,
                "lie": result.lie_score,
                "coherence": result.coherence_score,
                "semantic_drift": result.semantic_drift,
                "temporal_consistency": result.temporal_consistency
            },
            "phase_separation": result.phase_separation,
            "violations": result.violations,
            "recommendations": result.recommendations,
            "confidence": result.confidence
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Discernment analysis failed: {str(e)}")

@app.post("/analyze/patterns")
async def analyze_patterns_endpoint(request: AnalysisRequest):
    """Pattern recognition analysis endpoint"""
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    try:
        result = analyze_patterns(request.text, request.context)
        
        return {
            "success": True,
            "timestamp": result.timestamp,
            "scores": {
                "manipulation": result.manipulation_score,
                "authenticity": result.authenticity_score,
                "structural_integrity": result.structural_integrity
            },
            "detected_patterns": len(result.detected_patterns),
            "pattern_types": result.pattern_clusters,
            "recurring_themes": result.recurring_themes,
            "anomalies": result.anomalies,
            "recommendations": result.recommendations
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pattern analysis failed: {str(e)}")

@app.post("/analyze/temporal")
async def analyze_temporal_endpoint(request: AnalysisRequest):
    """Temporal coherence analysis endpoint"""
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    try:
        # Need to provide scores - use defaults for now
        scores = {
            'truth': 0.5,
            'fact': 0.5,
            'lie': 0.0,
            'coherence': 0.5,
            'lambda': 1.0
        }
        
        result = analyze_temporal_coherence(request.text, scores)
        
        return {
            "success": True,
            "timestamp": result.current_snapshot.timestamp.isoformat(),
            "consistency_score": result.consistency_score,
            "drift_magnitude": result.drift_magnitude,
            "drift_direction": result.drift_direction,
            "evolution_trajectory": result.evolution_trajectory,
            "stability_index": result.stability_index,
            "anomalous_changes": result.anomalous_changes,
            "predictions": result.predictions,
            "recommendations": result.recommendations
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Temporal analysis failed: {str(e)}")

@app.post("/report/generate")
async def generate_report(request: ReportRequest):
    """Generate formatted report from analysis"""
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    # Get cached result
    if request.analysis_id not in analysis_cache:
        raise HTTPException(status_code=404, detail="Analysis ID not found")
    
    result = analysis_cache[request.analysis_id]
    
    try:
        if request.format == "markdown":
            report = generate_markdown_report(result)
            return {"success": True, "format": "markdown", "report": report}
        
        elif request.format == "html":
            report = generate_html_report(result)
            return HTMLResponse(content=report)
        
        elif request.format == "json":
            report = export_analysis_json(result)
            return JSONResponse(content={"success": True, "format": "json", "report": report})
        
        elif request.format == "summary":
            report = generate_summary_report(result)
            return {"success": True, "format": "summary", "report": report}
        
        else:
            raise HTTPException(status_code=400, detail="Invalid format. Use: markdown, html, json, or summary")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {str(e)}")

@app.get("/stats")
async def get_statistics(engine: Optional[str] = None):
    """Get engine statistics"""
    
    if not ENGINES_AVAILABLE:
        raise HTTPException(status_code=503, detail="Enhanced engines not available")
    
    try:
        if engine == "orchestrator" or engine is None:
            stats = get_orchestrator_statistics()
            return StatsResponse(success=True, engine="orchestrator", statistics=stats)
        
        elif engine == "discernment":
            stats = get_discernment_statistics()
            return StatsResponse(success=True, engine="discernment", statistics=stats)
        
        elif engine == "pattern":
            stats = get_pattern_statistics()
            return StatsResponse(success=True, engine="pattern", statistics=stats)
        
        elif engine == "temporal":
            stats = get_temporal_statistics()
            return StatsResponse(success=True, engine="temporal", statistics=stats)
        
        else:
            raise HTTPException(status_code=400, detail="Invalid engine. Use: orchestrator, discernment, pattern, or temporal")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Statistics retrieval failed: {str(e)}")

@app.get("/analysis/{analysis_id}")
async def get_analysis(analysis_id: str):
    """Retrieve cached analysis by ID"""
    
    if analysis_id not in analysis_cache:
        raise HTTPException(status_code=404, detail="Analysis ID not found")
    
    result = analysis_cache[analysis_id]
    
    return {
        "success": True,
        "analysis_id": result.analysis_id,
        "timestamp": result.timestamp,
        "overall_status": result.overall_status,
        "risk_level": result.risk_level,
        "unified_scores": result.unified_scores
    }

# ============================================================================
# Server Startup
# ============================================================================

def start_server(host: str = "0.0.0.0", port: int = 8000):
    """Start the API server"""
    print("=" * 70)
    print("ALETHEIA ENGINE API SERVER v2.0")
    print("=" * 70)
    print(f"Enhanced Engines Available: {ENGINES_AVAILABLE}")
    print(f"Legacy Engines Available: {LEGACY_AVAILABLE}")
    print(f"Starting server on {host}:{port}")
    print("=" * 70)
    print()
    
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_server()
