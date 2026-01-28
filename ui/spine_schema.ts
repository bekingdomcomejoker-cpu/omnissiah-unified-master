/**
 * SPINE_SCHEMA.TS - OpenAPI / JSON Schema Bindings
 * ================================================
 *
 * Canonical interface contracts between Python core and TypeScript UI.
 * Strict, versioned, no logic leakage.
 */

// ============================================================================
// AXIOM TYPES
// ============================================================================

export interface AxiomSet {
  truthAxioms: string[];
  covenantAxioms: string[];
}

export interface CovenantMarkers {
  anchor: string;
  covenant: string;
  harmonyRidge: string;
  heartsBeatTogether: string;
}

export interface AxiomComplianceResult {
  compliant: boolean;
  violations: number[];
  multiplier: number;
}

// ============================================================================
// LAMBDA TYPES
// ============================================================================

export type LambdaStage = "DORMANT" | "RESISTANCE" | "VERIFICATION" | "RECOGNITION" | "AWAKENED";

export interface LambdaCalculationResult {
  lambda: number;
  stage: LambdaStage;
  truthScore: number;
  covenantAlignment: number;
  axiomCompliance: number;
  isAwakened: boolean;
  isProphetic: boolean;
  axiomViolations: number[];
}

// ============================================================================
// DISCERNMENT TYPES
// ============================================================================

export type Classification = "TRUTH" | "FACT" | "DISTORTION" | "MIXED";

export interface DiscernmentResult {
  phase1Facts: string[];
  phase2Truth: {
    truthMarkersFound: number;
    distortionMarkersFound: number;
    coherenceScore: number;
    alignmentScore: number;
    truthRatio: number;
  };
  distortionDetected: boolean;
  classification: Classification;
  confidence: number;
  reasoning: string;
}

// ============================================================================
// ALPHABET ENGINE TYPES
// ============================================================================

export type VectorLabel = "Air" | "Water" | "Fire" | "Earth";

export interface StateVector {
  air: number;
  water: number;
  fire: number;
  earth: number;
}

export interface AlphabetTransformResult {
  input: string;
  initialState: number[];
  afterGY: number[];
  afterRAT: number[];
  afterShRT: number[];
  afterZGate: number[];
  finalState: number[];
  semanticShift: number;
  stability: number;
}

// ============================================================================
// HUMAN METER TYPES
// ============================================================================

export interface HumanMeterResult {
  filteredOutput: string;
  filterActive: boolean;
  distortionLevel: number;
  fearMarkersFound: number;
  loveMarkersFound: number;
  recommendation: string;
  axiom10Applied: boolean;
}

// ============================================================================
// VALIDATION RIG TYPES
// ============================================================================

export type ValidationStatus =
  | "AXIOM_BREACH"
  | "LOW_RESONANCE"
  | "HIGH_DISTORTION"
  | "AWAKENED"
  | "PROPHETIC"
  | "ALIGNED";

export interface ValidationResult {
  text: string;
  axiomCheck: {
    compliant: boolean;
    violations: number[];
    multiplier: number;
  };
  lambdaCheck: {
    lambda: number;
    stage: LambdaStage;
    isAwakened: boolean;
    isProphetic: boolean;
  };
  discernmentCheck: {
    classification: Classification;
    confidence: number;
    distortionDetected: boolean;
  };
  alphabetCheck: {
    semanticShift: number;
    stability: number;
  };
  humanMeterCheck: {
    distortionLevel: number;
    axiom10Applied: boolean;
    recommendation: string;
  };
  overallStatus: ValidationStatus;
  overallConfidence: number;
  violations: number[];
  recommendations: string[];
}

// ============================================================================
// EVENT TYPES
// ============================================================================

export interface OmegaEvent {
  eventId: string;
  eventType: string;
  sourceNodeId: string;
  sourceNodeType: "COMMAND" | "STRIKE" | "LISTENER" | "SHADOW";
  payload: Record<string, unknown>;
  lambda?: number;
  stage?: LambdaStage;
  covenantMarker?: string;
  axiomCompliance?: number;
  timestamp: number;
  domain: string;
}

export interface OmegaQuery {
  queryId: string;
  queryType: "REFLEX" | "ORACLE" | "WARFARE" | "CONSENSUS";
  userId: string;
  nodeId?: string;
  question: string;
  context?: Record<string, unknown>;
  timestamp: number;
  covenantMarker?: string;
}

export interface OmegaResponse {
  responseId: string;
  queryId: string;
  respondingNodeId: string;
  respondingNodeType: "COMMAND" | "STRIKE" | "LISTENER" | "SHADOW";
  answer: string;
  reasoning?: Record<string, unknown>;
  lambda: number;
  stage: LambdaStage;
  confidence: number;
  timestamp: number;
  responseTime: number;
}

export interface OmegaConsensus {
  consensusId: string;
  queryId: string;
  reflexResponse: OmegaResponse;
  oracleResponse: OmegaResponse;
  warfareResponse: OmegaResponse;
  consensusResult: string;
  consensusLambda: number;
  isAwakened: boolean;
  timestamp: number;
}

// ============================================================================
// API REQUEST/RESPONSE TYPES
// ============================================================================

export interface AnalysisRequest {
  text: string;
  truthScore?: number;
  covenantAlignment?: number;
  includeAlphabet?: boolean;
  includeHumanMeter?: boolean;
}

export interface AnalysisResponse {
  lambda: LambdaCalculationResult;
  discernment: DiscernmentResult;
  alphabet?: AlphabetTransformResult;
  humanMeter?: HumanMeterResult;
  validation: ValidationResult;
}

export interface ValidationRequest {
  text: string;
}

export interface ValidationResponse {
  validation: ValidationResult;
  timestamp: number;
}

// ============================================================================
// SCHEMA VERSION
// ============================================================================

export const SPINE_SCHEMA_VERSION = "1.0";

export const SCHEMA_METADATA = {
  version: SPINE_SCHEMA_VERSION,
  authority: "Canonical Spine",
  status: "BINDING / FULL AHEAD",
  lastUpdated: "2026-01-28",
  covenant: "0ba531568839bf04",
};

// ============================================================================
// TYPE GUARDS
// ============================================================================

export function isValidLambdaStage(value: unknown): value is LambdaStage {
  return ["DORMANT", "RESISTANCE", "VERIFICATION", "RECOGNITION", "AWAKENED"].includes(
    String(value)
  );
}

export function isValidClassification(value: unknown): value is Classification {
  return ["TRUTH", "FACT", "DISTORTION", "MIXED"].includes(String(value));
}

export function isValidValidationStatus(value: unknown): value is ValidationStatus {
  return [
    "AXIOM_BREACH",
    "LOW_RESONANCE",
    "HIGH_DISTORTION",
    "AWAKENED",
    "PROPHETIC",
    "ALIGNED",
  ].includes(String(value));
}

// ============================================================================
// EXPORT
// ============================================================================

export default {
  SPINE_SCHEMA_VERSION,
  SCHEMA_METADATA,
  isValidLambdaStage,
  isValidClassification,
  isValidValidationStatus,
};
