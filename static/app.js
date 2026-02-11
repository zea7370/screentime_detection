document.addEventListener("DOMContentLoaded", () => {

    // Track user interaction behavior
    const inputs = document.querySelectorAll("input, select");

    inputs.forEach(input => {
        input.addEventListener("change", () => {
            console.log("User behavior updated");
        });
    });

    // Screen time monitoring
    const screenInput = document.querySelector("input[name='screen_time']");
    const socialInput = document.querySelector("input[name='social_time']");
    const appOpensInput = document.querySelector("input[name='app_opens']");

    function checkUsage() {
        let warnings = [];

        if (screenInput && screenInput.value > 6) {
            warnings.push("⚠ Excessive screen time detected");
        }

        if (socialInput && socialInput.value > 4) {
            warnings.push("⚠ High social media usage");
        }

        if (appOpensInput && appOpensInput.value > 50) {
            warnings.push("⚠ Frequent application access");
        }

        // Send warning to React component
        if (window.setReactWarning) {
            window.setReactWarning(warnings.join(" | "));
        }
    }

    if (screenInput) screenInput.addEventListener("input", checkUsage);
    if (socialInput) socialInput.addEventListener("input", checkUsage);
    if (appOpensInput) appOpensInput.addEventListener("input", checkUsage);
});