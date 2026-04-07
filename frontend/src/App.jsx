import React, { useState } from 'react';
import WasteSubmissionForm from './components/WasteSubmissionForm';
import ResultsDashboard from './components/ResultsDashboard';

function App() {
  const [showResults, setShowResults] = useState(false);
  const [apiResult, setApiResult] = useState(null);

  const handleBackendSuccess = (data) => {
    setApiResult(data);
    setShowResults(true);
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#121212', padding: '2rem' }}>
      <header style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{ color: '#fff', fontSize: '2.5rem', margin: '0' }}>Agentic Edge AI</h1>
        <p style={{ color: '#4ADE80', marginTop: '10px' }}>EcoRoute: Industrial Waste Intelligence</p>
      </header>
      
      <main style={{ display: 'flex', flexWrap: 'wrap', gap: '2rem', justifyContent: 'center', alignItems: 'flex-start' }}>
        <div style={{ flex: '1 1 400px', maxWidth: '500px' }}>
           <WasteSubmissionForm onProcessComplete={handleBackendSuccess} />
        </div>
        {showResults && (
          <div style={{ flex: '1 1 400px', maxWidth: '600px', animation: 'fadeIn 0.5s ease-in' }}>
            <ResultsDashboard result={apiResult} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
