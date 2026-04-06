import React, { useState } from 'react';
import WasteSubmissionForm from './components/WasteSubmissionForm';
import ResultsDashboard from './components/ResultsDashboard';

function App() {
  const [showResults, setShowResults] = useState(false);

  // This function simulates the AI processing time when you click submit
  const handleSimulatedSubmit = () => {
    setShowResults(true);
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#121212', padding: '2rem' }}>
      <header style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{ color: '#fff', fontSize: '2.5rem', margin: '0' }}>Agentic Edge AI</h1>
        <p style={{ color: '#4ADE80', marginTop: '10px' }}>EcoRoute: Industrial Waste Intelligence</p>
      </header>
      
      <main style={{ display: 'flex', flexWrap: 'wrap', gap: '2rem', justifyContent: 'center', alignItems: 'flex-start' }}>
        {/* We pass the handleSimulatedSubmit down to the form so we can trigger the dashboard */}
        <div style={{ flex: '1 1 400px', maxWidth: '500px' }} onClick={handleSimulatedSubmit}>
           <WasteSubmissionForm />
        </div>
        
        {/* The dashboard only shows up after the user clicks Submit */}
        {showResults && (
          <div style={{ flex: '1 1 400px', maxWidth: '600px', animation: 'fadeIn 0.5s ease-in' }}>
            <ResultsDashboard />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;