import axios from "axios";
import { useState } from "react";

interface PredictionResponse {
  prediction: string;
  confidence: number;
  is_fake: boolean;
}

export default function Page() {
  const [text, setText] = useState<string>("");
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  async function handleAnalyze(e: React.FormEvent) {
    e.preventDefault();

    if (!text.trim()) {
      setError("Please send a valid text.");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post<PredictionResponse>(
        "http://127.0.0.1:8000/predict",
        { text },
      );
      console.log(response.data);
      setResult(response.data);
    } catch (err: any) {
      if (err.response) {
        console.log(err.response.data);
        console.log(err.response.status);
        setError("Server error occurred.");
      } else {
        console.log(err.message);
        setError("Cannot connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
  <div className="min-h-screen bg-black text-white flex items-center justify-center px-6">
    <div className="w-full max-w-2xl space-y-14">

      {/* Header */}
      <div className="text-center space-y-6">
        <h1 className="text-2xl md:text-4xl font-bold tracking-[0.15em] whitespace-nowrap">
          THE ACTUAL FOURTH PILLAR
        </h1>

        <div className="h-px bg-red-700/40 w-40 mx-auto"></div>

        <div className="text-center space-y-1">
          <p className="text-gray-500 text-xs tracking-[0.25em] uppercase">
            Intelligence Verification Console*️
          </p>

          <p className="text-gray-600 text-[11px] leading-snug">
            Model evaluates linguistic patterns and structure, not factual truth.
          </p>
        </div>
      </div>

      {/* Input Section */}
      <div className="bg-zinc-900 border border-red-700/30 rounded-2xl shadow-xl shadow-red-900/10 p-8 space-y-6">
        <form onSubmit={handleAnalyze} className="space-y-6">

          <div className="space-y-3">
            <label className="text-xs tracking-[0.2em] text-gray-500 uppercase">
              Input Transmission
            </label>

            <textarea
              value={text}
              onChange={(e) => setText(e.target.value)}
              rows={8}
              placeholder="Paste news article content here..."
              className="w-full bg-black border border-zinc-800 rounded-xl p-5 text-gray-200 placeholder-gray-600 focus:outline-none focus:border-red-600 focus:ring-1 focus:ring-red-600 transition resize-none"
            />

            <div className="flex justify-between text-xs text-gray-600">
              <span>Character Count</span>
              <span>{text.length}</span>
            </div>
          </div>

          {error && (
            <div className="text-red-500 text-sm border border-red-800/40 bg-red-950/30 p-3 rounded-lg">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-red-700 hover:bg-red-800 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed transition rounded-xl py-3 font-semibold tracking-widest"
          >
            {loading ? "ANALYZING…" : "INITIATE ANALYSIS"}
          </button>

        </form>
      </div>

      {/* Result Section */}
      {result && (
        <div className="bg-zinc-900 border border-red-700/30 rounded-2xl shadow-xl shadow-red-900/10 p-8 space-y-8 transition-all">

          <div className="flex items-center justify-between">
            <span className="text-xs tracking-[0.2em] text-gray-500 uppercase">
              Classification Result
            </span>

            <span
              className={`text-2xl font-bold tracking-wider ${
                result.is_fake ? "text-red-500" : "text-green-400"
              }`}
            >
              {result.prediction.toUpperCase()}
            </span>
          </div>

          <div className="space-y-4">

            <div className="flex justify-between text-sm text-gray-400">
              <span>Confidence Index</span>
              <span className="font-semibold text-white">
                {result.confidence.toFixed(2)}%
              </span>
            </div>

            <div className="w-full bg-zinc-800 rounded-full h-3 overflow-hidden">
              <div
                className={`h-3 transition-all duration-700 ${
                  result.is_fake ? "bg-red-500" : "bg-green-400"
                }`}
                style={{ width: `${result.confidence}%` }}
              />
            </div>

            {result.confidence < 55 && (
              <div className="text-yellow-500 text-sm pt-3 border-t border-yellow-700/30">
                Low confidence. Model uncertain. Treat result cautiously.
              </div>
            )}

            {result.confidence >= 55 && result.confidence < 75 && (
              <div className="text-orange-400 text-sm pt-3 border-t border-orange-700/30">
                Moderate confidence. Pattern-based classification.
              </div>
            )}

            {result.confidence >= 75 && (
              <div className="text-green-400 text-sm pt-3 border-t border-green-700/30">
                High stylistic confidence detected.
              </div>
            )}

          </div>
        </div>
      )}

    </div>
  </div>
);
}
