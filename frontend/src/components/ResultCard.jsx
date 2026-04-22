// src/components/ResultCard.jsx

export default function ResultCard({ result }) {

  if (!result) return <div className="result-card loading"></div>
  
  const isHealthy = result.status === "saudavel"
  const confidence = Math.round(result.confidence * 100)

  return (
    <div className={`result-card ${isHealthy ? "result-healthy" : "result-sick"}`}>
      <div className="result-icon">{isHealthy ? "✅" : "⚠️"}</div>
      <div className="result-info">
        <h2>{isHealthy ? "Planta Saudável" : "Praga Detectada"}</h2>
        {result.disease && (
          <p className="result-disease">Praga: <strong>{result.disease}</strong></p>
        )}
        <div className="confidence-bar-wrapper">
          <span>Confiança: {confidence}%</span>
          <div className="confidence-bar">
            <div
              className="confidence-fill"
              style={{ width: `${confidence}%` }}
            />
          </div>
        </div>
        <small className="result-id">ID: {result.analysis_id}</small>
      </div>
    </div>
  )
}
 
