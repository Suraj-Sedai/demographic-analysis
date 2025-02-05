import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DataChart from './DataChart';
import ChartTabs from './ChartTabs';
import '../styles/main.css';

const Dashboard = () => {  // ✅ Hooks must be inside this function
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [activeChart, setActiveChart] = useState('Gender Distribution');

  const API_BASE_URL = 'http://localhost:8000/api';

  const generateData = async () => {
    try {
      await axios.get(`${API_BASE_URL}/generate/`);
      fetchAnalysis();
    } catch (error) {
      console.error('Error generating data:', error);
    }
  };

  const fetchAnalysis = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/analyze/`);
      console.log("API Response:", response.data);
      setData(response.data);
    } catch (error) {
      console.error('Error fetching analysis:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchAnalysis();
  }, []);

  const chartConfig = {
    'Gender Distribution': {
      labels: data?.gender_counts ? Object.keys(data.gender_counts) : [],
      data: data?.gender_counts ? Object.values(data.gender_counts) : [],
    },
    'Occupation Counts': {
      labels: data?.occupation_counts ? Object.keys(data.occupation_counts) : [],
      data: data?.occupation_counts ? Object.values(data.occupation_counts) : [],
    },
    'Location Counts': {
      labels: data?.location_counts ? Object.keys(data.location_counts) : [],
      data: data?.location_counts ? Object.values(data.location_counts) : [],
    },
    'Education Level Counts': {
      labels: data?.education_counts ? Object.keys(data.education_counts) : [],
      data: data?.education_counts ? Object.values(data.education_counts) : [],
    },
  };

  return (
    <div className="dashboard-container">
      <button onClick={generateData}>Generate New Data</button>

      {isLoading && <p>Loading data...</p>}
      {!isLoading && data && (
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
      {!isLoading && !data && <p>No data available.</p>}
    </div>
  );
};

export default Dashboard;
