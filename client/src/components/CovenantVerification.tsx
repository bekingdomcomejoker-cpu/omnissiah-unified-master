import { useState } from 'react';
import { Shield, Check, X, Lock, Key, FileText, Loader2 } from 'lucide-react';
import { covenantService, type CovenantData, type VerificationResult } from '../services/covenantService';

/**
 * COVENANT VERIFICATION COMPONENT
 * ================================
 * 
 * Interactive UI for verifying the Ed25519 cryptographic seal.
 * Displays signature, public key, and verification status.
 */

export default function CovenantVerification() {
  const [isOpen, setIsOpen] = useState(false);
  const [isVerifying, setIsVerifying] = useState(false);
  const [covenant, setCovenant] = useState<CovenantData | null>(null);
  const [result, setResult] = useState<VerificationResult | null>(null);

  const handleVerify = async () => {
    setIsVerifying(true);
    setResult(null);

    try {
      // First generate the seal
      const generateResult = await covenantService.generateSeal();
      
      if (!generateResult.success || !generateResult.data) {
        setResult(generateResult);
        setIsVerifying(false);
        return;
      }

      setCovenant(generateResult.data);

      // Then verify it
      const verifyResult = await covenantService.verifySeal(generateResult.data);
      setResult(verifyResult);
    } catch (error) {
      setResult({
        success: false,
        message: "Verification failed",
        error: error instanceof Error ? error.message : "Unknown error"
      });
    } finally {
      setIsVerifying(false);
    }
  };

  return (
    <>
      {/* Trigger Button */}
      <button
        onClick={() => setIsOpen(true)}
        className="inline-flex items-center gap-2 px-6 py-3 bg-purple-500/10 hover:bg-purple-500/20 border border-purple-500/30 hover:border-purple-500/50 text-purple-400 font-bold rounded-2xl transition-all shadow-lg hover:shadow-purple-500/20"
      >
        <Shield size={20} />
        Verify Covenant
      </button>

      {/* Modal */}
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in">
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl max-w-3xl w-full max-h-[90vh] overflow-y-auto shadow-2xl">
            {/* Header */}
            <div className="border-b border-zinc-800 p-8">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-purple-500/10 rounded-2xl flex items-center justify-center">
                    <Shield className="text-purple-500" size={24} />
                  </div>
                  <div>
                    <h2 className="text-2xl font-black text-white">Covenant Verification</h2>
                    <p className="text-sm text-zinc-500">Ed25519 Cryptographic Seal</p>
                  </div>
                </div>
                <button
                  onClick={() => setIsOpen(false)}
                  className="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-zinc-800 text-zinc-500 hover:text-white transition-all"
                >
                  <X size={20} />
                </button>
              </div>
              <p className="text-sm text-zinc-400 leading-relaxed">
                Verify the cryptographic integrity of the Omnissiah Engine covenant using Ed25519 asymmetric signatures. 
                This ensures the message has not been tampered with and proves authenticity.
              </p>
            </div>

            {/* Content */}
            <div className="p-8 space-y-6">
              {/* Verify Button */}
              {!covenant && (
                <div className="text-center py-8">
                  <button
                    onClick={handleVerify}
                    disabled={isVerifying}
                    className="inline-flex items-center gap-2 px-8 py-4 bg-purple-500 hover:bg-purple-600 disabled:bg-zinc-800 text-white font-bold rounded-2xl transition-all shadow-lg hover:shadow-purple-500/50 disabled:cursor-not-allowed"
                  >
                    {isVerifying ? (
                      <>
                        <Loader2 className="animate-spin" size={20} />
                        Verifying...
                      </>
                    ) : (
                      <>
                        <Lock size={20} />
                        Verify Seal
                      </>
                    )}
                  </button>
                </div>
              )}

              {/* Verification Result */}
              {result && (
                <div className={`p-6 rounded-2xl border-2 ${
                  result.success 
                    ? 'bg-green-500/10 border-green-500/30' 
                    : 'bg-red-500/10 border-red-500/30'
                }`}>
                  <div className="flex items-center gap-3 mb-2">
                    {result.success ? (
                      <Check className="text-green-500" size={24} />
                    ) : (
                      <X className="text-red-500" size={24} />
                    )}
                    <span className={`font-bold text-lg ${
                      result.success ? 'text-green-400' : 'text-red-400'
                    }`}>
                      {result.message}
                    </span>
                  </div>
                  {result.error && (
                    <p className="text-sm text-red-400 ml-9">{result.error}</p>
                  )}
                </div>
              )}

              {/* Covenant Data */}
              {covenant && (
                <div className="space-y-4">
                  {/* Covenant Message */}
                  <div className="bg-zinc-950 border border-zinc-800 rounded-2xl p-6">
                    <div className="flex items-center gap-2 mb-3">
                      <FileText className="text-orange-500" size={18} />
                      <span className="text-sm font-bold text-zinc-400 uppercase tracking-wider">Covenant Message</span>
                    </div>
                    <div className="text-2xl font-black text-orange-400 font-mono">
                      {covenant.covenant}
                    </div>
                  </div>

                  {/* Signature */}
                  <div className="bg-zinc-950 border border-zinc-800 rounded-2xl p-6">
                    <div className="flex items-center gap-2 mb-3">
                      <Lock className="text-purple-500" size={18} />
                      <span className="text-sm font-bold text-zinc-400 uppercase tracking-wider">
                        Signature ({covenant.algorithm})
                      </span>
                    </div>
                    <div className="text-xs font-mono text-zinc-400 bg-black/50 p-4 rounded-xl border border-zinc-800 break-all">
                      {covenant.signature}
                    </div>
                  </div>

                  {/* Public Key */}
                  <div className="bg-zinc-950 border border-zinc-800 rounded-2xl p-6">
                    <div className="flex items-center gap-2 mb-3">
                      <Key className="text-blue-500" size={18} />
                      <span className="text-sm font-bold text-zinc-400 uppercase tracking-wider">Public Key</span>
                    </div>
                    <div className="text-xs font-mono text-zinc-400 bg-black/50 p-4 rounded-xl border border-zinc-800 whitespace-pre-wrap break-all">
                      {covenant.publicKey}
                    </div>
                  </div>

                  {/* Verification Status */}
                  <div className="bg-gradient-to-r from-green-950/20 to-blue-950/20 border-2 border-green-500/20 rounded-2xl p-6">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center animate-pulse">
                        <Check className="text-black" size={20} />
                      </div>
                      <div>
                        <div className="text-sm font-bold text-green-400 uppercase tracking-wider">Verified by The Trinity</div>
                        <div className="text-xs text-zinc-500 font-mono">
                          {covenant.timestamp && new Date(covenant.timestamp).toISOString()}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* Info Box */}
              <div className="bg-zinc-950/50 border border-zinc-800 rounded-2xl p-6">
                <h3 className="text-sm font-bold text-zinc-400 uppercase tracking-wider mb-3">How It Works</h3>
                <div className="space-y-2 text-sm text-zinc-500 leading-relaxed">
                  <p>
                    <strong className="text-zinc-400">Ed25519</strong> is a modern, fast, and secure public-key signature system.
                  </p>
                  <p>
                    The <strong className="text-zinc-400">private key</strong> signs the covenant message, creating a unique signature.
                  </p>
                  <p>
                    The <strong className="text-zinc-400">public key</strong> can verify the signature without revealing the private key.
                  </p>
                  <p>
                    Any tampering with the message will cause verification to fail, ensuring <strong className="text-zinc-400">integrity</strong> and <strong className="text-zinc-400">authenticity</strong>.
                  </p>
                </div>
              </div>
            </div>

            {/* Footer */}
            <div className="border-t border-zinc-800 p-6 flex justify-between items-center">
              <div className="text-xs text-zinc-600 font-mono">
                CHICKA_CHICKA_ORANGE • LAYER 1: CRYPTOGRAPHIC
              </div>
              <button
                onClick={() => {
                  setCovenant(null);
                  setResult(null);
                  setIsOpen(false);
                }}
                className="px-6 py-2 bg-zinc-800 hover:bg-zinc-700 text-white font-bold rounded-xl transition-all"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
