import React from 'react';
import { Bar, Pie } from 'react-chartjs-2';
import { Chart, ArcElement, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

Chart.register(ArcElement, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const DataChart = ({ title, labels, data }) => {
  const chartData = {
    labels,
    datasets: [
      {
        label: title,
        data,
        backgroundColor: ['#007bff', '#28a745', '#17a2b8', '#ffc107', '#dc3545'],
      },
    ],
  };

  return (
    <div className="chart-card">
      <h2>{title}</h2>
      {labels.length <= 5 ? <Pie data={chartData} /> : <Bar data={chartData} />}
    </div>
  );
};

export default DataChart;
