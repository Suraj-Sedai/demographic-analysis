import React from 'react';

const ChartTabs = ({ charts, activeChart, setActiveChart }) => {
  return (
    <div className="chart-tabs">
      {charts.map((chart) => (
        <button
          key={chart}
          onClick={() => setActiveChart(chart)}
          className={activeChart === chart ? 'active' : ''}
        >
          {chart}
        </button>
      ))}
    </div>
  );
};

export default ChartTabs;
