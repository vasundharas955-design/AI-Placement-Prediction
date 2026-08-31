const navItems = document.querySelectorAll(".nav-item");
navItems.forEach(item => {
    item.addEventListener("click", function (event) {
        navItems.forEach(nav => {
            nav.classList.remove("active");
        });
        this.classList.add("active");
        
        const target = this.getAttribute("href");

        if (target && target.startsWith("#")) {

            const section = document.querySelector(target);

            if (section) {
                event.preventDefault();
                section.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        }
    });
});
const cgpa =
    document.querySelector('input[name="CGPA"]');
const projects =
    document.querySelector('input[name="Projects"]');
const internships =
    document.querySelector('input[name="Internships"]');
const aptitude =
    document.querySelector('input[name="AptitudeTestScore"]');
const certifications =
    document.querySelector('input[name="Certifications"]');
const softSkills =
    document.querySelector('input[name="SoftSkillsRating"]');
if (cgpa) {
    cgpa.addEventListener("input", function () {
        if (this.value > 10) {
            this.value = 10;
        }
        if (this.value < 0) {
            this.value = 0;
        }
    });
}
if (aptitude) {
    aptitude.addEventListener("input", function () {
        if (this.value > 100) {
            this.value = 100;
        }
        if (this.value < 0) {
            this.value = 0;
        }
    });

}

if (softSkills) {
    softSkills.addEventListener("input", function () {
        if (this.value > 5) {
            this.value = 5;
        }
        if (this.value < 0) {
            this.value = 0;
        }
    });
}
[projects, internships, certifications].forEach(input => {
    if (input) {
        input.addEventListener("input", function () {
            if (this.value < 0) {
                this.value = 0;
            }
        });
    }
});
const inputWrappers =
    document.querySelectorAll(".input-wrapper");
inputWrappers.forEach(wrapper => {
    const field =
        wrapper.querySelector("input, select");

    if (!field) return;
    field.addEventListener("focus", function () {
        wrapper.style.borderColor = "#7049ed";
    });
    field.addEventListener("blur", function () {

        if (this.value === "") {
            wrapper.style.borderColor = "#28334c";
        }
    });
});

const form =
    document.getElementById("predictionForm");

const predictButton =
    document.querySelector(".predict-button");

if (form && predictButton) {
    form.addEventListener("submit", function () {
        predictButton.disabled = true;
        predictButton.innerHTML =
            "⏳ Analyzing Profile...";
        predictButton.style.opacity = "0.7";
        predictButton.style.cursor = "wait";
    });
}


// ==========================================
// RESULT CARD
// ==========================================

const resultCard =
    document.querySelector(".result-card");

const predictionText =
    document.querySelector(".gauge-content strong");


if (predictionText && resultCard) {

    const prediction =
        predictionText.innerText.trim();

    if (
        prediction === "YES" ||
        prediction === "NO"
    ) {

        resultCard.style.borderColor =
            "#7049ed";

    }
}
if (predictButton && form) {
    predictButton.addEventListener("click", function () {
        const inputs =
            form.querySelectorAll(
                "input[required], select[required]"
            );

        let valid = true;
        inputs.forEach(input => {
            if (input.value.trim() === "") {
                valid = false;
                input.style.borderColor =
                    "#e34c6f";
            }
        });
        if (!valid) {
            alert(
                "Please fill all the fields before prediction."
            );
        }
    });
}
const requiredFields =
    document.querySelectorAll(
        ".input-wrapper input, .input-wrapper select"
    );
requiredFields.forEach(field => {
    field.addEventListener("input", function () {

        if (this.value.trim() !== "") {
            this.parentElement.style.borderColor =
                "#28334c";
        }
    });
    field.addEventListener("change", function () {
        if (this.value.trim() !== "") {
            this.parentElement.style.borderColor =
                "#28334c";
        }
    });
});
document.addEventListener(
    "DOMContentLoaded",
    function () {
        console.log(
            "Placement Console loaded successfully."
        );

    }
);