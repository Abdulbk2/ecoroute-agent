import React from 'react';
import WasteSubmissionForm from './components/WasteSubmissionForm';

function App() {
  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#121212', padding: '2rem' }}>
      <header style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{ color: '#fff', fontSize: '2.5rem', margin: '0' }}>Agentic Edge AI</h1>
        <p style={{ color: '#4ADE80', marginTop: '10px' }}>B2B Logistics & Sustainability Agent</p>
      </header>
      
      <main>
        <WasteSubmissionForm />
      </main>
    </div>
  );
}

export default App;