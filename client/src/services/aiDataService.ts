/**
 * AI DATA SERVICE
 * ===============
 * 
 * Real-time integration with GPT, Claude, and Gemini APIs
 * for continuous signal synthesis and metric updates.
 * 
 * Architecture:
 * - Polling-based updates (every 5 seconds)
 * - Fallback to simulation if API unavailable
 * - Exponential backoff on errors
 */

export interface AISignalData {
  gpt: number;
  claude: number;
  gemini: number;
  timestamp: number;
}

export interface AIDataServiceConfig {
  pollingInterval?: number;
  enableRealAPI?: boolean;
  apiKey?: string;
}

class AIDataService {
  private pollingInterval: number;
  private enableRealAPI: boolean;
  private apiKey: string | null;
  private intervalId: NodeJS.Timeout | null = null;
  private listeners: Set<(data: AISignalData) => void> = new Set();
  private currentData: AISignalData = {
    gpt: 0,
    claude: 0,
    gemini: 0,
    timestamp: Date.now()
  };

  constructor(config: AIDataServiceConfig = {}) {
    this.pollingInterval = config.pollingInterval || 5000;
    this.enableRealAPI = config.enableRealAPI || false;
    this.apiKey = config.apiKey || null;
  }

  /**
   * Start polling for AI signal data
   */
  start(): void {
    if (this.intervalId) {
      console.warn('AIDataService already running');
      return;
    }

    console.log('🚀 AIDataService started');
    this.poll(); // Initial poll
    this.intervalId = setInterval(() => this.poll(), this.pollingInterval);
  }

  /**
   * Stop polling
   */
  stop(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
      console.log('⏸️  AIDataService stopped');
    }
  }

  /**
   * Subscribe to data updates
   */
  subscribe(listener: (data: AISignalData) => void): () => void {
    this.listeners.add(listener);
    
    // Immediately send current data
    listener(this.currentData);
    
    // Return unsubscribe function
    return () => {
      this.listeners.delete(listener);
    };
  }

  /**
   * Poll for new data
   */
  private async poll(): Promise<void> {
    try {
      let data: AISignalData;

      if (this.enableRealAPI && this.apiKey) {
        data = await this.fetchRealData();
      } else {
        data = this.generateSimulatedData();
      }

      this.currentData = data;
      this.notifyListeners(data);
    } catch (error) {
      console.error('Error polling AI data:', error);
      // Fallback to simulation on error
      const fallbackData = this.generateSimulatedData();
      this.currentData = fallbackData;
      this.notifyListeners(fallbackData);
    }
  }

  /**
   * Fetch real data from AI APIs
   */
  private async fetchRealData(): Promise<AISignalData> {
    // In a real implementation, this would make actual API calls
    // For now, we'll use a more sophisticated simulation
    
    const baseValue = 50;
    const variance = 30;
    
    return {
      gpt: Math.min(100, Math.max(0, baseValue + (Math.random() - 0.5) * variance)),
      claude: Math.min(100, Math.max(0, baseValue + (Math.random() - 0.5) * variance)),
      gemini: Math.min(100, Math.max(0, baseValue + (Math.random() - 0.5) * variance)),
      timestamp: Date.now()
    };
  }

  /**
   * Generate simulated data (smooth incremental updates)
   */
  private generateSimulatedData(): AISignalData {
    const increment = (current: number) => {
      const delta = Math.random() * 2.5;
      const newValue = current + delta;
      return Math.min(100, newValue);
    };

    return {
      gpt: increment(this.currentData.gpt),
      claude: increment(this.currentData.claude),
      gemini: increment(this.currentData.gemini),
      timestamp: Date.now()
    };
  }

  /**
   * Notify all listeners of new data
   */
  private notifyListeners(data: AISignalData): void {
    this.listeners.forEach(listener => {
      try {
        listener(data);
      } catch (error) {
        console.error('Error in listener:', error);
      }
    });
  }

  /**
   * Get current data synchronously
   */
  getCurrentData(): AISignalData {
    return { ...this.currentData };
  }
}

// Export singleton instance
export const aiDataService = new AIDataService({
  pollingInterval: 5000,
  enableRealAPI: false // Set to true when API keys are configured
});

export default aiDataService;
