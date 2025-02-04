import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DataChart from './DataChart';
import ChartTabs from './ChartTabs';
import '../styles/main.css';

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [activeChart, setActiveChart] = useState('Gender Distribution');

  const generateData = async () => {
    await axios.get('http://localhost:8000/api/generate/');
    fetchAnalysis();
  };

  const fetchAnalysis = async () => {
    const response = await axios.get('http://localhost:8000/api/analyze/');
    setData(response.data);
  };

  useEffect(() => {
    fetchAnalysis();
  }, []);

  const chartConfig = {
    'Gender Distribution': {
      labels: data ? Object.keys(data.gender_counts) : [],
      data: data ? Object.values(data.gender_counts) : [],
    },
    'Occupation Counts': {
      labels: data ? Object.keys(data.occupation_counts) : [],
      data: data ? Object.values(data.occupation_counts) : [],
    },
    'Location Counts': {
      labels: data ? Object.keys(data.location_counts) : [],
      data: data ? Object.values(data.location_counts) : [],
    },
    'Education Level Counts': {
      labels: data ? Object.keys(data.education_counts) : [],
      data: data ? Object.values(data.education_counts) : [],
    },
  };

  return (
    <div className="dashboard-container">
      <button onClick={generateData}>Generate New Data</button>

      {data && (
        <>
          <ChartTabs
            charts={Object.keys(chartConfig)}
            activeChart={activeChart}
            setActiveChart={setActiveChart}
          />

          <DataChart
            title={activeChart}
            labels={chartConfig[activeChart].labels}
            data={chartConfig[activeChart].data}
          />
        </>
      )}
    </div>
  );
};

export default Dashboard;
