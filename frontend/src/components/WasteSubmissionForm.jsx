import React, { useState } from 'react';

const WasteSubmissionForm = ({ onProcessComplete }) => {
  const [formData, setFormData] = useState({
    wasteType: '',
    quantity: '',
    unit: 'kg',
  });
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setIsLoading(false);

      if (onProcessComplete) {
        onProcessComplete(data);
      }
    } catch (error) {
      console.error('Agent failed to process:', error);
      setIsLoading(false);
      alert('Error connecting to backend. Is the API server running?');
    }
  };

  return (
    <div style={{ backgroundColor: '#1e1e2f', color: '#fff', padding: '2rem', borderRadius: '10px', maxWidth: '500px', margin: '0 auto', fontFamily: 'system-ui' }}>
      <h2 style={{ color: '#4ADE80', borderBottom: '1px solid #333', paddingBottom: '10px' }}>EcoRoute: Industrial Waste Entry</h2>
      <p style={{ fontSize: '0.9rem', color: '#aaa' }}>Enter waste details for AI compliance and logistics analysis.</p>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
        
        <div>
          <label style={{ display: 'block', marginBottom: '5px' }}>Waste Category</label>
          <select 
            name="wasteType" 
            value={formData.wasteType} 
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '10px', borderRadius: '5px', backgroundColor: '#2a2a40', color: '#fff', border: '1px solid #444' }}
          >
            <option value="">Select Category...</option>
            <option value="lead_acid_batteries">Lead-Acid Batteries</option>
            <option value="industrial_oil">Used Industrial Oil</option>
            <option value="scrap_copper">Scrap Copper / Metal</option>
            <option value="e_waste">Electronic Waste (E-Waste)</option>
            <option value="chemical_solvents">Chemical Solvents</option>
          </select>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <div style={{ flex: '2' }}>
            <label style={{ display: 'block', marginBottom: '5px' }}>Quantity</label>
            <input 
              type="number" 
              name="quantity" 
              value={formData.quantity} 
              onChange={handleChange}
              required
              placeholder="e.g., 500"
              style={{ width: '100%', padding: '10px', borderRadius: '5px', backgroundColor: '#2a2a40', color: '#fff', border: '1px solid #444' }}
            />
          </div>
          <div style={{ flex: '1' }}>
            <label style={{ display: 'block', marginBottom: '5px' }}>Unit</label>
            <select 
              name="unit" 
              value={formData.unit} 
              onChange={handleChange}
              style={{ width: '100%', padding: '10px', borderRadius: '5px', backgroundColor: '#2a2a40', color: '#fff', border: '1px solid #444' }}
            >
              <option value="kg">Kilograms (kg)</option>
              <option value="tons">Tons</option>
              <option value="gallons">Gallons</option>
              <option value="liters">Liters</option>
            </select>
          </div>
        </div>

        <button 
          type="submit" 
          disabled={isLoading}
          style={{
            marginTop: '10px',
            padding: '12px',
            backgroundColor: isLoading ? '#6b7280' : '#4ADE80',
            color: '#000',
            fontWeight: 'bold',
            border: 'none',
            borderRadius: '5px',
            cursor: isLoading ? 'not-allowed' : 'pointer'
          }}
        >
          {isLoading ? 'Agent is Analyzing...' : 'Analyze Compliance & Routing'}
        </button>
      </form>
    </div>
  );
};

export default WasteSubmissionForm;
