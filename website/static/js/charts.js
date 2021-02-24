
function generateChart(type, dataset1) {
var firstChartObject = document.getElementById('first_chart')

var chart = new Chart(firstChartObject, {
  type: type,
  data: {
    labels: ["7 day incidence", "new cases", "new cases last 7 days","deaths"],
    datasets : [
      {
      label: "Niedersachsen",
      fill: true,
      backgroundColor: "rgba(255,0,0,0.4)",
      borderColor: "rgba(255,0,0,1)",
      data: dataset1

    }]
  },
  options: {
    scales: {
      radialAxis: [
        {
          type: "linear",
          labelString: "7 day incidence",
          suggestedMin: 50,
          suggestedMax: 100,
          ticks: {
            stepSize: 5
          }
        },
        {
          type: "linear",
          labelString: "new cases",
          ticks: {
            stepSize: 15
          }
        },
        {
          type: "linear",
          labelString: "new cases last 7 days",
          ticks: {
            stepSize: 100
          }
        }
      ]
    },
    legend: {
      display: false,
      position: "bottom",
      align: "center"
    },
    title: {
      text: "Super krasser Titel",
      position: "top",
      display: true,
    },
    tooltip: {
      enabled: false,
      mode: "nearest"
      
    }
}
});
}