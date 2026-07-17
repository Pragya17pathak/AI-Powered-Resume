// ---------- Theme Toggle ----------

function toggleTheme() {

    const body = document.body;

    body.classList.toggle("dark");

    const currentTheme = body.classList.contains("dark")
        ? "dark"
        : "light";

    localStorage.setItem("theme", currentTheme);

    updateThemeButton(currentTheme);

}

// ---------- Update Theme Button ----------

function updateThemeButton(theme) {

    const btn = document.getElementById("themeBtn");

    if (!btn) return;

    if (theme === "dark") {

        btn.innerHTML = "☀️ Light Mode";

    } else {

        btn.innerHTML = "🌙 Dark Mode";

    }

}

// ---------- Apply Saved Theme ----------

function loadTheme() {

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {

        document.body.classList.add("dark");

        updateThemeButton("dark");

    } else {

        document.body.classList.remove("dark");

        updateThemeButton("light");

    }

}

// ---------- Animate ATS Progress Bar ----------

function animateProgressBar() {

    const progressBar = document.getElementById("scoreBar");

    if (!progressBar) return;

    const score = progressBar.dataset.score;

    progressBar.style.width = "0%";

    setTimeout(() => {

        progressBar.style.transition = "width 1.2s ease-in-out";

        progressBar.style.width = score + "%";

    }, 300);

}

// ---------- Card Hover Animation ----------

function addCardAnimation() {

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-5px)";
            card.style.transition = "0.3s";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

}

// ---------- Fade In Page ----------

function fadeInPage() {

    document.body.style.opacity = "0";

    document.body.style.transition = "opacity 0.5s";

    setTimeout(() => {

        document.body.style.opacity = "1";

    }, 100);

}

// ---------- Initialize Everything ----------

document.addEventListener("DOMContentLoaded", () => {

    loadTheme();

    animateProgressBar();

    addCardAnimation();

    fadeInPage();

});

// ---------- Chart.js Dashboard ----------

document.addEventListener("DOMContentLoaded", () => {

    const atsCanvas = document.getElementById("atsChart");

    const breakdownCanvas = document.getElementById("breakdownChart");

    if (!atsCanvas || !breakdownCanvas) {

        return;

    }

    const score = Number(document.body.dataset.score);

    const breakdown = JSON.parse(document.body.dataset.breakdown);

    new Chart(

        atsCanvas,

        {

            type: "doughnut",

            data: {

                labels: [

                    "ATS Score",

                    "Remaining"

                ],

                datasets: [

                    {

                        data: [

                            score,

                            100 - score

                        ],

                        backgroundColor: [

                            "#0d6efd",

                            "#dee2e6"

                        ],

                        borderWidth: 2

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: true,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );

    new Chart(

        breakdownCanvas,

        {

            type: "bar",

            data: {

                labels: [

                    "Similarity",

                    "Skills",

                    "Experience",

                    "Projects",

                    "Education",

                    "Certificates",

                    "Contact",

                    "Length"

                ],

                datasets: [

                    {

                        label: "Score",

                        data: [

                            breakdown.similarity,

                            breakdown.skills,

                            breakdown.experience,

                            breakdown.projects,

                            breakdown.education,

                            breakdown.certifications,

                            breakdown.contact,

                            breakdown.length

                        ],

                        backgroundColor: [

                            "#0d6efd",

                            "#198754",

                            "#0dcaf0",

                            "#ffc107",

                            "#6c757d",

                            "#dc3545",

                            "#212529",

                            "#6610f2"

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                },

                plugins: {

                    legend: {

                        display: false

                    }

                }

            }

        }

    );

});