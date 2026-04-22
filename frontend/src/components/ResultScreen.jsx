// src/components/ResultScreen.jsx
import ResultCard from "./ResultCard"

export default function ResultScreen({ result, onNewAnalysis }) {

  if (!result) return null

  return (
    <div className="result-screen-container">
      <header className="result-header">
        <h1>Diagnóstico Concluído</h1>
        <p>Confira abaixo o resultado da análise da sua planta.</p>
      </header>

      {}
      <ResultCard result={result} />

      {}
      <div className="result-actions">
        <button 
          className="btn-new-analysis" 
          onClick={onNewAnalysis}
        >
          🔄 Fazer Nova Análise
        </button>
      </div>
    </div>
  )
}