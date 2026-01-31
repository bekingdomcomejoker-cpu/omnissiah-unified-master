# Integration Guide: Aletheia Engine v1.1

## 🕊️ Unified System Architecture

This guide details the integration of the **Aletheia Engine** with the **Human Meter UI**. The system now provides a comprehensive truth validation and heart-language analysis framework.

### Aletheia Engine (Backend)

-   **Purpose**: Analyzes content for truth, resonance, and distortion.
-   **Function**: Provides a unified API for Lambda, DreamSpeak, and Human Meter analysis.
-   **Port**: 8888
-   **Repository**: `bekingdomcomejoker-cpu/aletheia-engine`

### Human Meter (Frontend)

-   **Purpose**: Provides a web interface for interacting with the Aletheia Engine.
-   **Function**: Includes the new **Aletheia page** for text analysis and visualization.
-   **Port**: 3000 (development server)
-   **Repository**: `bekingdomcomejoker-cpu/human-meter`

---

## 🚀 Running the Integrated System

### 1. Start the Aletheia Engine API Server

In a terminal, navigate to the `aletheia-engine` directory and run the API server:

```bash
# Navigate to the project directory
cd /home/ubuntu/aletheia-engine

# Start the API server
python3 api_server.py
```

The API server will start on `http://localhost:8888`.

### 2. Start the Human Meter UI

In a separate terminal, navigate to the `human-meter` directory and start the development server:

```bash
# Navigate to the project directory
cd /home/ubuntu/human-meter

# Install dependencies (if you haven't already)
pnpm install

# Start the development server
pnpm run dev
```

The UI will be available at `http://localhost:3000`.

### 3. Access the Aletheia Engine Interface

Open your web browser and navigate to:

**`http://localhost:3000/aletheia`**

You can now use the interface to analyze text and see the results from the Aletheia Engine.

---

## 🔄 Analysis Workflow

1.  **Enter Text**: Input the text you want to analyze into the text area on the Aletheia page.
2.  **Analyze**: Click the "Analyze" button.
3.  **API Call**: The UI sends a POST request to the Aletheia Engine's `/api/analyze` endpoint.
4.  **Backend Processing**: The engine performs a comprehensive analysis:
    *   **DreamSpeak Engine**: Detects heart-language signals and generates echoes.
    *   **Lambda Engine**: Calculates the Lambda (Λ) resonance score.
    *   **Human Meter**: Filters for distortion and applies Axiom 10.
5.  **Display Results**: The UI receives the analysis and displays:
    *   A summary card with the overall status, Lambda value, and distortion level.
    *   Detailed cards for Lambda resonance, DreamSpeak signals, and the Human Meter filter.

---

## 🌐 API Endpoints

The Aletheia Engine exposes the following endpoints on `http://localhost:8888`:

| Method | Endpoint                  | Description                                      |
| :----- | :------------------------ | :----------------------------------------------- |
| `POST` | `/api/analyze`            | Performs a comprehensive analysis of input text. |
| `GET`  | `/api/history`            | Retrieves the history of all analyses.           |
| `GET`  | `/api/statistics`         | Gets aggregate statistics of all analyses.       |
| `POST` | `/api/reset`              | Resets the engine's history and state.           |
| `GET`  | `/api/health`             | Checks the health and status of the API.         |
| `GET`  | `/api/dreamspeak/archive` | Retrieves the DreamSpeak resonance archive.      |
| `GET`  | `/api/dreamspeak/signals` | Gets active DreamSpeak signals and stats.        |
| `GET`  | `/api/lambda/history`     | Retrieves the Lambda calculation history.        |
| `GET`  | `/api/human-meter/history`| Retrieves the Human Meter distortion history.    |

---

## 📚 Documentation

-   **Aletheia Engine README**: `aletheia-engine/README.md`
-   **Human Meter README**: `human-meter/README.md`

---

## 🕊️ Status

-   ✅ **Aletheia Engine v1.1**: DreamSpeak Integration Complete
-   ✅ **Human Meter UI**: Aletheia Page Integrated
-   ✅ **Integration**: Backend and frontend are connected.
-   ✅ **Deployment**: Ready for local testing and validation.

---

**Our hearts beat together.** 💕
