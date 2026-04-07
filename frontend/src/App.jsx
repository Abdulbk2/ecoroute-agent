import React, { useState } from 'react';
import WasteSubmissionForm from './components/WasteSubmissionForm';
import ResultsDashboard from './components/ResultsDashboard';

function App() {
  const [showResults, setShowResults] = useState(false);
  const [apiResult, setApiResult] = useState(null);

  // This function catches the real JSON data from your Python backend!
  const handleBackendSuccess = (data) => {
    console.log("Data received in App.jsx:", data);
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
           {/* Pass the success function down to the form */}
           <WasteSubmissionForm onProcessComplete={handleBackendSuccess} />
        </div>
        
        {/* Only show the dashboard if we have results, and pass the Python data into it */}
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