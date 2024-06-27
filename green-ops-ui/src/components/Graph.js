import React from 'react';
import { Line } from 'react-chartjs-2';
import moment from 'moment';
import 'chartjs-adapter-moment';

import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
} from 'chart.js';

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend, TimeScale);

const MultiAxisLineChart = ({ data }) => {
  // Extracting data for X and Y axes
  const xData = data?.X?.map(entry => ({
      x: moment(entry.time).toDate(),  // Convert time to Date object
      y: entry.count,
  }));

  const yData = data?.Y?.map(entry => ({
      x: moment(entry.time).toDate(),  // Convert time to Date object
      y: entry.count,
  }));

  // Chart data and options
  const chartData = {
      datasets: [
          {
              label: 'X',
              data: xData,
              borderColor: 'rgb(255, 99, 132)',
              backgroundColor: 'rgba(255, 99, 132, 0.5)',
              yAxisID: 'y',
          },
          {
              label: 'Y',
              data: yData,
              borderColor: 'rgb(54, 162, 235)',
              backgroundColor: 'rgba(54, 162, 235, 0.5)',
              yAxisID: 'y1',
          },
      ],
  };

  const options = {
      responsive: true,
      plugins: {
          legend: {
              position: 'top',
          },
          title: {
              display: true,
              text: 'Multi-Axis Line Chart',
          },
      },
      scales: {
          x: {
              type: 'time',
              title: {
                  display: true,
                  text: 'Time',
              },
          },
          y: {
              type: 'linear',
              display: true,
              position: 'left',
              title: {
                  display: true,
                  text: 'Count',
              },
          },
          y1: {
              type: 'linear',
              display: true,
              position: 'right',
              title: {
                  display: true,
                  text: 'Count',
              },
              grid: {
                  drawOnChartArea: false,
              },
          },
      },
  };

  return <Line data={chartData} options={options} />;
};



export default MultiAxisLineChart;
