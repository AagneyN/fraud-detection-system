let riskChart;
let trendChart;

let fraudCount = 0;
let safeCount = 0;

let trendData = [];

async function predict() {

    let features = document
        .getElementById("features")
        .value
        .split(",")
        .map(Number);

    let loading = document.getElementById("loading");
    let result = document.getElementById("result");

    loading.classList.remove("hidden");

    try {
        let response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ features })
        });

        let data = await response.json();

        loading.classList.add("hidden");

        let risk = data.fraud_probability;

        updateStats(data.prediction);
        updateResult(data.prediction, risk);
        updateRiskBar(risk);
        renderRiskChart(risk);
        updateTrendChart(risk);

    } catch (error) {
        loading.classList.add("hidden");
        result.innerText = "Error connecting to server";
    }
}


function generateTransaction() {
    let values = [];

    for (let i = 0; i < 30; i++) {
        let num = (Math.random() * 6 - 3).toFixed(3); // wider range
        values.push(num);
    }

    document.getElementById("features").value = values.join(",");
}


function updateStats(prediction) {
    if (prediction.includes("Fraud")) {
        fraudCount++;
    } else {
        safeCount++;
    }

    document.getElementById("fraudCount").innerText = fraudCount;
    document.getElementById("safeCount").innerText = safeCount;
}


function updateResult(prediction, risk) {
    let result = document.getElementById("result");

    let riskClass = risk > 50 ? "high-risk" : "low-risk";

    result.className = riskClass;
    result.innerText = prediction + " — Fraud Risk: " + risk + "%";
}


function updateRiskBar(risk) {
    let bar = document.querySelector(".risk-bar");
    let fill = document.getElementById("risk-fill");

    bar.classList.remove("hidden");
    fill.style.width = risk + "%";
}


function renderRiskChart(risk) {
    let ctx = document.getElementById("riskChart").getContext("2d");

    if (riskChart) riskChart.destroy();

    riskChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Fraud Risk", "Safe"],
            datasets: [{
                data: [risk, 100 - risk],
                backgroundColor: ["#ef4444", "#22c55e"]
            }]
        },
        options: {
            cutout: "70%",
            plugins: { legend: { display: false } }
        }
    });
}


function updateTrendChart(risk) {
    trendData.push(risk);

    let ctx = document.getElementById("trendChart").getContext("2d");

    if (trendChart) trendChart.destroy();

    trendChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: trendData.map((_, i) => i + 1),
            datasets: [{
                data: trendData,
                borderColor: "#4D7CFF",
                fill: true
            }]
        }
    });
}