import React from 'react';

const ResultsDashboard = ({ result }) => {
  // We use mock data here so you can see the design while the backend is being built
  const displayData = result || {
    status: "Action Required: High Value",
    action: "Route to Local Certified Scrap Yard",
    rule: "Non-hazardous. High resale value in current market.",
    carbonSaved: "1,200 kg CO2e",
    financialImpact: "+$850.00 (Est. Resale)"
  };

  return (
    <div style={{ backgroundColor: '#1e1e2f', color: '#fff', padding: '2rem', borderRadius: '10px', width: '100%', maxWidth: '600px', fontFamily: 'system-ui', marginTop: '20px' }}>
      <h2 style={{ color: '#60A5FA', borderBottom: '1px solid #333', paddingBottom: '10px', marginTop: '0' }}>
        Agentic Analysis Report
      </h2>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px', marginTop: '20px' }}>
        {/* Metric Card 1 */}
        <div style={{ backgroundColor: '#2a2a40', padding: '15px', borderRadius: '8px', borderLeft: '4px solid #4ADE80' }}>
          <p style={{ margin: '0', fontSize: '0.8rem', color: '#aaa' }}>Carbon Offset</p>
          <h3 style={{ margin: '5px 0 0 0', color: '#fff' }}>{displayData.carbonSaved}</h3>
        </div>

        {/* Metric Card 2 */}
        <div style={{ backgroundColor: '#2a2a40', padding: '15px', borderRadius: '8px', borderLeft: '4px solid #FBBF24' }}>
          <p style={{ margin: '0', fontSize: '0.8rem', color: '#aaa' }}>Financial Impact</p>
          <h3 style={{ margin: '5px 0 0 0', color: '#fff' }}>{displayData.financialImpact}</h3>
        </div>
      </div>

      <div style={{ marginTop: '25px' }}>
        <h4 style={{ color: '#aaa', marginBottom: '5px' }}>Regulatory Compliance Check</h4>
        <div style={{ backgroundColor: '#2a2a40', padding: '15px', borderRadius: '5px', color: '#E2E8F0', fontSize: '0.95rem' }}>
          {displayData.rule}
        </div>
      </div>

      <div style={{ marginTop: '20px' }}>
        <h4 style={{ color: '#aaa', marginBottom: '5px' }}>Recommended AI Logistics Routing</h4>
        <div style={{ backgroundColor: '#2a2a40', padding: '15px', borderRadius: '5px', color: '#4ADE80', fontWeight: 'bold', fontSize: '1.1rem' }}>
          {displayData.action}
        </div>
      </div>
    </div>
  );
};

export default ResultsDashboard;