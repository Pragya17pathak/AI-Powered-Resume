// ---------- Theme Toggle ----------

function toggleTheme() {

    const body = document.body;

    body.classList.toggle("dark");

    const theme = body.classList.contains("dark")

        ? "dark"

        : "light";

    localStorage.setItem(

        "theme",

        theme

    );

    updateThemeButton(theme);

}


// ---------- Theme Button ----------

function updateThemeButton(theme) {

    const btn = document.getElementById(

        "themeBtn"

    );

    if (!btn) {

        return;

    }

    btn.innerHTML =

        theme === "dark"

            ? "☀️ Light Mode"

            : "🌙 Dark Mode";

}


// ---------- Load Theme ----------

function loadTheme() {

    const theme =

        localStorage.getItem("theme")

        || "light";

    if (theme === "dark") {

        document.body.classList.add(

            "dark"

        );

    }

    updateThemeButton(theme);

}


// ---------- Fade In ----------

function fadeInPage() {

    document.body.style.opacity = "0";

    document.body.style.transition =

        "opacity .6s ease";

    setTimeout(() => {

        document.body.style.opacity = "1";

    }, 100);

}


// ---------- Progress Bars ----------

function animateProgressBars() {

    const bars = document.querySelectorAll(

        ".progress-bar[data-width]"

    );

    bars.forEach(bar => {

        const width =

            Number(

                bar.dataset.width

            ) || 0;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.transition =

                "width 1.5s ease";

            bar.style.width =

                width + "%";

        }, 300);

    });

}


// ---------- Card Hover ----------

function addCardAnimation() {

    document

        .querySelectorAll(".card")

        .forEach(card => {

            card.addEventListener(

                "mouseenter",

                () => {

                    card.style.transition =

                        ".3s";

                    card.style.transform =

                        "translateY(-8px)";

                    card.style.boxShadow =

                        "0 20px 40px rgba(124,58,237,.25)";

                }

            );

            card.addEventListener(

                "mouseleave",

                () => {

                    card.style.transform =

                        "translateY(0)";

                    card.style.boxShadow = "";

                }

            );

        });

}


// ---------- Counter Animation ----------

function animateCounters() {

    const counters = document.querySelectorAll(

        "[data-counter]"

    );

    counters.forEach(counter => {

        const target = Number(

            counter.dataset.counter

        ) || 0;

        let current = 0;

        const increment = Math.max(

            1,

            Math.ceil(

                target / 60

            )

        );

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {

                current = target;

                clearInterval(timer);

            }

            if (

                counter.dataset.percent

            ) {

                counter.textContent =

                    current + "%";

            }

            else {

                counter.textContent =

                    current;

            }

        }, 20);

    });

}


// ---------- Badge Hover ----------

function animateBadges() {

    document

        .querySelectorAll(".badge")

        .forEach(badge => {

            badge.addEventListener(

                "mouseenter",

                () => {

                    badge.style.transform =

                        "scale(1.08)";

                    badge.style.transition =

                        ".25s";

                }

            );

            badge.addEventListener(

                "mouseleave",

                () => {

                    badge.style.transform =

                        "scale(1)";

                }

            );

        });

}


// ---------- Copy Resume ----------

function copyResumeText() {

    const preview =

        document.getElementById(

            "resumePreview"

        );

    if (!preview) {

        return;

    }

    navigator.clipboard.writeText(

        preview.innerText

    );

    const btn =

        document.getElementById(

            "copyBtn"

        );

    if (btn) {

        const original =

            btn.innerHTML;

        btn.innerHTML =

            "✅ Copied";

        setTimeout(() => {

            btn.innerHTML =

                original;

        }, 2000);

    }

}


// ---------- Print ----------

function printReport() {

    window.print();

}


// ---------- Scroll Top ----------

function scrollToTop() {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}


// ---------- Scroll Button ----------

function initializeScrollButton() {

    const topBtn =

        document.getElementById(

            "topBtn"

        );

    if (!topBtn) {

        return;

    }

    topBtn.style.display =

        "none";

    window.addEventListener(

        "scroll",

        () => {

            if (

                window.scrollY > 300

            ) {

                topBtn.style.display =

                    "block";

            }

            else {

                topBtn.style.display =

                    "none";

            }

        }

    );

}


// ---------- Loading Overlay ----------

function initializeLoader() {

    const form =

        document.querySelector(

            "form"

        );

    if (!form) {

        return;

    }

    form.addEventListener(

        "submit",

        () => {

            const loader =

                document.getElementById(

                    "loadingOverlay"

                );

            if (loader) {

                loader.style.display =

                    "flex";

            }

        }

    );

}
// ---------- ATS Doughnut Chart ----------

function createATSChart() {

    const canvas = document.getElementById(

        "atsChart"

    );

    if (!canvas) {

        return;

    }

    Chart.getChart(canvas)?.destroy();

    const score = Number(

        document.body.dataset.score || 0

    );

    const centerText = {

        id: "centerText",

        afterDraw(chart) {

            const {

                ctx,

                chartArea

            } = chart;

            ctx.save();

            ctx.font = "bold 34px Arial";

            ctx.fillStyle = "#7C3AED";

            ctx.textAlign = "center";

            ctx.textBaseline = "middle";

            ctx.fillText(

                score + "%",

                (chartArea.left + chartArea.right) / 2,

                (chartArea.top + chartArea.bottom) / 2

            );

            ctx.restore();

        }

    };

    new Chart(canvas, {

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

                        "#7C3AED",

                        "#DDD6FE"

                    ],

                    borderWidth: 0,

                    hoverOffset: 10

                }

            ]

        },

        options: {

            responsive: true,

            cutout: "72%",

            animation: {

                duration: 1800

            },

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        },

        plugins: [

            centerText

        ]

    });

}


// ---------- Breakdown Radar Chart ----------

function createBreakdownChart() {

    const canvas = document.getElementById(

        "breakdownChart"

    );

    if (!canvas) {

        return;

    }

    Chart.getChart(canvas)?.destroy();

    let breakdown = {};

    try {

        breakdown = JSON.parse(

            document.body.dataset.breakdown || "{}"

        );

    }

    catch {

        breakdown = {};

    }

    new Chart(canvas, {

        type: "radar",

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

                    label: "Resume Analysis",

                    data: [

                        breakdown.similarity || 0,

                        breakdown.skills || 0,

                        breakdown.experience || 0,

                        breakdown.projects || 0,

                        breakdown.education || 0,

                        breakdown.certifications || 0,

                        breakdown.contact || 0,

                        breakdown.length || 0

                    ],

                    backgroundColor:

                        "rgba(124,58,237,.20)",

                    borderColor:

                        "#7C3AED",

                    borderWidth: 3,

                    pointBackgroundColor:

                        "#7C3AED",

                    pointRadius: 5

                }

            ]

        },

        options: {

            responsive: true,

            animation: {

                duration: 2000

            },

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                r: {

                    beginAtZero: true,

                    suggestedMax: 30,

                    grid: {

                        color:

                            "#D8B4FE"

                    },

                    angleLines: {

                        color:

                            "#D8B4FE"

                    },

                    pointLabels: {

                        color:

                            "#6D28D9",

                        font: {

                            size: 12,

                            weight: "bold"

                        }

                    }

                }

            }

        }

    });

}


// ---------- Initialize Charts ----------

function initializeCharts() {

    createATSChart();

    createBreakdownChart();

}


// ---------- Initialize Everything ----------

document.addEventListener(

    "DOMContentLoaded",

    () => {

        loadTheme();

        fadeInPage();

        animateProgressBars();

        animateCounters();

        addCardAnimation();

        animateBadges();

        initializeCharts();

        initializeLoader();

        initializeScrollButton();

        document

            .getElementById(

                "printBtn"

            )

            ?.addEventListener(

                "click",

                printReport

            );

        document

            .getElementById(

                "copyBtn"

            )

            ?.addEventListener(

                "click",

                copyResumeText

            );

        document

            .getElementById(

                "topBtn"

            )

            ?.addEventListener(

                "click",

                scrollToTop

            );

        document

            .getElementById(

                "themeBtn"

            )

            ?.addEventListener(

                "click",

                toggleTheme

            );

    }

);